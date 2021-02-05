#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Importing the mcm subset download for facsimile and formatting them for use
within the INCHEM-Py.
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
import itertools
import copy

def speciesin(filename):
    '''
    Imports species names as list from MCM download
    
    inputs:
        filename = name of mcm download file
        
    returns:
        species = list of species
    '''
    species_in=[]
    with open(filename,'r') as file:
        line = file.readline()
        start = 'VARIABLE'
        end = '******************************************************'
        started = False
        for line in file:
            if start in line:
                started = True
            elif end in line:
                started = False
            if started == True and start not in line:
                species_in.append(line.split(' '))
                
    species=list(itertools.chain(*species_in))
    #species.pop(0)
    species.pop(-1)
    
    del species_in
    
    for i in range(len(species)):
        species[i]=species[i].rstrip()
    return species


def rate_coeff(filename):
    '''
    Import generic and complex rate coefficients as list
    
    inputs:
        filename = name of mcm download file
        
    returns:
        rates_in = list of generic and complex rate coefficient calculations
    '''        
    rates_in=[]
    with open(filename,'r') as file:
        line = file.readline()
        start = 'Generic Rate Coefficients'
        end = 'Complex reactions'
        started = False
        for line in file:
            if start in line:
                started = True
            elif end in line:
                started = False
            if '*;' in line:
                pass
            elif started == True and start not in line:
                rates_in.append(line.strip(' ;\n'))
    
    with open(filename,'r') as file:
        line = file.readline()
        start = 'Complex reactions'
        end = '******************************************************'
        started = False
        for line in file:
            if start in line:
                started = True
            elif end in line:
                started = False
            if '*;' in line:
                pass
            elif started == True and start not in line:
                rates_in.append(line.strip(' ;\n'))
                
    for i in range(len(rates_in)):
        rates_in[i]=rates_in[i].split(' = ')           
        '''
        Reactions and rates need converting into maths that will be understood
        by python.
        '''
        rates_in[i][1]=rates_in[i][1].replace('@','**')
        rates_in[i][1]=rates_in[i][1].replace('LOG10','log10')
        rates_in[i][1]=rates_in[i][1].replace('EXP','exp')
        rates_in[i][1]=rates_in[i][1].replace('SQRT','sqrt')
        rates_in[i][1]=rates_in[i][1].replace('D-','e-')
        rates_in[i][1]=rates_in[i][1].replace('D+','e+')
        rates_in[i][1]=rates_in[i][1].replace('D1','e+1')
        rates_in[i][1]=rates_in[i][1].replace('D2','e+2')
        rates_in[i][1]=rates_in[i][1].replace('D3','e+3')
        rates_in[i][1]=rates_in[i][1].replace('D4','e+4')
        rates_in[i][1]=rates_in[i][1].replace('D5','e+5')
        rates_in[i][1]=rates_in[i][1].replace('D6','e+6')
        rates_in[i][1]=rates_in[i][1].replace('D7','e+7')
        rates_in[i][1]=rates_in[i][1].replace('D8','e+8')
        rates_in[i][1]=rates_in[i][1].replace('D9','e+9')
        #rates_in[i][1]=rates_in[i][1].replace(' ','')
    return rates_in
            
    
def ppool_in(filename):
    '''
    Import peroxy radical summation as list
    
    inputs:
        filename = name of mcm download file
        
    returns:
        ppool = List of RO2 species for RO2 summation
    '''
    ppool_in=[]       
    with open(filename,'r') as file:
        line = file.readline()
        start = 'Peroxy radicals'
        end = 'Reaction definitions'
        started = False
        for line in file:
            if start in line:
                started = True
            elif end in line:
                started = False
            if '*' in line:
                pass
            elif started == True and start not in line:
                ppool_in.append(line.split(' + '))
            
    ppool = list(itertools.chain(*ppool_in))
    del ppool_in


    ppool[0]=ppool[0].replace('RO2 = ','')
    for i in range(len(ppool)):
        ppool[i]=ppool[i].strip()
        ppool[i]=ppool[i].strip('+')
        ppool[i]=ppool[i].strip(';')
        ppool[i]=ppool[i].strip(' ')
        
    ppool = list(filter(None, ppool))
    return ppool


