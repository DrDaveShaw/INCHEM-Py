# -*- coding: utf-8 -*-
"""
A series of functions defining outdoor rates for INCHEM-Py.
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

def outdoor_rates(AER,particles,species):
    '''
    Concentrations of outdoor species that are assumed to be constant

    inputs:
        AER = Air exchange rate per hour
        particles = True or False for whether particles are included in the simulation
        species = list of species

    returns:
        outdoor_dict = dictionary of fixed outdoor species concentrations
    '''
    outdoor_dict={}
    outdoor_dict['AER']=AER
    outdoor_dict['NOOUT']=2.59e10
    outdoor_dict['NO2OUT']=9.52e10
    outdoor_dict['O3OUT']=7.68e11

    #outdoor concentrations for Milan
    outdoor_dict['BENZENEOUT']=5.9e9
    outdoor_dict['TOLUENEOUT']=2e10
    outdoor_dict['OXYLOUT']=1.3e10
    outdoor_dict['MXYLOUT']=0.65e10
    outdoor_dict['PXYLOUT']=0.65e10
    outdoor_dict['EBENZOUT']=3.4e9
    outdoor_dict['NC6H14OUT']=9.15e9
    outdoor_dict['APINENEOUT']=1.45e9
    outdoor_dict['BPINENEOUT']=2.5e7
    outdoor_dict['LIMONENEOUT']=9e8
    outdoor_dict['BUOX2ETOHOUT']=0.519e10
    outdoor_dict['STYRENEOUT']=5.67e9
    outdoor_dict['HCHOOUT']=9.13e10
    outdoor_dict['CH3CHOOUT']=7.15e10
    outdoor_dict['BENZALOUT']=6.13e10

    #other typical outdoor values, mainly from Sarwar
    outdoor_dict['C2H6OUT']=2.08e10
    outdoor_dict['C3H8OUT']=1.25e10
    outdoor_dict['NC4H10OUT']=3.33e10
    outdoor_dict['NC5H12OUT']=9.13e9
    outdoor_dict['NC7H16OUT']=2.58e9
    outdoor_dict['NC8H18OUT']=7.5e9
    outdoor_dict['NC9H20OUT']=1e10
    outdoor_dict['NC10H22OUT']=1.96e9
    outdoor_dict['NC11H24OUT']=1.95e9
    outdoor_dict['NC12H26OUT']=5.22e8
    outdoor_dict['CHEXOUT']=1.19e9
    outdoor_dict['CH3CCL3OUT']=8.33e10
    outdoor_dict['CH2CL2OUT']=1e9
    outdoor_dict['CHCL3OUT']=2.93e8
    outdoor_dict['CH3COCH3OUT']=1.3e10
    outdoor_dict['MEKOUT']=2.41e9
    outdoor_dict['CH3OHOUT']=1.3e11
    outdoor_dict['C2H5OHOUT']=1.2e12
    outdoor_dict['IPROPOLOUT']=2.0e10
    outdoor_dict['IPBENZOUT']=1.56e8
    outdoor_dict['TM124BOUT']=2.23e9
    outdoor_dict['TM135BOUT']=2.2e10
    outdoor_dict['PHENOLOUT']=5e10
    outdoor_dict['C2H4OUT']=1.25e10
    outdoor_dict['C3H6OUT']=0.43e10
    outdoor_dict['MEPROPENEOUT']=0.5e10
    outdoor_dict['CBUT2ENEOUT']=3.5e9
    outdoor_dict['TBUT2ENEOUT']=4e9
    outdoor_dict['ME2BUT2ENEOUT']=7e9
    outdoor_dict['C5H8OUT']=1.0e10
    outdoor_dict['C4H6OUT']=2.5e9
    outdoor_dict['CAROUT']=9e8
    outdoor_dict['C5H11CHOOUT']=9.25e9
    outdoor_dict['C6H13CHOOUT']=3.75e9
    outdoor_dict['C7H15CHOOUT']=7.25e9
    outdoor_dict['C8H17CHOOUT']=2.5e10
    outdoor_dict['C9H19CHOOUT']=2.75e9

    #values below have been estimated and ideally need to be revised when
    #appropriate lit sources are found. They have been set to make indoor values
    #consistent with measurements reported in Canada by Zhu
    outdoor_dict['NPROPOLOUT']=1.2e9
    outdoor_dict['NBUTOLOUT']=1.3e10
    outdoor_dict['TBUTOLOUT']=5.0e8
    outdoor_dict['IPEAOHOUT']=2.3e9
    outdoor_dict['TM123BOUT']=8.0e9
    outdoor_dict['MPRKOUT']=8.0e8
    outdoor_dict['MIBKOUT']=5.0e8
    outdoor_dict['CYHEXONEOUT']=0.9e9
    outdoor_dict['CAMPHENEOUT']=5e8
    outdoor_dict['TRICLETHOUT']=3e7
    outdoor_dict['TCEOUT']=2e8
    outdoor_dict['ACROUT']=4.94e10
    outdoor_dict['C2H5CHOOUT']=2.02e10
    outdoor_dict['H2O2OUT']=5e10
    outdoor_dict['HNO3OUT']=5e10
    #outdoor_dict['CH4OUT']=4.63e13
    #outdoor_dict['COOUT']=2.5e12

    outdoor_dict['BCARYOUT']=2.5e7

    #non-diurnal outdoor concentrations from homechem
    outdoor_dict['HONOOUT']=1.6e9
    outdoor_dict['MVKOUT']=1.78e10
    outdoor_dict['OHOUT']=1e6
    outdoor_dict['PANOUT']=1.51e10

    if particles == True:
        outdoor_dict['TSPOUT']=1.4e11

    for specie in species:
        if '%sOUT' % specie not in outdoor_dict.keys():
            outdoor_dict['%sOUT' % specie]=0
    return outdoor_dict


def outdoor_rates_diurnal(city):
    '''
    Diurnal concentration calculations for outdoor species

    returns:
        outdoor_dict_diurnal = dictionary of compiled equations for outdoor
                               species concentrations that vary throughout
                               the day
    '''
    outdoor_dict_diurnal={}

    outdoor_dict_diurnal['OHOUT']=compile("5e4+(((6.073E-05*numba_abs(cosx)**(1.743)*numba_exp(-1.0*0.474*secx))*0.01)/3e-7*5e6)",'<string>','eval') #J1
    outdoor_dict_diurnal['HO2OUT']=compile("2.5e7+(((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*0.1)/1e-3*1e8)",'<string>','eval') #J4
    outdoor_dict_diurnal['CH3O2OUT']=compile("2e6+(((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*0.1)/1e-3*3e7)",'<string>','eval') #J4
    outdoor_dict_diurnal['HONOOUT']=compile("7.5e9-(((2.644E-03*numba_abs(cosx)**(0.261)*numba_exp(-1.0*0.288*secx))*0.1)/1.9e-4*7.1e9)",'<string>','eval') #J7

    if city == "London_urban":
        outdoor_dict_diurnal['O3OUT']=compile("5.181e11 - 7.056e10*numba_cos(n*7.273e-5) - 2.065e11*numba_sin(n*7.273e-5) + 2.032e9*numba_cos(2*n*7.273e-5) + 9.256e10*numba_sin(2*n*7.273e-5) - 1.903e10*numba_cos(3*n*7.273e-5) - 6.693e9*numba_sin(3*n*7.273e-5)","<string>","eval")
        outdoor_dict_diurnal['NO2OUT']=compile("1.801e11 + 4.985e9*numba_cos(n*7.272e-5) + 1.786e9*numba_sin(n*7.272e-5) + 5.915e9*numba_cos(2*n*7.272e-5) - 3.785e10*numba_sin(2*n*7.272e-5) + 1.134e10*numba_cos(3*n*7.272e-5) + 6.164e9*numba_sin(3*n*7.272e-5) - 3.807e9*numba_cos(4*n*7.272e-5) + 3.127e9*numba_sin(4*n*7.272e-5) + 3.2e9*numba_cos(5*n*7.272e-5) - 3.641e9*numba_sin(5*n*7.272e-5)","<string>","eval")
        outdoor_dict_diurnal['NOOUT']=compile("1.148e11 - 5.721e10*numba_cos(n*7.273e-5) + 5.568e10*numba_sin(n*7.273e-5) + 7.857e9*numba_cos(2*n*7.273e-5) - 5.238e10*numba_sin(2*n*7.273e-5) + 3.502e10*numba_cos(3*n*7.273e-5) + 1.907e10*numba_sin(3*n*7.273e-5) - 1.439e10*numba_cos(4*n*7.273e-5) + 2.458e9*numba_sin(4*n*7.273e-5) + 8.617e9*numba_cos(5*n*7.273e-5) - 1.52e10*numba_sin(5*n*7.273e-5) + 5.765e9*numba_cos(6*n*7.273e-5) + 5.59e9*numba_sin(6*n*7.273e-5)","<string>","eval")
        outdoor_dict_diurnal['TSPOUT']=compile("2.919e10 + 1.617e8*numba_cos(n*7.272e-5) + 1.438e9*numba_sin(n*7.272e-5) + 4.693e8*numba_cos(2*n*7.272e-5) - 2.637e9*numba_sin(2*n*7.272e-5) + 2.274e8*numba_cos(3*n*7.272e-5) - 1.023e8*numba_sin(3*n*7.272e-5) - 9.719e8*numba_cos(4*n*7.272e-5) + 8.915e8*numba_sin(4*n*7.272e-5) + 3.994e7*numba_cos(5*n*7.272e-5) - 7.249e8*numba_sin(5*n*7.272e-5) + 1.916e7*numba_cos(6*n*7.272e-5) + 2.037e8*numba_sin(6*n*7.272e-5)","<string>","eval")
    elif city == "London_suburban":
        outdoor_dict_diurnal['O3OUT']=compile("6.116e+11 - 1.140e+11*numba_cos(n*7.273e-05) - 2.818e+11*numba_sin(n*7.273e-05) + 4.643e+09*numba_cos(2*n*7.273e-05) + 5.900e+10*numba_sin(2*n*7.273e-05) - 1.321e+10*numba_cos(3*n*7.273e-05) + 1.279e+10*numba_sin(3*n*7.273e-05)","<string>","eval")
        outdoor_dict_diurnal['NO2OUT']=compile("8.369e+10 + 1.337e+10*numba_cos(n*7.272e-05) + 1.762e+10*numba_sin(n*7.272e-05) + 1.038e+09*numba_cos(2*n*7.272e-05) - 2.247e+10*numba_sin(2*n*7.272e-05) + 6.894e+09*numba_cos(3*n*7.272e-05) - 2.022e+08*numba_sin(3*n*7.272e-05) - 3.716e+09*numba_cos(4*n*7.272e-05) + 3.955e+09*numba_sin(4*n*7.272e-05) - 7.484e+08*numba_cos(5*n*7.272e-05) - 1.078e+09*numba_sin(5*n*7.272e-05)","<string>","eval")
        outdoor_dict_diurnal['NOOUT']=compile("6.813e+10 - 1.960e+10*numba_cos(n*7.272e-05) + 3.616e+10*numba_sin(n*7.272e-05) - 5.563e+09*numba_cos(2*n*7.272e-05) - 2.968e+10*numba_sin(2*n*7.272e-05) + 2.005e+10*numba_cos(3*n*7.272e-05) + 3.878e+09*numba_sin(3*n*7.272e-05) - 1.313e+10*numba_cos(4*n*7.272e-05) + 1.043e+10*numba_sin(4*n*7.272e-05) - 5.528e+09*numba_cos(5*n*7.272e-05) - 7.556e+09*numba_sin(5*n*7.272e-05) + 2.353e+09*numba_cos(6*n*7.272e-05) + 1.804e+09*numba_sin(6*n*7.272e-05)","<string>","eval")
        outdoor_dict_diurnal['TSPOUT']=compile("2.824e+10 + 1.425e+09*numba_cos(n*7.274e-05) + 2.862e+09*numba_sin(n*7.274e-05) + 2.570e+08*numba_cos(2*n*7.274e-05) - 1.763e+09*numba_sin(2*n*7.274e-05) + 1.188e+09*numba_cos(3*n*7.274e-05) + 3.803e+08*numba_sin(3*n*7.274e-05) - 4.320e+08*numba_cos(4*n*7.274e-05) + 8.815e+07*numba_sin(4*n*7.274e-05) - 3.145e+08*numba_cos(5*n*7.274e-05) - 3.596e+08*numba_sin(5*n*7.274e-05) - 1.573e+08*numba_cos(6*n*7.274e-05) + 2.899e+08*numba_sin(6*n*7.274e-05) + 2.315e+08*numba_cos(7*n*7.274e-05) - 1.671e+08*numba_sin(7*n*7.274e-05)","<string>","eval")
    elif city == "Bergen_urban":
        outdoor_dict_diurnal['O3OUT']=compile("6.645e+11 - 2.109e+10*numba_cos(n*7.272e-05) - 9.541e+10*numba_sin(n*7.272e-05) + 2.513e+10*numba_cos(2*n*7.272e-05) + 2.874e+10*numba_sin(2*n*7.272e-05) - 2.430e+10*numba_cos(3*n*7.272e-05) - 2.579e+09*numba_sin(3*n*7.272e-05) + 4.459e+09*numba_cos(4*n*7.272e-05) - 6.178e+09*numba_sin(4*n*7.272e-05) + 9.739e+09*numba_cos(5*n*7.272e-05) + 6.574e+09*numba_sin(5*n*7.272e-05)","<string>","eval")
        outdoor_dict_diurnal['NO2OUT']=compile("8.970e+10 - 1.725e+10*numba_cos(n*7.273e-05) + 6.237e+09*numba_sin(n*7.273e-05) - 8.023e+09*numba_cos(2*n*7.273e-05) - 1.338e+10*numba_sin(2*n*7.273e-05) + 1.359e+10*numba_cos(3*n*7.273e-05) + 3.919e+09*numba_sin(3*n*7.273e-05) - 2.993e+09*numba_cos(4*n*7.273e-05) + 3.224e+09*numba_sin(4*n*7.273e-05) - 2.413e+09*numba_cos(5*n*7.273e-05) - 3.722e+09*numba_sin(5*n*7.273e-05) + 1.450e+09*numba_cos(6*n*7.273e-05) + -3.109e+09*numba_sin(6*n*7.273e-05) + 3.238e+09*numba_cos(7*n*7.273e-05) + 2.316e+09*numba_sin(7*n*7.273e-05)","<string>","eval")
        outdoor_dict_diurnal['NOOUT']=compile("1.059e+11 - 1.026e+11*numba_cos(n*7.272e-05) + 3.369e+10*numba_sin(n*7.272e-05) - 1.430e+10*numba_cos(2*n*7.272e-05) - 4.850e+10*numba_sin(2*n*7.272e-05) + 4.388e+10*numba_cos(3*n*7.272e-05) + 2.897e+10*numba_sin(3*n*7.272e-05) - 2.131e+10*numba_cos(4*n*7.272e-05) + 3.353e+09*numba_sin(4*n*7.272e-05) - 8.281e+07*numba_cos(5*n*7.272e-05) - 9.473e+09*numba_sin(5*n*7.272e-05)","<string>","eval")
        outdoor_dict_diurnal['TSPOUT']=compile("1.702e+10 - 3.385e+08*numba_cos(n*7.274e-05) - 2.597e+08*numba_sin(n*7.274e-05) + 6.821e+08*numba_cos(2*n*7.274e-05) - 6.258e+08*numba_sin(2*n*7.274e-05) + 9.532e+07*numba_cos(3*n*7.274e-05) + 2.896e+08*numba_sin(3*n*7.274e-05) - 6.208e+08*numba_cos(4*n*7.274e-05) + 1.362e+08*numba_sin(4*n*7.274e-05) - 7.349e+07*numba_cos(5*n*7.274e-05) - 1.045e+08*numba_sin(5*n*7.274e-05)","<string>","eval")
    elif city == "Milan_urban_Aug2003":
        outdoor_dict_diurnal['O3OUT']=compile("1.38e+12 - 6.305e+11*numba_cos(n*7.271e-05) - 9.43e+11*numba_sin(n*7.271e-05) + 3.484e+10*numba_cos(2*n*7.271e-05) + 1.832e+11*numba_sin(2*n*7.271e-05)","<string>","eval")
        outdoor_dict_diurnal['NO2OUT']=compile("9.498e+11 + 2.203e+11*numba_cos(n*7.272e-05) - 4.447e+10*numba_sin(n*7.272e-05) + 4.498e+10*numba_cos(2*n*7.272e-05) - 2.061e+11*numba_sin(2*n*7.272e-05) + 5.042e+10*numba_cos(3*n*7.272e-05) + 2.214e+10*numba_sin(3*n*7.272e-05) - 2.47e+10*numba_cos(4*n*7.272e-05) + 3.932e+10*numba_sin(4*n*7.272e-05)","<string>","eval")
        outdoor_dict_diurnal['NOOUT']=compile("4.337e+11 + 1.122e+11*numba_cos(n*7.274e-05) - 1.383e+11*numba_sin(n*7.274e-05) + 8.572e+10*numba_cos(2*n*7.274e-05) - 1.095e+11*numba_sin(2*n*7.274e-05) + 2.409e+10*numba_cos(3*n*7.274e-05) + 3.912e+10*numba_sin(3*n*7.274e-05) + 4.645e+10*numba_cos(4*n*7.274e-05) - 5.773e+10*numba_sin(4*n*7.274e-05) + 2.542e+10*numba_cos(5*n*7.274e-05) + 2.898e+10*numba_sin(5*n*7.274e-05)","<string>","eval")
        outdoor_dict_diurnal['TSPOUT']=compile("1.394e+11 - 3.414e+10*numba_cos(n*7.275e-05) + 2.977e+10*numba_sin(n*7.275e-05) + 5.563e+08*numba_cos(2*n*7.275e-05) - 5.124e+08*numba_sin(2*n*7.275e-05) - 5.652e+09*numba_cos(3*n*7.275e-05) - 8.424e+08*numba_sin(3*n*7.275e-05) + 3.788e+09*numba_cos(4*n*7.275e-05) - 5.369e+09*numba_sin(4*n*7.275e-05) - 7.5e+09*numba_cos(5*n*7.275e-05) + 1.936e+09*numba_sin(5*n*7.275e-05) + 9.628e+09*numba_cos(6*n*7.275e-05) - 2.673e+08*numba_sin(6*n*7.275e-05)","<string>","eval")
    else:
        print("City not recognised, no diurnal rates for O3, NO2, NO, or PM2.5")

    return outdoor_dict_diurnal

def outdoor_rates_calc(outdoor_dict,outdoor_dict_diurnal,out_calc_dict):
    '''
    Function for evaluating the diurnal outdoor concentration calculations

    inputs:
        outdoor_dict = dictionary of fixed outdoor species concentrations
        outdoor_dict_diurnal = dictionary of compiled equations for outdoor
                               species concentrations that vary throughout
                               the day
        out_calc_dict = dictionary of variables for use in calculating outdoor
                        diurnal species concentration variation
    '''
    for i in outdoor_dict_diurnal:
        outdoor_dict[i] = eval(outdoor_dict_diurnal[i],{},out_calc_dict)
    return None
