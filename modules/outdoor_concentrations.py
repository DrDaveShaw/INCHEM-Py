'''
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
'''
def ACRate_updater(t,ACRate_dict,outdoor_dict):
    '''
    inputs:
        t = time of day in seconds
        ACRate_dict = dictionary of times and air change rates per hour
        outdoor_dict = dictionary of fixed outdoor species concentrations
    returns:
        None
    '''
    for key in ACRate_dict.keys():
        if t >= key:
            outdoor_dict['ACRate'] = ACRate_dict[key]
            
    return None


def outdoor_rates(particles,species):
    '''
    inputs:
        particles = boolean for whether particles are included in the simulation
        species = list of species
    
    returns:
        outdoor_dict = dictionary of fixed outdoor species concentrations
    '''
    outdoor_dict={}
    
    #ALDEHYDES
    outdoor_dict['HCHOOUT']=6.017E10
    outdoor_dict['CH3CHOOUT']=3.896E10
    outdoor_dict['C2H5CHOOUT']=9.332E9
    outdoor_dict['C3ME3CHOOUT']=1.049E9
    outdoor_dict['ACROUT']=2.685E9
    outdoor_dict['MACROUT']=2.792E9
    outdoor_dict['C4ALDBOUT']=1.718E9
    outdoor_dict['C4H9CHOOUT']=2.447E9
    outdoor_dict['C5H11CHOOUT']=2.706E9
    outdoor_dict['C6H13CHOOUT']=1.846E9
    outdoor_dict['C7H15CHOOUT']=2.349E9
    outdoor_dict['C8H17CHOOUT']=1.482E10
    outdoor_dict['C9H19CHOOUT']=4.047E9
    outdoor_dict['TNON2ENECHOOUT']=1.288E9
    
    #KETONES
    outdoor_dict['CH3COCH3OUT']=4.977E10
    outdoor_dict['MEKOUT']=5.429E9
    outdoor_dict['MVKOUT']=2.792E9
    outdoor_dict['CYHEXONEOUT']=1.706E10
    
    #AROMATICS
    outdoor_dict['BENZALOUT']=1.419E9
    outdoor_dict['OXYLALOUT']=1.253E9
    outdoor_dict['MXYLALOUT']=2.005E9
    outdoor_dict['PXYLALOUT']=2.005E9
    outdoor_dict['TM125BCHOOUT']=7.854E9
    outdoor_dict['BENZENEOUT']=9.637E9
    outdoor_dict['TOLUENEOUT']=4.085E10
    outdoor_dict['PXYLOUT']=6.098E9
    outdoor_dict['MXYLOUT']=6.098E9
    outdoor_dict['OXYLOUT']=4.254E9
    outdoor_dict['EBENZOUT']=8.792E9
    outdoor_dict['PBENZOUT']=4.008E9
    outdoor_dict['OETHTOLOUT']=2.505E8
    outdoor_dict['METHTOLOUT']=6.013E8
    outdoor_dict['PETHTOLOUT']=3.006E8
    outdoor_dict['TM135BOUT']=1.754E9
    outdoor_dict['TM124BOUT']=5.511E9
    outdoor_dict['TM123BOUT']=1.253E9
    outdoor_dict['DCBENEOUT']=1.229E10
    outdoor_dict['STYRENEOUT']=2.313E9
    outdoor_dict['IPBENZOUT']=3.006E9
    outdoor_dict['PHENOLOUT']=1.747E10
    
    #ALKANES
    outdoor_dict['C2H6OUT']=9.133E10
    outdoor_dict['C3H8OUT']=3.797E10
    outdoor_dict['NC4H10OUT']=3.471E10
    outdoor_dict['IC4H10OUT']=2.321E10
    outdoor_dict['M22C4OUT']=2.027E9
    outdoor_dict['M23C4OUT']=2.586E9
    outdoor_dict['NC5H12OUT']=8.681E9
    outdoor_dict['M2PEOUT']=3.844E9
    outdoor_dict['M3PEOUT']=2.446E9
    outdoor_dict['IC5H12OUT']=1.469E10
    outdoor_dict['NC6H14OUT']=1.118E10
    outdoor_dict['M2HEXOUT']=2.464E9
    outdoor_dict['M3HEXOUT']=3.125E9
    outdoor_dict['NC7H16OUT']=6.010E8
    outdoor_dict['NC8H18OUT']=5.272E8
    outdoor_dict['NC9H20OUT']=3.052E9
    outdoor_dict['NC10H22OUT']=9.946E9
    outdoor_dict['NC11H24OUT']=1.445E10
    outdoor_dict['NC12H26OUT']=1.061E9
    outdoor_dict['CHEXOUT']=6.440E8
    
    #ALKENES
    outdoor_dict['C2H4OUT']=3.327E10
    outdoor_dict['C3H6OUT']=9.159E9
    outdoor_dict['BUT1ENEOUT']=3.971E9
    outdoor_dict['CBUT2ENEOUT']=4.293E8
    outdoor_dict['TBUT2ENEOUT']=5.367E8
    outdoor_dict['ME2BUT1ENEOUT']=5.152E8
    outdoor_dict['ME2BUT2ENEOUT']=4.293E8
    outdoor_dict['C5H8OUT']=2.299E9
    outdoor_dict['C4H6OUT']=5.567E8
    outdoor_dict['TPENT2ENEOUT']=4.293E8
    outdoor_dict['CPENT2ENEOUT']=2.576E8
    
    #ALKYNES
    outdoor_dict['C2H2OUT']=1.573E10
    
    #ALCOHOLS
    outdoor_dict['CH3OHOUT']=1.107E11
    outdoor_dict['C2H5OHOUT']=1.613E11
    outdoor_dict['IPROPOLOUT']=9.239E10
    outdoor_dict['NPROPOLOUT']=1.243E10
    outdoor_dict['NBUTOLOUT']=2.519E10
    outdoor_dict['PEAOHOUT']=5.658E7
    outdoor_dict['HEXAOHOUT']=3.014E7
    outdoor_dict['BUOX2ETOHOUT']=2.507E10
    outdoor_dict['LINALOOLOUT']=1.292E7
    
    #HALOGENATED
    outdoor_dict['CHCL3OUT']=7.567E8
    outdoor_dict['CH3CCL3OUT']=7.674E9
    outdoor_dict['CH2CL2OUT']=2.340E9
    outdoor_dict['TRICLETHOUT']=9.075E9
    outdoor_dict['TCEOUT']=5.084E8
    outdoor_dict['CH2CLCH2CLOUT']=4.260E8
    outdoor_dict['CH3CLOUT']=1.396E10
    outdoor_dict['HCLOUT']=3.716E10
    
    #ESTERS
    outdoor_dict['ETHACETOUT']=2.392E9
    outdoor_dict['NBUTACETOUT']=1.296E9
    
    #MONOTERPENES
    outdoor_dict['APINENEOUT']=3.094E9
    outdoor_dict['BPINENEOUT']=1.238E9
    outdoor_dict['LIMONENEOUT']=2.431E9
    outdoor_dict['CAROUT']=2.718E9
    outdoor_dict['CAMPHENEOUT']=3.978E8
    
    #CARBOXYLIC ACIDS
    outdoor_dict['HCOOHOUT']=1.832E11
    outdoor_dict['CH3CO2HOUT']=3.861E11
    outdoor_dict['PROPACIDOUT']=1.873E9
    outdoor_dict['BUTACIDOUT']=1.381E9
    outdoor_dict['PENTACIDOUT']=7.534E8
    outdoor_dict['C6H13CO2HOUT']=9.932E7
    
    #KEY ATMOSPHERIC SPECIES / OTHER
    outdoor_dict['H2O2OUT']=3.13E10
    outdoor_dict['BCARYOUT']=9.348E7
    outdoor_dict['CH4OUT']=4.652E13
    outdoor_dict['COOUT']=6.642E12
    outdoor_dict['SO2OUT']=1.715E10
    outdoor_dict['HNO3OUT']=9.557E9
    outdoor_dict['HONOOUT']=1.588E10
    outdoor_dict['OHOUT']=1.09E6
    outdoor_dict['PANOUT']=5.449E10
    outdoor_dict['NOOUT']=6.81e10   #Average London_suburban
    outdoor_dict['NO2OUT']=8.37e10  #Average London_suburban
    outdoor_dict['O3OUT']=6.11e11   #Average London_suburban

    #Total Suspended Particles (TSP)
    if particles == 1:
        outdoor_dict['TSPOUT']=1.4E11
    
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
    
    outdoor_dict_diurnal['OHOUT']=compile("(5e4+(((6.073E-05*numba_abs(cosx)**(1.743)*numba_exp(-1.0*0.474*secx))*0.01)/3e-7*5e6))",'<string>','eval') #J1
    outdoor_dict_diurnal['HO2OUT']=compile("(2.5e7+(((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*0.1)/1e-3*1e8))",'<string>','eval') #J4
    outdoor_dict_diurnal['CH3O2OUT']=compile("(2e6+(((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*0.1)/1e-3*3e7))",'<string>','eval') #J4
    outdoor_dict_diurnal['HONOOUT']=compile("(7.5e9-(((2.644E-03*numba_abs(cosx)**(0.261)*numba_exp(-1.0*0.288*secx))*0.1)/1.9e-4*7.1e9))",'<string>','eval') #J7

    if city == "London_urban":
        outdoor_dict_diurnal['O3OUT']=compile("5.181e11 - 7.056e10*numba_cos(n*7.273e-5) - 2.065e11*numba_sin(n*7.273e-5) + 2.032e9*numba_cos(2*n*7.273e-5) + 9.256e10*numba_sin(2*n*7.273e-5) - 1.903e10*numba_cos(3*n*7.273e-5) - 6.693e9*numba_sin(3*n*7.273e-5)","<string>","eval")
        outdoor_dict_diurnal['NO2OUT']=compile("1.801e11 + 4.985e9*numba_cos(n*7.272e-5) + 1.786e9*numba_sin(n*7.272e-5) + 5.915e9*numba_cos(2*n*7.272e-5) - 3.785e10*numba_sin(2*n*7.272e-5) + 1.134e10*numba_cos(3*n*7.272e-5) + 6.164e9*numba_sin(3*n*7.272e-5) - 3.807e9*numba_cos(4*n*7.272e-5) + 3.127e9*numba_sin(4*n*7.272e-5) + 3.2e9*numba_cos(5*n*7.272e-5) - 3.641e9*numba_sin(5*n*7.272e-5)","<string>","eval")
        outdoor_dict_diurnal['NOOUT']=compile("1.148e11 - 5.721e10*numba_cos(n*7.273e-5) + 5.568e10*numba_sin(n*7.273e-5) + 7.857e9*numba_cos(2*n*7.273e-5) - 5.238e10*numba_sin(2*n*7.273e-5) + 3.502e10*numba_cos(3*n*7.273e-5) + 1.907e10*numba_sin(3*n*7.273e-5) - 1.439e10*numba_cos(4*n*7.273e-5) + 2.458e9*numba_sin(4*n*7.273e-5) + 8.617e9*numba_cos(5*n*7.273e-5) - 1.52e10*numba_sin(5*n*7.273e-5) + 5.765e9*numba_cos(6*n*7.273e-5) + 5.59e9*numba_sin(6*n*7.273e-5)","<string>","eval")
        outdoor_dict_diurnal['TSPOUT']=compile("3.648e+10 + 2.021e+08*numba_cos(n*7.272e-5) + 1.798e+09*numba_sin(n*7.272e-5) + 5.866e+08*numba_cos(2*n*7.272e-5) - 3.296e+09*numba_sin(2*n*7.272e-5) + 2.842e+08*numba_cos(3*n*7.272e-5) - 1.278e+08*numba_sin(3*n*7.272e-5) - 1.215e+09*numba_cos(4*n*7.272e-5) + 1.114e+09*numba_sin(4*n*7.272e-5) + 4.992e+07*numba_cos(5*n*7.272e-5) - 9.061e+08*numba_sin(5*n*7.272e-5) + 2.395e+07*numba_cos(6*n*7.272e-5) + 2.546e+08*numba_sin(6*n*7.272e-5)","<string>","eval")
    elif city == "London_suburban":
        outdoor_dict_diurnal['O3OUT']=compile("(6.116e+11 - 1.140e+11*numba_cos(n*7.273e-05) - 2.818e+11*numba_sin(n*7.273e-05) + 4.643e+09*numba_cos(2*n*7.273e-05) + 5.900e+10*numba_sin(2*n*7.273e-05) - 1.321e+10*numba_cos(3*n*7.273e-05) + 1.279e+10*numba_sin(3*n*7.273e-05))","<string>","eval")
        outdoor_dict_diurnal['NO2OUT']=compile("(8.369e+10 + 1.337e+10*numba_cos(n*7.272e-05) + 1.762e+10*numba_sin(n*7.272e-05) + 1.038e+09*numba_cos(2*n*7.272e-05) - 2.247e+10*numba_sin(2*n*7.272e-05) + 6.894e+09*numba_cos(3*n*7.272e-05) - 2.022e+08*numba_sin(3*n*7.272e-05) - 3.716e+09*numba_cos(4*n*7.272e-05) + 3.955e+09*numba_sin(4*n*7.272e-05) - 7.484e+08*numba_cos(5*n*7.272e-05) - 1.078e+09*numba_sin(5*n*7.272e-05))","<string>","eval")
        outdoor_dict_diurnal['NOOUT']=compile("(6.813e+10 - 1.960e+10*numba_cos(n*7.272e-05) + 3.616e+10*numba_sin(n*7.272e-05) - 5.563e+09*numba_cos(2*n*7.272e-05) - 2.968e+10*numba_sin(2*n*7.272e-05) + 2.005e+10*numba_cos(3*n*7.272e-05) + 3.878e+09*numba_sin(3*n*7.272e-05) - 1.313e+10*numba_cos(4*n*7.272e-05) + 1.043e+10*numba_sin(4*n*7.272e-05) - 5.528e+09*numba_cos(5*n*7.272e-05) - 7.556e+09*numba_sin(5*n*7.272e-05) + 2.353e+09*numba_cos(6*n*7.272e-05) + 1.804e+09*numba_sin(6*n*7.272e-05))","<string>","eval")
        outdoor_dict_diurnal['TSPOUT']=compile("(3.53e+10 + 1.781e+09*numba_cos(n*7.274e-05) + 3.578e+09*numba_sin(n*7.274e-05) + 3.223e+08*numba_cos(2*n*7.274e-05) - 2.203e+09*numba_sin(2*n*7.274e-05) + 1.485e+09*numba_cos(3*n*7.274e-05) + 4.762e+08*numba_sin(3*n*7.274e-05) - 5.397e+08*numba_cos(4*n*7.274e-05) + 1.098e+08*numba_sin(4*n*7.274e-05) - 3.925e+08*numba_cos(5*n*7.274e-05) - 4.499e+08*numba_sin(5*n*7.274e-05) - 1.969e+08*numba_cos(6*n*7.274e-05) + 3.621e+08*numba_sin(6*n*7.274e-05))","<string>","eval")
    elif city == "Bergen_urban":
        outdoor_dict_diurnal['O3OUT']=compile("6.645e+11 - 2.109e+10*numba_cos(n*7.272e-05) - 9.541e+10*numba_sin(n*7.272e-05) + 2.513e+10*numba_cos(2*n*7.272e-05) + 2.874e+10*numba_sin(2*n*7.272e-05) - 2.430e+10*numba_cos(3*n*7.272e-05) - 2.579e+09*numba_sin(3*n*7.272e-05) + 4.459e+09*numba_cos(4*n*7.272e-05) - 6.178e+09*numba_sin(4*n*7.272e-05) + 9.739e+09*numba_cos(5*n*7.272e-05) + 6.574e+09*numba_sin(5*n*7.272e-05)","<string>","eval")
        outdoor_dict_diurnal['NO2OUT']=compile("8.970e+10 - 1.725e+10*numba_cos(n*7.273e-05) + 6.237e+09*numba_sin(n*7.273e-05) - 8.023e+09*numba_cos(2*n*7.273e-05) - 1.338e+10*numba_sin(2*n*7.273e-05) + 1.359e+10*numba_cos(3*n*7.273e-05) + 3.919e+09*numba_sin(3*n*7.273e-05) - 2.993e+09*numba_cos(4*n*7.273e-05) + 3.224e+09*numba_sin(4*n*7.273e-05) - 2.413e+09*numba_cos(5*n*7.273e-05) - 3.722e+09*numba_sin(5*n*7.273e-05) + 1.450e+09*numba_cos(6*n*7.273e-05) + -3.109e+09*numba_sin(6*n*7.273e-05) + 3.238e+09*numba_cos(7*n*7.273e-05) + 2.316e+09*numba_sin(7*n*7.273e-05)","<string>","eval")
        outdoor_dict_diurnal['NOOUT']=compile("1.059e+11 - 1.026e+11*numba_cos(n*7.272e-05) + 3.369e+10*numba_sin(n*7.272e-05) - 1.430e+10*numba_cos(2*n*7.272e-05) - 4.850e+10*numba_sin(2*n*7.272e-05) + 4.388e+10*numba_cos(3*n*7.272e-05) + 2.897e+10*numba_sin(3*n*7.272e-05) - 2.131e+10*numba_cos(4*n*7.272e-05) + 3.353e+09*numba_sin(4*n*7.272e-05) - 8.281e+07*numba_cos(5*n*7.272e-05) - 9.473e+09*numba_sin(5*n*7.272e-05)","<string>","eval")
        outdoor_dict_diurnal['TSPOUT']=compile("2.127e+10 - 4.231e+08*numba_cos(n*7.274e-05) - 3.246e+08*numba_sin(n*7.274e-05) + 8.526e+08*numba_cos(2*n*7.274e-05) - 7.822e+08*numba_sin(2*n*7.274e-05) + 1.192e+08*numba_cos(3*n*7.274e-05) + 3.62e+08*numba_sin(3*n*7.274e-05) - 7.76e+08*numba_cos(4*n*7.274e-05) + 1.703e+08*numba_sin(4*n*7.274e-05) - 9.186e+07*numba_cos(5*n*7.274e-05) - 1.306e+08*numba_sin(5*n*7.274e-05)","<string>","eval")
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

    outdoor_dict['cosx'] = out_calc_dict['cosx']
    outdoor_dict['secx'] = out_calc_dict['secx']
    return None
