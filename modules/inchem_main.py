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
def run_inchem(filename, particles, INCHEM_additional, custom, rel_humidity,
               M, const_dict, ACRate_dict, diurnal, city, date, lat, light_type, 
               light_on_times, glass, volume, initials_from_run,
               initial_conditions_gas, timed_emissions, timed_inputs, dt, t0,
               seconds_to_integrate, custom_name, output_graph, output_species,
               reactions_output, H2O2_dep, O3_dep, adults, children,
               surface_area, settings_file, temperatures, spline, custom_filename,
               constrained_file):
  
    '''
    import all modules
    '''
    import sys
    import pickle
    from modules.inchem_import import import_all, custom_import 
    from modules.particle_input import particle_import, particle_calcs, reactions_check, HOMS_chemistry,\
        particle_calc_dict
    from modules.photolysis import photolysis_J, Zixu_photolysis, Zixu_photolysis_compiled
    from modules.initial_dictionaries import initial_conditions, master_calc, master_compiler,\
        reaction_rate_compile, reaction_eval, construct_jacobian, INCHEM_species_calc, timed_import
    from modules.outdoor_concentrations import outdoor_rates, outdoor_rates_diurnal, outdoor_rates_calc,\
        ACRate_updater
    from modules.constraints import constraints_import, constrained_update
    from modules.inchem_main_class import InChemPyMainClass
    import numpy as np
    import numba as nb
    from scipy.integrate import ode
    from scipy import interpolate
    import time
    from modules.surface_dictionary import surface_deposition, O3_deposition, H2O2_deposition, breath_emissions
    from threadpoolctl import threadpool_limits
    #import importlib.util
    import pandas as pd
    import os
    import datetime
    import math
    import time as timing
    from modules.reactivity import reactivity_summation, reactivity_calc, production_calc
    import bisect
    
    sys.setrecursionlimit(4000) #to compile the master array the recursion limit
    #must be increased as some of the evaluated ODEs are greater than the usual
    #system limit
    
    
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
    copyfile(settings_file, "%s/%s/%s_settings.py" % (path,output_folder,custom_name))
    copyfile(filename, "%s/%s/mcm.fac" % (path,output_folder))
    
        
    '''
    Custom reactions and rates. Those not in the MCM download, the code does not
    check this so please make sure you are not adding any reactions that already 
    exist as it will just duplicate them.
    '''
    if custom == True:
        copyfile("custom_input.txt", "%s/%s/custom_input.txt" % (path,output_folder))

    inchem_py_runner = InChemPyMainClass(filename, INCHEM_additional, particles, constrained_file,
                                         output_folder, dt, volume, surface_area,
                                         const_dict, H2O2_dep, O3_dep, custom, timed_emissions, timed_inputs,
                                         custom_filename)


    '''
    Write INCHEM inputs to output folder for future reference
    '''   
    if INCHEM_additional == True:
        from modules.inchem_chemistry import INCHEM_RO2, INCHEM_reactions, \
            INCHEM_rates, INCHEM_sums
        INCHEM_species = INCHEM_species_calc(INCHEM_reactions, inchem_py_runner.species)
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
    
    

    
    if reactions_output == True:
        ###
        # Saving a dictionary of reactions and their numbers
        reactions_save={}
        for i,x in enumerate(inchem_py_runner.reactions_numba):
            reactions_save[inchem_py_runner.reaction_number[i]]=x
            
        with open('%s/reactions.pickle' % output_folder,'wb') as handle:
            pickle.dump(reactions_save,handle)
        ###
    
    
    #saving the master array to the output folder
    with open('%s/%s/master_array.pickle' % (path,output_folder),'wb') as handle:
        pickle.dump(inchem_py_runner.master_array_dict,handle)
    
    output_data, integration_times = inchem_py_runner.run(t0, seconds_to_integrate, dt, timed_emissions,
                                                          timed_inputs, spline, temperatures, rel_humidity, M, light_type,
                                                          glass, diurnal, city, date, lat, ACRate_dict, light_on_times, const_dict,
                                                          initial_conditions_gas, initials_from_run, path, adults, children,
                                                          output_folder, reactions_output)

    
    
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
        plt.figure(dpi=300,figsize=(8,4))
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

