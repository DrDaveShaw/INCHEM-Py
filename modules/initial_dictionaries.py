'''
Creates initial dictionary files for INCHEM-Py. Initial concentrations, the
master array of ODEs and the Jacobian. Also providec functions for compilation
and evaluation.
A detailed description of this file can be found within the user manual.

Copyright (C) 2019-2021 
David Shaw : david.shaw@york.ac.uk
Nicola Carslaw : nicola.carslaw@york.ac.uk

All rights reserved.

This file is part of INCHEM-Py.

INCHEM-Py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

INCHEM-Py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with INCHEM-Py.  If not, see <https://www.gnu.org/licenses/>.
'''

import numpy as np
from tqdm import tqdm
import pandas as pd
import re

def initial_conditions(initial_filename,M,species,rate_numba,calc_dict,particles,initials_from_run,t0,path):
    '''
    importing initial concentrations of gas phase species and particles if particles = True
    
    inputs:
        initial_filename = initial conditions filename
        M = air density
        species = list of species
        rate_numba = rates of reactions with expressions replaced with numba versions
        calc_dict = dictionary of constants and variables for use in calculations
        particles = True/False depeding if using particles or not
        initials_from_run = True/False depending if taking initials from previous run
        t0 = starting time of simulation (s)
        path = current working directory
        
    returns:
        density_dict = dictionary of current species concentrations {species : concentration}
        calc_dict = dictionary of constants and variables for use in calculations
    '''
    initial=[]
    
    if initials_from_run == True:
        '''import initial conditions from previous run'''
        from bisect import bisect_left
        #with open("%s/in_data.pickle" % path,'rb') as handle:
            #in_data = pickle.load(handle)
        in_data = pd.read_pickle("%s/in_data.pickle" % path)
        index_values = in_data.index.values
        pos = bisect_left(index_values, t0)
        if pos == 0:
            index_import = index_values[0]
        if pos == len(index_values):
            index_import = index_values[-1]
        before = index_values[pos - 1]
        after = index_values[pos]
        if after - t0 < t0 - before:
           index_import = after
        else:
           index_import = before
               
        density_dict = {}
        for i in species:
            try:
                density_dict[i] = in_data.loc[index_import,i]
            except KeyError:
                #if new species added since imported run set it to 0
                density_dict[i] = 0
                
    else:
        '''Import initial conditions from file'''
        with open(initial_filename, 'r') as f:
            line=f.readlines()
            for i in range(len(line)):
                initial.append(line[i].split('='))
            
        for i in range(len(initial)):
            initial[i][1]=initial[i][1].strip(' ;\n')
            initial[i][1]=initial[i][1].replace('D-','e-')
            
        density_dict={}
        for i in initial:
            if i[0] in species:
                density_dict[i[0]]=eval(i[1],{},calc_dict)
                
        for i in species:
            if i not in density_dict and i.startswith('PART'):
                density_dict[i]=0
            elif i not in density_dict:
                density_dict[i]=0
            
    if particles == True and 'seed_1' not in density_dict:
        density_dict['seed_1']=2.09e10
        density_dict['seed']=density_dict['seed_1']*1.33e-4
            
    for i in rate_numba:
        calc_dict[i[0]]=eval(i[1],{},{**density_dict,**calc_dict})    
    return density_dict,calc_dict

def master_calc(reactions_in,species,reaction_number,particles,particle_species,timed_emissions):
    '''
    Creates the master array by populating with sting values for 
    species and rates. Sources and sinks are determined and negative and 
    positive rates given accordingly. Each row of the created array 
    corresponds to a species in the order that they are provided in the
    input files. The format is dA/second = k1*nA*nB - k2*nC*nD ...
    
    inputs:
        reactions_in = full list of included chemical reactions [rate, reaction]
        species = list of species
        reaction_number = list of strings to relate reactions to locations within master array
        particles = True/False depeding if using particles or not 
        particle_species = list of particle species
        timed_emissions = True/False depending on if using timed emissions or not
        
    returns:
        master_array_dict = dictionary of arrays of reactions that can be reduced
                            to form the system of ODEs to be solved
    '''
    
    master_array_dict={} #for saving array as dict
    for s in species:
        master_array_dict[s]=[]

    reaction=np.zeros([len(reactions_in)]).tolist()
    loss_array_temp=[[] for i in range(len(reactions_in))] #temporary array for loss side of reaction
    gain_array_temp=[[] for i in range(len(reactions_in))] #temporary array for loss side of reaction
    
    for i in tqdm(range(len(reactions_in)),desc="Creating master array"):
        reaction[i]=reactions_in[i][1].replace(' ','') #remove spaces
        reaction[i]=reaction[i].split('=') #split into loss and gain
        loss_array_temp[i]=reaction[i][0].split('+')
        gain_array_temp[i]=reaction[i][1].split('+')
        for j in species:
            temp_loss=[]
            temp_loss.append('%s' % reaction_number[i]) #assign reaction
            temp_loss.append('-1') #negative if loss
            if loss_array_temp[i] != ['']:
                temp_loss.extend(loss_array_temp[i])
            else:
                temp_loss.extend('1')
            temp_gain=[]
            temp_gain.append('%s' % reaction_number[i]) #assign reaction
            if loss_array_temp[i] != ['']:
                temp_gain.extend(loss_array_temp[i])
            else:
                temp_gain.extend('1')
            
            #if species is being lost append loss, if gained append gain
            for k in loss_array_temp[i]:
                if j == k:
                    master_array_dict[j].append(temp_loss)
            for k in gain_array_temp[i]:
                if j == k:
                    master_array_dict[j].append(temp_gain)
                    
    
    for s in species:
        #outdoor exchange
        if particles == True and s in particle_species:
            master_array_dict[s].append(['%s' % s, 'AER', '-1'])
            if s == 'seed_1':
                master_array_dict[s].append(['TSPOUT','AER*0.3'])
            elif s == 'tspnonorg':
                master_array_dict[s].append(['TSPOUT','AER*0.7'])
        else:
            master_array_dict[s].append(['%sOUT' % s, 'AER'])
            master_array_dict[s].append(['%s' % s, 'AER', '-1'])
        
        #surface deposition
        master_array_dict[s].append(['%s_SURF' % s, s,'-1'])   
        
        #timed densities
        if timed_emissions == True:
            master_array_dict[s].append(["%s_timed" % s, "1"])
            
    return master_array_dict

