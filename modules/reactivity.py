# -*- coding: utf-8 -*-
"""
Functions to calculate reactivity and production rates of species for INCHEM-Py.
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
def reactivity_summation(master_array_dict):
    '''
    Takes the master array and calculates summations for reactivity.
    The total reactivity of a speacies is the inverse of the lifetime 
    of the species and is calculated by summing the reactivity for each
    chemical species with the reactivity species. Production is the 
    other side of this where the rate of production of the species can be
    calculated.
    
    inputs:
        master_array_dict = dictionary of arrays of reactions that can be reduced
                            to form the system of ODEs to be solved
                            
    returns:
        reactivity_compiled = dictionary of the compiled reactivity equations 
                              for the specified reactivity species
        production_compiled = dictionary of the compiled production equations 
                              for the specified reactivity species
    '''
    reactivity_species = ['OH']
    reactivity_compiled = {}
    for species in reactivity_species:
        x = []
        try:
            for i in master_array_dict[species]:
                if "-1" in i:
                    if "ACRate" not in i:
                        if "%s_SURF" % species not in i:
                            if "%s_timed" % species not in i:
                                i = list(filter((species).__ne__, i))
                                x.append('*'.join(i))
            if len(x) > 0:
                reactivity = '+'.join(x)
                reactivity_compiled[species] = compile(reactivity,'<string>','eval')
        except KeyError:
            continue
     
    production_compiled = {}
    for species in reactivity_species:
        x = []
        try:
            for i in master_array_dict[species]:
                if "-1" not in i:
                    if "ACRate" not in i:
                        if "%s_SURF" % species not in i:
                            if "%s_timed" % species not in i:
                                i = list(filter((species).__ne__, i))
                                x.append('*'.join(i))
            if len(x) > 0:
                production = '+'.join(x)
                production_compiled[species] = compile(production,'<string>','eval')
        except KeyError:
            continue        
    
    return reactivity_compiled, production_compiled


def reactivity_calc(reactivity_dict,reactivity_compiled,reaction_rate_dict,calc_dict,density_dict):
    """
    Evaluates the reactiivity equations
    
    inputs:
        reactivity_dict = Dictionary of reactivity values to be updated
        reactivity_compiled = dictionary of the compiled reactivity equations 
                              for the specified reactivity species
        reaction_rate_dict = dictionary of reaction rate values at current time
        calc_dict = dictionary of constants and variables for use in calculations
        density_dict = dictionary of current concentrations
    """
    full_dict={**reaction_rate_dict,**calc_dict,**density_dict}
    for species in reactivity_compiled.keys():
        reactivity_dict['%s_reactivity' % species] = eval(reactivity_compiled[species],{},full_dict)*(-1)
    return None

def production_calc(production_dict,production_compiled,reaction_rate_dict,calc_dict,density_dict):
    '''
    Evaluates the production equations
    
    inputs:
        production_dict = Dictionary of reactivity values to be updated
        production_compiled = dictionary of the compiled production equations 
                              for the specified reactivity species
        reaction_rate_dict = dictionary of reaction rate values at current time
        calc_dict = dictionary of constants and variables for use in calculations
        density_dict = dictionary of current concentrations
    '''
    full_dict={**reaction_rate_dict,**calc_dict,**density_dict}
    for species in production_compiled.keys():
        production_dict['%s_production' % species] = eval(production_compiled[species],{},full_dict)
    return None