def reactionslist(filename):
    '''
    Import reactions as list
    
    inputs:
        filename = name of mcm download file
    
    returns:
        reactions_in = list of reactions 
    '''
    reactions_in=[]
    with open(filename,'r') as file:
        line = file.readline()
        start = 'Reaction definitions.'
        end = 'End of Subset'
        started = False
        for line in file:
            if start in line:
                started = True
            elif end in line:
                started = False
            if '*;' in line:
                pass
            elif started == True and start not in line:
                if '%' in line:
                    reactions_in.append(line)
                else:
                    reactions_in[-1] = reactions_in[-1] + line
                    
    for i in range(len(reactions_in)):
        reactions_in[i]=reactions_in[i].strip('%')
        reactions_in[i]=reactions_in[i].strip()
        reactions_in[i]=reactions_in[i].strip(' ; ')
        reactions_in[i]=reactions_in[i].split(' : ')
        '''
        Reactions and rates need converting into maths that will be understood
        by python.
        '''
        reactions_in[i][0]=reactions_in[i][0].replace('@','**')
        reactions_in[i][0]=reactions_in[i][0].replace('LOG10','log10')
        reactions_in[i][0]=reactions_in[i][0].replace('EXP','exp')
        reactions_in[i][0]=reactions_in[i][0].replace('SQRT','sqrt')
        reactions_in[i][0]=reactions_in[i][0].replace('D-','e-')
        reactions_in[i][0]=reactions_in[i][0].replace('D+','e+')
        reactions_in[i][0]=reactions_in[i][0].replace('D1','e+1')
        reactions_in[i][0]=reactions_in[i][0].replace('D2','e+2')
        reactions_in[i][0]=reactions_in[i][0].replace('D3','e+3')
        reactions_in[i][0]=reactions_in[i][0].replace('D4','e+4')
        reactions_in[i][0]=reactions_in[i][0].replace('D5','e+5')
        reactions_in[i][0]=reactions_in[i][0].replace('D6','e+6')
        reactions_in[i][0]=reactions_in[i][0].replace('D7','e+7')
        reactions_in[i][0]=reactions_in[i][0].replace('D8','e+8')
        reactions_in[i][0]=reactions_in[i][0].replace('D9','e+9')
        reactions_in[i][0]=reactions_in[i][0].replace('<','')
        reactions_in[i][0]=reactions_in[i][0].replace('>','')
        reactions_in[i][0]=reactions_in[i][0].replace(' ','')
        reactions_in[i][1]=reactions_in[i][1].replace('\n','')         
    return reactions_in

def numba_rate(rates_in):
    '''
    Conversion of rates from MCM facsimile download to numba format
    
    inputs:
        rates_in = list of generic and complex rate coefficient calculations
        
    returns:
        numba_rates_in = list of generic and complex rate coefficient calculations
                         with numba functions replacing regular functions
    '''
    numba_rates_in=copy.deepcopy(rates_in)
    
    for rate in numba_rates_in:
        rate[1]=rate[1].replace('exp','numba_exp')
        rate[1]=rate[1].replace('log10','numba_log10')
        rate[1]=rate[1].replace('TEMP','temp')  
        rate[1]=rate[1].replace('sqrt','numba_sqrt')
    return numba_rates_in


def numba_reactions(reactions_in):
    '''
    Conversion of reactions from MCM facsimile download to numba 
    
    inputs:
        reactions_in = list of reactions
        
    returns:
        numba_reactions_in = list of reactions with numba functions 
                             replacing regular functions
    '''
    numba_reactions_in=copy.deepcopy(reactions_in)
    
    for reaction in numba_reactions_in:
        reaction[0]=reaction[0].replace('exp','numba_exp')
        reaction[0]=reaction[0].replace('log10','numba_log10')
        reaction[0]=reaction[0].replace('TEMP','temp') 
        reaction[0]=reaction[0].replace('sqrt','numba_sqrt')
    return numba_reactions_in

def import_all(filename):
    '''
    Function to import all of the species, reactions, rates, and the RO2
    summation and convert to a format that can be read and used with INCHEM-Py
    
    inputs:
        filename = name of mcm download file
        
    returns:
        species = list of species
        ppool = List of RO2 species for RO2 summation
        rate_numba = list of generic and complex rate coefficient calculations
                     with numba functions replacing regular functions
        reactions_numba = list of reactions with numba functions 
                          replacing regular functions
    '''
    #Import species, rates, reactions, and peroxyl pool
    species = speciesin(filename)
    ppool = ppool_in(filename)
    reactions_in = reactionslist(filename)
    rates_in = rate_coeff(filename)   
    
    #Check the species import for blank values and remove
    if species[0] == '':
        species.pop(0)
        
    species.sort() #alphabetic
    
    #Taking the imported values and converting into numba format for efficient
    #calculations
    rate_numba=numba_rate(rates_in)
    reactions_numba=numba_reactions(reactions_in)   
    return species,ppool,rate_numba,reactions_numba
    