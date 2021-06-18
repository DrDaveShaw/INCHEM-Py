# -*- coding: utf-8 -*-
"""
The main function for INCHEM-Py. 
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
"""
def run_inchem(filename, particles, INCHEM_additional, custom, temp, rel_humidity,
               M, const_dict, AER, diurnal, city, date, lat, light_type, 
               light_on_times, glass, HMIX, initials_from_run,
               initial_conditions_gas, timed_emissions, timed_inputs, dt, t0,
               seconds_to_integrate, custom_name, output_graph, output_species):
  
    '''
    import all modules
    '''
    import sys
    import pickle
    from modules.inchem_import import import_all, custom_import 
    from modules.particle_input import particle_import, particle_calcs, reactions_check
    from modules.photolysis import photolysis_J, Zixu_photolysis, Zixu_photolysis_compiled
    from modules.initial_dictionaries import initial_conditions, master_calc, master_compiler,\
        reaction_rate_compile, reaction_eval, write_jacobian_build, INCHEM_species_calc
    from modules.outdoor_concentrations import outdoor_rates, outdoor_rates_diurnal, outdoor_rates_calc
    import numpy as np
    import numba as nb
    from scipy.integrate import ode
    import time
    from modules.surface_dictionary import surface_deposition
    from threadpoolctl import threadpool_limits
    import importlib.util
    import pandas as pd
    import os
    import datetime
    import math
    import time as timing
    from modules.reactivity import reactivity_summation, reactivity_calc, production_calc
    
    sys.setrecursionlimit(4000) #to compile the master array the recursion limit
    #must be increased as some of the evaluated ODEs are greater than the usual
    #system limit
    
    save_rate = 1 #sets the rate at which outputs are saved within the integrator.
    #Useful if the timestep has to be reduced but an output at a specific interval
    #is still required. A save rate of 1 will save every dt, a save rate of 2 will
    #save every 2*dt    
    
    def summations_compile(sums):
        '''
        compiles any custom summations
        
        inputs:
            sums = list of summations [name of sum, calculation]
            
        returns:
            summation_dict = dictionary of summations {name of sum : compiled calculation}
        '''
        summation_dict={}
        for i in sums:
            summation_dict[i[0]]=compile(i[1],'<string>','eval')
        return summation_dict
    
    
    def summations_eval(summation_dict,density_dict,calc_dict):
        '''
        evaluates custom summations
        
        inputs:
            summation_dict = dictionary of summations {name of sum : compiled calculation}
            density_dict = dictionary of current species concentrations {species : concentration}
            calc_dict = dictionary of constants and variables for use in calculations
            
        returns:
            sums_dict = dictionary of evaluated sum calculations {name of sum : value}
        '''
        full_dict={**density_dict,**calc_dict}
        for spec in summation_dict.keys():
            sums_dict[spec]=(eval(summation_dict[spec],{},full_dict)) 
        return sums_dict
    
    
    def h2o_rh(time,temp,rel_humidity,numba_exp):
        '''
        calculates relative humidity and water at a given time and temperature
    
        inputs:
            time = current simulation time (s)
            temp = current temperature value (C)
            rel_humidity = current relative humidity (%), can be calculation
            numba_exp = exponent
            
        returns:
            h20 = water vapour
            rh = relative humidity (%)
        '''
        rh = rel_humidity 
        h2o=6.1078*numba_exp(-1.0e+0*(597.3-0.57*(temp-273.16))*18.0/1.986*
                       (1.0/temp-1.0/273.16))*10./(1.38e-16*temp)*rh               
        return h2o,rh
    
    
    def ppool_density_calc(density_dict,ppool):
        '''
        peroxy radical summation evaluation
        
        inputs:
            density_dict = dictionary of current concentrations
            ppool = list of species to be summed for RO2
        
        returns:
            RO2 = summed peroxy radical species
        '''
        RO2 = 0.
        for p in ppool:
            RO2 += eval(p,{},density_dict)
        return RO2
    
    
    def dy_calc(master_compiled,reaction_rate_dict,calc_dict,density_dict,outdoor_dict,\
                surface_dict,species,timed_dict):
        '''
        evaluating the master array of species
        
        inputs:
            master_compiled = dictionary of compiled ODEs
            reaction_rate_dict = dictionary of reaction rate values at current time
            calc_dict = dictionary of constants and variables for use in calculations
            density_dict = dictionary of current concentrations
            outdoor_dict = dictionary of outdoor species concentrations
            surface_dict = dictionary of surface deposition rates for each species
            species = list of species
            timed_dict = dictionary of rates for any timed inputs for current time
            
        returns:
            dy_dict = dictionary of changes in concentration for each species per second
        '''
        dy_dict={}    
        full_dict={**reaction_rate_dict,**calc_dict,**density_dict,**outdoor_dict,\
                   **surface_dict,**timed_dict}
        
        for specie in species:
            dy_dict[specie]=(eval(master_compiled[specie],{},full_dict))
        return dy_dict
    
    
    def dy_dy_calc(dy_dy_dict,J_dict,calc_dict,density_dict,species,outdoor_dict,\
                   surface_dict,num_species,timed_dict,reaction_rate_dict):
        '''
        Evaluating the Jacobian during integration
        
        inputs:
            dy_dy_dict = dictionary jacobian {index:[x,y,compiled calculation]}
            J_dict = dictionary of current photolysys values
            reaction_rate_dict = dictionary of reaction rate values at current time
            calc_dict = dictionary of constants and variables for use in calculations
            density_dict = dictionary of current concentrations
            outdoor_dict = dictionary of outdoor species concentrations
            surface_dict = dictionary of surface deposition rates for each species
            num_species = number of species
            
        returns:
            dy_dy = dictionary of values of species change with species per second
        '''
        dy_dy=np.zeros((num_species,num_species),dtype=np.float32) #twice as fast as lil_matrix
        
        full_dict={**reaction_rate_dict,**density_dict,**outdoor_dict,**surface_dict,\
                   **calc_dict,**timed_dict}
        for k,v in dy_dy_dict.items():
                dy_dy[v[0],v[1]]=eval(v[2],{},full_dict)
        return dy_dy
    
    
    def dydt(t,y0):
        '''
        The function to calculate dydt that is fed to the integrator
    
        inputs:
        	t = time
        	y0 = concentration of species
    
        returns:
        	dy = dictionary of change in species concentration with change in time
        '''
        #Update density dictionary
        for i in range(num_species):
            density_dict[species[i]]=y0[i]  
        density_dict['RO2']=ppool_density_calc(density_dict,ppool)
        
        #if summations are included they need to be updated to the density dictionary also           
        if summations == True:
            sums_dict = summations_eval(summations_dict,density_dict,calc_dict)
            density_dict.update(sums_dict)
            
        #n = time in seconds from midnight for each day
        n = t-((int(t/86400))*86400)
        
        # recalculate photolysis
        # COSX and SECX involve local hour angles dependant on position and time
        # of year (latitude of location and declination of sun)
    
        lha = (1+((n-time_correct)/4.32E+4))*pi     # local hour angle, radians. Midnight start
        cosx = ((numba_cos(lha)*cosld)+sinld)       # solar zenith angle 
        
        # Set negative cosx to zero and calculate the inverse  
        # (secx=1/cosx). The MCM photolysis parameterisation  
        # (http://mcm.leeds.ac.uk/MCM/parameters/photolysis_param.htt)  
        # requires cosx and secx to calculate the photolysis rates.
        if cosx <= 1E-30:
            cosx = 0.0  
            secx = 1.0E+30  
        else:  
            secx = 1.0 / (((cosx + numba_abs(cosx))/2)+1.0E-30) #no divison by 0
        
        #updates the relevant dictionary whether lights are on or off
        for i in light_on_times:
            if i[0] <= t <= i[1]:
                indoor_photo_dict["cosx"] = cosx
                indoor_photo_dict["secx"] = secx
                photolysis_J(indoor_photo_dict,photo_dict,J_dict)
                break
            else:
                indoor_photo_dict_off["cosx"] = cosx
                indoor_photo_dict_off["secx"] = secx
                photolysis_J(indoor_photo_dict_off,photo_dict,J_dict)
        
        #diurnal outdoor rates
        if diurnal == True:
            out_calc_dict["n"] = n
            out_calc_dict["cosx"] = cosx
            out_calc_dict["secx"] = secx
            outdoor_rates_calc(outdoor_dict,outdoor_dict_diurnal,out_calc_dict)
        
        #recalculate humidity,water
        h2o,rh = h2o_rh(t,temp,rel_humidity,numba_exp)
        calc_dict['h2o']=h2o
     
        #recalculate particle sums
        if particles == True:
            particle_dict = particle_calcs(part_calc_dict,density_dict)
            density_dict.update(particle_dict)
            
        #checks time, if between times set for a forced density change the rate
        #is applied to the specific species
        if timed_emissions == True:
            for key in timed_inputs:
                for i in timed_inputs[key]:
                    if i[0] <= t <= i[1]:
                        timed_dict["%s_timed" % key] = i[2]
                        break
                    else:
                        timed_dict["%s_timed" % key] = 0
        
        #recalculate reaction rates
        reaction_rate_dict=reaction_eval(reaction_number,J_dict,calc_dict,\
                                         density_dict,dt,reaction_compiled_dict,\
                                             outdoor_dict,surface_dict,\
                                                 timed_dict)
        
        #evaluate the mater array to recalculate concentrations
        dy_dict=dy_calc(master_compiled,reaction_rate_dict,calc_dict,density_dict,\
                        outdoor_dict,surface_dict,species,timed_dict)
        
        #output the new concentration values
        dy = [dy_dict[i] for i in species]
        return dy
    
    
    def dydy(t,y0): 
        '''
        The function to calculate the jacobian that is fed to the integrator
    
        inputs:
        	t = time
        	y0 = concentration of species
    
        returns:
        	dydy = array of change in species concentration with change 
        		   in other species concentrations
        '''
        #Update density dictionary
        for i in range(num_species):
            density_dict[species[i]]=y0[i]            
        density_dict['RO2']=ppool_density_calc(density_dict,ppool)
        
        #if summations are included they need to be updated to the density dictionary also            
        if summations == True:
            sums_dict = summations_eval(summations_dict,density_dict,calc_dict)
            density_dict.update(sums_dict)
        
        #n = time in seconds from midnight for each day
        n = t-((int(t/86400))*86400)
        
        # recalculate photolysis
        # COSX and SECX involve local hour angles dependant on position and time
        # of year (latitude of location and declination of sun)
    
        lha = (1+((n-time_correct)/4.32E+4))*pi     # local hour angle, radians. Midnight start
        cosx = ((numba_cos(lha)*cosld)+sinld)       # solar zenith angle 
        
        # Set negative cosx to zero and calculate the inverse  
        # (secx=1/cosx). The MCM photolysis parameterisation  
        # (http://mcm.leeds.ac.uk/MCM/parameters/photolysis_param.htt)  
        # requires cosx and secx to calculate the photolysis rates.
        if cosx <= 1E-30:
            cosx = 0.0  
            secx = 1.0E+30  
        else:  
            secx = 1.0 / (((cosx + numba_abs(cosx))/2)+1.0E-30) # no division by 0
        
        #updates the relevant dictionary whether lights are on or off
        for i in light_on_times:
            if i[0] <= t <= i[1]:
                indoor_photo_dict["cosx"] = cosx
                indoor_photo_dict["secx"] = secx
                photolysis_J(indoor_photo_dict,photo_dict,J_dict)
                break
            else:
                indoor_photo_dict_off["cosx"] = cosx
                indoor_photo_dict_off["secx"] = secx
                photolysis_J(indoor_photo_dict_off,photo_dict,J_dict)
        
        #diurnal outdoor rates
        if diurnal == True:
            out_calc_dict["n"] = n
            out_calc_dict["cosx"] = cosx
            out_calc_dict["secx"] = secx
            outdoor_rates_calc(outdoor_dict,outdoor_dict_diurnal,out_calc_dict)
        
        #recalculate temp,humidity,water
        h2o,rh = h2o_rh(t,temp,rel_humidity,numba_exp)
        calc_dict['h2o']=h2o
     
        #recalculate particle sums
        if particles == True:
            particle_dict = particle_calcs(part_calc_dict,density_dict)
            density_dict.update(particle_dict)
        
        #checks time, if between times set for a forced density change the rate
        #is applied to the specific species
        if timed_emissions == True:
            for key in timed_inputs:
                for i in timed_inputs[key]:
                    if i[0] <= t <= i[1]:
                        timed_dict["%s_timed" % key] = i[2]
                        break
                    else:
                        timed_dict["%s_timed" % key] = 0
                    
        #recalculate reaction rates
        reaction_rate_dict=reaction_eval(reaction_number,J_dict,calc_dict,density_dict,\
                                         dt,reaction_compiled_dict,outdoor_dict,\
                                             surface_dict,timed_dict)
        
        #recalculate jacobian
        dydy_jac=dy_dy_calc(dy_dy_dict,J_dict,calc_dict,density_dict,species,\
                            outdoor_dict,surface_dict,num_species,\
                                timed_dict,reaction_rate_dict)
        return dydy_jac
    
    def integrate_function(iters,t_bound_internal,y0,t0,ret,save_rate,num_species,\
                           total_iter,dt):
        '''
        Using lsoda to calculate density evolution and output as n_new
    
        inputs:
        	iters = number of iterations that have already been performed 
        			through the integrator, used to calculate when an output
        			is saved
        	t_bound_internal = the time to integrate to within this function (s)
        	y0 = initial species concentration
        	t0 = start time (s)
        	ret = integrator return code from scipy.integrate.ode.get_return_code
        		  set as 1 prior to calling the integrator
        	save_rate = how many iterations to perform before saving an output
        	num_species = the total number of species 
        	total_iter = the total number of iterations to be completed
        	dt = time step (s)
    
        returns:
        	dt_out = list of output times
        	n_new = array of output concentrations for each species at each time
        	iters = total number of iterations completed
        	ret = integrator return code from scipy.integrate.ode.get_return_code
        	iter_time = list of time stamps for the completion of each integration
        				over dt
        	calculated_output = dictionary of lists of calculated values for each
        						iteration. These are calculations done using the species
        						concentrations and are only for output purposes
        '''
        #assign arrays to populate
        n_new=[[] for i in range(num_species)]
        dt_out=[]
        iter_time=[]
        
        calculated_output = {}
        calculated_output['RO2'] = []
        if particles == True:
            calculated_output['tsp'] = []
            calculated_output['acidsum'] = []
            calculated_output['tspx'] = []
            calculated_output['mwomv'] = []
        for i in reactivity_dict:
            calculated_output[i] = []
        for i in production_dict:
            calculated_output[i] = []
        for i in J_dict:
            calculated_output[i] = []
        for i in outdoor_dict:
            calculated_output[i] = []
        if summations == True:
            for i in sums_dict:
                calculated_output[i] = []
        
        #set integrator args
        atol = [1e-6]*num_species     #Default 1e-6
        rtol = 1e-6                  #Default 1e-6
        first_step = 1e-10              #size of first integration step to try (s)
        nsteps = 5000                   #max number of internal timesteps
        
        #set the integrator and arguments
        r=ode(dydt,dydy).set_integrator('lsoda',atol=atol,rtol=rtol,first_step=\
                                        first_step,nsteps=nsteps)
        r.set_initial_value(y0,t0)
        
        #integrate
        while r.successful() and r.t<t_bound_internal:
            print('Iteration ', iters+1,'/', total_iter,'¦',r.t,' to ',r.t+dt)
            r.integrate(r.t+dt)
            iters=iters+1
            ret=r.get_return_code()
            if iters % save_rate == 0: #output every save_rate iterations
                dt_out.append(int(r.t))
                iter_time.append(timing.time()-start_time)
                calculated_output['RO2'].append(density_dict["RO2"])
                reactivity_calc(reactivity_dict,reactivity_compiled,reaction_rate_dict,\
                                calc_dict,density_dict)
                production_calc(production_dict,production_compiled,reaction_rate_dict,\
                                calc_dict,density_dict)
                for i in reactivity_dict:
                    calculated_output[i].append(reactivity_dict[i])
                for i in production_dict:
                    calculated_output[i].append(production_dict[i])
                if particles == True:
                    calculated_output['tsp'].append(density_dict['tsp'])
                    calculated_output['acidsum'].append(density_dict['acidsum'])
                    calculated_output['tspx'].append(density_dict['tspx'])
                    calculated_output['mwomv'].append(density_dict['mwomv'])
                for i in range(num_species):
                    n_new[i].append(r.y[i])
                for i in J_dict:
                    calculated_output[i].append(J_dict[i])
                for i in outdoor_dict:
                    calculated_output[i].append(outdoor_dict[i])
                if summations == True:
                    for i in sums_dict:
                        calculated_output[i].append(density_dict[i])
        return dt_out,n_new,iters,ret,iter_time,calculated_output
       
    '''
    numba functions to increase speed of mathamatical operations
    '''
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_exp(x):
        return np.exp(x)
    
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_cos(x):
        return np.cos(x)
    
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_arctan(x):
        return np.arctan(x)
    
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_sin(x):
        return np.sin(x)
    
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_arccos(x):
        return np.arccos(x)
    
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_sqrt(x):
        return np.sqrt(x)
    
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_abs(x):
        return np.abs(x)
    
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_log(x):
        return np.log(x)
    
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_log10(x):
        return np.log10(x)
        
    start_time=timing.time() #program start time
    
    '''
    setting the output folder in current working directory
    '''
    path=os.getcwd()
    now = datetime.datetime.now()
    output_folder = ("%s_%s" % (now.strftime("%Y%m%d_%H%M%S"), custom_name))
    os.mkdir('%s/%s' % (path,output_folder))
    with open('%s/__init__.py' % output_folder,'w') as f:
        pass
    
    print('Creating folder:', output_folder)
    
    '''
    Saving a copy of the settings and MCM files to the output folder
    '''
    from shutil import copyfile
    copyfile("settings.py", "%s/%s/settings.py" % (path,output_folder))
    copyfile(filename, "%s/%s/mcm.fac" % (path,output_folder))
    
    t_bound = t0+seconds_to_integrate #Maximum time to integrate to
    iters = 0 #the number of iterations that have been performed already (leave as 0)
    total_iter = math.ceil(int(t_bound-t0)/dt) #calculated to show the user how long is left   
    print('total iterations:', total_iter)
    
    
    '''
    calculate initial values
    '''
    h2o,rh = h2o_rh(t0,temp,rel_humidity,numba_exp)   
    
    species,ppool,rate_numba,reactions_numba=import_all(filename) #import from MCM download
    
    pi = 4.0*numba_arctan(1.0) #for photolysis and some rates
    
    # dictionary for evaluating the reaction rates
    calc_dict={'M':M,
           'numba_exp':numba_exp,
           'temp':temp,
           'numba_log10':numba_log10,
           'numba_sqrt':numba_sqrt,
           'H2O':h2o,
           'PI':pi,
           'HMIX':HMIX,
           'numba_abs':numba_abs}
    
    calc_dict.update(const_dict) # add constants from settings to calc_dict
    
    '''
    Particles
    '''
    particle_species=[]
    if particles == True:
        #if the full MCM is not being used then the calcuations for tsp and anything involving tsp
        #will fail so particles can only be used with the full MCM at the moment 04/2020
        particle_species, particle_reactions, particle_vap_dict, part_calc_dict = particle_import()
        species = species + particle_species #add particle species to species list
        reactions_numba = reactions_check(reactions_numba,particle_reactions,species)
        rate_numba = rate_numba + [['kacid' , '1.5e-32*numba_exp(14770/temp)']]
        calc_dict.update(particle_vap_dict)
    
    '''
    Custom reactions and rates. Those not in the MCM download, the code does not
    check this so please make sure you are not adding any reactions that already 
    exist as it will just duplicate them.
    '''
    sums = []
    if custom == True:
        custom_filename="custom_input.txt"
        custom_rates, custom_reactions, custom_species, custom_RO2, sums = \
            custom_import(custom_filename,species)
        # Check that rates/constants/RO2 have not been added as species
        custom_species = [item for item in custom_species
                          if item not in (['RO2'] + list(calc_dict.keys()) +
                                          [name[0] for name in rate_numba])]
        species = species + custom_species
        rate_numba = rate_numba + custom_rates
        reactions_numba = reactions_numba + custom_reactions
        ppool = ppool + custom_RO2
        copyfile("custom_input.txt", "%s/%s/custom_input.txt" % (path,output_folder))
     
    '''
    INCHEM reactions and rates that are not included in MCM download.
    '''    
    if INCHEM_additional == True:
        from modules.inchem_chemistry import INCHEM_RO2, INCHEM_reactions, \
            INCHEM_rates, INCHEM_sums
        INCHEM_species = INCHEM_species_calc(INCHEM_reactions,species)
        species = species + INCHEM_species
        ppool = ppool + INCHEM_RO2
        reactions_numba = reactions_numba + INCHEM_reactions
        rate_numba = rate_numba + INCHEM_rates
        sums.extend(INCHEM_sums)
        '''
        Write INCHEM inputs to output folder for future reference
        '''
        with open("%s/%s/INCHEM_inputs.txt" % (path,output_folder), 'w') as f:
            f.write('Species:\n')
            for i in INCHEM_species:
                f.write("%s\n" % i)
            f.write('RO2 species:\n')
            for i in INCHEM_RO2:
                f.write("%s\n" % i)
            f.write('Summations:\n')
            for i in INCHEM_sums:
                f.write("%s\n" % i)
            f.write('Rates:\n')
            for i in INCHEM_rates:
                f.write("%s\n" % i)
            f.write('Reactions:\n')
            for i in INCHEM_reactions:
                f.write("%s\n" % i)
    
    '''
    Additional clean up, checking for summations from custom inputs
    '''
    summations = False
    if custom == True or INCHEM_additional == True:
        if len(sums) >= 1:
            summations = True
           
    reaction_number=[]
    for i in range(len(reactions_numba)): #for assigning within the master array
        reaction_number.append('r%s' % i)
        
    #if it's in the calc dict it shouldn't be calculated in any of the integrations
    for i in calc_dict.keys():
        if i in species: 
            species.remove(i)
        for j in rate_numba:
            if j[0] == i:
                rate_numba.remove(j)
                print("%s from custom_input.txt ignored. Defined elsewhere." % i)
    
    
    '''
    Photolysis
    
    The simulation works on solar time of day and does not require any input 
    of longitude. However, if a comparison is being done with measured data then
    the time_correct variable can be used to shift the photolysis a number of
    seconds in either direction, this will also shift the outdoor photolysis
    used in some of the outdoor concentration calculations. Not all of the
    outdoor concentrations rely on this method of calculation so adjustments
    must also be made to any other outdoor rates and thus I do not recommend 
    using this method. I would instead adjust the full output after the run.
    '''
    #calculations for determining solar position given time of year    
    day, month, year = map(int, date.split('-'))
    date = datetime.date(year, month, day)
    year_day = (date - datetime.date(year, 1, 1)).days + 1
    days_in_year = (datetime.date(year,12,31) - datetime.date(year, 1, 1)).days + 1
    radian = 180.0/pi
    dec = -23.45 * np.cos(((360/days_in_year)/radian)*(year_day+10))
    
    lat = lat/radian #conversion to radians
    dec = dec/radian #conversion to radians
    
    time_correct = 0 #adjustment for correction of solar time to measured time
    
    #calculations for spherical law of cosines for solar zenith angle
    sinld = numba_sin(lat)*numba_sin(dec)
    cosld = numba_cos(lat)*numba_cos(dec)
    
    photo_dict=Zixu_photolysis_compiled() #compiled equations
    
    #full dictionary of attenuation factors for different lights/glass
    light_dict=Zixu_photolysis(numba_abs,numba_exp) 
    
    
    indoor_photo_dict={**light_dict[light_type],**light_dict[glass]}
    indoor_photo_dict_off={**light_dict["off"],**light_dict[glass]}
    
    n = t0-((int(t0/86400))*86400) # keeps time within 24 hour cycle 
    
    # COSX and SECX involve local hour angles dependant on position and time
    # of year (latitude of location and declination of sun)
    lha = (1+((n-time_correct)/4.32E+4))*pi    # local hour angle, radians. Midnight start
    cosx = ((numba_cos(lha)*cosld)+sinld) # solar zenith angle
     
    # (http://mcm.leeds.ac.uk/MCM/parameters/photolysis_param.htt)
    # Keep cosx 0 or positive, we don't have negative photolysis
    if cosx <= 1E-30:
        cosx = 0.0  
        secx = 1.0E+30  
    else:  
        secx = 1.0 / (((cosx + numba_abs(cosx))/2)+1.0E-30)
    
    light_on_times = [[j * 3600 for j in i]for i in light_on_times] #conversion to seconds
    
    J_dict = {}
    for i in light_on_times:
        if i[0] <= t0 <= i[1]:
            indoor_photo_dict["cosx"] = cosx
            indoor_photo_dict["secx"] = secx
            photolysis_J(indoor_photo_dict,photo_dict,J_dict)
            break
        else:
            indoor_photo_dict_off["cosx"] = cosx
            indoor_photo_dict_off["secx"] = secx
            photolysis_J(indoor_photo_dict_off,photo_dict,J_dict)
    
    '''
    Outdoor species concentration calculations
    '''        
    out_calc_dict = {"numba_abs":numba_abs,
                     "numba_exp":numba_exp,
                     "numba_cos":numba_cos,
                     "numba_sin":numba_sin,
                     "n":n,
                     "cosx":cosx,
                     "secx":secx}
    
    #Outdoor dictionaries
    outdoor_dict=outdoor_rates(AER,particles,species)
    if diurnal == True:
        outdoor_dict_diurnal = outdoor_rates_diurnal(city)
        outdoor_rates_calc(outdoor_dict,outdoor_dict_diurnal,out_calc_dict)
        #diurnal rates will overide static rates if species shown in both
    
    '''
    Surface deposition
    '''
    surface_dict=surface_deposition(HMIX)
    for specie in species:
        if particles == True and specie in particle_species:
            surface_dict['%s_SURF' % specie]=0.004*HMIX
        elif '%s_SURF' % specie not in surface_dict.keys():
            surface_dict['%s_SURF' % specie]=0
    
    '''
    timed concentrations
    '''
    timed_dict={}
    if timed_emissions == True:
        for specie in species:
            timed_dict["%s_timed" % specie] = 0
        for key in timed_inputs:
            if key in species:
                for i in timed_inputs[key]:
                    if i[0] <= t0 <= i[1]:
                        timed_dict["%s_timed" % key] = i[2]
                        break
                    else:
                        timed_dict["%s_timed" % key] = 0
            else:
                print('%s not found in species list (timed input)' % key)
    
    '''
    importing initial concentrations
    '''
    density_dict,calc_dict = initial_conditions(initial_conditions_gas,M,species,\
                                                rate_numba,calc_dict,particles,\
                                                    initials_from_run,t0,path)
    density_dict['RO2']=ppool_density_calc(density_dict,ppool)
    
    #calculating t0 summations
    summations_dict={}
    if summations == True:
        summations_dict = summations_compile(sums)
        sums_dict={}
        sums_dict=summations_eval(summations_dict,density_dict,calc_dict)
        density_dict.update(sums_dict)
    
    if particles == True:
        particle_dict = particle_calcs(part_calc_dict,density_dict)
        density_dict.update(particle_dict)
    
    '''    
    saving initial conditions to an output directory for reference
    '''
    f = open("%s/%s/initial_concentrations.txt" % (path,output_folder),"w")
    for i in species:
        f.write('%s=%s ;\n' % (i,density_dict[i]))
    f.close()
    
    '''
    Calculating the reaction rates and compiling the master array of ODEs
    '''
    num_species=len(species) #some calculations ask for the number of species
    #better to calculate it once rather than every time
    
    reaction_compiled_dict=reaction_rate_compile(reactions_numba,reaction_number)
    reaction_rate_dict=reaction_eval(reaction_number,J_dict,calc_dict,density_dict,\
                                     dt,reaction_compiled_dict,outdoor_dict,\
                                         surface_dict,timed_dict)
    
    #creating the master array
    master_array_dict=master_calc(reactions_numba,species,reaction_number,particles,\
                                  particle_species,timed_emissions)
    
    #saving the master array to the output folder
    with open('%s/%s/master_array.pickle' % (path,output_folder),'wb') as handle:
        pickle.dump(master_array_dict,handle)
    
    #compiling the master array
    master_compiled=master_compiler(master_array_dict,species)
    
    #Create the jacobian and save it to the output folder
    write_jacobian_build(master_array_dict,species,output_folder,path)
    
    #import the jacobian function to create the jacobian dictionary which is a
    #dictionary of compiled calculations
    spec = importlib.util.spec_from_file_location("jac.jacobian_calc",\
                                                  "%s/%s/Jacobian.py" % (path,output_folder))
    jac = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(jac)
    #jac = importlib.import_module(path+output_folder+".Jacobian")
    dy_dy_dict=jac.jacobian_calc(species) 
    
    # reactivity and production calculations, details in the reactivity.py script
    reactivity_compiled, production_compiled = reactivity_summation(master_array_dict)
    reactivity_dict = {}
    reactivity_calc(reactivity_dict,reactivity_compiled,reaction_rate_dict,calc_dict,\
                    density_dict)
    production_dict = {}
    production_calc(production_dict,production_compiled,reaction_rate_dict,calc_dict,\
                    density_dict)
     
    '''
    #Integration
    '''
    #Create an array of concentrations to be updated during the integration. This
    #can then be used to repopulate the dictionaries with updated values
    y0=[[] for i in range(num_species)]     
    for i in range(num_species):    
        y0[i]=density_dict[species[i]]
    
    #Create arrays for storing the output. 
    n_new=np.array([[y0[i]] for i in range(num_species)])
    dt_out=np.array([])
    dt_out=np.append(dt_out,int(t0)) 
    iter_time_tot=[timing.time()-start_time]
    calculated_output_tot = {}
    calculated_output_tot['RO2'] = [density_dict['RO2']]
    if particles == True:
        calculated_output_tot['tsp'] = [density_dict['tsp']]
        calculated_output_tot['acidsum'] = [density_dict['acidsum']]
        calculated_output_tot['tspx'] = [density_dict['tspx']]
        calculated_output_tot['mwomv'] = [density_dict['mwomv']]
    for i in reactivity_dict:
        calculated_output_tot[i] = [reactivity_dict[i]]
    for i in production_dict:
        calculated_output_tot[i] = [production_dict[i]]
    for i in J_dict:
        calculated_output_tot[i] = [J_dict[i]]
    for i in outdoor_dict:
        calculated_output_tot[i] = [outdoor_dict[i]]
    if summations == True:
        for i in sums_dict:
            calculated_output_tot[i] = [density_dict[i]]
    
    ret=1 #if ret=2 success. ODE return code
    
    print('Integration starting')
    
    with threadpool_limits(limits=4, user_api='blas'): #limits threads used by integration
        while iters < total_iter and ret > 0:  
                n_new_in = n_new[:,-1]
                dt_out_in = dt_out[-1]
                dt_out_temp,n_new_temp,iters,ret,iter_time,calculated_output=\
                    integrate_function(iters,t_bound,n_new_in,dt_out_in,ret,save_rate,\
                                       num_species,total_iter,dt)
                dt_out=np.append(dt_out,dt_out_temp)
                n_new=np.append(n_new,n_new_temp,axis=1)
                iter_time_tot.extend(iter_time)
                for x in calculated_output:
                    calculated_output_tot[x].extend(calculated_output[x])
                
    output_data = pd.DataFrame(np.transpose(n_new),columns=species,index=dt_out)
    output_data = output_data.join(pd.DataFrame(calculated_output_tot,index=dt_out))
    
    integration_times = pd.DataFrame(np.transpose(iter_time_tot),index=dt_out)
    
    end_time=timing.time()
    delta = datetime.timedelta(seconds=(end_time-start_time))
    print('Return code:', ret) #ODE return code
    print('Total run time =', str(delta - datetime.timedelta(microseconds=delta.microseconds)))
    
    print('Saving output')
    
    # saves all of the output data to the output folder
    with open('%s/%s/out_data.pickle' % (path,output_folder),'wb') as handle:
        pickle.dump(output_data,handle)  
        
    #saves times for integrating each time step to a csv, useful for
    #analysing slow points in the system
    integration_times.to_csv("%s/%s/integration_times.csv" % (path,output_folder))
    print('Output saved')
    if output_graph == True:
        # creates and saves a simple graph of the set species from settings
        import matplotlib.pyplot as plt
        from itertools import cycle
        plt.figure(dpi=600,figsize=(8,4))
        colour=iter(plt.cm.gist_rainbow(np.linspace(0,1,len(output_species))))
        linestyle=cycle(['solid','dotted','dashed','dashdot'])
        for x in output_species:
            c=next(colour)
            l=next(linestyle)
            plt.plot(output_data.index/3600,output_data[x],label=x,c=c,linestyle=l)
        plt.yscale("log")
        plt.legend(loc='upper center', bbox_to_anchor=(0.45, -0.15),
          fancybox=True, shadow=True, ncol=6)
        plt.xlabel("Time of day (hours)")
        plt.ylabel("Concentration (molecules/cm\N{SUPERSCRIPT THREE})")
        plt.savefig('%s/%s/graph.png' % (path,output_folder), bbox_inches='tight')

        # additionally saves a csv of these set species for easy analysis
        output_data.to_csv("%s/%s/output.csv" % (path,output_folder), columns = output_species)

        plt.show()

    return None

