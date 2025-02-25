# -*- coding: utf-8 -*-
"""
Additional tools for importing and interpolating an input file of concentrations
with time. Also for updating internal dictionaries with these concentrations.

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
from scipy.interpolate import interp1d
import pandas as pd
from shutil import copyfile

def constraints_import(constrained_file, output_folder, dt):
    '''
    For updating the required dictionaries of concentrations and variables with
    interpolated input variables from the MOCCIE input file.
    
    inputs:
        constrained_file = filename of input MOCCIE .csv file
        output_folder = name of output directory
        dt = simulation time step
    
    returns:
        interp_inputs = dictionary of interpolated inputs
        constrained_variables = list of constrained variables and species. Column titles
                                from input .csv
        seconds_to_integrate = the number of seconds to integrate over
        t0 = time to begin integration (s)
    '''
    copyfile(constrained_file, "%s/constrained_import.csv" % output_folder)  
    constrained_df = pd.read_csv(constrained_file,index_col=0)
    constrained_variables = list(constrained_df.columns)
    interp_inputs = {}
    for i in constrained_variables:
        interp_inputs[i] = interp1d(constrained_df.index,constrained_df[i])
    seconds_to_integrate = (constrained_df.index[-1]-constrained_df.index[0])-dt
    t0 = constrained_df.index[0]
    return interp_inputs, constrained_variables, seconds_to_integrate, t0


def constrained_update(time, interp_inputs, constrained_variables, constrained_J, constrained_species,
                  constrained_out, calc_dict, J_dict, outdoor_dict, constrained_rates,rh):
    '''
    For updating the required dictionaries of concentrations and variables with
    interpolated input variables from the MOCCIE input file.
    
    inputs:
        time = simulation time (s)
        interp_inputs = dictionary of interpolated constrained inputs
        constrained_variables = list of constrained variables and species. Column titles
                         from input .csv
        constrained_J = list of photolysis J names from constrained input
        constrained_species = list of species names from constrained input
        constrained_out = list of outdoor species names from constrained input
        calc_dict = dictionary of constants and variables for use in calculations
        J_dict = dictionary of current photolysys values
        outdoor_dict = dictionary of outdoor species concentrations
        rh = relative humidity (%)
    
    returns:
        None
    '''
    if 'temp' in constrained_variables:
        calc_dict['temp'] = float(interp_inputs['temp'](time))
    if 'rh' in constrained_variables:
        #calc_dict['rel_humidity'] = float(interp_inputs['rh'](time))
        rh = float(interp_inputs['rh'](time))
    if 'H2O' in constrained_variables:
        calc_dict['H2O'] = float(interp_inputs['H2O'](time))
    else:
        calc_dict['H2O'] = 6.1078*calc_dict['numba_exp'](-1.0e+0*(597.3-0.57*\
                           (calc_dict['temp']-273.16))*18.0/1.986*\
                           (1.0/calc_dict['temp']-1.0/273.16))*10./\
                           (1.38e-16*calc_dict['temp'])*rh
    
    for i in constrained_species:
        calc_dict[i] = float(interp_inputs[i](time))
    for i in constrained_J:
        J_dict[i] = float(interp_inputs[i](time))
    for i in constrained_out:
        outdoor_dict[i] = float(interp_inputs[i](time))
    for i in constrained_rates:
        calc_dict[i] = float(interp_inputs[i](time))
    return None