def master_compiler(master_array_dict,species):
    '''
    compiles the master array to be evaluated during integration
    
    inputs:
        master_array_dict = dictionary of arrays of reactions that can be reduced
                            to form the system of ODEs to be solved
        species = list of species
        
    returns:
        master_compiled = dictionary of reduced and compiled ODEs for feeding
                          into the integrator. Equations of the form 
                          dA/second = k1*nA*nB - k2*nC*nD ...
    '''
    master_compiled={}
    
    for i in species:
        x=[]
        for j in master_array_dict[i]:
            x.append('*'.join(j))
        y='+'.join(x)
        master_compiled[i]=compile(y,'<string>','eval')   
    return master_compiled


def reaction_rate_compile(reactions_numba,reaction_number):
    '''
    compiling generic reaction rates for evaluation during integration
    
    inputs:
        reactions_numba = full list of included chemical reactions [rate, reaction]
                          with reaction calculations in numba format
        reaction_number = list of strings to relate reactions to locations within master array
        
    returns:
        reaction_compiled_dict = dictionary of compiled reaction rates {reaction number : reaction rate}
        
    '''
    reaction_compiled_dict={}
    
    for i,x in enumerate(reactions_numba):
        reaction_compiled_dict[str(reaction_number[i])]=compile(x[0],'<string>','eval')      
    return reaction_compiled_dict


def reaction_eval(reaction_number,J_dict,calc_dict,density_dict,dt,reaction_compiled_dict,outdoor_dict,surface_dict,timed_dict):
    '''
    compiling specific reaction rates for evaluation during integration
    
    inputs:
        reaction_number = list of strings to relate reactions to locations within master array
        J_dict = dictionary of current photolysys values
        calc_dict = dictionary of constants and variables for use in calculations
        density_dict = dictionary of current concentrations
        dt = time step (s)
        reaction_compiled_dict = dictionary of compiled reaction rates {reaction number : reaction rate}
        outdoor_dict = dictionary of outdoor species concentrations
        surface_dict = dictionary of surface deposition rates for each species
        timed_dict = dictionary of rates for any timed inputs for current time
        
    returns:
        reaction_rate_dict = dictionary of reaction rate values at current time
    '''
    reaction_rate_dict={}
    
    full_dict={**J_dict,**calc_dict,**density_dict,**outdoor_dict,**surface_dict,**timed_dict}
    
    #for key in tqdm(reaction_compiled_dict.keys(),desc='Calculating reaction rate'):
    for key in reaction_compiled_dict.keys():
        reaction_rate_dict[key]=(eval(reaction_compiled_dict[key],{},full_dict))   
    return reaction_rate_dict


def write_jacobian_build(master_array_dict,species,output_folder,path):
    '''
    creating the jacobian of the master array
    
    Currently writes the calculation to a file so that it can be saved but also
    so that the function can be called to create a compiled jacobian to speed up
    evaluation
    
    inputs:
        master_array_dict = dictionary of arrays of reactions that can be reduced
                            to form the system of ODEs to be solved
        species = list of species
        output_folder = string name of output folder within current working directory
        
    returns:
        None
        
    writes:
        Jacobian.py containing jacobian_calc which compiles a dictionary of 
        indexed values for dydy of the form {index:[x,y,compiled partial differential]}
    '''
    f=open('%s/%s/Jacobian.py'% (path,output_folder),'w')
    f.write('import numpy as np\n')
    f.write('def jacobian_calc(species):\n')
    
    f.write('    dy_dy_dict={}\n')
    
    counter=0
    
    for i,x in enumerate(tqdm(species,desc='Constructing Jacobian')):
        for j,y in enumerate(species):
            temp_list=[]
            jac_list=[]
            temp_list=list(map(list,master_array_dict[x]))
            for z in temp_list:
                #differentiate with respect to y
                if y in z:
                    #how many of y in k
                    num = z.count(y)
                    #remove one instance (reduce power by 1)
                    z.remove(y)
                    #if more than one instance then times by number that there are
                    if num > 1:
                        z.append(str(num))
                    if len(z) > 1:
                        jac_list.append('*'.join(z))
                    else:
                        jac_list.append(z[0])
            jac_list='+'.join(jac_list)
            if jac_list:
                f.write('    dy_dy_dict[%s]=([%s,%s,compile(\'%s\',\'<string>\',\'eval\')])\n' % (counter,i,j,jac_list))
                counter=counter+1
    f.write('    return dy_dy_dict\n')
    f.close
    
def INCHEM_species_calc(INCHEM_reactions,species):
    '''
    extracts species from the INCHEM reactions and returns any that are not
    already included in the species list
    
    inputs:
        INCHEM_reactions = list of reactions from INCHEM file
        
    returns:
        INCHEM_species = list of species in INCHEM if not already in species list
    '''
    temp=[]
    for i in INCHEM_reactions:
        temp.extend(re.split('[=+]',i[1]))
    temp = [x for x in temp if x != ""]
    temp = list( dict.fromkeys(temp) )                  #removes duplicates
    INCHEM_species = [item for item in temp if item not in species]
    return INCHEM_species