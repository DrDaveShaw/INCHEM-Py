'''
Photolysis coefficients and calculations for INCHEM-Py.
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

"""
J1	O3 O(1D)
J2	O3 O(3P)
J3	H2O2
J4	NO2
J5	NO3 (NO + O2)
J6	NO3( NO2 + O(3P))
J7	HONO
J8	HNO3(OH)
J11	HCHO(H+HCO)
J12	HCHO(H2+CO)
J13	CH3CHO(CH3 + HCO)
J14	C2H5CHO
J15	C3H7CHO(n-C3H7 + HCO)
J16	C3H7CHO(C2H4 + CH2CHOH)
J17	IPRCHO(n-C4H9 + HCO)
J18	MACR (CH2=CCH3+HCO
J19	MACR (CH2C(CH3)CO+H
J20	C5HPALD1
J21	CH3C(O)CH3
J22	MEK (CH3CO+C2H5)
J23	MVK(CH3CH=CH2 + CO)
J24	MVK(CH3CO + CH2=CH)
J31	GLYOX(CO + CO + H2)
J32	GLYOX(HCHO + CO)
J33	GLYOX(HCO + HCO)
J34	MGLYOX
J35	BIACET
J41	CH3OOH
J51	CH3ONO2
J52	C2H5ONO2
J53	n-C3H7ONO2
J54	i-C3H7ONO2
J55	TC4H9NO3
J56	NOA
J57	route 2 NOA
J70	CL2
J71	ClNO2
J72	ClONO2 = NO2
J73	ClONO2 = NO3
J74	HOCl
J75	OClO
J76	ClO
J77	ClOOCl = Cl
J78	ClOOCl = ClO
"""

def photolysis_J(indoor_photo,photo_dict,J_dict):
    '''
    Function for evaluating compiled photolysis equations
    
    inputs:
        indoor_photo = dictionary of attenuation values for specific light
                       sources and window glass types
        photo_dict = dictionary of compiled photolysis equations
        J_dict = dictionary of photolysis values for calculating photolysis reactions
    '''
    
    for i in photo_dict:
        J_dict[i]=(eval(photo_dict[i],{},indoor_photo))  
            
    return None

def Zixu_photolysis(numba_abs,numba_exp):
    '''
    Attenuation values for photolysis 1m from a window. Details in Wang 2020.
    https://doi.org/10.1111/ina.12702
    
    inputs:
        numba_abs = numba absolute function
        numba_exp = numba exponential function
    
    returns:
        light_dict = dictionary of attenuation factors for varying light sources
                     and window glass types
    '''
    light_dict={}
    light_dict["Incand"]={"JIN1":3.64E-08,
                          "JIN2":4.28E-06,
                          "JIN3":4.52E-09,
                          "JIN4":1.08E-05,
                          "JIN5":3.69E-04,
                          "JIN6":1.37E-03,
                          "JIN7":1.42E-06,
                          "JIN8":5.32E-10,
                          "JIN11":1.48E-08,
                          "JIN12":2.10E-08,
                          "JIN13":4.26E-09,
                          "JIN14":1.11E-08,
                          "JIN15":5.98E-09,
                          "JIN16":2.85E-09,
                          "JIN17":3.16E-08,
                          "JIN18":6.07E-10,
                          "JIN19":6.07E-10,
                          "JIN20":3.11E-07,
                          "JIN21":3.68E-10,
                          "JIN22":1.12E-09,
                          "JIN23":1.08E-09,
                          "JIN24":1.08E-09,
                          "JIN31":3.75E-09,
                          "JIN32":1.86E-08,
                          "JIN33":7.52E-08,
                          "JIN34":1.32E-07,
                          "JIN35":5.44E-07,
                          "JIN41":3.10E-09,
                          "JIN51":8.03E-10,
                          "JIN52":1.24E-09,
                          "JIN53":1.43E-09,
                          "JIN54":1.95E-09,
                          "JIN55":4.53E-09,
                          "JIN56":1.77E-08,
                          "JIN57":1.77E-08,
                          "JIN70":2.72527E-06,
                          "JIN71":2.45038E-07,
                          "JIN72":3.68392E-08,
                          "JIN73":5.22571E-09,
                          "JIN74":1.92278E-07,
                          "JIN75":5.92897E-06,
                          "JIN76":1.07431E-06,
                          "JIN77":1.35704E-06,
                          "JIN78":3.39261E-07}
    light_dict["Halogen"]={"JIN1":1.18E-08,
                           "JIN2":3.70E-06,
                           "JIN3":4.01E-09,
                           "JIN4":1.30E-05,
                           "JIN5":3.18E-04,
                           "JIN6":1.25E-03,
                           "JIN7":1.75E-06,
                           "JIN8":2.76E-10,
                           "JIN11":1.19E-08,
                           "JIN12":2.26E-08,
                           "JIN13":2.17E-09,
                           "JIN14":5.00E-09,
                           "JIN15":4.63E-09,
                           "JIN16":2.21E-09,
                           "JIN17":2.43E-08,
                           "JIN18":7.17E-10,
                           "JIN19":7.17E-10,
                           "JIN20":3.68E-07,
                           "JIN21":1.12E-10,
                           "JIN22":5.90E-10,
                           "JIN23":1.05E-09,
                           "JIN24":1.05E-09,
                           "JIN31":3.02E-09,
                           "JIN32":1.80E-08,
                           "JIN33":8.43E-08,
                           "JIN34":1.43E-07,
                           "JIN35":6.05E-07,
                           "JIN41":2.94E-09,
                           "JIN51":4.27E-10,
                           "JIN52":6.72E-10,
                           "JIN53":8.72E-10,
                           "JIN54":1.13E-09,
                           "JIN55":2.86E-09,
                           "JIN56":1.31E-08,
                           "JIN57":1.31E-08,
                           "JIN70":2.97738E-06,
                           "JIN71":2.58634E-07,
                           "JIN72":4.07906E-08,
                           "JIN73":4.05384E-09,
                           "JIN74":2.15874E-07,
                           "JIN75":6.7192E-06,
                           "JIN76":4.47694E-07,
                           "JIN77":1.45398E-06,
                           "JIN78":3.63495E-07}
    light_dict["LED"]={"JIN1":0.00E+00,
                       "JIN2":4.35E-06,
                       "JIN3":3.64E-10,
                       "JIN4":5.05E-07,
                       "JIN5":5.52E-04,
                       "JIN6":1.99E-03,
                       "JIN7":0.00E+00,
                       "JIN8":0.00E+00,
                       "JIN11":0.00E+00,
                       "JIN12":0.00E+00,
                       "JIN13":0.00E+00,
                       "JIN14":0.00E+00,
                       "JIN15":0.00E+00,
                       "JIN16":0.00E+00,
                       "JIN17":0.00E+00,
                       "JIN18":0.00E+00,
                       "JIN19":0.00E+00,
                       "JIN20":0.00E+00,
                       "JIN21":0.00E+00,
                       "JIN22":0.00E+00,
                       "JIN23":0.00E+00,
                       "JIN24":0.00E+00,
                       "JIN31":0.00E+00,
                       "JIN32":1.38E-10,
                       "JIN33":3.24E-08,
                       "JIN34":2.61E-08,
                       "JIN35":7.66E-07,
                       "JIN41":0.00E+00,
                       "JIN51":0.00E+00,
                       "JIN52":0.00E+00,
                       "JIN53":0.00E+00,
                       "JIN54":0.00E+00,
                       "JIN55":0.00E+00,
                       "JIN56":0.00E+00,
                       "JIN57":0.00E+00,
                       "JIN70":1.765E-06,
                       "JIN71":2.63043E-08,
                       "JIN72":2.41686E-09,
                       "JIN73":0,
                       "JIN74":2.29238E-09,
                       "JIN75":5.46777E-06,
                       "JIN76":0,
                       "JIN77":6.97951E-07,
                       "JIN78":1.74488E-07}
    light_dict["CFL"]={"JIN1":9.60E-10,
                       "JIN2":6.10E-06,
                       "JIN3":3.58E-09,
                       "JIN4":4.47E-05,
                       "JIN5":9.46E-04,
                       "JIN6":3.37E-03,
                       "JIN7":6.31E-06,
                       "JIN8":5.46E-11,
                       "JIN11":2.89E-09,
                       "JIN12":2.22E-08,
                       "JIN13":3.69E-11,
                       "JIN14":7.10E-11,
                       "JIN15":1.62E-09,
                       "JIN16":7.72E-10,
                       "JIN17":4.63E-09,
                       "JIN18":2.68E-09,
                       "JIN19":2.68E-09,
                       "JIN20":1.38E-06,
                       "JIN21":0.00E+00,
                       "JIN22":3.39E-11,
                       "JIN23":1.74E-09,
                       "JIN24":1.74E-09,
                       "JIN31":1.65E-09,
                       "JIN32":3.81E-08,
                       "JIN33":3.49E-07,
                       "JIN34":5.92E-07,
                       "JIN35":2.43E-06,
                       "JIN41":7.41E-09,
                       "JIN51":6.24E-11,
                       "JIN52":1.16E-10,
                       "JIN53":3.75E-10,
                       "JIN54":2.96E-10,
                       "JIN55":4.62E-10,
                       "JIN56":4.70E-09,
                       "JIN57":4.70E-09,
                       "JIN70":6.67907E-06,
                       "JIN71":6.22848E-07,
                       "JIN72":1.35954E-07,
                       "JIN73":3.42904E-09,
                       "JIN74":6.84841E-07,
                       "JIN75":1.50259E-05,
                       "JIN76":0,
                       "JIN77":3.38602E-06,
                       "JIN78":8.46506E-07}
    light_dict["UFT"]={"JIN1":1.40E-06,
                       "JIN2":1.02E-05,
                       "JIN3":1.70E-07,
                       "JIN4":5.65E-05,
                       "JIN5":1.25E-03,
                       "JIN6":4.89E-03,
                       "JIN7":1.01E-05,
                       "JIN8":2.57E-08,
                       "JIN11":7.82E-07,
                       "JIN12":6.48E-07,
                       "JIN13":2.31E-07,
                       "JIN14":6.34E-07,
                       "JIN15":2.98E-07,
                       "JIN16":1.42E-07,
                       "JIN17":1.67E-06,
                       "JIN18":1.13E-08,
                       "JIN19":1.13E-08,
                       "JIN20":5.77E-06,
                       "JIN21":1.56E-08,
                       "JIN22":6.06E-08,
                       "JIN23":3.93E-08,
                       "JIN24":3.93E-08,
                       "JIN31":1.74E-07,
                       "JIN32":6.39E-07,
                       "JIN33":1.06E-06,
                       "JIN34":2.23E-06,
                       "JIN35":3.73E-06,
                       "JIN41":1.10E-07,
                       "JIN51":4.06E-08,
                       "JIN52":6.14E-08,
                       "JIN53":6.56E-08,
                       "JIN54":9.65E-08,
                       "JIN55":2.34E-07,
                       "JIN56":8.70E-07,
                       "JIN57":8.70E-07,
                       "JIN70":2.36365E-05,
                       "JIN71":6.51095E-06,
                       "JIN72":5.52355E-07,
                       "JIN73":2.28963E-07,
                       "JIN74":3.64387E-06,
                       "JIN75":2.23108E-05,
                       "JIN76":7.95721E-06,
                       "JIN77":1.90738E-05,
                       "JIN78":4.76845E-06}
    light_dict["CFT"]={"JIN1":4.79E-12,
                       "JIN2":4.04E-06,
                       "JIN3":6.33E-10,
                       "JIN4":6.47E-06,
                       "JIN5":5.62E-04,
                       "JIN6":2.27E-03,
                       "JIN7":1.53E-07,
                       "JIN8":0.00E+00,
                       "JIN11":0.00E+00,
                       "JIN12":0.00E+00,
                       "JIN13":0.00E+00,
                       "JIN14":0.00E+00,
                       "JIN15":8.81E-13,
                       "JIN16":4.20E-13,
                       "JIN17":0.00E+00,
                       "JIN18":4.35E-11,
                       "JIN19":4.35E-11,
                       "JIN20":2.23E-08,
                       "JIN21":0.00E+00,
                       "JIN22":0.00E+00,
                       "JIN23":1.77E-11,
                       "JIN24":1.77E-11,
                       "JIN31":0.00E+00,
                       "JIN32":4.33E-09,
                       "JIN33":1.28E-07,
                       "JIN34":1.73E-07,
                       "JIN35":1.45E-06,
                       "JIN41":8.39E-11,
                       "JIN51":0.00E+00,
                       "JIN52":0.00E+00,
                       "JIN53":0.00E+00,
                       "JIN54":5.39E-13,
                       "JIN55":0.00E+00,
                       "JIN56":0.00E+00,
                       "JIN57":0.00E+00,
                       "JIN70":8.88556E-07,
                       "JIN71":2.55288E-08,
                       "JIN72":1.2771E-08,
                       "JIN73":1.70952E-11,
                       "JIN74":4.83936E-08,
                       "JIN75":8.87035E-06,
                       "JIN76":0,
                       "JIN77":5.4533E-07,
                       "JIN78":1.36333E-07}
    light_dict["FT"]={"JIN1":4.08E-07,
                      "JIN2":3.31E-06,
                      "JIN3":5.08E-08,
                      "JIN4":1.99E-05,
                      "JIN5":4.09E-04,
                      "JIN6":1.61E-03,
                      "JIN7":3.50E-06,
                      "JIN8":7.41E-09,
                      "JIN11":2.27E-07,
                      "JIN12":1.99E-07,
                      "JIN13":6.61E-08,
                      "JIN14":1.80E-07,
                      "JIN15":8.68E-08,
                      "JIN16":4.14E-08,
                      "JIN17":4.83E-07,
                      "JIN18":3.61E-09,
                      "JIN19":3.61E-09,
                      "JIN20":1.85E-06,
                      "JIN21":4.51E-09,
                      "JIN22":1.74E-08,
                      "JIN23":1.18E-08,
                      "JIN24":1.18E-08,
                      "JIN31":5.10E-08,
                      "JIN32":1.90E-07,
                      "JIN33":3.27E-07,
                      "JIN34":6.79E-07,
                      "JIN35":1.17E-06,
                      "JIN41":3.31E-08,
                      "JIN51":1.17E-08,
                      "JIN52":1.77E-08,
                      "JIN53":1.91E-08,
                      "JIN54":2.79E-08,
                      "JIN55":6.75E-08,
                      "JIN56":2.53E-07,
                      "JIN57":2.53E-07,
                      "JIN70":7.60327E-06,
                      "JIN71":1.98205E-06,
                      "JIN72":1.71507E-07,
                      "JIN73":6.70884E-08,
                      "JIN74":1.12817E-06,
                      "JIN75":7.31706E-06,
                      "JIN76":8.49358E-06,
                      "JIN77":5.87615E-06,
                      "JIN78":1.46904E-06}
    light_dict["off"]={"JIN1":0,
                      "JIN2":0,
                      "JIN3":0,
                      "JIN4":0,
                      "JIN5":0,
                      "JIN6":0,
                      "JIN7":0,
                      "JIN8":0,
                      "JIN11":0,
                      "JIN12":0,
                      "JIN13":0,
                      "JIN14":0,
                      "JIN15":0,
                      "JIN16":0,
                      "JIN17":0,
                      "JIN18":0,
                      "JIN19":0,
                      "JIN20":0,
                      "JIN21":0,
                      "JIN22":0,
                      "JIN23":0,
                      "JIN24":0,
                      "JIN31":0,
                      "JIN32":0,
                      "JIN33":0,
                      "JIN34":0,
                      "JIN35":0,
                      "JIN41":0,
                      "JIN51":0,
                      "JIN52":0,
                      "JIN53":0,
                      "JIN54":0,
                      "JIN55":0,
                      "JIN56":0,
                      "JIN57":0,
                      "JIN70":0,
                      "JIN71":0,
                      "JIN72":0,
                      "JIN73":0,
                      "JIN74":0,
                      "JIN75":0,
                      "JIN76":0,
                      "JIN77":0,
                      "JIN78":0}
    
    for key in light_dict:
        light_dict[key]['numba_abs']=numba_abs
        light_dict[key]['numba_exp']=numba_exp
         
    light_dict["glass_C"]= {"ATTJ1":0.0030,
                            "ATTJ2":0.1666,
                            "ATTJ3":0.0593,
                            "ATTJ4":0.5993,
                            "ATTJ5":0.8494,
                            "ATTJ6":0.8536,
                            "ATTJ7":0.5809,
                            "ATTJ8":0.0075,
                            "ATTJ11":0.0293,
                            "ATTJ12":0.1526,
                            "ATTJ13":0.0032,
                            "ATTJ14":0.0006,
                            "ATTJ15":0.0300,
                            "ATTJ16":0.0300,
                            "ATTJ17":0.0187,
                            "ATTJ18":0.3004,
                            "ATTJ19":0.3004,
                            "ATTJ20":0.3004,
                            "ATTJ21":0.0005,
                            "ATTJ22":0.0054,
                            "ATTJ23":0.0921,
                            "ATTJ24":0.0921,
                            "ATTJ31":0.0343,
                            "ATTJ32":0.0741,
                            "ATTJ33":0.2484,
                            "ATTJ34":0.1576,
                            "ATTJ35":0.7743,
                            "ATTJ41":0.0803,
                            "ATTJ51":0.0066,
                            "ATTJ52":0.0076,
                            "ATTJ53":0.0157,
                            "ATTJ54":0.0102,
                            "ATTJ55":0.0103,
                            "ATTJ56":0.0220,
                            "ATTJ57":0.0220,
                            "ATTJ70":0.3458,
                            "ATTJ71":0.1297,
                            "ATTJ72":0.1964,
                            "ATTJ73":0.0352,
                            "ATTJ74":0.2088,
                            "ATTJ75":0.8009,
                            "ATTJ76":0.0036,
                            "ATTJ77":0.1919,
                            "ATTJ78":0.1919}
    light_dict["low_emissivity"]={"ATTJ1":0.0001,
                                  "ATTJ2":0.0972,
                                  "ATTJ3":0.0075,
                                  "ATTJ4":0.2954,
                                  "ATTJ5":0.6323,
                                  "ATTJ6":0.6572,
                                  "ATTJ7":0.2405,
                                  "ATTJ8":0.0004,
                                  "ATTJ11":0.0008,
                                  "ATTJ12":0.0245,
                                  "ATTJ13":0.0000,
                                  "ATTJ14":0.0000,
                                  "ATTJ15":0.0020,
                                  "ATTJ16":0.0020,
                                  "ATTJ17":0.0000,
                                  "ATTJ18":0.0937,
                                  "ATTJ19":0.0937,
                                  "ATTJ20":0.0937,
                                  "ATTJ21":0.0000,
                                  "ATTJ22":0.0002,
                                  "ATTJ23":0.0180,
                                  "ATTJ24":0.0180,
                                  "ATTJ31":0.0028,
                                  "ATTJ32":0.0173,
                                  "ATTJ33":0.1102,
                                  "ATTJ34":0.0758,
                                  "ATTJ35":0.5126,
                                  "ATTJ41":0.0162,
                                  "ATTJ51":0.0001,
                                  "ATTJ52":0.0002,
                                  "ATTJ53":0.0010,
                                  "ATTJ54":0.0005,
                                  "ATTJ55":0.0000,
                                  "ATTJ56":0.0009,
                                  "ATTJ57":0.0009,
                                  "ATTJ70":0.1219,
                                  "ATTJ71":0.0351,
                                  "ATTJ72":0.0818,
                                  "ATTJ73":0.0046,
                                  "ATTJ74":0.0744,
                                  "ATTJ75":0.4879,
                                  "ATTJ76":0.0000,
                                  "ATTJ77":0.0710,
                                  "ATTJ78":0.0710}
    light_dict["low_emissivity_film"]={"ATTJ1":0.0000,
                                       "ATTJ2":0.0774,
                                       "ATTJ3":0.0000,
                                       "ATTJ4":0.0408,
                                       "ATTJ5":0.5092,
                                       "ATTJ6":0.5494,
                                       "ATTJ7":0.0008,
                                       "ATTJ8":0.0000,
                                       "ATTJ11":0.0000,
                                       "ATTJ12":0.0000,
                                       "ATTJ13":0.0000,
                                       "ATTJ14":0.0000,
                                       "ATTJ15":0.0000,
                                       "ATTJ16":0.0000,
                                       "ATTJ17":0.0000,
                                       "ATTJ18":0.0001,
                                       "ATTJ19":0.0001,
                                       "ATTJ20":0.0001,
                                       "ATTJ21":0.0000,
                                       "ATTJ22":0.0000,
                                       "ATTJ23":0.0000,
                                       "ATTJ24":0.0000,
                                       "ATTJ31":0.0000,
                                       "ATTJ32":0.0024,
                                       "ATTJ33":0.0356,
                                       "ATTJ34":0.0247,
                                       "ATTJ35":0.3392,
                                       "ATTJ41":0.0000,
                                       "ATTJ51":0.0000,
                                       "ATTJ52":0.0000,
                                       "ATTJ53":0.0000,
                                       "ATTJ54":0.0000,
                                       "ATTJ55":0.0000,
                                       "ATTJ56":0.0000,
                                       "ATTJ57":0.0000,
                                       "ATTJ70":0.0100,
                                       "ATTJ71":0.0023,
                                       "ATTJ72":0.0137,
                                       "ATTJ73":0.0000,
                                       "ATTJ74":0.0067,
                                       "ATTJ75":0.1801,
                                       "ATTJ76":0.0000,
                                       "ATTJ77":0.0132,
                                       "ATTJ78":0.0132}
    light_dict["no_sunlight"]= {"ATTJ1":0,
                                "ATTJ2":0,
                                "ATTJ3":0,
                                "ATTJ4":0,
                                "ATTJ5":0,
                                "ATTJ6":0,
                                "ATTJ7":0,
                                "ATTJ8":0,
                                "ATTJ11":0,
                                "ATTJ12":0,
                                "ATTJ13":0,
                                "ATTJ14":0,
                                "ATTJ15":0,
                                "ATTJ16":0,
                                "ATTJ17":0,
                                "ATTJ18":0,
                                "ATTJ19":0,
                                "ATTJ20":0,
                                "ATTJ21":0,
                                "ATTJ22":0,
                                "ATTJ23":0,
                                "ATTJ24":0,
                                "ATTJ31":0,
                                "ATTJ32":0,
                                "ATTJ33":0,
                                "ATTJ34":0,
                                "ATTJ35":0,
                                "ATTJ41":0,
                                "ATTJ51":0,
                                "ATTJ52":0,
                                "ATTJ53":0,
                                "ATTJ54":0,
                                "ATTJ55":0,
                                "ATTJ56":0,
                                "ATTJ57":0,
                                "ATTJ70":0,
                                "ATTJ71":0,
                                "ATTJ72":0,
                                "ATTJ73":0,
                                "ATTJ74":0,
                                "ATTJ75":0,
                                "ATTJ76":0,
                                "ATTJ77":0,
                                "ATTJ78":0}
    light_dict["no_glass"]= {"ATTJ1":1,
                                "ATTJ2":1,
                                "ATTJ3":1,
                                "ATTJ4":1,
                                "ATTJ5":1,
                                "ATTJ6":1,
                                "ATTJ7":1,
                                "ATTJ8":1,
                                "ATTJ11":1,
                                "ATTJ12":1,
                                "ATTJ13":1,
                                "ATTJ14":1,
                                "ATTJ15":1,
                                "ATTJ16":1,
                                "ATTJ17":1,
                                "ATTJ18":1,
                                "ATTJ19":1,
                                "ATTJ20":1,
                                "ATTJ21":1,
                                "ATTJ22":1,
                                "ATTJ23":1,
                                "ATTJ24":1,
                                "ATTJ31":1,
                                "ATTJ32":1,
                                "ATTJ33":1,
                                "ATTJ34":1,
                                "ATTJ35":1,
                                "ATTJ41":1,
                                "ATTJ51":1,
                                "ATTJ52":1,
                                "ATTJ53":1,
                                "ATTJ54":1,
                                "ATTJ55":1,
                                "ATTJ56":1,
                                "ATTJ57":1,
                                "ATTJ70":1,
                                "ATTJ71":1,
                                "ATTJ72":1,
                                "ATTJ73":1,
                                "ATTJ74":1,
                                "ATTJ75":1,
                                "ATTJ76":1,
                                "ATTJ77":1,
                                "ATTJ78":1}
    return light_dict

def Zixu_photolysis_compiled():   
    '''
    Function to compile photolysis equations
    
    returns:
        photo_dict = dictionary of compiled photolysis equations
    '''
    photo_dict={}
    photo_dict['J1']=compile('((6.073E-05*numba_abs(cosx)**(1.743)*numba_exp(-1.0*0.474*secx))*ATTJ1)+JIN1','<string>','eval')
    photo_dict['J2']=compile('((4.775E-04*numba_abs(cosx)**(0.298)*numba_exp(-1.0*0.080*secx))*ATTJ2)+JIN2','<string>','eval')
    photo_dict['J3']=compile('((1.041E-05*numba_abs(cosx)**(0.723)*numba_exp(-1.0*0.279*secx))*ATTJ3)+JIN3','<string>','eval')
    photo_dict['J4']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ4)+JIN4','<string>','eval')
    photo_dict['J5']=compile('((2.485E-02*numba_abs(cosx)**(0.168)*numba_exp(-1.0*0.108*secx))*ATTJ5)+JIN5','<string>','eval')
    photo_dict['J6']=compile('((1.747E-01*numba_abs(cosx)**(0.155)*numba_exp(-1.0*0.125*secx))*ATTJ6)+JIN6','<string>','eval')
    photo_dict['J7']=compile('((2.644E-03*numba_abs(cosx)**(0.261)*numba_exp(-1.0*0.288*secx))*ATTJ7)+JIN7','<string>','eval')
    photo_dict['J8']=compile('((9.312E-07*numba_abs(cosx)**(1.230)*numba_exp(-1.0*0.307*secx))*ATTJ8)+JIN8','<string>','eval')
    photo_dict['J11']=compile('((4.642E-05*numba_abs(cosx)**(0.762)*numba_exp(-1.0*0.353*secx))*ATTJ11)+JIN11','<string>','eval')
    photo_dict['J12']=compile('((6.853E-05*numba_abs(cosx)**(0.477)*numba_exp(-1.0*0.323*secx))*ATTJ12)+JIN12','<string>','eval')
    photo_dict['J13']=compile('((7.344E-06*numba_abs(cosx)**(1.202)*numba_exp(-1.0*0.417*secx))*ATTJ13)+JIN13','<string>','eval')
    photo_dict['J14']=compile('((2.879E-05*numba_abs(cosx)**(1.067)*numba_exp(-1.0*0.358*secx))*ATTJ14)+JIN14','<string>','eval')
    photo_dict['J15']=compile('((2.792E-05*numba_abs(cosx)**(0.805)*numba_exp(-1.0*0.338*secx))*ATTJ15)+JIN15','<string>','eval')
    photo_dict['J16']=compile('((1.675E-05*numba_abs(cosx)**(0.805)*numba_exp(-1.0*0.338*secx))*ATTJ16)+JIN16','<string>','eval')
    photo_dict['J17']=compile('((7.914E-05*numba_abs(cosx)**(0.764)*numba_exp(-1.0*0.364*secx))*ATTJ17)+JIN17','<string>','eval')
    photo_dict['J18']=compile('((1.482E-06*numba_abs(cosx)**(0.396)*numba_exp(-1.0*0.298*secx))*ATTJ18)+JIN18','<string>','eval')
    photo_dict['J19']=compile('((1.482E-06*numba_abs(cosx)**(0.396)*numba_exp(-1.0*0.298*secx))*ATTJ19)+JIN19','<string>','eval')
    photo_dict['J20']=compile('((7.600E-04*numba_abs(cosx)**(0.396)*numba_exp(-1.0*0.298*secx))*ATTJ20)+JIN20','<string>','eval')
    photo_dict['J21']=compile('((7.992E-07*numba_abs(cosx)**(1.578)*numba_exp(-1.0*0.271*secx))*ATTJ21)+JIN21','<string>','eval')
    photo_dict['J22']=compile('((5.804E-06*numba_abs(cosx)**(1.092)*numba_exp(-1.0*0.377*secx))*ATTJ22)+JIN22','<string>','eval')
    photo_dict['J23']=compile('((2.424E-06*numba_abs(cosx)**(0.395)*numba_exp(-1.0*0.296*secx))*ATTJ23)+JIN23','<string>','eval')
    photo_dict['J24']=compile('((2.424E-06*numba_abs(cosx)**(0.395)*numba_exp(-1.0*0.296*secx))*ATTJ24)+JIN24','<string>','eval')
    photo_dict['J31']=compile('((6.845E-05*numba_abs(cosx)**(0.130)*numba_exp(-1.0*0.201*secx))*ATTJ31)+JIN31','<string>','eval')
    photo_dict['J32']=compile('((1.032E-05*numba_abs(cosx)**(0.130)*numba_exp(-1.0*0.201*secx))*ATTJ32)+JIN32','<string>','eval')
    photo_dict['J33']=compile('((3.802E-05*numba_abs(cosx)**(0.644)*numba_exp(-1.0*0.312*secx))*ATTJ33)+JIN33','<string>','eval')
    photo_dict['J34']=compile('((1.537E-04*numba_abs(cosx)**(0.170)*numba_exp(-1.0*0.208*secx))*ATTJ34)+JIN34','<string>','eval')
    photo_dict['J35']=compile('((3.326E-04*numba_abs(cosx)**(0.148)*numba_exp(-1.0*0.215*secx))*ATTJ35)+JIN35','<string>','eval')
    photo_dict['J41']=compile('((7.649E-06*numba_abs(cosx)**(0.682)*numba_exp(-1.0*0.279*secx))*ATTJ41)+JIN41','<string>','eval')
    photo_dict['J51']=compile('((1.588E-06*numba_abs(cosx)**(1.154)*numba_exp(-1.0*0.318*secx))*ATTJ51)+JIN51','<string>','eval')
    photo_dict['J52']=compile('((1.907E-06*numba_abs(cosx)**(1.244)*numba_exp(-1.0*0.335*secx))*ATTJ52)+JIN52','<string>','eval')
    photo_dict['J53']=compile('((2.485E-06*numba_abs(cosx)**(1.196)*numba_exp(-1.0*0.328*secx))*ATTJ53)+JIN53','<string>','eval')
    photo_dict['J54']=compile('((4.095E-06*numba_abs(cosx)**(1.111)*numba_exp(-1.0*0.316*secx))*ATTJ54)+JIN54','<string>','eval')
    photo_dict['J55']=compile('((1.135E-05*numba_abs(cosx)**(0.974)*numba_exp(-1.0*0.309*secx))*ATTJ55)+JIN55','<string>','eval')
    photo_dict['J56']=compile('((4.365E-05*numba_abs(cosx)**(1.089)*numba_exp(-1.0*0.323*secx))*ATTJ56)+JIN56','<string>','eval')
    photo_dict['J70']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ70)+JIN70','<string>','eval')
    photo_dict['J71']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ71)+JIN71','<string>','eval')
    photo_dict['J72']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ72)+JIN72','<string>','eval')
    photo_dict['J73']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ73)+JIN73','<string>','eval')
    photo_dict['J74']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ74)+JIN74','<string>','eval')
    photo_dict['J75']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ75)+JIN75','<string>','eval')
    photo_dict['J76']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ76)+JIN76','<string>','eval')
    photo_dict['J77']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ77)+JIN77','<string>','eval')
    photo_dict['J78']=compile('((1.165E-02*numba_abs(cosx)**(0.244)*numba_exp(-1.0*0.267*secx))*ATTJ78)+JIN78','<string>','eval')
    return photo_dict
