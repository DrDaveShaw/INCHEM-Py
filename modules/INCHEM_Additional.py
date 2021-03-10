'''
INCHEM and INCHEM-Py Additional reactions maintained by Shaw and Carslaw.
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

#RO2 to add to summation
INCHEM_RO2 = ["LINALAO2","LINALBO2","C7H15CO3","C8H17CO3","C9H19CO3","CH3CHOHO2"
             ,"OLECLO2","IPROCLPER","HYPROCLO2"]

INCHEM_sums = [["OLEFIN","BUT1ENE+CBUT2ENE+TBUT2ENE+MEPROPENE+PENT1ENE+CPENT2ENE+\
               TPENT2ENE+ME2BUT1ENE+ME3BUT1ENE+ME2BUT2ENE+HEX1ENE+CHEX2ENE+\
                   THEX2ENE+DM23BU2ENE+STYRENE+MVK+(0.55*MACR)"]]

INCHEM_rates=[
#KMT19:clo+clo=cloocl*,
#*IUPAC2019*
["K190","2.00e-32*((temp/300)**-4)*M"],
["K19I","1.0e-11"],
["KR19","K190/K19I"],
["FC19","0.6"],
["N19","(0.75-1.27*numba_log10(FC19))"],
["F19","10**(numba_log10(FC19)/(1+(numba_log10(KR19)/N19)**2))"],
["KMT19","(K190*K19I)*F19/(K190+K19I)"],
#*KMT20:CLOOCL=CLO+CLO*,
#*IUPAC2001*
["K200","3.7e-07*numba_exp(-7690/temp)*M"],
["K20I","1.80e+14*numba_exp(-7690/temp)"],
["KR20","K200/K20I"],
["FC20","0.6"],
["N20","(0.75-1.27*numba_log10(FC20))"],
["F20","10**(numba_log10(FC20)/(1+(numba_log10(KR20)/N20)**2))"],
["KMT20","(K200*K20I)*F20/(K200+K20I)"],
["CNO3","numba_sqrt(8.0*8.31*temp/(PI*6.20e-2))"],
["KNO3","2.5e-1*CNO3*4.0e-3*saero"],
["CN2O5","numba_sqrt(8.0*8.31*temp/(PI*1.08e-1))"],
["KN2O5","2.5e-1*CN2O5*1.0e-2*saero"],
["CCLNO3","numba_sqrt(8.0*8.31*temp/(PI*9.75e-2))"],
["KCLNO3","2.5e-1*CCLNO3*1.0e-2*saero"],
["CCLHO","numba_sqrt(8.0*8.31*temp/(PI*5.25e-2))"],
["KHOCL","2.5e-1*CCLHO*1.0e-2*saero"]
]

INCHEM_reactions=[
#Linalool
["1.7e-10*0.23","LINALOOL+OH=LINALAO2"],
["1.7e-10*0.77","LINALOOL+OH=LINALBO2"],
["KRO2NO*0.772","LINALAO2+NO=LINALAO+NO2"],
["KRO2NO*0.228","LINALAO2+NO=LINALANO3"],
["KRO2NO3","LINALAO2+NO3=LINALAO+NO2"],
["KRO2HO2*0.914","LINALAO2+HO2=LINALAOOH"],
["9.20e-14*RO2*0.7","LINALAO2=LINALAO"],
["9.20e-14*RO2*0.3","LINALAO2=LINALAOH"],
["KRO2NO*0.772","LINALBO2+NO=LINALBO+NO2"],
["KRO2NO*0.228","LINALBO2+NO=LINALBNO3"],
["KRO2NO3","LINALBO2+NO3=LINALBO+NO2"],
["KRO2HO2*0.914","LINALBO2+HO2=LINALBOOH"],
["9.20e-14*RO2*0.7","LINALBO2=LINALBO"],
["9.20e-14*RO2*0.3","LINALBO2=LINALBOH"],
["7.36e-11","LINALAOOH+OH=LINALAO2"],
["J41","LINALAOOH=LINALAO+OH"],
["6.20e-11","LINALANO3+OH=OCT3ONE+NO2"],
["KDEC","LINALAO=OCT3ONE+HO2+HOCH2CHO"],
["7.02e-11","LINALAOH+OH=OCT3ONE+HO2"],
["1.04e-10","LINALBOOH+OH=LINALBO2"],
["J41","LINALBOOH=LINALBO+OH"],
["6.20e-11","LINALBNO3+OH=C6H13CHO+NO2"],
["KDEC","LINALBO=CH3COCH3+HO2+C6H13CHO"],
["6.70e-11","LINALBOH+OH=C6H13CHO+HO2"],
["4.1e-16*0.8","LINALOOL+O3=CH3CCH3OOA+C6H13CHO"],
["4.1e-16*0.2","LINALOOL+O3=LINALOOB"],
["KDEC*0.5","LINALOOB=LINALBOO+OH"],
["KDEC*0.5","LINALOOB=C923O2+CO+OH"],
["1.20e-15","LINALBOo+CO=CH3COCH3"],
["1.00e-14","LINALBOo+NO=CH3COCH3+NO2"],
["1.00e-15","LINALBOo+NO2=CH3COCH3+NO3"],
["7.00e-14","LINALBOo+SO2=CH3COCH3+SO3"],
["1.40e-17*H2O","LINALBOO=CH3COCH3+H2O2"],
["2.00e-18*H2O","LINALBOO=CH3COCH3"],
#octanal scheme
["J15","C7H15CHO=HO2+CO+HEPTO2"],
["KNO3AL*5.5","NO3+C7H15CHO=C7H15CO3+HNO3"],
["3.2e-11","OH+C7H15CHO=C7H15CO3"],
["KAPHO2*0.15","C7H15CO3+HO2=C7H15CO2H+O3"],
["KAPHO2*0.41","C7H15CO3+HO2=C7H15CO3H"],
["KAPHO2*0.44","C7H15CO3+HO2=HEPTO2+OH"],
["KAPNO","C7H15CO3+NO=HEPTO2+NO2"],
["KFPAN","C7H15CO3+NO2=C7H15PAN"],
["KRO2NO3*1.74","C7H15CO3+NO3=HEPTO2+NO2"],
["1.00e-11*0.3*RO2","C7H15CO3=C7H15CO2H"],
["1.00e-11*0.7*RO2","C7H15CO3=HEPTO2"],
["9.89e-12","OH+C7H15CO2H=HEPTO2"],
["J41","C7H15CO3H=HEXAO2+OH"],
["1.33e-11","OH+C7H15CO3H=C7H15CO3"],
["6.16e-12","OH+C7H15PAN=C6H13CHO+CO+NO2"],
["KBPAN","C7H15PAN=C7H15CO3+NO2"],
#nonanal scheme
["J15","C8H17CHO=HO2+CO+OCTO2"],
["KNO3AL*5.5","NO3+C8H17CHO=C8H17CO3+HNO3"],
["3.6e-11","OH+C8H17CHO=C8H17CO3"],
["KAPHO2*0.15","C8H17CO3+HO2=C8H17CO2H+O3"],
["KAPHO2*0.41","C8H17CO3+HO2=C8H17CO3H"],
["KAPHO2*0.44","C8H17CO3+HO2=OCTO2+OH"],
["KAPNO","C8H17CO3+NO=OCTO2+NO2"],
["KFPAN","C8H17CO3+NO2=C8H17PAN"],
["KRO2NO3*1.74","C8H17CO3+NO3=OCTO2+NO2"],
["1.00e-11*0.3*RO2","C8H17CO3=C8H17CO2H"],
["1.00e-11*0.7*RO2","C8H17CO3=OCTO2"],
["9.89e-12","OH+C8H17CO2H=OCTO2"],
["J41","C8H17CO3H=HEPTO2+OH"],
["1.33e-11","OH+C8H17CO3H=C8H17CO3"],
["6.16e-12","OH+C8H17PAN=C7H15CHO+CO+NO2"],
["KBPAN","C8H17PAN=C8H17CO3+NO2"],
#decanal scheme
["J15","C9H19CHO=HO2+CO+NONO2"],
["KNO3AL*5.5","NO3+C9H19CHO=C9H19CO3+HNO3"],
["3.6e-11","OH+C9H19CHO=C9H19CO3"],
["KAPHO2*0.15","C9H19CO3+HO2=C9H19CO2H+O3"],
["KAPHO2*0.41","C9H19CO3+HO2=C9H19CO3H"],
["KAPHO2*0.44","C9H19CO3+HO2=NONO2+OH"],
["KAPNO","C9H19CO3+NO=NONO2+NO2"],
["KFPAN","C9H19CO3+NO2=C9H19PAN"],
["KRO2NO3*1.74","C9H19CO3+NO3=NONO2+NO2"],
["1.00e-11*0.3*RO2","C9H19CO3=C9H19CO2H"],
["1.00e-11*0.7*RO2","C9H19CO3=NONO2"],
["9.89e-12","OH+C9H19CO2H=NONO2"],
["J41","C9H19CO3H=OCTO2+OH"],
["1.33e-11","OH+C9H19CO3H=C9H19CO3"],
["6.16e-12","OH+C9H19PAN=C8H17CHO+CO+NO2"],
["KBPAN","C9H19PAN=C9H19CO3+NO2"],
#new CL chemistry from Zixu
["J75","OCLO=O+CLO"],
["J76","CLO=O+CL"],
["J77","CLOOCL=CLOO+CL"],
["J78","CLOOCL=CLO+CLO"],
["KMT19","CLO+CLO=CLOOCL"],
["KMT20","CLOOCL=CLO+CLO"],
["5.62e-13*N2","CLOO=CL"],
["2.5e-12*numba_exp(-600/temp)","NO+OCLO=NO2+CLO"],
["3.4e-11*numba_exp(160/temp)","CL+OCLO=CLO+CLO"],
["2.4e-12*numba_exp(-960/temp)","O+OCLO=CLO"],
["1.4e-12*numba_exp(600/temp)","OH+OCLO=HOCL"],

#monoterpenes
["8.80E-11*0.572","CAR+OH=APINAO2"],
["8.80E-11*0.353","CAR+OH=APINBO2"],
["8.80E-11*0.075","CAR+OH=APINCO2"],
["9.1E-12*0.65","CAR+NO3=NAPINAO2"],
["9.1E-12*0.35","CAR+NO3=NAPINBO2"],
["3.7E-17*0.5","CAR+O3=APINOOA"],
["3.7E-17*0.5","CAR+O3=APINOOB"],

#CAMPHENE
#CAMPHENE+OH
["5.33e-11*0.849","CAMPHENE+OH=CAMAO2"],
["5.33e-11*0.076","CAMPHENE+OH=CAMBO2"],
["5.33e-11*0.075","CAMPHENE+OH=CAMCO2"],
["KRO2NO*0.760","CAMAO2+NO=BPINAO+NO2"],
["KRO2NO*0.240","CAMAO2+NO=BPINANO3"],
["KRO2NO3","CAMAO2+NO3=BPINAO+NO2"],
["KRO2HO2*0.914","CAMAO2+HO2=BPINAOOH"],
["9.20e-14*RO2*0.7","CAMAO2=BPINAO"],
["9.20e-14*RO2*0.3","CAMAO2=BPINAOH"],
["KRO2NO*0.760","CAMBO2+NO=BPINBO+NO2"],
["KRO2NO*0.240","CAMBO2+NO=BPINBNO3"],
["KRO2NO3","CAMBO2+NO3=BPINBO+NO2"],
["KRO2HO2*0.914","CAMBO2+HO2=BPINBOOH"],
["2.00e-12*RO2*0.6","CAMBO2=BPINBO"],
["2.00e-12*RO2*0.2","CAMBO2=BPINAOH"],
["2.00e-12*RO2*0.2","CAMBO2=C918CHO"],
["KRO2NO*0.875","CAMCO2+NO=BPINCO+NO2"],
["KRO2NO*0.125","CAMCO2+NO=BPINCNO3"],
["KRO2NO3","CAMCO2+NO3=BPINCO+NO2"],
["KRO2HO2*0.914","CAMCO2+HO2=BPINCOOH"],
["6.70e-15*RO2*0.7","CAMCO2=BPINCO"],
["6.70e-15*RO2*0.3","CAMCO2=BPINCOH"],
#CAMPHENE+NO3
["6.6e-13*0.8","CAMPHENE+NO3=NCAMAO2"],
["6.6e-13*0.2","CAMPHENE+NO3=NCAMBO2"],
["9.20e-14*RO2*0.7","NCAMAO2=NBPINAO"],
["9.20e-14*RO2*0.3","NCAMAO2=BPINBNO3"],
["KRO2NO","NCAMAO2+NO=NBPINAO+NO2"],
["KRO2HO2*0.914","NCAMAO2+HO2=NBPINAOOH"],
["KRO2NO3","NCAMAO2+NO3=NBPINAO+NO2"],
["KRO2NO","NCAMBO2+NO=NBPINBO+NO2"],
["KRO2NO3","NCAMBO2+NO3=NBPINBO+NO2"],
["KRO2HO2*0.914","NCAMBO2+HO2=NBPINBOOH"],
["2.00e-12*RO2*0.6","NCAMBO2=NBPINBO"],
["2.00e-12*RO2*0.2","NCAMBO2=BPINANO3"],
["2.00e-12*RO2*0.6","NCAMBO2=NC91CHO"],
#CAMPHENE+O3 (OH Yield 18%)
["9.0e-19*0.6","CAMPHENE+O3=NOCAMOOA+HCHO"],
["9.0e-19*0.4","CAMPHENE+O3=CH2OOF"],
["KDEC*0.170","NOCAMOOA=NOPINOO"],
["KDEC*0.500*0.5","NOCAMOOA=NOPINDO2+OH"],
["KDEC*0.500*0.5","NOCAMOOA=NOPINDO2"],
["KDEC*0.330","NOCAMOOA=C8BC"],

#ALPHA-TERPINEOL SCHEME BASED ON A-PINENE
["1.9e-10*0.572","ATERP+OH=APINAO2"],
["1.9e-10*0.353","ATERP+OH=APINBO2"],
["1.9e-10*0.075","ATERP+OH=APINCO2"],
["16e-12*0.65","ATERP+NO3=NAPINAO2"],
["16e-12*0.35","ATERP+NO3=NAPINBO2"],
["3e-16*0.6","ATERP+O3=TERPOOA"],
["3e-16*0.4","ATERP+O3=TERPOOB"],
["KDEC*0.55*0.8","TERPOOA=C107O2+OH"],
["KDEC*0.55*0.2","TERPOOA=C107O2"],
["KDEC*0.45*0.8","TERPOOA=C109O2+OH"],
["KDEC*0.45*0.2","TERPOOA=C109O2"],
["KDEC*0.50","TERPOOB=APINBOO"],
["KDEC*0.50*0.8","TERPOOB=C96O2+OH+CO"],
["KDEC*0.50*0.2","TERPOOB=C96O2+CO"],

#GAMMA TERPINENE SCHEME BASED ON LIMONENE SCHEME
#GAMMATERPINENE+OH
["4.28e-11*numba_exp(401/temp)*0.408","GTERP+OH=GTERPAO2"],
["4.28e-11*numba_exp(401/temp)*0.222","GTERP+OH=GTERPBO2"],
["4.28e-11*numba_exp(401/temp)*0.370","GTERP+OH=GTERPCO2"],
["KRO2NO*0.772","GTERPAO2+NO=LIMAO+NO2"],
["KRO2NO*0.228","GTERPAO2+NO=LIMANO3"],
["KRO2NO3","GTERPAO2+NO3=LIMAO+NO2"],
["KRO2HO2*0.914","GTERPAO2+HO2=LIMAOOH"],
["9.20e-14*RO2*0.7","GTERPAO2=LIMAO"],
["9.20e-14*RO2*0.3","GTERPAO2=LIMAOH"],
["KRO2NO*0.772","GTERPBO2+NO=LIMBO+NO2"],
["KRO2NO*0.228","GTERPBO2+NO=LIMBNO3"],
["KRO2NO3","GTERPBO2+NO3=LIMBO+NO2"],
["KRO2HO2*0.914","GTERPBO2+HO2=LIMBOOH"],
["8.80e-13*RO2*0.6","GTERPBO2=LIMBO"],
["8.80e-13*RO2*0.2","GTERPBO2=LIMAOH"],
["8.80e-13*RO2*0.2","GTERPBO2=LIMBCO"],
["KRO2NO*0.772","GTERPCO2+NO=LIMCO+NO2"],
["KRO2NO*0.228","GTERPCO2+NO=LIMCNO3"],
["KRO2NO3","GTERPCO2+NO3=LIMCO+NO2"],
["KRO2HO2*0.914","GTERPCO2+HO2=LIMCOOH"],
["9.20e-14*RO2*0.7","GTERPCO2=LIMCO"],
["9.20e-14*RO2*0.3","GTERPCO2=LIMCOH"],
#GAMMA TERPINENE AND O3 (OH YIELD 81%)
["2.95e-15*numba_exp(-783/temp)*0.730","GTERP+O3=GTERPOOA"],
["2.95e-15*numba_exp(-783/temp)*0.270","GTERP+O3=GTERPOOB"],
["KDEC*0.5","GTERPOOA=LIMALAO2+OH"],
["KDEC*0.5","GTERPOOA=LIMALBO2+OH"],
["KDEC*0.5","GTERPOOB=LIMBOO"],
["KDEC*0.5*0.94","GTERPOOB=C923O2+CO+OH"],
["KDEC*0.5*0.06","GTERPOOB=C923O2+CO"],
#GAMMA TERPIENE AND NO3
["1.22e-11","GTERP+NO3=NGTERPO2"],
["KRO2NO","NGTERPO2+NO=NLIMO+NO2"],
["KRO2NO3","NGTERPO2+NO3=NLIMO+NO2"],
["KRO2HO2*0.914","NGTERPO2+HO2=NLIMOOH"],
["9.20e-14*RO2*0.7","NGTERPO2=NLIMO"],
["9.20e-14*RO2*0.3","NGTERPO2=LIMBNO3"],

#additional surface transformation
["4.83E-3*HMIX","NO2=HONO"],

# new chemistry for lactic acid + OH                                  
#     - based on 3-hydroxy propanoic acid + OH (MCM)                  
#     - lactic acid = 2-hydroxy propanoic acid
["1.39e-11","OH+CH3CHOHCO2H=CH3CHOHO2"],
["1.53e-13*numba_exp(1300/temp)","CH3CHOHO2+HO2=HY2ETHO2H"],
["KRO2NO*0.005","CH3CHOHO2+NO=ETHOH2NO3"],
["KRO2NO*0.995","CH3CHOHO2+NO=CH3CHOHO+NO2"],
["KRO2NO3","CH3CHOHO2+NO3=CH3CHOHO+NO2"],
["2*(KCH3O2*7.8e-14*numba_exp(1000/temp))**0.5*RO2*0.2","CH3CHOHO2=ETH2OH"],
["2*(KCH3O2*7.8e-14*numba_exp(1000/temp))**0.5*RO2*0.6","CH3CHOHO2=CH3CHOHO"],
["2*(KCH3O2*7.8e-14*numba_exp(1000/temp))**0.5*RO2*0.2","CH3CHOHO2=CH3CO2H"],
["1.90e-12*numba_exp(190/temp)","HY2ETHO2H+OH=CH3CHOHO2"],
["1.38e-11","HY2ETHO2H+OH=CH3CO2H+OH"],
["J41","HY2ETHO2H=CH3CHOHO+OH"],
["8.40e-13","ETHOH2NO3+OH=CH3CO2H+NO2"],
["9.50e+13*numba_exp(-5988/temp)","CH3CHOHO=HO2+CH3CHO"],
["KROPRIM*O2","CH3CHOHO=HO2+CH3CO2H"],
["1.45e-11","ETH2OH+OH=CH3CO2H+HO2"],

# CL reaction scheme to be incorporated to the MCM framework          
# Code compiled by Drs Likun Xue and Sam Saunders                     

# Inorganic reactions                                                 
# All of the kinetic data are taken from the IUPAC summary created    
# on 01 March 2010                                                    
# The outdoor photolysis frequencies are scaled to JNO2 based on the  
# TUV model calculations for Hong Kong                                

# top three reactions relate to mopping event 
["1.7e-12*numba_exp(-230/temp)","HCL+OH=CL"],
["J70","CL2=CL+CL"],
["J71","CLNO2=NO2+CL"],
["2.8e-11*numba_exp(-250/temp)","CL+O3=CLO"],
["7.00e-11","CLO+NO2=CLONO2"],
["2.2e-12*numba_exp(340/temp)","CLO+HO2=HOCL"],
["6.2e-12*numba_exp(295/temp)","CLO+NO=CL+NO2"],
["J73","CLONO2=NO3+CL"],
["J72","CLONO2=NO2+CLO"],
["J74","HOCL=OH+CL"],
["3.50e-11","CL+HO2=HCL"],
["7.5e-11*numba_exp(-620/temp)","CL+HO2=CLO+OH"],
["1.1e-11*numba_exp(-980/temp)","CL+H2O2=HCL+HO2"],
["2.40e-11","CL+NO3=NO2+CLO"],
["6.2e-12*numba_exp(145/temp)","CL+CLONO2=CL2+NO3"],
["3.6e-12*numba_exp(-1200/temp)","OH+CL2=HOCL+CL"],
["5.00e-13","OH+HOCL=CLO"],
["1.80e-11","OH+CLO=HO2+CL"],
["1.20e-12","OH+CLO=HCL"],
["J75","OCLO=O+CLO"],
["J76","CLO=O+CL"],
["J77","CLOOCL=CLOO+CL"],
["J78","CLOOCL=CLO+CLO"],

# Heterogeneous Processes 
# Heterogeneous reactions of NO3 and N2O5
["KNO3","NO3="],
["KN2O5*0.90","N2O5=NA+NA"],
["KN2O5*0.10","N2O5=NA+CLNO2"],
# Heterogeneous reactions of CLONO2 AND HOCL
["KCLNO3","CLONO2=CL2+HNO3"],
["KHOCL","HOCL=CL2"],

# Organic reactions                                                  
# Reactions of CL + OVOCs                                            
# H abstraction pathway dominates with the products already existing 
# in the MCM                                                                                                                             
# Reactions of CL + Aldehydes                                        
# Kinetic data from IUPAC for HCHO, CH3CHO AND C2H5CHO               
# Average ratio of kcl/koh for CH3CHO AND C2H5CHO is used for        
# other species                                                      
["8.1e-11*numba_exp(-34/temp)","HCHO+CL=HCL+HO2+CO"],
["8.0e-11*0.99","CL+CH3CHO=CH3CO3+HCL"],
["8.0e-11*0.01","CL+CH3CHO=HCOCH2O2+HCL"],
["1.3e-10","C2H5CHO+CL=C2H5CO3+HCL"],
["6.08*6.0e-12*numba_exp(410/temp)*0.151","C3H7CHO+CL=BUTALO2+HCL"],
["6.08*6.0e-12*numba_exp(410/temp)*0.849","C3H7CHO+CL=C3H7CO3+HCL"],
["6.08*6.8e-12*numba_exp(410/temp)*0.054","IPRCHO+CL=IBUTALBO2+HCL"],
["6.08*6.8e-12*numba_exp(410/temp)*0.059","IPRCHO+CL=IBUTALCO2+HCL"],
["6.08*6.8e-12*numba_exp(410/temp)*0.887","IPRCHO+CL=IPRCO3+HCL"],
["6.08*6.34e-12*numba_exp(448/temp)*0.19","C4H9CHO+CL=C4CHOBO2+HCL"],
["6.08*6.34e-12*numba_exp(448/temp)*0.81","C4H9CHO+CL=C4H9CO3+HCL"],
["6.08*5.9e-12*numba_exp(225/temp)","CL+BENZAL=C6H5CO3+HCL"],

# Reactions of CL with glyoxal and methyl glyoxal
# The mechanism is adopted from SAPRC, assuming same mechanism as for
# OH and same rate constants as for HCHO (GLYOX) and CH3CHO (MGLYOX)
["8.1e-11*numba_exp(-34/temp)*0.6","CL+GLYOX=CO+CO+HO2+HCL"],
["8.1e-11*numba_exp(-34/temp)*0.4","CL+GLYOX=HCOCO3+HCL"],
["8.0e-11","CL+MGLYOX=CH3CO3+CO+HCL"],


# Reaction of Cl with MACR
# Assuming the same mechanism as for OH
# In MCM, OH oxidation of MACR takes place by abstraction of H (45%)
# and addition of OH to double bond (55%)
# Here, 45of MACR is oxidized by Cl by H abstraction, and 55is
# oxidized by addition of Cl to double bond
# Hence, 55MACR is assigned to the lumped species OLEFIN, see later
# 6.08*8.0e-12*numba_exp(380/temp)*0.45 "," CL + MACR = MACO3 + HCL

# Reactions of CL + Ketones 
# Kinetic data from IUPAC for CH3COCH3 AND MEK 
# Average ratio of kcl/koh for CH3COCH3 AND MEK is used for
# other species 
["1.5e-11*numba_exp(-590/temp)","CH3COCH3+CL=CH3COCH2O2+HCL"],
["3.05e-11*numba_exp(80/temp)*0.459","MEK+CL=MEKAO2+HCL"],
["3.05e-11*numba_exp(80/temp)*0.462","MEK+CL=MEKBO2+HCL"],
["3.05e-11*numba_exp(80/temp)*0.079","MEK+CL=MEKCO2+HCL"],
["23.9*4.90e-12*0.818","MPRK+CL=CO2C54O2+HCL"],
["23.9*4.90e-12*0.182","MPRK+CL=MPRKAO2+HCL"],
["23.9*2.00e-12*0.501","DIEK+CL=DIEKAO2+HCL"],
["23.9*2.00e-12*0.499","DIEK+CL=DIEKBO2+HCL"],
["23.9*2.77e-12*0.523","CL+MIPK=MIPKAO2+HCL"],
["23.9*2.77e-12*0.477","CL+MIPK=MIPKBO2+HCL"],
["23.9*9.10e-12*0.715","HEX2ONE+CL=HEX2ONAO2+HCL"],
["23.9*9.10e-12*0.162","HEX2ONE+CL=HEX2ONBO2+HCL"],
["23.9*9.10e-12*0.123","HEX2ONE+CL=HEX2ONCO2+HCL"],
["23.9*6.90e-12*0.638","HEX3ONE+CL=HEX3ONAO2+HCL"],
["23.9*6.90e-12*0.142","HEX3ONE+CL=HEX3ONBO2+HCL"],
["23.9*6.90e-12*0.110","HEX3ONE+CL=HEX3ONCO2+HCL"],
["23.9*6.90e-12*0.110","HEX3ONE+CL=HEX3ONDO2+HCL"],
["23.9*1.41e-11*0.91","MIBK+CL=MIBKAO2+HCL"],
["23.9*1.41e-11*0.09","MIBK+CL=MIBKBO2+HCL"],
["23.9*1.21e-12","CL+MTBK=MTBKO2+HCL"],
["23.9*5.40e-12","CYHEXONE+CL=CYHXONAO2+HCL"],

# Reaction of Cl with MVK
# Assuming the same mechanism as for OH
# In MCM, OH oxidation of MVK takes place by addition of OH to
# double bond
# Hence, MVK is assigned to the lumped species OLEFIN, see later
                                                                 
# Reactions of CL + Alcohols 
# Kinetic data from IUPAC for CH3OH, C2H5OH, C3H7OH AND NC4H90H
# Average ratio of kcl/koh for IC3H7OH is used for other species
["7.1e-11*numba_exp(-75/temp)","CH3OH+CL=HO2+HCHO+HCL"],
["6.0e-11*numba_exp(155/temp)*0.92","C2H5OH+CL=CH3CHO+HO2+HCL"],
["6.0e-11*numba_exp(155/temp)*0.08","C2H5OH+CL=HOCH2CH2O2+HCL"],
["2.7e-11*numba_exp(525/temp)*0.60","NPROPOL+CL=C2H5CHO+HO2+HCL"],
["2.7e-11*numba_exp(525/temp)*0.15","NPROPOL+CL=HO1C3O2+HCL"],
["2.7e-11*numba_exp(525/temp)*0.25","NPROPOL+CL=HYPROPO2+HCL"],
["7.4e-11","IPROPOL+CL=CH3COCH3+HO2+HCL"],
["1.3e-11","IPROPOL+CL=IPROPOLO2+HCL"],
["3.5e-11*numba_exp(550/temp)*0.358","NBUTOL+CL=C3H7CHO+HO2+HCL"],
["3.5e-11*numba_exp(550/temp)*0.321","NBUTOL+CL=NBUTOLAO2+HCL"],
["3.5e-11*numba_exp(550/temp)*0.321","NBUTOL+CL=NBUTOLBO2+HCL"],
["17.1*8.7e-12*0.361","BUT2OL+CL=BUT2OLO2+HCL"],
["17.1*8.7e-12*0.639","BUT2OL+CL=MEK+HO2+HCL"],
["17.1*2.73e-12*numba_exp(352/temp)*0.558","IBUTOL+CL=IBUTOLBO2+HCL"],
["17.1*2.73e-12*numba_exp(352/temp)*0.090","IBUTOL+CL=IBUTOLCO2+HCL"],
["17.1*2.73e-12*numba_exp(352/temp)*0.352","IBUTOL+CL=IPRCHO+HO2+HCL"],
["17.1*1.6e-12*numba_exp(-121/temp)*0.888","CL+TBUTOL=TBUTOLO2+HCL"],
["17.1*1.6e-12*numba_exp(-121/temp)*0.112","CL+TBUTOL=TC4H9O+HCL"],
["17.1*1.22e-11*0.436","CL+PECOH=DIEK+HO2+HCL"],
["17.1*1.22e-11*0.070","CL+PECOH=HO3C5O2+HCL"],
["17.1*1.22e-11*0.493","CL+PECOH=PE2ENEBO2+HCL"],
["17.1*1.12e-11*0.288","CL+IPEAOH=BUT2CHO+HO2+HCL"],
["17.1*1.12e-11*0.258","CL+IPEAOH=HM2C43O2+HCL"],
["17.1*1.12e-11*0.454","CL+IPEAOH=M2BUOL2O2+HCL"],
["17.1*1.31e-11*0.288","ME3BUOL+CL=C3ME3CHO+HO2+HCL"],
["17.1*1.31e-11*0.454","ME3BUOL+CL=HM33C3O2+HCL"],
["17.1*1.31e-11*0.258","ME3BUOL+CL=ME3BUOLO2+HCL"],
["17.1*3.85e-12*0.100","CL+IPECOH=HO2M2C4O2+HCL"],
["17.1*3.85e-12*0.701","CL+IPECOH=ME2BU2OLO2+HCL"],
["17.1*3.85e-12*0.199","CL+IPECOH=PROL11MO2+HCL"],
["17.1*1.24e-11*0.074","CL+IPEBOH=H2M3C4O2+HCL"],
["17.1*1.24e-11*0.463","CL+IPEBOH=ME2BUOLO2+HCL"],
["17.1*1.24e-11*0.463","CL+IPEBOH=MIPK+HO2+HCL"],
["17.1*1.77e-11*0.739","CYHEXOL+CL=CYHEXOLAO2+HCL"],
["17.1*1.77e-11*0.261","CYHEXOL+CL=CYHEXONE+HO2+HCL"],
["17.1*2.88e-12*0.693","MIBKAOH+CL=MIBKAOHAO2+HCL"],
["17.1*2.88e-12*0.270","MIBKAOH+CL=MIBKAOHBO2+HCL"],
["17.1*2.88e-12*0.037","MIBKAOH+CL=MIBKHO4O2+HCL"],
["17.1*1.45e-11","ETHGLY+CL=HOCH2CHO+HO2+HCL"],
["17.1*1.20e-11*0.613","PROPGLY+CL=ACETOL+HO2+HCL"],
["17.1*1.20e-11*0.387","PROPGLY+CL=CH3CHOHCHO+HO2+HCL"],

# Reaction of Cl with cresol
# The mechanism is adopted from SAPRC
["6.2e-11","CRESOL+CL=OXYL1O2+HCL"],

#Reactions of CL + selected organic acids and nitrates 
#Kinetic data from IUPAC 
["5.9e-11*0.6","CL+CH3OOH=CH3O2+HCL"],
["5.9e-11*0.4","CL+CH3OOH=HCHO+OH+HCL"],
["1.9e-13","HCOOH+CL=HO2+HCL"],
["2.65e-14","CH3CO2H+CL=CH3O2+HCL"],
["0.033*1.2e-12","PROPACID+CL=C2H5O2+HCL"],
["2.4e-13","CL+CH3NO3=HCHO+NO2+HCL"],
["4.7e-12","CL+C2H5NO3=CH3CHO+NO2+HCL"],
["2.2e-11","CL+NC3H7NO3=C2H5CHO+NO2+HCL"],
["3.8e-12","CL+IC3H7NO3=CH3COCH3+NO2+HCL"],
["8.5e-11","CL+NC4H9NO3=C3H7CHO+NO2+HCL"],
                                                                   
# Reactions of CL + Aromatics 
# Kinetic data from Shi and Bernhard 1997 for toluene and oXylene 
# Average ratio of kcl/koh for toluene and oXylene is used for
# the other species
# Addition of Cl to aromatic ring is very slow, about 100 folder
# slower than addition of OH to the aromatic ring, thus only H abstraction
# pathway was considered here 
["5.9e-11","TOLUENE+CL=C6H5CH2O2+HCL"],
["1.5e-10","OXYL+CL=OXYLO2+HCL"],
["185.0*2.31e-11*0.04","MXYL+CL=MXYLO2+HCL"],
["185.0*1.43e-11*0.10","PXYL+CL=PXYLO2+HCL"],
["185.0*7.00e-12*0.07","EBENZ+CL=C6H5C2H4O2+HCL"],
["185.0*5.80e-12*0.07","PBENZ+CL=PHC3O2+HCL"],
["185.0*6.30e-12*0.07","IPBENZ+CL=PHIC3O2+HCL"],
["185.0*3.27e-11*0.06","TM123B+CL=TM123BO2+HCL"],
["185.0*3.25e-11*0.06","TM124B+CL=TM124BO2+HCL"],
["185.0*5.67e-11*0.03","TM135B+CL=TMBO2+HCL"],
["185.0*1.19e-11*0.05","OETHTOL+CL=ETOLO2+HCL"],
["185.0*1.86e-11*0.04","METHTOL+CL=ETOLO2+HCL"],
["185.0*1.18e-11*0.10","PETHTOL+CL=ETOLO2+HCL"], 
                                                                   
# Reactions of CL + Alkenes 
# Addition of CL to the double bond dominates 

# Reaction of CL + C2H4 
# Kinetic data from IUPAC 
# Product CH2CLCH2O2 already exists in the MCM 
["1.0e-10","C2H4+CL=CH2CLCH2O2"],

# Reaction of CL + C3H6 
# Reaction scheme from Riedel et al., ACP, 2014 with Kinetic data
# from IUPAC 
["2.7e-10*0.10","C3H6+CL=C3H5O2+HCL"],
["2.7e-10*0.50","C3H6+CL=IPROCLO2"],
["2.7e-10*0.40","C3H6+CL=HYPROCLO2"],

# Reactions of C3H5O2
# Assuming unit conversion of NO to NO2
["KRO2NO","C3H5O2+NO=ACR+NO2+HO2"],
["KRO2HO2*0.520","C3H5O2+HO2=C3H5O2H"],
["KRO2NO3","C3H5O2+NO3=ACR+NO2+HO2"],
["2.00e-12*0.6*RO2","C3H5O2=ACR+HO2"],
["2.00e-12*0.4*RO2","C3H5O2="],
# Simplification - further reactions of C3H5O2H not considered

# Reactions of IPROCLO2
# Assuming reaction rates and branching ratios similar to
# those of IPROPOLO2 in the MCM
["KRO2HO2*0.520","IPROCLO2+HO2=IPROCLO2H"],
["KRO2NO","IPROCLO2+NO=CH3CHCLCHO+NO2+HO2"],
# Assuming unit conversion of NO to NO2
["KRO2NO3","IPROCLO2+NO3=CH3CHCLCHO+NO2+HO2"],
["2.00e-12*0.6*RO2","IPROCLO2=CH3CHCLCHO+HO2"],
["2.00e-12*0.4*RO2","IPROCLO2="],
# Simplification -  further reactions of IPROCLO2H not considered 

# Reactions of CH3CHCLCHO 
["KNO3AL*2.4","CH3CHCLCHO+NO3=CH3CHCLCO3+HNO3"],
["1.7e-11","CH3CHCLCHO+OH=CH3CHCLCO3"],
["J17","CH3CHCLCHO=CH3CHCLO2+HO2+CO"], 
# Product CH3CHCLO2 already exsited in the MCM 
# Reactions of CH3CHCLCO3 
["KAPHO2*0.44","CH3CHCLCO3+HO2=CH3CHCLO2+OH"],
["KAPHO2*0.41","CH3CHCLCO3+HO2=IPROCLPER"],
["KAPHO2*0.15","CH3CHCLCO3+HO2=C2H4CLCO2H+O3"],
["KAPNO","CH3CHCLCO3+NO=CH3CHCLO2+NO2"],
["KFPAN","CH3CHCLCO3+NO2=IPROCLPAN"],
["KRO2NO3*1.74","CH3CHCLCO3+NO3=CH3CHCLO2+NO2"],
["1.00e-11*RO2*0.70","CH3CHCLCO3=CH3CHCLO2"],
["1.00e-11*RO2*0.30","CH3CHCLCO3=C2H4CLCO2H"], 

["9.34e-12","IPROCLPER+OH=CH3CHCLCO3"],
["J41","IPROCLPER=CH3CHCLO2+OH"],

["1.2e-12","C2H4CLCO2H+OH=CH3CHCLO2"],

["2.34e-12","IPROCLPAN+OH=CLETAL+CO+NO2"],
["KBPAN","IPROCLPAN=CH3CHCLCO3+NO2"], 
# Product CLETAL already exists in the MCM

# Reactions of HYPROCLO2
# Assuming reaction rates and branching ratios similar to
# those of HYPROPO2

["KRO2HO2*0.520","HYPROCLO2+HO2=HYPROCLO2H"],
# Simplification - further reactions of HYPROCLO2H not considered
["KRO2NO3","HYPROCLO2+NO3=CH3CHCLCHO+NO2+HO2"],
["8.80e-13*0.6*RO2","HYPROCLO2=CH3CHCLCHO+HO2"],
["8.80e-13*0.4*RO2","HYPROCLO2="],
# Simplification - further reactions of products not considered 
["KRO2NO","NO+HYPROCLO2=CH3CHCLCHO+NO2+HO2"], 
# Assuming unit conversion of NO to NO2
# Simplification - assuming the same reactions of CH3CHCLCHO
# to those of ACETCL

# Reactions of CL + other alkenes
# Given the complexity, a lump method is adopted here 
# Define a new parameter OLEFIN that is the sum of all primary alkenes
# other than ethene and propene, styrene, MVK and 0.55#MACR
#
# OLEFIN reacts with CL by adding CL to the double bond, producing
# OLECLO2 
# OLECLO2 further reacts with NO, NO3, HO2, RO2 to produce OLECLCHO 
# OLECLCHO reacts with OH and NO3 to produce OLECLCO3 
# OLECLCO3 then reacts with NO, NO3, HO2, RO2 to produce OVOCs that
# are not further considered 
#
# Reaction rate of CL + OLEFIN is assumed to be 20 fold that
# of OH + OLEFIN, based on the CB-IV protocol 
# Reaction rate of OH + OLEFIN is calculated as the average of those
# for the 15 alkenes
#
["11.0*5.33e-11*OLEFIN","CL=OLECLO2"],
["KRO2HO2*0.706","OLECLO2+HO2=OLECLO2H"],
# Simplification - further reactions of OLECLO2H not considered
["KRO2NO","OLECLO2+NO=OLECLCHO+NO2+HO2"],
# Assuming unit conversion of NO to NO2
["KRO2NO3","OLECLO2+NO3=OLECLCHO+NO2+HO2"],
["2.00e-12*0.6*RO2","OLECLO2=OLECLCHO+HO2"],
["2.00e-12*0.4*RO2","OLECLO2="],
# Simplification -further reactions of products not considered 
["KNO3AL*5.5","OLECLCHO+NO3=OLECLCO3+HNO3"],
["6.34e-12*numba_exp(448/temp)","OLECLCHO+OH=OLECLCO3"],
["J15","OLECLCHO=OLECLO2+HO2+CO"],
["KAPHO2","OLECLCO3+HO2="],
["KAPNO","OLECLCO3+NO=OLECLO2+NO2"],
["KRO2NO3*1.74","OLECLCO3+NO3=OLECLO2+NO2"],
["1.00e-11*RO2*0.70","OLECLCO3=OLECLO2"],
["1.00e-11*RO2*0.30","OLECLCO3="],
["KFPAN","OLECLCO3+NO2=OLECLPAN"],
["KBPAN","OLECLPAN=OLECLCO3+NO2"],
#
#
# Reaction of CL + C5H8
# Reactions of CL + C5H8 are very complex and remain unclear, thus
# the very simplified scheme from the CB-IV mechanism is adopted here,
# to mainly represent the enhancement in ozone production 
# The reaction rate of CL + C5H8 is 4.75 fold that of OH + C5H8,
# based on the CB-IV 
#
["4.75*2.7e-11*numba_exp(390/temp)","C5H8+CL=ISOCLO2"],
["KRO2NO","ISOCLO2+NO=ISOCLO+NO2"],
["KDEC","ISOCLO=ISOCLCHO+CH3O2"],
# Simplification - other reactions of ISOCLCHO not considered
#
# Reaction of CL with acetylene
# The mechanism is taken from SAPRC
["4.97e-11","C2H2+CL=CHOCL+CO+HO2"] 
# CHANGED PRODUCT CLCHO TO CHOCL AS ALREADY IN MCM
]