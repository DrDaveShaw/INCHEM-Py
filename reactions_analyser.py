# -*- coding: utf-8 -*-
"""
Reaction calculater for INCHEM-Py. 
A detailed description of this file can be found within the user manual.

Copyright (C) 2019-2021 
David Shaw : david.shaw@york.ac.uk
Nicola Carslaw : nicola.carslaw@york.ac.uk

All rights reserved.

This file is additional to INCHEM-Py.

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

This script uses the master_array.pickle, out_data.pickle, reactions.pickle and
the surface_dictionary.py to give a csv file containing the actual rates of production
or loss rate of a species due to a specific reaction.
"""

#import required packages
import pickle
import os
import pandas as pd

def data_import(out_directory):
    '''
    inputs
        out_directory : the output folder created by INCHEM-Py
    
    outputs
        master_array : the unpickled master array
        reactions : the unpickled reaction rate coefficients
        out_data : the unpickled species concentration with time created by 
                    INCHEM-Py
    '''
    with open("%s/out_data.pickle" % out_directory,'rb') as handle:
        out_data=pd.read_pickle(handle)
            
    with open("%s/reactions.pickle" % out_directory,'rb') as handle:
        reactions=pd.read_pickle(handle)
            
    with open("%s/master_array.pickle" % out_directory,'rb') as handle:
        master_array=pd.read_pickle(handle)
    return master_array, reactions, out_data

def reactions_output(output_folder, out_directory, species, master_array,
                     reactions, out_data, time_index,
                     surface_dict_path, timed_emissions,
                     timed_inputs,H2O2_dep, O3_dep):
    '''

    Parameters
    ----------
    output_folder : string
        The name of the folder to save the csv of reaction rates to.
    out_directory : string
        The name of the folder created by INCHEM-Py when running the model
        that contains the outputs from the model.
    species : string
        Name of the species for which reaction rates should be calculated in
        MCM format.
    master_array : dict
        dictionary of arrays of reactions that can be reduced
        to form the system of ODEs to be solved within INCHEM-Py.
    reactions : dict
        the unpickled reaction rate coefficients.
    out_data : dict
        the unpickled species concentration with time created by INCHEM-Py.
    time_index : float
        Time of simulation, in seconds, for which to calculate the reaction
        rates. Must be divisible by dt from the INCHEM-Py simulation.
    surface_dict_path : string
        File path to the surface dictionary used for the simulation being analysed.
        Can be absolute or ralative to this file.
    timed_emissions : boolean
        Are timed emissions being used?
    timed_inputs : dict
        Timed emissions from the settings.py file of the simulation being analysed.
    H2O2_dep : boolean
        Are H2O2 deposition reactions being used?
    O3_dep : boolean
        Are O3 deposition reactions being used?

    Returns
    -------
    df : pandas dataframe
        dataframe containing the actual rates of production or loss rate of a 
        species due to a specific reaction. Is exported to a csv.
    spec_calc : dict
        Full rates of reaction for each species in the master array at time_index.

    '''
    #get the current working directory and create the output folder 
    #if it doesn't exist        
    path=os.getcwd()
    if not os.path.exists('%s/%s' % (path,output_folder)):
        os.mkdir('%s/%s' % (path,output_folder))
        
    #import surface
    import importlib.util
    spec = importlib.util.spec_from_file_location("surface_dictionary", surface_dict_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    surface_dict = foo.surface_deposition(out_data['AV'],H2O2_dep, O3_dep)  
    
    if '%s_SURF' % species not in surface_dict.keys():
        surface_dict['%s_SURF' % species] = 0
    
    #extract time point concentrations/rates
    time_data = {}  
    for i in out_data.keys():
        time_data[i] = out_data[i][time_index]   

    for i in surface_dict:
        try:
            time_data[i] = surface_dict[i][time_index]
        except:
            time_data[i] = surface_dict[i]
            
    if '%sOUT' % species not in time_data.keys():
        time_data['%sOUT' % species] = 0
        
    if timed_emissions == True:
        for specie in out_data.keys():
            time_data["%s_timed" % specie] = 0
        for key in timed_inputs:
            if key in out_data.keys():
                for i in timed_inputs[key]:
                    if i[0] <= time_index <= i[1]:
                        time_data["%s_timed" % key] = i[2]
                        break
                    else:
                        time_data["%s_timed" % key] = 0

    
    spec_calc = {i[0] : eval("*".join(i[:]),{},time_data) for i in master_array[species]}
    

    df = pd.DataFrame(index=spec_calc.keys())
    df['rate (molecules cm$^{-3}$ s$^{-1}$)'] = df.index.map(spec_calc)
    df['temp'] = df.index.map(reactions)
    df[['rate coefficient','reaction']] = df['temp'].apply(pd.Series)
    del df['temp']
    
    #create and save csvs
    df.to_csv('%s/%s_%s_%s.csv' % (output_folder,species,time_index,out_directory))
    return df, spec_calc

#########################################################################
if __name__ == "__main__":
    #Edit below this bit!
    
    #folder to save csv and png graphs to output_folder. Can already exist or
    #it will be created
    output_folder = "output_folder"
    
    #directories of data to extract
    out_directory = 'INCHEM-Py_output_folder'
    
    #species to extract
    species='HCHO'
    
    #import all dataframes
    master_array, reactions, out_data = data_import(out_directory)
    
    #time index of out_data to analyse rates
    time_index = out_data['HCHO'].idxmax() #<-- calcs the time index at peak
    
    
    # surface dictionary needs to be from the version of the model used to create the 
    # out_directory. 
    surface_dict_path = 'modules/surface_dictionary.py'
    
    # The below inputs need to be the same as from the settings file of the INCHEM-Py
    # simulation. 
    timed_emissions = False
    timed_inputs = {"LIMONENE":[[46800,47400,5e8],[107600,108000,5e8]],
                    "BPINENE":[[46800,47400,5e8]]}
    
    H2O2_dep = True
    O3_dep = True

#########################################################################

df, spec_calc = reactions_output(output_folder, out_directory, species, master_array,
                     reactions, out_data, time_index, surface_dict_path, timed_emissions,
                     timed_inputs,H2O2_dep, O3_dep)