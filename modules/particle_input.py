# -*- coding: utf-8 -*-
"""
Defines parameters for particle reactions for INCHEM-Py.
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
import re

def particle_species_def():
    '''
    particle species list

    returns:
        particle_species = list of particle species
    '''
    particle_species=   ['SEED', # aerosol formed from chemistry
                        'SEED_1', # 30% TSPOUT
                        'TSPNONORG', # 70% TSPOUT
                        'PART1',
                        'PART100',
                        'PART101',
                        'PART102',
                        'PART103',
                        'PART104',
                        'PART105',
                        'PART106',
                        'PART107',
                        'PART108',
                        'PART109',
                        'PART11',
                        'PART110',
                        'PART111',
                        'PART112',
                        'PART113',
                        'PART114',
                        'PART115',
                        'PART116',
                        'PART117',
                        'PART118',
                        'PART119',
                        'PART120',
                        'PART121',
                        'PART122',
                        'PART123',
                        'PART124',
                        'PART125',
                        'PART126',
                        'PART127',
                        'PART128',
                        'PART129',
                        'PART13',
                        'PART130',
                        'PART131',
                        'PART132',
                        'PART133',
                        'PART134',
                        'PART135',
                        'PART136',
                        'PART137',
                        'PART138',
                        'PART139',
                        'PART14',
                        'PART140',
                        'PART141',
                        'PART142',
                        'PART143',
                        'PART144',
                        'PART145',
                        'PART146',
                        'PART147',
                        'PART148',
                        'PART149',
                        'PART15',
                        'PART150',
                        'PART151',
                        'PART152',
                        'PART153',
                        'PART154',
                        'PART155',
                        'PART156',
                        'PART157',
                        'PART158',
                        'PART159',
                        'PART16',
                        'PART160',
                        'PART161',
                        'PART162',
                        'PART163',
                        'PART164',
                        'PART165',
                        'PART166',
                        'PART167',
                        'PART168',
                        'PART169',
                        'PART17',
                        'PART170',
                        'PART171',
                        'PART172',
                        'PART173',
                        'PART174',
                        'PART175',
                        'PART176',
                        'PART177',
                        'PART178',
                        'PART179',
                        'PART180',
                        'PART181',
                        'PART182',
                        'PART183',
                        'PART184',
                        'PART185',
                        'PART186',
                        'PART200',
                        'PART201',
                        'PART202',
                        'PART203',
                        'PART204',
                        'PART205',
                        'PART206',
                        'PART207',
                        'PART209',
                        'PART210',
                        'PART211',
                        'PART212',
                        'PART213',
                        'PART214',
                        'PART215',
                        'PART216',
                        'PART217',
                        'PART218',
                        'PART219',
                        'PART22',
                        'PART220',
                        'PART221',
                        'PART222',
                        'PART223',
                        'PART224',
                        'PART225',
                        'PART226',
                        'PART227',
                        'PART228',
                        'PART229',
                        'PART23',
                        'PART230',
                        'PART231',
                        'PART232',
                        'PART233',
                        'PART234',
                        'PART235',
                        'PART236',
                        'PART237',
                        'PART238',
                        'PART239',
                        'PART24',
                        'PART240',
                        'PART241',
                        'PART242',
                        'PART243',
                        'PART244',
                        'PART245',
                        'PART246',
                        'PART247',
                        'PART248',
                        'PART249',
                        'PART25',
                        'PART250',
                        'PART251',
                        'PART252',
                        'PART253',
                        'PART254',
                        'PART255',
                        'PART256',
                        'PART257',
                        'PART258',
                        'PART259',
                        'PART26',
                        'PART260',
                        'PART261',
                        'PART262',
                        'PART263',
                        'PART264',
                        'PART265',
                        'PART266',
                        'PART267',
                        'PART268',
                        'PART269',
                        'PART27',
                        'PART270',
                        'PART271',
                        'PART272',
                        'PART273',
                        'PART274',
                        'PART275',
                        'PART276',
                        'PART277',
                        'PART278',
                        'PART279',
                        'PART28',
                        'PART280',
                        'PART281',
                        'PART282',
                        'PART283',
                        'PART284',
                        'PART285',
                        'PART286',
                        'PART287',
                        'PART288',
                        'PART289',
                        'PART29',
                        'PART290',
                        'PART291',
                        'PART292',
                        'PART293',
                        'PART294',
                        'PART295',
                        'PART296',
                        'PART297',
                        'PART298',
                        'PART299',
                        'PART2A',
                        'PART2B',
                        'PART3',
                        'PART30',
                        'PART300',
                        'PART301',
                        'PART302',
                        'PART303',
                        'PART304',
                        'PART305',
                        'PART306',
                        'PART307',
                        'PART308',
                        'PART309',
                        'PART31',
                        'PART310',
                        'PART311',
                        'PART312',
                        'PART313',
                        'PART314',
                        'PART315',
                        'PART316',
                        'PART317',
                        'PART318',
                        'PART319',
                        'PART32',
                        'PART320',
                        'PART321',
                        'PART322',
                        'PART323',
                        'PART324',
                        'PART325',
                        'PART326',
                        'PART327',
                        'PART33',
                        'PART34',
                        'PART35',
                        'PART350',
                        'PART351',
                        'PART352',
                        'PART353',
                        'PART354',
                        'PART355',
                        'PART356',
                        'PART357',
                        'PART358',
                        'PART359',
                        'PART36',
                        'PART360',
                        'PART361',
                        'PART362',
                        'PART363',
                        'PART364',
                        'PART365',
                        'PART366',
                        'PART367',
                        'PART368',
                        'PART369',
                        'PART37',
                        'PART370',
                        'PART371',
                        'PART372',
                        'PART373',
                        'PART374',
                        'PART375',
                        'PART376',
                        'PART377',
                        'PART378',
                        'PART379',
                        'PART38',
                        'PART380',
                        'PART381',
                        'PART382',
                        'PART383',
                        'PART384',
                        'PART385',
                        'PART386',
                        'PART387',
                        'PART388',
                        'PART389',
                        'PART39',
                        'PART390',
                        'PART391',
                        'PART392',
                        'PART393',
                        'PART394',
                        'PART395',
                        'PART396',
                        'PART397',
                        'PART398',
                        'PART399',
                        'PART4',
                        'PART40',
                        'PART400',
                        'PART401',
                        'PART402',
                        'PART403',
                        'PART404',
                        'PART405',
                        'PART406',
                        'PART407',
                        'PART408',
                        'PART409',
                        'PART41',
                        'PART410',
                        'PART411',
                        'PART412',
                        'PART413',
                        'PART414',
                        'PART415',
                        'PART416',
                        'PART417',
                        'PART418',
                        'PART419',
                        'PART42',
                        'PART420',
                        'PART421',
                        'PART422',
                        'PART423',
                        'PART424',
                        'PART425',
                        'PART426',
                        'PART427',
                        'PART428',
                        'PART429',
                        'PART43',
                        'PART430',
                        'PART431',
                        'PART432',
                        'PART433',
                        'PART434',
                        'PART435',
                        'PART436',
                        'PART437',
                        'PART438',
                        'PART439',
                        'PART44',
                        'PART440',
                        'PART441',
                        'PART442',
                        'PART443',
                        'PART444',
                        'PART445',
                        'PART446',
                        'PART447',
                        'PART448',
                        'PART449',
                        'PART45',
                        'PART450',
                        'PART451',
                        'PART452',
                        'PART453',
                        'PART454',
                        'PART455',
                        'PART456',
                        'PART457',
                        'PART458',
                        'PART459',
                        'PART46',
                        'PART460',
                        'PART461',
                        'PART462',
                        'PART463',
                        'PART464',
                        'PART465',
                        'PART466',
                        'PART467',
                        'PART468',
                        'PART469',
                        'PART47',
                        'PART470',
                        'PART471',
                        'PART472',
                        'PART473',
                        'PART474',
                        'PART475',
                        'PART476',
                        'PART477',
                        'PART478',
                        'PART479',
                        'PART48',
                        'PART480',
                        'PART481',
                        'PART482',
                        'PART483',
                        'PART484',
                        'PART485',
                        'PART486',
                        'PART487',
                        'PART488',
                        'PART489',
                        'PART49',
                        'PART490',
                        'PART491',
                        'PART492',
                        'PART493',
                        'PART494',
                        'PART495',
                        'PART496',
                        'PART497',
                        'PART498',
                        'PART499',
                        'PART5',
                        'PART50',
                        'PART500',
                        'PART501',
                        'PART502',
                        'PART503',
                        'PART504',
                        'PART505',
                        'PART506',
                        'PART507',
                        'PART508',
                        'PART509',
                        'PART51',
                        'PART510',
                        'PART511',
                        'PART512',
                        'PART513',
                        'PART514',
                        'PART515',
                        'PART516',
                        'PART517',
                        'PART518',
                        'PART519',
                        'PART52',
                        'PART520',
                        'PART521',
                        'PART522',
                        'PART523',
                        'PART524',
                        'PART525',
                        'PART526',
                        'PART527',
                        'PART528',
                        'PART529',
                        'PART53',
                        'PART530',
                        'PART531',
                        'PART532',
                        'PART533',
                        'PART534',
                        'PART535',
                        'PART536',
                        'PART537',
                        'PART538',
                        'PART539',
                        'PART54',
                        'PART540',
                        'PART541',
                        'PART542',
                        'PART543',
                        'PART544',
                        'PART545',
                        'PART546',
                        'PART547',
                        'PART548',
                        'PART549',
                        'PART55',
                        'PART550',
                        'PART551',
                        'PART552',
                        'PART553',
                        'PART554',
                        'PART555',
                        'PART556',
                        'PART557',
                        'PART558',
                        'PART559',
                        'PART56',
                        'PART560',
                        'PART561',
                        'PART562',
                        'PART563',
                        'PART564',
                        'PART565',
                        'PART566',
                        'PART567',
                        'PART568',
                        'PART569',
                        'PART57',
                        'PART570',
                        'PART571',
                        'PART572',
                        'PART573',
                        'PART574',
                        'PART575',
                        'PART576',
                        'PART577',
                        'PART578',
                        'PART579',
                        'PART58',
                        'PART580',
                        'PART581',
                        'PART582',
                        'PART583',
                        'PART584',
                        'PART585',
                        'PART586',
                        'PART587',
                        'PART588',
                        'PART589',
                        'PART59',
                        'PART590',
                        'PART591',
                        'PART592',
                        'PART593',
                        'PART594',
                        'PART595',
                        'PART596',
                        'PART597',
                        'PART598',
                        'PART599',
                        'PART6',
                        'PART60',
                        'PART600',
                        'PART601',
                        'PART602',
                        'PART603',
                        'PART604',
                        'PART605',
                        'PART606',
                        'PART607',
                        'PART608',
                        'PART609',
                        'PART61',
                        'PART610',
                        'PART62',
                        'PART63',
                        'PART64',
                        'PART65',
                        'PART66',
                        'PART67',
                        'PART68',
                        'PART69',
                        'PART70',
                        'PART71',
                        'PART72',
                        'PART73',
                        'PART74',
                        'PART75',
                        'PART76',
                        'PART77',
                        'PART78',
                        'PART79',
                        'PART80',
                        'PART81',
                        'PART82',
                        'PART83',
                        'PART84',
                        'PART85',
                        'PART86',
                        'PART87',
                        'PART88',
                        'PART89',
                        'PART90',
                        'PART91',
                        'PART92',
                        'PART93',
                        'PART94',
                        'PART95',
                        'PART96',
                        'PART97',
                        'PART98',
                        'PART99',
                        'DIMER1',
                        'DIMER2',
                        'DIMER3',
                        'DIMER4',
                        'DIMER5',
                        'DIMER6',
                        'DIMER7',
                        'DIMER8',
                        'DIMER9',
                        'DIMER10',
                        'DIMER11',
                        'DIMER12',
                        'DIMER13',
                        'DIMER14',
                        'DIMER15',
                        'DIMER16',
                        'DIMER17',
                        'DIMER18',
                        'DIMER19',
                        'DIMER20',
                        'DIMER21',
                        'HNO3S',
                        'PART1S',
                        'PART13S',
                        'PART14S',
                        'PART15S',
                        'PART17S']
    return particle_species

def particle_reactions_in():
    '''
    particle reactions
    
    returns:
        part_in = dictionary of particle reactions
    '''
    on_dict={"KP1" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P1))*1e12*184.26/6.02e23*SCALINGFAC",
            "KON1" : "6.2E-3*1E12*184.26/6.02E23",
            "KP2A" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P2A))*1e12*215.25/6.02e23*SCALINGFAC",
            "KON2A" : "6.2E-3*1E12*215.25/6.02E23",
            "KP2B" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P2B))*1e12*215.25/6.02e23*SCALINGFAC",
            "KON2B" : "6.2E-3*1E12*215.25/6.02E23",
            "KP3" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P3))*1e12*215.25/6.02e23*SCALINGFAC",
            "KON3" : "6.2E-3*1E12*215.25/6.02E23",
            "KP4" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P4))*1e12*245.23/6.02e23*SCALINGFAC",
            "KON4" : "6.2E-3*1E12*245.23/6.02E23",
            "KP5" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P5))*1e12*247.2/6.02e23*SCALINGFAC",
            "KON5" : "6.2E-3*1E12*247.2/6.02E23",
            "KP6" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P6))*1e12*217.22/6.02e23*SCALINGFAC",
            "KON6" : "6.2E-3*1E12*217.22/6.02E23",
            "KP11" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P11))*1e12*186.21/6.02e23*SCALINGFAC",
            "KON11" : "6.2E-3*1E12*186.21/6.02E23",
            "KP13" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P13))*1e12*186.21/6.02e23*SCALINGFAC",
            "KON13" : "6.2E-3*1E12*186.21/6.02E23",
            "KP14" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P14))*1e12*168.23/6.02e23*SCALINGFAC",
            "KON14" : "6.2E-3*1E12*168.23/6.02E23",
            "KP15" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P15))*1e12*170.21/6.02e23*SCALINGFAC",
            "KON15" : "6.2E-3*1E12*170.21/6.02E23",
            "KP16" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P16))*1e12*184.23/6.02e23*SCALINGFAC",
            "KON16" : "6.2E-3*1E12*184.23/6.02E23",
            "KP17" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P17))*1e12*182.22/6.02e23*SCALINGFAC",
            "KON17" : "6.2E-3*1E12*182.22/6.02E23",
            "KP22" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P22))*1e12*249.17/6.02e23*SCALINGFAC",
            "KON22" : "6.2E-3*1E12*249.17/6.02E23",
            "KP23" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P23))*1e12*188.18/6.02e23*SCALINGFAC",
            "KON23" : "6.2E-3*1E12*188.18/6.02E23",
            "KP24" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P24))*1e12*172.18/6.02e23*SCALINGFAC",
            "KON24" : "6.2E-3*1E12*172.18/6.02E23",
            "KP25" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P25))*1e12*170.21/6.02e23*SCALINGFAC",
            "KON25" : "6.2E-3*1E12*170.21/6.02E23",
            "KP26" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P26))*1e12*218.28/6.02e23*SCALINGFAC",
            "KON26" : "6.2E-3*1E12*218.28/6.02E23",
            "KP27" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P27))*1e12*186.28/6.02e23*SCALINGFAC",
            "KON27" : "6.2E-3*1E12*186.28/6.02E23",
            "KP28" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P28))*1e12*174.22/6.02e23*SCALINGFAC",
            "KON28" : "6.2E-3*1E12*174.22/6.02E23",
            "KP29" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P29))*1e12*186.28/6.02e23*SCALINGFAC",
            "KON29" : "6.2E-3*1E12*186.28/6.02E23",
            "KP30" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P30))*1e12*190.22/6.02e23*SCALINGFAC",
            "KON30" : "6.2E-3*1E12*190.22/6.02E23",
            "KP31" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P31))*1e12*172.2/6.02e23*SCALINGFAC",
            "KON31" : "6.2E-3*1E12*172.2/6.02E23",
            "KP32" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P32))*1e12*202.28/6.02e23*SCALINGFAC",
            "KON32" : "6.2E-3*1E12*202.28/6.02E23",
            "KP33" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P33))*1e12*178.21/6.02e23*SCALINGFAC",
            "KON33" : "6.2E-3*1E12*178.21/6.02E23",
            "KP34" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P34))*1e12*200.26/6.02e23*SCALINGFAC",
            "KON34" : "6.2E-3*1E12*200.26/6.02E23",
            "KP35" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P35))*1e12*200.26/6.02e23*SCALINGFAC",
            "KON35" : "6.2E-3*1E12*200.26/6.02E23",
            "KP36" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P36))*1e12*188.25/6.02e23*SCALINGFAC",
            "KON36" : "6.2E-3*1E12*188.25/6.02E23",
            "KP37" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P37))*1e12*190.22/6.02e23*SCALINGFAC",
            "KON37" : "6.2E-3*1E12*190.22/6.02E23",
            "KP38" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P38))*1e12*188.25/6.02e23*SCALINGFAC",
            "KON38" : "6.2E-3*1E12*188.25/6.02E23",
            "KP39" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P39))*1e12*204.25/6.02e23*SCALINGFAC",
            "KON39" : "6.2E-3*1E12*204.25/6.02E23",
            "KP40" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P40))*1e12*170.28/6.02e23*SCALINGFAC",
            "KON40" : "6.2E-3*1E12*170.28/6.02E23",
            "KP41" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P41))*1e12*172.25/6.02e23*SCALINGFAC",
            "KON41" : "6.2E-3*1E12*172.25/6.02E23",
            "KP42" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P42))*1e12*184.26/6.02e23*SCALINGFAC",
            "KON42" : "6.2E-3*1E12*184.26/6.02E23",
            "KP43" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P43))*1e12*220.25/6.02e23*SCALINGFAC",
            "KON43" : "6.2E-3*1E12*220.25/6.02E23",
            "KP44" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P44))*1e12*170.28/6.02e23*SCALINGFAC",
            "KON44" : "6.2E-3*1E12*170.28/6.02E23",
            "KP45" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P45))*1e12*174.22/6.02e23*SCALINGFAC",
            "KON45" : "6.2E-3*1E12*174.22/6.02E23",
            "KP46" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P46))*1e12*162.21/6.02e23*SCALINGFAC",
            "KON46" : "6.2E-3*1E12*162.21/6.02E23",
            "KP47" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P47))*1e12*174.22/6.02e23*SCALINGFAC",
            "KON47" : "6.2E-3*1E12*174.22/6.02E23",
            "KP48" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P48))*1e12*186.28/6.02e23*SCALINGFAC",
            "KON48" : "6.2E-3*1E12*186.28/6.02E23",
            "KP49" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P49))*1e12*186.23/6.02e23*SCALINGFAC",
            "KON49" : "6.2E-3*1E12*186.23/6.02E23",
            "KP50" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P50))*1e12*220.22/6.02e23*SCALINGFAC",
            "KON50" : "6.2E-3*1E12*220.22/6.02E23",
            "KP51" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P51))*1e12*206.19/6.02e23*SCALINGFAC",
            "KON51" : "6.2E-3*1E12*206.19/6.02E23",
            "KP52" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P52))*1e12*164.11/6.02e23*SCALINGFAC",
            "KON52" : "6.2E-3*1E12*164.11/6.02E23",
            "KP53" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P53))*1e12*178.14/6.02e23*SCALINGFAC",
            "KON53" : "6.2E-3*1E12*178.14/6.02E23",
            "KP54" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P54))*1e12*235.19/6.02e23*SCALINGFAC",
            "KON54" : "6.2E-3*1E12*235.19/6.02E23",
            "KP55" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P55))*1e12*204.22/6.02e23*SCALINGFAC",
            "KON55" : "6.2E-3*1E12*204.22/6.02E23",
            "KP56" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P56))*1e12*190.19/6.02e23*SCALINGFAC",
            "KON56" : "6.2E-3*1E12*190.19/6.02E23",
            "KP57" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P57))*1e12*190.19/6.02e23*SCALINGFAC",
            "KON57" : "6.2E-3*1E12*190.19/6.02E23",
            "KP58" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P58))*1e12*233.13/6.02e23*SCALINGFAC",
            "KON58" : "6.2E-3*1E12*233.13/6.02E23",
            "KP59" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P59))*1e12*249.13/6.02e23*SCALINGFAC",
            "KON59" : "6.2E-3*1E12*249.13/6.02E23",
            "KP60" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P60))*1e12*261.23/6.02e23*SCALINGFAC",
            "KON60" : "6.2E-3*1E12*261.23/6.02E23",
            "KP61" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P61))*1e12*176.17/6.02e23*SCALINGFAC",
            "KON61" : "6.2E-3*1E12*176.17/6.02E23",
            "KP62" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P62))*1e12*204.22/6.02e23*SCALINGFAC",
            "KON62" : "6.2E-3*1E12*204.22/6.02E23",
            "KP63" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P63))*1e12*294.13/6.02e23*SCALINGFAC",
            "KON63" : "6.2E-3*1E12*294.13/6.02E23",
            "KP64" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P64))*1e12*200.23/6.02e23*SCALINGFAC",
            "KON64" : "6.2E-3*1E12*200.23/6.02E23",
            "KP65" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P65))*1e12*174.19/6.02e23*SCALINGFAC",
            "KON65" : "6.2E-3*1E12*174.19/6.02E23",
            "KP66" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P66))*1e12*174.15/6.02e23*SCALINGFAC",
            "KON66" : "6.2E-3*1E12*174.15/6.02E23",
            "KP67" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P67))*1e12*176.17/6.02e23*SCALINGFAC",
            "KON67" : "6.2E-3*1E12*176.17/6.02E23",
            "KP68" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P68))*1e12*219.15/6.02e23*SCALINGFAC",
            "KON68" : "6.2E-3*1E12*219.15/6.02E23",
            "KP69" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P69))*1e12*245.23/6.02e23*SCALINGFAC",
            "KON69" : "6.2E-3*1E12*245.23/6.02E23",
            "KP70" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P70))*1e12*205.17/6.02e23*SCALINGFAC",
            "KON70" : "6.2E-3*1E12*205.17/6.02E23",
            "KP71" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P71))*1e12*216.23/6.02e23*SCALINGFAC",
            "KON71" : "6.2E-3*1E12*216.23/6.02E23",
            "KP72" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P72))*1e12*186.21/6.02e23*SCALINGFAC",
            "KON72" : "6.2E-3*1E12*186.21/6.02E23",
            "KP73" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P73))*1e12*216.23/6.02e23*SCALINGFAC",
            "KON73" : "6.2E-3*1E12*216.23/6.02E23",
            "KP74" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P74))*1e12*216.23/6.02e23*SCALINGFAC",
            "KON74" : "6.2E-3*1E12*216.23/6.02E23",
            "KP75" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P75))*1e12*190.15/6.02e23*SCALINGFAC",
            "KON75" : "6.2E-3*1E12*190.15/6.02E23",
            "KP76" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P76))*1e12*233.22/6.02e23*SCALINGFAC",
            "KON76" : "6.2E-3*1E12*233.22/6.02E23",
            "KP77" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P77))*1e12*162.14/6.02e23*SCALINGFAC",
            "KON77" : "6.2E-3*1E12*162.14/6.02E23",
            "KP78" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P78))*1e12*188.22/6.02e23*SCALINGFAC",
            "KON78" : "6.2E-3*1E12*188.22/6.02E23",
            "KP79" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P79))*1e12*162.14/6.02e23*SCALINGFAC",
            "KON79" : "6.2E-3*1E12*162.14/6.02E23",
            "KP80" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P80))*1e12*174.19/6.02e23*SCALINGFAC",
            "KON80" : "6.2E-3*1E12*174.19/6.02E23",
            "KP81" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P81))*1e12*134.09/6.02e23*SCALINGFAC",
            "KON81" : "6.2E-3*1E12*134.09/6.02E23",
            "KP82" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P82))*1e12*160.17/6.02e23*SCALINGFAC",
            "KON82" : "6.2E-3*1E12*160.17/6.02E23",
            "KP83" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P83))*1e12*235.15/6.02e23*SCALINGFAC",
            "KON83" : "6.2E-3*1E12*235.15/6.02E23",
            "KP84" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P84))*1e12*188.22/6.02e23*SCALINGFAC",
            "KON84" : "6.2E-3*1E12*188.22/6.02E23",
            "KP85" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P85))*1e12*172.18/6.02e23*SCALINGFAC",
            "KON85" : "6.2E-3*1E12*172.18/6.02E23",
            "KP86" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P86))*1e12*134.09/6.02e23*SCALINGFAC",
            "KON86" : "6.2E-3*1E12*134.09/6.02E23",
            "KP87" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P87))*1e12*261.23/6.02e23*SCALINGFAC",
            "KON87" : "6.2E-3*1E12*261.23/6.02E23",
            "KP88" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P88))*1e12*188.22/6.02e23*SCALINGFAC",
            "KON88" : "6.2E-3*1E12*188.22/6.02E23",
            "KP89" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P89))*1e12*202.20/6.02e23*SCALINGFAC",
            "KON89" : "6.2E-3*1E12*202.20/6.02E23",
            "KP90" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P90))*1e12*162.10/6.02e23*SCALINGFAC",
            "KON90" : "6.2E-3*1E12*162.10/6.02E23",
            "KP91" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P91))*1e12*245.23/6.02e23*SCALINGFAC",
            "KON91" : "6.2E-3*1E12*245.23/6.02E23",
            "KP92" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P92))*1e12*245.23/6.02e23*SCALINGFAC",
            "KON92" : "6.2E-3*1E12*245.23/6.02E23",
            "KP93" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P93))*1e12*247.20/6.02e23*SCALINGFAC",
            "KON93" : "6.2E-3*1E12*247.20/6.02E23",
            "KP94" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P94))*1e12*174.15/6.02e23*SCALINGFAC",
            "KON94" : "6.2E-3*1E12*174.15/6.02E23",
            "KP95" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P95))*1e12*174.15/6.02e23*SCALINGFAC",
            "KON95" : "6.2E-3*1E12*174.15/6.02E23",
            "KP96" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P96))*1e12*231.25/6.02e23*SCALINGFAC",
            "KON96" : "6.2E-3*1E12*231.25/6.02E23",
            "KP97" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P97))*1e12*231.25/6.02e23*SCALINGFAC",
            "KON97" : "6.2E-3*1E12*231.25/6.02E23",
            "KP98" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P98))*1e12*160.17/6.02e23*SCALINGFAC",
            "KON98" : "6.2E-3*1E12*160.17/6.02E23",
            "KP99" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P99))*1e12*200.23/6.02e23*SCALINGFAC",
            "KON99" : "6.2E-3*1E12*200.23/6.02E23",
            "KP100" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P100))*1e12*191.14/6.02e23*SCALINGFAC",
            "KON100" : "6.2E-3*1E12*191.14/6.02E23",
            "KP101" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P101))*1e12*207.10/6.02e23*SCALINGFAC",
            "KON101" : "6.2E-3*1E12*207.10/6.02E23",
            "KP102" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P102))*1e12*188.18/6.02e23*SCALINGFAC",
            "KON102" : "6.2E-3*1E12*188.18/6.02E23",
            "KP103" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P103))*1e12*188.14/6.02e23*SCALINGFAC",
            "KON103" : "6.2E-3*1E12*188.14/6.02E23",
            "KP104" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P104))*1e12*186.25/6.02e23*SCALINGFAC",
            "KON104" : "6.2E-3*1E12*186.25/6.02E23",
            "KP105" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P105))*1e12*203.19/6.02e23*SCALINGFAC",
            "KON105" : "6.2E-3*1E12*203.19/6.02E23",
            "KP106" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P106))*1e12*186.25/6.02e23*SCALINGFAC",
            "KON106" : "6.2E-3*1E12*186.25/6.02E23",
            "KP107" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P107))*1e12*233.13/6.02e23*SCALINGFAC",
            "KON107" : "6.2E-3*1E12*233.13/6.02E23",
            "KP108" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P108))*1e12*200.23/6.02e23*SCALINGFAC",
            "KON108" : "6.2E-3*1E12*200.23/6.02E23",
            "KP109" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P109))*1e12*200.23/6.02e23*SCALINGFAC",
            "KON109" : "6.2E-3*1E12*200.23/6.02E23",
            "KP110" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P110))*1e12*200.23/6.02e23*SCALINGFAC",
            "KON110" : "6.2E-3*1E12*200.23/6.02E23",
            "KP111" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P111))*1e12*200.23/6.02e23*SCALINGFAC",
            "KON111" : "6.2E-3*1E12*200.23/6.02E23",
            "KP112" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P112))*1e12*158.20/6.02e23*SCALINGFAC",
            "KON112" : "6.2E-3*1E12*158.20/6.02E23",
            "KP113" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P113))*1e12*146.14/6.02e23*SCALINGFAC",
            "KON113" : "6.2E-3*1E12*146.14/6.02E23",
            "KP114" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P114))*1e12*146.14/6.02e23*SCALINGFAC",
            "KON114" : "6.2E-3*1E12*146.14/6.02E23",
            "KP115" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P115))*1e12*160.12/6.02e23*SCALINGFAC",
            "KON115" : "6.2E-3*1E12*160.12/6.02E23",
            "KP116" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P116))*1e12*174.19/6.02e23*SCALINGFAC",
            "KON116" : "6.2E-3*1E12*174.19/6.02E23",
            "KP117" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P117))*1e12*160.12/6.02e23*SCALINGFAC",
            "KON117" : "6.2E-3*1E12*160.12/6.02E23",
            "KP118" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P118))*1e12*186.25/6.02e23*SCALINGFAC",
            "KON118" : "6.2E-3*1E12*186.25/6.02E23",
            "KP119" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P119))*1e12*132.12/6.02e23*SCALINGFAC",
            "KON119" : "6.2E-3*1E12*132.12/6.02E23",
            "KP120" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P120))*1e12*203.15/6.02e23*SCALINGFAC",
            "KON120" : "6.2E-3*1E12*203.15/6.02E23",
            "KP121" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P121))*1e12*201.13/6.02e23*SCALINGFAC",
            "KON121" : "6.2E-3*1E12*201.13/6.02E23",
            "KP122" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P122))*1e12*172.22/6.02e23*SCALINGFAC",
            "KON122" : "6.2E-3*1E12*172.22/6.02E23",
            "KP123" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P123))*1e12*184.23/6.02e23*SCALINGFAC",
            "KON123" : "6.2E-3*1E12*184.23/6.02E23",
            "KP124" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P124))*1e12*215.25/6.02e23*SCALINGFAC",
            "KON124" : "6.2E-3*1E12*215.25/6.02E23",
            "KP125" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P125))*1e12*174.19/6.02e23*SCALINGFAC",
            "KON125" : "6.2E-3*1E12*174.19/6.02E23",
            "KP126" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P126))*1e12*229.23/6.02e23*SCALINGFAC",
            "KON126" : "6.2E-3*1E12*229.23/6.02E23",
            "KP127" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P127))*1e12*184.23/6.02e23*SCALINGFAC",
            "KON127" : "6.2E-3*1E12*184.23/6.02E23",
            "KP128" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P128))*1e12*203.19/6.02e23*SCALINGFAC",
            "KON128" : "6.2E-3*1E12*203.19/6.02E23",
            "KP129" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P129))*1e12*215.25/6.02e23*SCALINGFAC",
            "KON129" : "6.2E-3*1E12*215.25/6.02E23",
            "KP130" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P130))*1e12*144.17/6.02e23*SCALINGFAC",
            "KON130" : "6.2E-3*1E12*144.17/6.02E23",
            "KP131" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P131))*1e12*148.11/6.02e23*SCALINGFAC",
            "KON131" : "6.2E-3*1E12*148.11/6.02E23",
            "KP132" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P132))*1e12*170.21/6.02e23*SCALINGFAC",
            "KON132" : "6.2E-3*1E12*170.21/6.02E23",
            "KP133" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P133))*1e12*158.15/6.02e23*SCALINGFAC",
            "KON133" : "6.2E-3*1E12*158.15/6.02E23",
            "KP134" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P134))*1e12*215.25/6.02e23*SCALINGFAC",
            "KON134" : "6.2E-3*1E12*215.25/6.02E23",
            "KP135" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P135))*1e12*215.25/6.02e23*SCALINGFAC",
            "KON135" : "6.2E-3*1E12*215.25/6.02E23",
            "KP136" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P136))*1e12*132.11/6.02e23*SCALINGFAC",
            "KON136" : "6.2E-3*1E12*132.11/6.02E23",
            "KP137" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P137))*1e12*200.23/6.02e23*SCALINGFAC",
            "KON137" : "6.2E-3*1E12*200.23/6.02E23",
            "KP138" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P138))*1e12*245.23/6.02e23*SCALINGFAC",
            "KON138" : "6.2E-3*1E12*245.23/6.02E23",
            "KP139" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P139))*1e12*144.13/6.02e23*SCALINGFAC",
            "KON139" : "6.2E-3*1E12*144.13/6.02E23",
            "KP140" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P140))*1e12*170.25/6.02e23*SCALINGFAC",
            "KON140" : "6.2E-3*1E12*170.25/6.02E23",
            "KP141" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P141))*1e12*193.11/6.02e23*SCALINGFAC",
            "KON141" : "6.2E-3*1E12*193.11/6.02E23",
            "KP142" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P142))*1e12*184.23/6.02e23*SCALINGFAC",
            "KON142" : "6.2E-3*1E12*184.23/6.02E23",
            "KP143" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P143))*1e12*184.23/6.02e23*SCALINGFAC",
            "KON143" : "6.2E-3*1E12*184.23/6.02E23",
            "KP144" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P144))*1e12*170.25/6.02e23*SCALINGFAC",
            "KON144" : "6.2E-3*1E12*170.25/6.02E23",
            "KP145" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P145))*1e12*156.18/6.02e23*SCALINGFAC",
            "KON145" : "6.2E-3*1E12*156.18/6.02E23",
            "KP146" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P146))*1e12*186.21/6.02e23*SCALINGFAC",
            "KON146" : "6.2E-3*1E12*186.21/6.02E23",
            "KP147" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P147))*1e12*172.22/6.02e23*SCALINGFAC",
            "KON147" : "6.2E-3*1E12*172.22/6.02E23",
            "KP148" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P148))*1e12*134.09/6.02e23*SCALINGFAC",
            "KON148" : "6.2E-3*1E12*134.09/6.02E23",
            "KP149" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P149))*1e12*213.23/6.02e23*SCALINGFAC",
            "KON149" : "6.2E-3*1E12*213.23/6.02E23",
            "KP150" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P150))*1e12*213.2304/6.02e23*SCALINGFAC",
            "KON150" : "6.2E-3*1E12*213.2304/6.02E23",
            "KP151" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P151))*1e12*158.195/6.02e23*SCALINGFAC",
            "KON151" : "6.2E-3*1E12*158.195/6.02E23",
            "KP152" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P152))*1e12*130.0987/6.02e23*SCALINGFAC",
            "KON152" : "6.2E-3*1E12*130.0987/6.02E23",
            "KP153" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P153))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON153" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP154" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P154))*1e12*161.1128/6.02e23*SCALINGFAC",
            "KON154" : "6.2E-3*1E12*161.1128/6.02E23",
            "KP155" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P155))*1e12*182.2164/6.02e23*SCALINGFAC",
            "KON155" : "6.2E-3*1E12*182.2164/6.02E23",
            "KP156" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P156))*1e12*231.2026/6.02e23*SCALINGFAC",
            "KON156" : "6.2E-3*1E12*231.2026/6.02E23",
            "KP157" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P157))*1e12*116.0722/6.02e23*SCALINGFAC",
            "KON157" : "6.2E-3*1E12*116.0722/6.02E23",
            "KP158" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P158))*1e12*146.0981/6.02e23*SCALINGFAC",
            "KON158" : "6.2E-3*1E12*146.0981/6.02E23",
            "KP159" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P159))*1e12*173.1665/6.02e23*SCALINGFAC",
            "KON159" : "6.2E-3*1E12*173.1665/6.02E23",
            "KP160" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P160))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON160" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP161" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P161))*1e12*179.085/6.02e23*SCALINGFAC",
            "KON161" : "6.2E-3*1E12*179.085/6.02E23",
            "KP162" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P162))*1e12*116.0722/6.02e23*SCALINGFAC",
            "KON162" : "6.2E-3*1E12*116.0722/6.02E23",
            "KP163" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P163))*1e12*231.2026/6.02e23*SCALINGFAC",
            "KON163" : "6.2E-3*1E12*231.2026/6.02E23",
            "KP164" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P164))*1e12*158.195/6.02e23*SCALINGFAC",
            "KON164" : "6.2E-3*1E12*158.195/6.02E23",
            "KP165" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P165))*1e12*191.0957/6.02e23*SCALINGFAC",
            "KON165" : "6.2E-3*1E12*191.0957/6.02E23",
            "KP166" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P166))*1e12*201.2197/6.02e23*SCALINGFAC",
            "KON166" : "6.2E-3*1E12*201.2197/6.02E23",
            "KP167" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P167))*1e12*156.136/6.02e23*SCALINGFAC",
            "KON167" : "6.2E-3*1E12*156.136/6.02E23",
            "KP168" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P168))*1e12*191.0957/6.02e23*SCALINGFAC",
            "KON168" : "6.2E-3*1E12*191.0957/6.02E23",
            "KP169" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P169))*1e12*146.0981/6.02e23*SCALINGFAC",
            "KON169" : "6.2E-3*1E12*146.0981/6.02E23",
            "KP170" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P170))*1e12*128.169/6.02e23*SCALINGFAC",
            "KON170" : "6.2E-3*1E12*128.169/6.02E23",
            "KP171" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P171))*1e12*158.195/6.02e23*SCALINGFAC",
            "KON171" : "6.2E-3*1E12*158.195/6.02E23",
            "KP172" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P172))*1e12*168.2328/6.02e23*SCALINGFAC",
            "KON172" : "6.2E-3*1E12*168.2328/6.02E23",
            "KP173" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P173))*1e12*132.0716/6.02e23*SCALINGFAC",
            "KON173" : "6.2E-3*1E12*132.0716/6.02E23",
            "KP174" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P174))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON174" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP175" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P175))*1e12*156.2221/6.02e23*SCALINGFAC",
            "KON175" : "6.2E-3*1E12*156.2221/6.02E23",
            "KP176" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P176))*1e12*177.0691/6.02e23*SCALINGFAC",
            "KON176" : "6.2E-3*1E12*177.0691/6.02E23",
            "KP177" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P177))*1e12*142.1094/6.02e23*SCALINGFAC",
            "KON177" : "6.2E-3*1E12*142.1094/6.02E23",
            "KP178" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P178))*1e12*187.1931/6.02e23*SCALINGFAC",
            "KON178" : "6.2E-3*1E12*187.1931/6.02E23",
            "KP179" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P179))*1e12*168.2328/6.02e23*SCALINGFAC",
            "KON179" : "6.2E-3*1E12*168.2328/6.02E23",
            "KP180" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P180))*1e12*126.1531/6.02e23*SCALINGFAC",
            "KON180" : "6.2E-3*1E12*126.1531/6.02E23",
            "KP181" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P181))*1e12*142.1956/6.02e23*SCALINGFAC",
            "KON181" : "6.2E-3*1E12*142.1956/6.02E23",
            "KP182" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P182))*1e12*114.0993/6.02e23*SCALINGFAC",
            "KON182" : "6.2E-3*1E12*114.0993/6.02E23",
            "KP183" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P183))*1e12*154.2063/6.02e23*SCALINGFAC",
            "KON183" : "6.2E-3*1E12*154.2063/6.02E23",
            "KP184" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P184))*1e12*102.0886/6.02e23*SCALINGFAC",
            "KON184" : "6.2E-3*1E12*102.0886/6.02E23",
            "KP185" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P185))*1e12*100.0728/6.02e23*SCALINGFAC",
            "KON185" : "6.2E-3*1E12*100.0728/6.02E23",
            "KP186" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P186))*1e12*114.0993/6.02e23*SCALINGFAC",
            "KON186" : "6.2E-3*1E12*114.0993/6.02E23",
            "KP200" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P200))*1e12*215.2463/6.02e23*SCALINGFAC",
            "KON200" : "6.2E-3*1E12*215.2463/6.02E23",
            "KP201" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P201))*1e12*170.2487/6.02e23*SCALINGFAC",
            "KON201" : "6.2E-3*1E12*170.2487/6.02E23",
            "KP202" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P202))*1e12*186.2481/6.02e23*SCALINGFAC",
            "KON202" : "6.2E-3*1E12*186.2481/6.02E23",
            "KP203" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P203))*1e12*215.2463/6.02e23*SCALINGFAC",
            "KON203" : "6.2E-3*1E12*215.2463/6.02E23",
            "KP204" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P204))*1e12*186.2481/6.02e23*SCALINGFAC",
            "KON204" : "6.2E-3*1E12*186.2481/6.02E23",
            "KP205" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P205))*1e12*215.2463/6.02e23*SCALINGFAC",
            "KON205" : "6.2E-3*1E12*215.2463/6.02E23",
            "KP206" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P206))*1e12*170.2487/6.02e23*SCALINGFAC",
            "KON206" : "6.2E-3*1E12*170.2487/6.02E23",
            "KP207" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P207))*1e12*186.2481/6.02e23*SCALINGFAC",
            "KON207" : "6.2E-3*1E12*186.2481/6.02E23",
            "KP209" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P209))*1e12*144.1253/6.02e23*SCALINGFAC",
            "KON209" : "6.2E-3*1E12*144.1253/6.02E23",
            "KP210" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P210))*1e12*160.1247/6.02e23*SCALINGFAC",
            "KON210" : "6.2E-3*1E12*160.1247/6.02E23",
            "KP211" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P211))*1e12*161.1128/6.02e23*SCALINGFAC",
            "KON211" : "6.2E-3*1E12*161.1128/6.02E23",
            "KP212" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P212))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON212" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP213" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P213))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON213" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP214" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P214))*1e12*205.1223/6.02e23*SCALINGFAC",
            "KON214" : "6.2E-3*1E12*205.1223/6.02E23",
            "KP215" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P215))*1e12*130.0987/6.02e23*SCALINGFAC",
            "KON215" : "6.2E-3*1E12*130.0987/6.02E23",
            "KP216" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P216))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON216" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP217" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P217))*1e12*148.114/6.02e23*SCALINGFAC",
            "KON217" : "6.2E-3*1E12*148.114/6.02E23",
            "KP218" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P218))*1e12*142.1094/6.02e23*SCALINGFAC",
            "KON218" : "6.2E-3*1E12*142.1094/6.02E23",
            "KP219" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P219))*1e12*128.0829/6.02e23*SCALINGFAC",
            "KON219" : "6.2E-3*1E12*128.0829/6.02E23",
            "KP220" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P220))*1e12*174.1082/6.02e23*SCALINGFAC",
            "KON220" : "6.2E-3*1E12*174.1082/6.02E23",
            "KP221" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P221))*1e12*146.0981/6.02e23*SCALINGFAC",
            "KON221" : "6.2E-3*1E12*146.0981/6.02E23",
            "KP222" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P222))*1e12*219.1058/6.02e23*SCALINGFAC",
            "KON222" : "6.2E-3*1E12*219.1058/6.02E23",
            "KP223" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P223))*1e12*134.1305/6.02e23*SCALINGFAC",
            "KON223" : "6.2E-3*1E12*134.1305/6.02E23",
            "KP224" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P224))*1e12*179.1281/6.02e23*SCALINGFAC",
            "KON224" : "6.2E-3*1E12*179.1281/6.02E23",
            "KP225" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P225))*1e12*128.1259/6.02e23*SCALINGFAC",
            "KON225" : "6.2E-3*1E12*128.1259/6.02E23",
            "KP226" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P226))*1e12*158.1519/6.02e23*SCALINGFAC",
            "KON226" : "6.2E-3*1E12*158.1519/6.02E23",
            "KP227" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P227))*1e12*174.1513/6.02e23*SCALINGFAC",
            "KON227" : "6.2E-3*1E12*174.1513/6.02E23",
            "KP228" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P228))*1e12*130.1418/6.02e23*SCALINGFAC",
            "KON228" : "6.2E-3*1E12*130.1418/6.02E23",
            "KP229" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P229))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON229" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP230" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P230))*1e12*219.1489/6.02e23*SCALINGFAC",
            "KON230" : "6.2E-3*1E12*219.1489/6.02E23",
            "KP231" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P231))*1e12*144.1253/6.02e23*SCALINGFAC",
            "KON231" : "6.2E-3*1E12*144.1253/6.02E23",
            "KP232" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P232))*1e12*160.1247/6.02e23*SCALINGFAC",
            "KON232" : "6.2E-3*1E12*160.1247/6.02E23",
            "KP233" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P233))*1e12*142.1525/6.02e23*SCALINGFAC",
            "KON233" : "6.2E-3*1E12*142.1525/6.02E23",
            "KP234" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P234))*1e12*158.1519/6.02e23*SCALINGFAC",
            "KON234" : "6.2E-3*1E12*158.1519/6.02E23",
            "KP235" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P235))*1e12*174.1513/6.02e23*SCALINGFAC",
            "KON235" : "6.2E-3*1E12*174.1513/6.02E23",
            "KP236" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P236))*1e12*130.1418/6.02e23*SCALINGFAC",
            "KON236" : "6.2E-3*1E12*130.1418/6.02E23",
            "KP237" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P237))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON237" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP238" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P238))*1e12*219.1489/6.02e23*SCALINGFAC",
            "KON238" : "6.2E-3*1E12*219.1489/6.02E23",
            "KP239" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P239))*1e12*158.1519/6.02e23*SCALINGFAC",
            "KON239" : "6.2E-3*1E12*158.1519/6.02E23",
            "KP240" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P240))*1e12*174.1513/6.02e23*SCALINGFAC",
            "KON240" : "6.2E-3*1E12*174.1513/6.02E23",
            "KP241" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P241))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON241" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP242" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P242))*1e12*219.1489/6.02e23*SCALINGFAC",
            "KON242" : "6.2E-3*1E12*219.1489/6.02E23",
            "KP243" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P243))*1e12*126.11/6.02e23*SCALINGFAC",
            "KON243" : "6.2E-3*1E12*126.11/6.02E23",
            "KP244" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P244))*1e12*128.1259/6.02e23*SCALINGFAC",
            "KON244" : "6.2E-3*1E12*128.1259/6.02E23",
            "KP245" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P245))*1e12*144.1253/6.02e23*SCALINGFAC",
            "KON245" : "6.2E-3*1E12*144.1253/6.02E23",
            "KP246" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P246))*1e12*144.1253/6.02e23*SCALINGFAC",
            "KON246" : "6.2E-3*1E12*144.1253/6.02E23",
            "KP247" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P247))*1e12*160.1247/6.02e23*SCALINGFAC",
            "KON247" : "6.2E-3*1E12*160.1247/6.02E23",
            "KP248" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P248))*1e12*130.1418/6.02e23*SCALINGFAC",
            "KON248" : "6.2E-3*1E12*130.1418/6.02E23",
            "KP249" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P249))*1e12*162.1406/6.02e23*SCALINGFAC",
            "KON249" : "6.2E-3*1E12*162.1406/6.02E23",
            "KP250" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P250))*1e12*207.1382/6.02e23*SCALINGFAC",
            "KON250" : "6.2E-3*1E12*207.1382/6.02E23",
            "KP251" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P251))*1e12*172.1785/6.02e23*SCALINGFAC",
            "KON251" : "6.2E-3*1E12*172.1785/6.02E23",
            "KP252" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P252))*1e12*188.1779/6.02e23*SCALINGFAC",
            "KON252" : "6.2E-3*1E12*188.1779/6.02E23",
            "KP253" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P253))*1e12*189.1659/6.02e23*SCALINGFAC",
            "KON253" : "6.2E-3*1E12*189.1659/6.02E23",
            "KP254" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P254))*1e12*144.1684/6.02e23*SCALINGFAC",
            "KON254" : "6.2E-3*1E12*144.1684/6.02E23",
            "KP255" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P255))*1e12*160.1678/6.02e23*SCALINGFAC",
            "KON255" : "6.2E-3*1E12*160.1678/6.02E23",
            "KP256" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P256))*1e12*233.1754/6.02e23*SCALINGFAC",
            "KON256" : "6.2E-3*1E12*233.1754/6.02E23",
            "KP257" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P257))*1e12*170.1626/6.02e23*SCALINGFAC",
            "KON257" : "6.2E-3*1E12*170.1626/6.02E23",
            "KP258" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P258))*1e12*200.1886/6.02e23*SCALINGFAC",
            "KON258" : "6.2E-3*1E12*200.1886/6.02E23",
            "KP259" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P259))*1e12*216.188/6.02e23*SCALINGFAC",
            "KON259" : "6.2E-3*1E12*216.188/6.02E23",
            "KP260" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P260))*1e12*172.1785/6.02e23*SCALINGFAC",
            "KON260" : "6.2E-3*1E12*172.1785/6.02E23",
            "KP261" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P261))*1e12*188.1779/6.02e23*SCALINGFAC",
            "KON261" : "6.2E-3*1E12*188.1779/6.02E23",
            "KP262" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P262))*1e12*261.1855/6.02e23*SCALINGFAC",
            "KON262" : "6.2E-3*1E12*261.1855/6.02E23",
            "KP263" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P263))*1e12*168.1898/6.02e23*SCALINGFAC",
            "KON263" : "6.2E-3*1E12*168.1898/6.02E23",
            "KP264" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P264))*1e12*154.1632/6.02e23*SCALINGFAC",
            "KON264" : "6.2E-3*1E12*154.1632/6.02E23",
            "KP265" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P265))*1e12*184.1892/6.02e23*SCALINGFAC",
            "KON265" : "6.2E-3*1E12*184.1892/6.02E23",
            "KP266" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P266))*1e12*200.1886/6.02e23*SCALINGFAC",
            "KON266" : "6.2E-3*1E12*200.1886/6.02E23",
            "KP267" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P267))*1e12*156.1791/6.02e23*SCALINGFAC",
            "KON267" : "6.2E-3*1E12*156.1791/6.02E23",
            "KP268" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P268))*1e12*172.1785/6.02e23*SCALINGFAC",
            "KON268" : "6.2E-3*1E12*172.1785/6.02E23",
            "KP269" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P269))*1e12*245.1861/6.02e23*SCALINGFAC",
            "KON269" : "6.2E-3*1E12*245.1861/6.02E23",
            "KP270" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P270))*1e12*110.1968/6.02e23*SCALINGFAC",
            "KON270" : "6.2E-3*1E12*110.1968/6.02E23",
            "KP271" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P271))*1e12*124.1803/6.02e23*SCALINGFAC",
            "KON271" : "6.2E-3*1E12*124.1803/6.02E23",
            "KP272" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P272))*1e12*171.1937/6.02e23*SCALINGFAC",
            "KON272" : "6.2E-3*1E12*171.1937/6.02E23",
            "KP273" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P273))*1e12*126.1962/6.02e23*SCALINGFAC",
            "KON273" : "6.2E-3*1E12*126.1962/6.02E23",
            "KP274" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P274))*1e12*142.1956/6.02e23*SCALINGFAC",
            "KON274" : "6.2E-3*1E12*142.1956/6.02E23",
            "KP275" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P275))*1e12*182.1733/6.02e23*SCALINGFAC",
            "KON275" : "6.2E-3*1E12*182.1733/6.02E23",
            "KP276" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P276))*1e12*184.1892/6.02e23*SCALINGFAC",
            "KON276" : "6.2E-3*1E12*184.1892/6.02E23",
            "KP277" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P277))*1e12*200.1886/6.02e23*SCALINGFAC",
            "KON277" : "6.2E-3*1E12*200.1886/6.02E23",
            "KP278" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P278))*1e12*215.2032/6.02e23*SCALINGFAC",
            "KON278" : "6.2E-3*1E12*215.2032/6.02E23",
            "KP279" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P279))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON279" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP280" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P280))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON280" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP281" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P281))*1e12*231.2026/6.02e23*SCALINGFAC",
            "KON281" : "6.2E-3*1E12*231.2026/6.02E23",
            "KP282" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P282))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON282" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP283" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P283))*1e12*202.2045/6.02e23*SCALINGFAC",
            "KON283" : "6.2E-3*1E12*202.2045/6.02E23",
            "KP284" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P284))*1e12*215.2032/6.02e23*SCALINGFAC",
            "KON284" : "6.2E-3*1E12*215.2032/6.02E23",
            "KP285" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P285))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON285" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP286" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P286))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON286" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP287" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P287))*1e12*168.2328/6.02e23*SCALINGFAC",
            "KON287" : "6.2E-3*1E12*168.2328/6.02E23",
            "KP288" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P288))*1e12*200.2316/6.02e23*SCALINGFAC",
            "KON288" : "6.2E-3*1E12*200.2316/6.02E23",
            "KP289" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P289))*1e12*215.2032/6.02e23*SCALINGFAC",
            "KON289" : "6.2E-3*1E12*215.2032/6.02E23",
            "KP290" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P290))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON290" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP291" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P291))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON291" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP292" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P292))*1e12*245.2292/6.02e23*SCALINGFAC",
            "KON292" : "6.2E-3*1E12*245.2292/6.02E23",
            "KP293" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P293))*1e12*231.2026/6.02e23*SCALINGFAC",
            "KON293" : "6.2E-3*1E12*231.2026/6.02E23",
            "KP294" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P294))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON294" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP295" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P295))*1e12*202.2045/6.02e23*SCALINGFAC",
            "KON295" : "6.2E-3*1E12*202.2045/6.02E23",
            "KP296" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P296))*1e12*152.1904/6.02e23*SCALINGFAC",
            "KON296" : "6.2E-3*1E12*152.1904/6.02E23",
            "KP297" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P297))*1e12*166.1739/6.02e23*SCALINGFAC",
            "KON297" : "6.2E-3*1E12*166.1739/6.02E23",
            "KP298" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P298))*1e12*213.1873/6.02e23*SCALINGFAC",
            "KON298" : "6.2E-3*1E12*213.1873/6.02E23",
            "KP299" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P299))*1e12*168.1898/6.02e23*SCALINGFAC",
            "KON299" : "6.2E-3*1E12*168.1898/6.02E23",
            "KP300" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P300))*1e12*184.1892/6.02e23*SCALINGFAC",
            "KON300" : "6.2E-3*1E12*184.1892/6.02E23",
            "KP301" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P301))*1e12*142.1094/6.02e23*SCALINGFAC",
            "KON301" : "6.2E-3*1E12*142.1094/6.02E23",
            "KP302" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P302))*1e12*114.0933/6.02e23*SCALINGFAC",
            "KON302" : "6.2E-3*1E12*114.0933/6.02E23",
            "KP303" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P303))*1e12*100.1158/6.02e23*SCALINGFAC",
            "KON303" : "6.2E-3*1E12*100.1158/6.02E23",
            "KP304" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P304))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON304" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP305" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P305))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON305" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP306" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P306))*1e12*172.1122/6.02e23*SCALINGFAC",
            "KON306" : "6.2E-3*1E12*172.1122/6.02E23",
            "KP307" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P307))*1e12*134.1305/6.02e23*SCALINGFAC",
            "KON307" : "6.2E-3*1E12*134.1305/6.02E23",
            "KP308" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P308))*1e12*130.1418/6.02e23*SCALINGFAC",
            "KON308" : "6.2E-3*1E12*130.1418/6.02E23",
            "KP309" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P269))*1e12*231.2457/6.02e23*SCALINGFAC",
            "KON309" : "6.2E-3*1E12*231.2457/6.02E23",
            "KP310" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P310))*1e12*231.2457/6.02e23*SCALINGFAC",
            "KON310" : "6.2E-3*1E12*231.2457/6.02E23",
            "KP311" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P311))*1e12*213.2304/6.02e23*SCALINGFAC",
            "KON311" : "6.2E-3*1E12*213.2304/6.02E23",
            "KP312" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P312))*1e12*245.2292/6.02e23*SCALINGFAC",
            "KON312" : "6.2E-3*1E12*245.2292/6.02E23",
            "KP313" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P313))*1e12*290.2268/6.02e23*SCALINGFAC",
            "KON313" : "6.2E-3*1E12*290.2268/6.02E23",
            "KP314" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P314))*1e12*199.2038/6.02e23*SCALINGFAC",
            "KON314" : "6.2E-3*1E12*199.2038/6.02E23",
            "KP315" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P315))*1e12*154.2063/6.02e23*SCALINGFAC",
            "KON315" : "6.2E-3*1E12*154.2063/6.02E23",
            "KP316" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P316))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON316" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP317" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P317))*1e12*152.1904/6.02e23*SCALINGFAC",
            "KON317" : "6.2E-3*1E12*152.1904/6.02E23",
            "KP318" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P318))*1e12*199.2038/6.02e23*SCALINGFAC",
            "KON318" : "6.2E-3*1E12*199.2038/6.02E23",
            "KP319" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P319))*1e12*154.2063/6.02e23*SCALINGFAC",
            "KON319" : "6.2E-3*1E12*154.2063/6.02E23",
            "KP320" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P320))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON320" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP321" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P321))*1e12*199.2038/6.02e23*SCALINGFAC",
            "KON321" : "6.2E-3*1E12*199.2038/6.02E23",
            "KP322" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P322))*1e12*154.2063/6.02e23*SCALINGFAC",
            "KON322" : "6.2E-3*1E12*154.2063/6.02E23",
            "KP323" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P323))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON323" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP324" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P324))*1e12*152.1904/6.02e23*SCALINGFAC",
            "KON324" : "6.2E-3*1E12*152.1904/6.02E23",
            "KP325" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P325))*1e12*154.2063/6.02e23*SCALINGFAC",
            "KON325" : "6.2E-3*1E12*154.2063/6.02E23",
            "KP326" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P326))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON326" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP327" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P327))*1e12*138.2069/6.02e23*SCALINGFAC",
            "KON327" : "6.2E-3*1E12*138.2069/6.02E23",
            "KP350" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P350))*1e12*82.1005/6.02e23*SCALINGFAC",
            "KON350" : "6.2E-3*1E12*82.1005/6.02E23",
            "KP351" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P351))*1e12*102.1317/6.02e23*SCALINGFAC",
            "KON351" : "6.2E-3*1E12*102.1317/6.02E23",
            "KP352" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P352))*1e12*102.1317/6.02e23*SCALINGFAC",
            "KON352" : "6.2E-3*1E12*102.1317/6.02E23",
            "KP353" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P353))*1e12*112.0835/6.02e23*SCALINGFAC",
            "KON353" : "6.2E-3*1E12*112.0835/6.02E23",
            "KP354" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P354))*1e12*114.0993/6.02e23*SCALINGFAC",
            "KON354" : "6.2E-3*1E12*114.0993/6.02E23",
            "KP355" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P355))*1e12*114.0993/6.02e23*SCALINGFAC",
            "KON355" : "6.2E-3*1E12*114.0993/6.02E23",
            "KP356" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P356))*1e12*114.1424/6.02e23*SCALINGFAC",
            "KON356" : "6.2E-3*1E12*114.1424/6.02E23",
            "KP357" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P357))*1e12*114.1424/6.02e23*SCALINGFAC",
            "KON357" : "6.2E-3*1E12*114.1424/6.02E23",
            "KP358" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P358))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON358" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP359" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P359))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON359" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP360" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P360))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON360" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP361" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P361))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON361" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP362" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P362))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON362" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP363" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P363))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON363" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP364" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P364))*1e12*116.1152/6.02e23*SCALINGFAC",
            "KON364" : "6.2E-3*1E12*116.1152/6.02E23",
            "KP365" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P365))*1e12*116.1583/6.02e23*SCALINGFAC",
            "KON365" : "6.2E-3*1E12*116.1583/6.02E23",
            "KP366" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P366))*1e12*116.1583/6.02e23*SCALINGFAC",
            "KON366" : "6.2E-3*1E12*116.1583/6.02E23",
            "KP367" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P367))*1e12*118.1311/6.02e23*SCALINGFAC",
            "KON367" : "6.2E-3*1E12*118.1311/6.02E23",
            "KP368" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P368))*1e12*118.1311/6.02e23*SCALINGFAC",
            "KON368" : "6.2E-3*1E12*118.1311/6.02E23",
            "KP369" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P369))*1e12*118.1311/6.02e23*SCALINGFAC",
            "KON369" : "6.2E-3*1E12*118.1311/6.02E23",
            "KP370" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P370))*1e12*118.1311/6.02e23*SCALINGFAC",
            "KON370" : "6.2E-3*1E12*118.1311/6.02E23",
            "KP371" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P371))*1e12*118.1311/6.02e23*SCALINGFAC",
            "KON371" : "6.2E-3*1E12*118.1311/6.02E23",
            "KP372" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P372))*1e12*118.1311/6.02e23*SCALINGFAC",
            "KON372" : "6.2E-3*1E12*118.1311/6.02E23",
            "KP373" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P373))*1e12*128.0829/6.02e23*SCALINGFAC",
            "KON373" : "6.2E-3*1E12*128.0829/6.02E23",
            "KP374" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P374))*1e12*128.1259/6.02e23*SCALINGFAC",
            "KON374" : "6.2E-3*1E12*128.1259/6.02E23",
            "KP375" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P375))*1e12*128.1259/6.02e23*SCALINGFAC",
            "KON375" : "6.2E-3*1E12*128.1259/6.02E23",
            "KP376" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P376))*1e12*128.169/6.02e23*SCALINGFAC",
            "KON376" : "6.2E-3*1E12*128.169/6.02E23",
            "KP377" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P377))*1e12*128.169/6.02e23*SCALINGFAC",
            "KON377" : "6.2E-3*1E12*128.169/6.02E23",
            "KP378" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P378))*1e12*130.0987/6.02e23*SCALINGFAC",
            "KON378" : "6.2E-3*1E12*130.0987/6.02E23",
            "KP379" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P379))*1e12*130.0987/6.02e23*SCALINGFAC",
            "KON379" : "6.2E-3*1E12*130.0987/6.02E23",
            "KP380" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P380))*1e12*130.0987/6.02e23*SCALINGFAC",
            "KON380" : "6.2E-3*1E12*130.0987/6.02E23",
            "KP381" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P381))*1e12*130.1418/6.02e23*SCALINGFAC",
            "KON381" : "6.2E-3*1E12*130.1418/6.02E23",
            "KP382" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P382))*1e12*130.1418/6.02e23*SCALINGFAC",
            "KON382" : "6.2E-3*1E12*130.1418/6.02E23",
            "KP383" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P383))*1e12*130.1418/6.02e23*SCALINGFAC",
            "KON383" : "6.2E-3*1E12*130.1418/6.02E23",
            "KP384" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P384))*1e12*130.1418/6.02e23*SCALINGFAC",
            "KON384" : "6.2E-3*1E12*130.1418/6.02E23",
            "KP385" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P385))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON385" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP386" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P386))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON386" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP387" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P387))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON387" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP388" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P388))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON388" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP389" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P389))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON389" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP390" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P390))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON390" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP391" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P391))*1e12*132.1146/6.02e23*SCALINGFAC",
            "KON391" : "6.2E-3*1E12*132.1146/6.02E23",
            "KP392" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P392))*1e12*132.1577/6.02e23*SCALINGFAC",
            "KON392" : "6.2E-3*1E12*132.1577/6.02E23",
            "KP393" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P393))*1e12*132.1577/6.02e23*SCALINGFAC",
            "KON393" : "6.2E-3*1E12*132.1577/6.02E23",
            "KP394" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P394))*1e12*134.1305/6.02e23*SCALINGFAC",
            "KON394" : "6.2E-3*1E12*134.1305/6.02E23",
            "KP395" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P395))*1e12*134.1305/6.02e23*SCALINGFAC",
            "KON395" : "6.2E-3*1E12*134.1305/6.02E23",
            "KP396" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P396))*1e12*134.1305/6.02e23*SCALINGFAC",
            "KON396" : "6.2E-3*1E12*134.1305/6.02E23",
            "KP397" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P397))*1e12*134.1305/6.02e23*SCALINGFAC",
            "KON397" : "6.2E-3*1E12*134.1305/6.02E23",
            "KP398" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P398))*1e12*138.2069/6.02e23*SCALINGFAC",
            "KON398" : "6.2E-3*1E12*138.2069/6.02E23",
            "KP399" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P399))*1e12*140.1797/6.02e23*SCALINGFAC",
            "KON399" : "6.2E-3*1E12*140.1797/6.02E23",
            "KP400" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P400))*1e12*140.1797/6.02e23*SCALINGFAC",
            "KON400" : "6.2E-3*1E12*140.1797/6.02E23",
            "KP401" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P401))*1e12*142.1525/6.02e23*SCALINGFAC",
            "KON401" : "6.2E-3*1E12*142.1525/6.02E23",
            "KP402" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P402))*1e12*142.1525/6.02e23*SCALINGFAC",
            "KON402" : "6.2E-3*1E12*142.1525/6.02E23",
            "KP403" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P403))*1e12*142.1525/6.02e23*SCALINGFAC",
            "KON403" : "6.2E-3*1E12*142.1525/6.02E23",
            "KP404" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P404))*1e12*142.1956/6.02e23*SCALINGFAC",
            "KON404" : "6.2E-3*1E12*142.1956/6.02E23",
            "KP405" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P405))*1e12*144.1684/6.02e23*SCALINGFAC",
            "KON405" : "6.2E-3*1E12*144.1684/6.02E23",
            "KP406" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P406))*1e12*144.1684/6.02e23*SCALINGFAC",
            "KON406" : "6.2E-3*1E12*144.1684/6.02E23",
            "KP407" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P407))*1e12*144.1684/6.02e23*SCALINGFAC",
            "KON407" : "6.2E-3*1E12*144.1684/6.02E23",
            "KP408" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P408))*1e12*144.1684/6.02e23*SCALINGFAC",
            "KON408" : "6.2E-3*1E12*144.1684/6.02E23",
            "KP409" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P409))*1e12*146.0981/6.02e23*SCALINGFAC",
            "KON409" : "6.2E-3*1E12*146.0981/6.02E23",
            "KP410" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P410))*1e12*146.0981/6.02e23*SCALINGFAC",
            "KON410" : "6.2E-3*1E12*146.0981/6.02E23",
            "KP411" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P411))*1e12*146.0981/6.02e23*SCALINGFAC",
            "KON411" : "6.2E-3*1E12*146.0981/6.02E23",
            "KP412" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P412))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON412" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP413" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P413))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON413" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP414" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P414))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON414" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP415" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P415))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON415" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP416" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P416))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON416" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP417" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P417))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON417" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP418" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P418))*1e12*146.1412/6.02e23*SCALINGFAC",
            "KON418" : "6.2E-3*1E12*146.1412/6.02E23",
            "KP419" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P419))*1e12*147.1293/6.02e23*SCALINGFAC",
            "KON419" : "6.2E-3*1E12*147.1293/6.02E23",
            "KP420" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P420))*1e12*147.1293/6.02e23*SCALINGFAC",
            "KON420" : "6.2E-3*1E12*147.1293/6.02E23",
            "KP421" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P421))*1e12*148.114/6.02e23*SCALINGFAC",
            "KON421" : "6.2E-3*1E12*148.114/6.02E23",
            "KP422" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P422))*1e12*148.114/6.02e23*SCALINGFAC",
            "KON422" : "6.2E-3*1E12*148.114/6.02E23",
            "KP423" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P423))*1e12*148.114/6.02e23*SCALINGFAC",
            "KON423" : "6.2E-3*1E12*148.114/6.02E23",
            "KP424" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P424))*1e12*148.114/6.02e23*SCALINGFAC",
            "KON424" : "6.2E-3*1E12*148.114/6.02E23",
            "KP425" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P425))*1e12*148.114/6.02e23*SCALINGFAC",
            "KON425" : "6.2E-3*1E12*148.114/6.02E23",
            "KP426" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P426))*1e12*148.114/6.02e23*SCALINGFAC",
            "KON426" : "6.2E-3*1E12*148.114/6.02E23",
            "KP427" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P427))*1e12*148.1571/6.02e23*SCALINGFAC",
            "KON427" : "6.2E-3*1E12*148.1571/6.02E23",
            "KP428" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P428))*1e12*148.1571/6.02e23*SCALINGFAC",
            "KON428" : "6.2E-3*1E12*148.1571/6.02E23",
            "KP429" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P429))*1e12*150.1299/6.02e23*SCALINGFAC",
            "KON429" : "6.2E-3*1E12*150.1299/6.02E23",
            "KP430" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P430))*1e12*150.1299/6.02e23*SCALINGFAC",
            "KON430" : "6.2E-3*1E12*150.1299/6.02E23",
            "KP431" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P431))*1e12*150.1299/6.02e23*SCALINGFAC",
            "KON431" : "6.2E-3*1E12*150.1299/6.02E23",
            "KP432" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P432))*1e12*150.1299/6.02e23*SCALINGFAC",
            "KON432" : "6.2E-3*1E12*150.1299/6.02E23",
            "KP433" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P433))*1e12*150.1299/6.02e23*SCALINGFAC",
            "KON433" : "6.2E-3*1E12*150.1299/6.02E23",
            "KP434" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P434))*1e12*154.2063/6.02e23*SCALINGFAC",
            "KON434" : "6.2E-3*1E12*154.2063/6.02E23",
            "KP435" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P435))*1e12*156.1791/6.02e23*SCALINGFAC",
            "KON435" : "6.2E-3*1E12*156.1791/6.02E23",
            "KP436" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P436))*1e12*156.1791/6.02e23*SCALINGFAC",
            "KON436" : "6.2E-3*1E12*156.1791/6.02E23",
            "KP437" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P437))*1e12*156.1791/6.02e23*SCALINGFAC",
            "KON437" : "6.2E-3*1E12*156.1791/6.02E23",
            "KP438" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P438))*1e12*156.1791/6.02e23*SCALINGFAC",
            "KON438" : "6.2E-3*1E12*156.1791/6.02E23",
            "KP439" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P439))*1e12*156.2221/6.02e23*SCALINGFAC",
            "KON439" : "6.2E-3*1E12*156.2221/6.02E23",
            "KP440" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P440))*1e12*158.195/6.02e23*SCALINGFAC",
            "KON440" : "6.2E-3*1E12*158.195/6.02E23",
            "KP441" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P441))*1e12*158.195/6.02e23*SCALINGFAC",
            "KON441" : "6.2E-3*1E12*158.195/6.02E23",
            "KP442" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P442))*1e12*158.195/6.02e23*SCALINGFAC",
            "KON442" : "6.2E-3*1E12*158.195/6.02E23",
            "KP443" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P443))*1e12*158.195/6.02e23*SCALINGFAC",
            "KON443" : "6.2E-3*1E12*158.195/6.02E23",
            "KP444" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P444))*1e12*160.1247/6.02e23*SCALINGFAC",
            "KON444" : "6.2E-3*1E12*160.1247/6.02E23",
            "KP445" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P445))*1e12*160.1678/6.02e23*SCALINGFAC",
            "KON445" : "6.2E-3*1E12*160.1678/6.02E23",
            "KP446" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P446))*1e12*160.1678/6.02e23*SCALINGFAC",
            "KON446" : "6.2E-3*1E12*160.1678/6.02E23",
            "KP447" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P447))*1e12*160.1678/6.02e23*SCALINGFAC",
            "KON447" : "6.2E-3*1E12*160.1678/6.02E23",
            "KP448" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P448))*1e12*160.1678/6.02e23*SCALINGFAC",
            "KON448" : "6.2E-3*1E12*160.1678/6.02E23",
            "KP449" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P449))*1e12*160.1678/6.02e23*SCALINGFAC",
            "KON449" : "6.2E-3*1E12*160.1678/6.02E23",
            "KP450" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P450))*1e12*160.1678/6.02e23*SCALINGFAC",
            "KON450" : "6.2E-3*1E12*160.1678/6.02E23",
            "KP451" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P451))*1e12*161.1558/6.02e23*SCALINGFAC",
            "KON451" : "6.2E-3*1E12*161.1558/6.02E23",
            "KP452" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P452))*1e12*161.1558/6.02e23*SCALINGFAC",
            "KON452" : "6.2E-3*1E12*161.1558/6.02E23",
            "KP453" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P453))*1e12*162.0975/6.02e23*SCALINGFAC",
            "KON453" : "6.2E-3*1E12*162.0975/6.02E23",
            "KP454" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P454))*1e12*162.0975/6.02e23*SCALINGFAC",
            "KON454" : "6.2E-3*1E12*162.0975/6.02E23",
            "KP455" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P455))*1e12*162.1406/6.02e23*SCALINGFAC",
            "KON455" : "6.2E-3*1E12*162.1406/6.02E23",
            "KP456" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P456))*1e12*162.1406/6.02e23*SCALINGFAC",
            "KON456" : "6.2E-3*1E12*162.1406/6.02E23",
            "KP457" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P457))*1e12*162.1406/6.02e23*SCALINGFAC",
            "KON457" : "6.2E-3*1E12*162.1406/6.02E23",
            "KP458" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P458))*1e12*162.1406/6.02e23*SCALINGFAC",
            "KON458" : "6.2E-3*1E12*162.1406/6.02E23",
            "KP459" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P459))*1e12*162.1837/6.02e23*SCALINGFAC",
            "KON459" : "6.2E-3*1E12*162.1837/6.02E23",
            "KP460" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P460))*1e12*163.0856/6.02e23*SCALINGFAC",
            "KON460" : "6.2E-3*1E12*163.0856/6.02E23",
            "KP461" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P461))*1e12*163.1287/6.02e23*SCALINGFAC",
            "KON461" : "6.2E-3*1E12*163.1287/6.02E23",
            "KP462" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P462))*1e12*164.1134/6.02e23*SCALINGFAC",
            "KON462" : "6.2E-3*1E12*164.1134/6.02E23",
            "KP463" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P463))*1e12*164.1565/6.02e23*SCALINGFAC",
            "KON463" : "6.2E-3*1E12*164.1565/6.02E23",
            "KP464" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P464))*1e12*164.1565/6.02e23*SCALINGFAC",
            "KON464" : "6.2E-3*1E12*164.1565/6.02E23",
            "KP465" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P465))*1e12*166.1293/6.02e23*SCALINGFAC",
            "KON465" : "6.2E-3*1E12*166.1293/6.02E23",
            "KP466" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P466))*1e12*166.1293/6.02e23*SCALINGFAC",
            "KON466" : "6.2E-3*1E12*166.1293/6.02E23",
            "KP467" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P467))*1e12*168.2328/6.02e23*SCALINGFAC",
            "KON467" : "6.2E-3*1E12*168.2328/6.02E23",
            "KP468" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P468))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON468" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP469" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P469))*1e12*170.2057/6.02e23*SCALINGFAC",
            "KON469" : "6.2E-3*1E12*170.2057/6.02E23",
            "KP470" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P470))*1e12*172.1785/6.02e23*SCALINGFAC",
            "KON470" : "6.2E-3*1E12*172.1785/6.02E23",
            "KP471" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P471))*1e12*172.1785/6.02e23*SCALINGFAC",
            "KON471" : "6.2E-3*1E12*172.1785/6.02E23",
            "KP472" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P472))*1e12*172.2215/6.02e23*SCALINGFAC",
            "KON472" : "6.2E-3*1E12*172.2215/6.02E23",
            "KP473" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P473))*1e12*172.2215/6.02e23*SCALINGFAC",
            "KON473" : "6.2E-3*1E12*172.2215/6.02E23",
            "KP474" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P474))*1e12*173.1665/6.02e23*SCALINGFAC",
            "KON474" : "6.2E-3*1E12*173.1665/6.02E23",
            "KP475" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P475))*1e12*174.1513/6.02e23*SCALINGFAC",
            "KON475" : "6.2E-3*1E12*174.1513/6.02E23",
            "KP476" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P476))*1e12*174.1513/6.02e23*SCALINGFAC",
            "KON476" : "6.2E-3*1E12*174.1513/6.02E23",
            "KP477" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P477))*1e12*174.1513/6.02e23*SCALINGFAC",
            "KON477" : "6.2E-3*1E12*174.1513/6.02E23",
            "KP478" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P478))*1e12*174.1513/6.02e23*SCALINGFAC",
            "KON478" : "6.2E-3*1E12*174.1513/6.02E23",
            "KP479" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P479))*1e12*174.1513/6.02e23*SCALINGFAC",
            "KON479" : "6.2E-3*1E12*174.1513/6.02E23",
            "KP480" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P480))*1e12*174.1944/6.02e23*SCALINGFAC",
            "KON480" : "6.2E-3*1E12*174.1944/6.02E23",
            "KP481" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P481))*1e12*174.1944/6.02e23*SCALINGFAC",
            "KON481" : "6.2E-3*1E12*174.1944/6.02E23",
            "KP482" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P482))*1e12*174.1944/6.02e23*SCALINGFAC",
            "KON482" : "6.2E-3*1E12*174.1944/6.02E23",
            "KP483" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P483))*1e12*175.0963/6.02e23*SCALINGFAC",
            "KON483" : "6.2E-3*1E12*175.0963/6.02E23",
            "KP484" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P484))*1e12*175.0963/6.02e23*SCALINGFAC",
            "KON484" : "6.2E-3*1E12*175.0963/6.02E23",
            "KP485" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P485))*1e12*175.1394/6.02e23*SCALINGFAC",
            "KON485" : "6.2E-3*1E12*175.1394/6.02E23",
            "KP486" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P486))*1e12*176.1672/6.02e23*SCALINGFAC",
            "KON486" : "6.2E-3*1E12*176.1672/6.02E23",
            "KP487" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P487))*1e12*176.1672/6.02e23*SCALINGFAC",
            "KON487" : "6.2E-3*1E12*176.1672/6.02E23",
            "KP488" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P488))*1e12*176.1672/6.02e23*SCALINGFAC",
            "KON488" : "6.2E-3*1E12*176.1672/6.02E23",
            "KP489" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P489))*1e12*177.1122/6.02e23*SCALINGFAC",
            "KON489" : "6.2E-3*1E12*177.1122/6.02E23",
            "KP490" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P490))*1e12*177.1122/6.02e23*SCALINGFAC",
            "KON490" : "6.2E-3*1E12*177.1122/6.02E23",
            "KP491" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P491))*1e12*177.1122/6.02e23*SCALINGFAC",
            "KON491" : "6.2E-3*1E12*177.1122/6.02E23",
            "KP492" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P492))*1e12*177.1122/6.02e23*SCALINGFAC",
            "KON492" : "6.2E-3*1E12*177.1122/6.02E23",
            "KP493" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P493))*1e12*177.1122/6.02e23*SCALINGFAC",
            "KON493" : "6.2E-3*1E12*177.1122/6.02E23",
            "KP494" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P494))*1e12*177.1122/6.02e23*SCALINGFAC",
            "KON494" : "6.2E-3*1E12*177.1122/6.02E23",
            "KP495" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P495))*1e12*178.1831/6.02e23*SCALINGFAC",
            "KON495" : "6.2E-3*1E12*178.1831/6.02E23",
            "KP496" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P496))*1e12*179.1281/6.02e23*SCALINGFAC",
            "KON496" : "6.2E-3*1E12*179.1281/6.02E23",
            "KP497" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P497))*1e12*179.1281/6.02e23*SCALINGFAC",
            "KON497" : "6.2E-3*1E12*179.1281/6.02E23",
            "KP498" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P498))*1e12*179.1281/6.02e23*SCALINGFAC",
            "KON498" : "6.2E-3*1E12*179.1281/6.02E23",
            "KP499" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P499))*1e12*179.1281/6.02e23*SCALINGFAC",
            "KON499" : "6.2E-3*1E12*179.1281/6.02E23",
            "KP500" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P500))*1e12*179.1281/6.02e23*SCALINGFAC",
            "KON500" : "6.2E-3*1E12*179.1281/6.02E23",
            "KP501" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P501))*1e12*180.1128/6.02e23*SCALINGFAC",
            "KON501" : "6.2E-3*1E12*180.1128/6.02E23",
            "KP502" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P502))*1e12*180.1128/6.02e23*SCALINGFAC",
            "KON502" : "6.2E-3*1E12*180.1128/6.02E23",
            "KP503" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P503))*1e12*181.1439/6.02e23*SCALINGFAC",
            "KON503" : "6.2E-3*1E12*181.1439/6.02E23",
            "KP504" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P504))*1e12*181.1439/6.02e23*SCALINGFAC",
            "KON504" : "6.2E-3*1E12*181.1439/6.02E23",
            "KP505" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P505))*1e12*182.0426/6.02e23*SCALINGFAC",
            "KON505" : "6.2E-3*1E12*182.0426/6.02E23",
            "KP506" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P506))*1e12*182.2164/6.02e23*SCALINGFAC",
            "KON506" : "6.2E-3*1E12*182.2164/6.02E23",
            "KP507" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P507))*1e12*184.1892/6.02e23*SCALINGFAC",
            "KON507" : "6.2E-3*1E12*184.1892/6.02E23",
            "KP508" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P508))*1e12*184.1892/6.02e23*SCALINGFAC",
            "KON508" : "6.2E-3*1E12*184.1892/6.02E23",
            "KP509" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P509))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON509" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP510" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P510))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON510" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP511" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P511))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON511" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP512" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P512))*1e12*186.2051/6.02e23*SCALINGFAC",
            "KON512" : "6.2E-3*1E12*186.2051/6.02E23",
            "KP513" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P513))*1e12*187.1931/6.02e23*SCALINGFAC",
            "KON513" : "6.2E-3*1E12*187.1931/6.02E23",
            "KP514" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P514))*1e12*188.1779/6.02e23*SCALINGFAC",
            "KON514" : "6.2E-3*1E12*188.1779/6.02E23",
            "KP515" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P515))*1e12*188.1779/6.02e23*SCALINGFAC",
            "KON515" : "6.2E-3*1E12*188.1779/6.02E23",
            "KP516" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P516))*1e12*188.2209/6.02e23*SCALINGFAC",
            "KON516" : "6.2E-3*1E12*188.2209/6.02E23",
            "KP517" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P517))*1e12*189.1659/6.02e23*SCALINGFAC",
            "KON517" : "6.2E-3*1E12*189.1659/6.02E23",
            "KP518" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P518))*1e12*190.1938/6.02e23*SCALINGFAC",
            "KON518" : "6.2E-3*1E12*190.1938/6.02E23",
            "KP519" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P519))*1e12*190.1938/6.02e23*SCALINGFAC",
            "KON519" : "6.2E-3*1E12*190.1938/6.02E23",
            "KP520" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P520))*1e12*191.1388/6.02e23*SCALINGFAC",
            "KON520" : "6.2E-3*1E12*191.1388/6.02E23",
            "KP521" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P521))*1e12*192.1666/6.02e23*SCALINGFAC",
            "KON521" : "6.2E-3*1E12*192.1666/6.02E23",
            "KP522" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P522))*1e12*193.1116/6.02e23*SCALINGFAC",
            "KON522" : "6.2E-3*1E12*193.1116/6.02E23",
            "KP523" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P523))*1e12*193.1116/6.02e23*SCALINGFAC",
            "KON523" : "6.2E-3*1E12*193.1116/6.02E23",
            "KP524" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P524))*1e12*193.1116/6.02e23*SCALINGFAC",
            "KON524" : "6.2E-3*1E12*193.1116/6.02E23",
            "KP525" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P525))*1e12*193.1116/6.02e23*SCALINGFAC",
            "KON525" : "6.2E-3*1E12*193.1116/6.02E23",
            "KP526" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P526))*1e12*193.1116/6.02e23*SCALINGFAC",
            "KON526" : "6.2E-3*1E12*193.1116/6.02E23",
            "KP527" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P527))*1e12*193.1546/6.02e23*SCALINGFAC",
            "KON527" : "6.2E-3*1E12*193.1546/6.02E23",
            "KP528" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P528))*1e12*193.1546/6.02e23*SCALINGFAC",
            "KON528" : "6.2E-3*1E12*193.1546/6.02E23",
            "KP529" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P529))*1e12*195.1275/6.02e23*SCALINGFAC",
            "KON529" : "6.2E-3*1E12*195.1275/6.02E23",
            "KP530" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P530))*1e12*195.1275/6.02e23*SCALINGFAC",
            "KON530" : "6.2E-3*1E12*195.1275/6.02E23",
            "KP531" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P531))*1e12*195.1275/6.02e23*SCALINGFAC",
            "KON531" : "6.2E-3*1E12*195.1275/6.02E23",
            "KP532" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P532))*1e12*195.1275/6.02e23*SCALINGFAC",
            "KON532" : "6.2E-3*1E12*195.1275/6.02E23",
            "KP533" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P533))*1e12*197.1433/6.02e23*SCALINGFAC",
            "KON533" : "6.2E-3*1E12*197.1433/6.02E23",
            "KP534" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P534))*1e12*197.1433/6.02e23*SCALINGFAC",
            "KON534" : "6.2E-3*1E12*197.1433/6.02E23",
            "KP535" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P535))*1e12*198.1281/6.02e23*SCALINGFAC",
            "KON535" : "6.2E-3*1E12*198.1281/6.02E23",
            "KP536" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P536))*1e12*200.2316/6.02e23*SCALINGFAC",
            "KON536" : "6.2E-3*1E12*200.2316/6.02E23",
            "KP537" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P537))*1e12*201.2197/6.02e23*SCALINGFAC",
            "KON537" : "6.2E-3*1E12*201.2197/6.02E23",
            "KP538" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P538))*1e12*202.2045/6.02e23*SCALINGFAC",
            "KON538" : "6.2E-3*1E12*202.2045/6.02E23",
            "KP539" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P539))*1e12*202.2045/6.02e23*SCALINGFAC",
            "KON539" : "6.2E-3*1E12*202.2045/6.02E23",
            "KP540" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P540))*1e12*202.2045/6.02e23*SCALINGFAC",
            "KON540" : "6.2E-3*1E12*202.2045/6.02E23",
            "KP541" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P541))*1e12*202.2045/6.02e23*SCALINGFAC",
            "KON541" : "6.2E-3*1E12*202.2045/6.02E23",
            "KP542" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P542))*1e12*202.2045/6.02e23*SCALINGFAC",
            "KON542" : "6.2E-3*1E12*202.2045/6.02E23",
            "KP543" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P543))*1e12*203.1925/6.02e23*SCALINGFAC",
            "KON543" : "6.2E-3*1E12*203.1925/6.02E23",
            "KP544" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P544))*1e12*203.1925/6.02e23*SCALINGFAC",
            "KON544" : "6.2E-3*1E12*203.1925/6.02E23",
            "KP545" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P545))*1e12*204.1773/6.02e23*SCALINGFAC",
            "KON545" : "6.2E-3*1E12*204.1773/6.02E23",
            "KP546" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P546))*1e12*204.1773/6.02e23*SCALINGFAC",
            "KON546" : "6.2E-3*1E12*204.1773/6.02E23",
            "KP547" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P547))*1e12*205.1223/6.02e23*SCALINGFAC",
            "KON547" : "6.2E-3*1E12*205.1223/6.02E23",
            "KP548" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P548))*1e12*205.1653/6.02e23*SCALINGFAC",
            "KON548" : "6.2E-3*1E12*205.1653/6.02E23",
            "KP549" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P549))*1e12*205.1653/6.02e23*SCALINGFAC",
            "KON549" : "6.2E-3*1E12*205.1653/6.02E23",
            "KP550" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P550))*1e12*205.1653/6.02e23*SCALINGFAC",
            "KON550" : "6.2E-3*1E12*205.1653/6.02E23",
            "KP551" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P551))*1e12*207.0951/6.02e23*SCALINGFAC",
            "KON551" : "6.2E-3*1E12*207.0951/6.02E23",
            "KP552" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P552))*1e12*207.1382/6.02e23*SCALINGFAC",
            "KON552" : "6.2E-3*1E12*207.1382/6.02E23",
            "KP553" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P553))*1e12*207.1382/6.02e23*SCALINGFAC",
            "KON553" : "6.2E-3*1E12*207.1382/6.02E23",
            "KP554" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P554))*1e12*207.1812/6.02e23*SCALINGFAC",
            "KON554" : "6.2E-3*1E12*207.1812/6.02E23",
            "KP555" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P555))*1e12*207.1812/6.02e23*SCALINGFAC",
            "KON555" : "6.2E-3*1E12*207.1812/6.02E23",
            "KP556" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P556))*1e12*207.1812/6.02e23*SCALINGFAC",
            "KON556" : "6.2E-3*1E12*207.1812/6.02E23",
            "KP557" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P557))*1e12*207.1812/6.02e23*SCALINGFAC",
            "KON557" : "6.2E-3*1E12*207.1812/6.02E23",
            "KP558" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P558))*1e12*209.111/6.02e23*SCALINGFAC",
            "KON558" : "6.2E-3*1E12*209.111/6.02E23",
            "KP559" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P559))*1e12*209.111/6.02e23*SCALINGFAC",
            "KON559" : "6.2E-3*1E12*209.111/6.02E23",
            "KP560" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P560))*1e12*209.111/6.02e23*SCALINGFAC",
            "KON560" : "6.2E-3*1E12*209.111/6.02E23",
            "KP561" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P561))*1e12*209.154/6.02e23*SCALINGFAC",
            "KON561" : "6.2E-3*1E12*209.154/6.02E23",
            "KP562" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P562))*1e12*211.1269/6.02e23*SCALINGFAC",
            "KON562" : "6.2E-3*1E12*211.1269/6.02E23",
            "KP563" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P563))*1e12*211.1269/6.02e23*SCALINGFAC",
            "KON563" : "6.2E-3*1E12*211.1269/6.02E23",
            "KP564" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P564))*1e12*211.1269/6.02e23*SCALINGFAC",
            "KON564" : "6.2E-3*1E12*211.1269/6.02E23",
            "KP565" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P565))*1e12*217.176/6.02e23*SCALINGFAC",
            "KON565" : "6.2E-3*1E12*217.176/6.02E23",
            "KP566" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P566))*1e12*217.2191/6.02e23*SCALINGFAC",
            "KON566" : "6.2E-3*1E12*217.2191/6.02E23",
            "KP567" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P567))*1e12*219.1489/6.02e23*SCALINGFAC",
            "KON567" : "6.2E-3*1E12*219.1489/6.02E23",
            "KP568" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P568))*1e12*219.1489/6.02e23*SCALINGFAC",
            "KON568" : "6.2E-3*1E12*219.1489/6.02E23",
            "KP569" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P569))*1e12*219.1919/6.02e23*SCALINGFAC",
            "KON569" : "6.2E-3*1E12*219.1919/6.02E23",
            "KP570" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P570))*1e12*219.1919/6.02e23*SCALINGFAC",
            "KON570" : "6.2E-3*1E12*219.1919/6.02E23",
            "KP571" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P571))*1e12*223.1806/6.02e23*SCALINGFAC",
            "KON571" : "6.2E-3*1E12*223.1806/6.02E23",
            "KP572" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P572))*1e12*223.1806/6.02e23*SCALINGFAC",
            "KON572" : "6.2E-3*1E12*223.1806/6.02E23",
            "KP573" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P573))*1e12*224.0826/6.02e23*SCALINGFAC",
            "KON573" : "6.2E-3*1E12*224.0826/6.02E23",
            "KP574" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P574))*1e12*224.0826/6.02e23*SCALINGFAC",
            "KON574" : "6.2E-3*1E12*224.0826/6.02E23",
            "KP575" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P575))*1e12*224.1256/6.02e23*SCALINGFAC",
            "KON575" : "6.2E-3*1E12*224.1256/6.02E23",
            "KP576" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P576))*1e12*224.1256/6.02e23*SCALINGFAC",
            "KON576" : "6.2E-3*1E12*224.1256/6.02E23",
            "KP577" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P577))*1e12*224.1256/6.02e23*SCALINGFAC",
            "KON577" : "6.2E-3*1E12*224.1256/6.02E23",
            "KP578" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P578))*1e12*226.0984/6.02e23*SCALINGFAC",
            "KON578" : "6.2E-3*1E12*226.0984/6.02E23",
            "KP579" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P579))*1e12*226.0984/6.02e23*SCALINGFAC",
            "KON579" : "6.2E-3*1E12*226.0984/6.02E23",
            "KP580" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P580))*1e12*226.1415/6.02e23*SCALINGFAC",
            "KON580" : "6.2E-3*1E12*226.1415/6.02E23",
            "KP581" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P581))*1e12*226.1415/6.02e23*SCALINGFAC",
            "KON581" : "6.2E-3*1E12*226.1415/6.02E23",
            "KP582" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P582))*1e12*227.1263/6.02e23*SCALINGFAC",
            "KON582" : "6.2E-3*1E12*227.1263/6.02E23",
            "KP583" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P583))*1e12*231.2026/6.02e23*SCALINGFAC",
            "KON583" : "6.2E-3*1E12*231.2026/6.02E23",
            "KP584" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P584))*1e12*231.2026/6.02e23*SCALINGFAC",
            "KON584" : "6.2E-3*1E12*231.2026/6.02E23",
            "KP585" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P585))*1e12*231.2457/6.02e23*SCALINGFAC",
            "KON585" : "6.2E-3*1E12*231.2457/6.02E23",
            "KP586" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P586))*1e12*233.1754/6.02e23*SCALINGFAC",
            "KON586" : "6.2E-3*1E12*233.1754/6.02E23",
            "KP587" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P587))*1e12*233.1754/6.02e23*SCALINGFAC",
            "KON587" : "6.2E-3*1E12*233.1754/6.02E23",
            "KP588" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P588))*1e12*233.2185/6.02e23*SCALINGFAC",
            "KON588" : "6.2E-3*1E12*233.2185/6.02E23",
            "KP589" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P589))*1e12*235.1913/6.02e23*SCALINGFAC",
            "KON589" : "6.2E-3*1E12*235.1913/6.02E23",
            "KP590" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P590))*1e12*240.125/6.02e23*SCALINGFAC",
            "KON590" : "6.2E-3*1E12*240.125/6.02E23",
            "KP591" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P591))*1e12*240.125/6.02e23*SCALINGFAC",
            "KON591" : "6.2E-3*1E12*240.125/6.02E23",
            "KP592" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P592))*1e12*240.125/6.02e23*SCALINGFAC",
            "KON592" : "6.2E-3*1E12*240.125/6.02E23",
            "KP593" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P593))*1e12*243.1257/6.02e23*SCALINGFAC",
            "KON593" : "6.2E-3*1E12*243.1257/6.02E23",
            "KP594" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P594))*1e12*247.202/6.02e23*SCALINGFAC",
            "KON594" : "6.2E-3*1E12*247.202/6.02E23",
            "KP595" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P595))*1e12*247.2451/6.02e23*SCALINGFAC",
            "KON595" : "6.2E-3*1E12*247.2451/6.02E23",
            "KP596" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P596))*1e12*247.2451/6.02e23*SCALINGFAC",
            "KON596" : "6.2E-3*1E12*247.2451/6.02E23",
            "KP597" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P597))*1e12*254.1085/6.02e23*SCALINGFAC",
            "KON597" : "6.2E-3*1E12*254.1085/6.02E23",
            "KP598" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P598))*1e12*254.1085/6.02e23*SCALINGFAC",
            "KON598" : "6.2E-3*1E12*254.1085/6.02E23",
            "KP599" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P599))*1e12*254.1085/6.02e23*SCALINGFAC",
            "KON599" : "6.2E-3*1E12*254.1085/6.02E23",
            "KP600" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P600))*1e12*256.1244/6.02e23*SCALINGFAC",
            "KON600" : "6.2E-3*1E12*256.1244/6.02E23",
            "KP601" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P601))*1e12*256.1244/6.02e23*SCALINGFAC",
            "KON601" : "6.2E-3*1E12*256.1244/6.02E23",
            "KP602" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P602))*1e12*256.1244/6.02e23*SCALINGFAC",
            "KON602" : "6.2E-3*1E12*256.1244/6.02E23",
            "KP603" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P603))*1e12*256.1244/6.02e23*SCALINGFAC",
            "KON603" : "6.2E-3*1E12*256.1244/6.02E23",
            "KP604" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P604))*1e12*256.1244/6.02e23*SCALINGFAC",
            "KON604" : "6.2E-3*1E12*256.1244/6.02E23",
            "KP605" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P605))*1e12*256.1244/6.02e23*SCALINGFAC",
            "KON605" : "6.2E-3*1E12*256.1244/6.02E23",
            "KP606" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P606))*1e12*263.2445/6.02e23*SCALINGFAC",
            "KON606" : "6.2E-3*1E12*263.2445/6.02E23",
            "KP607" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P607))*1e12*272.1238/6.02e23*SCALINGFAC",
            "KON607" : "6.2E-3*1E12*272.1238/6.02E23",
            "KP608" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P608))*1e12*301.122/6.02e23*SCALINGFAC",
            "KON608" : "6.2E-3*1E12*301.122/6.02E23",
            "KP609" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P609))*1e12*301.122/6.02e23*SCALINGFAC",
            "KON609" : "6.2E-3*1E12*301.122/6.02E23",
            "KP610" : "((7.501*1E-9*8.314*temp)/(mwomv*ACTIVITY*P610))*1e12*301.122/6.02e23*SCALINGFAC",
            "KON610" : "6.2E-3*1E12*301.122/6.02E23",
            "kacid" : "1.5e-32*numba_exp(14770/temp)"}
    
    off_temp=  [['KOFF1', 'KON1/KP1'],
                ['KOFF2A', 'KON2A/KP2A'],
                ['KOFF2B', 'KON2B/KP2B'],
                ['KOFF3', 'KON3/KP3'],
                ['KOFF4', 'KON4/KP4'],
                ['KOFF5', 'KON5/KP5'],
                ['KOFF6', 'KON6/KP6'],
                ['KOFF11', 'KON11/KP11'],
                ['KOFF13', 'KON13/KP13'],
                ['KOFF14', 'KON14/KP14'],
                ['KOFF15', 'KON15/KP15'],
                ['KOFF16', 'KON16/KP16'],
                ['KOFF17', 'KON17/KP17'],
                ['KOFF22', 'KON22/KP22'],
                ['KOFF23', 'KON23/KP23'],
                ['KOFF24', 'KON24/KP24'],
                ['KOFF25', 'KON25/KP25'],
                ['KOFF26', 'KON26/KP26'],
                ['KOFF27', 'KON27/KP27'],
                ['KOFF28', 'KON28/KP28'],
                ['KOFF29', 'KON29/KP29'],
                ['KOFF30', 'KON30/KP30'],
                ['KOFF31', 'KON31/KP31'],
                ['KOFF32', 'KON32/KP32'],
                ['KOFF33', 'KON33/KP33'],
                ['KOFF34', 'KON34/KP34'],
                ['KOFF35', 'KON35/KP35'],
                ['KOFF36', 'KON36/KP36'],
                ['KOFF37', 'KON37/KP37'],
                ['KOFF38', 'KON38/KP38'],
                ['KOFF39', 'KON39/KP39'],
                ['KOFF40', 'KON40/KP40'],
                ['KOFF41', 'KON41/KP41'],
                ['KOFF42', 'KON42/KP42'],
                ['KOFF43', 'KON43/KP43'],
                ['KOFF44', 'KON44/KP44'],
                ['KOFF45', 'KON45/KP45'],
                ['KOFF46', 'KON46/KP46'],
                ['KOFF47', 'KON47/KP47'],
                ['KOFF48', 'KON48/KP48'],
                ['KOFF49', 'KON49/KP49'],
                ['KOFF50', 'KON50/KP50'],
                ['KOFF51', 'KON51/KP51'],
                ['KOFF52', 'KON52/KP52'],
                ['KOFF53', 'KON53/KP53'],
                ['KOFF54', 'KON54/KP54'],
                ['KOFF55', 'KON55/KP55'],
                ['KOFF56', 'KON56/KP56'],
                ['KOFF57', 'KON57/KP57'],
                ['KOFF58', 'KON58/KP58'],
                ['KOFF59', 'KON59/KP59'],
                ['KOFF60', 'KON60/KP60'],
                ['KOFF61', 'KON61/KP61'],
                ['KOFF62', 'KON62/KP62'],
                ['KOFF63', 'KON63/KP63'],
                ['KOFF64', 'KON64/KP64'],
                ['KOFF65', 'KON65/KP65'],
                ['KOFF66', 'KON66/KP66'],
                ['KOFF67', 'KON67/KP67'],
                ['KOFF68', 'KON68/KP68'],
                ['KOFF69', 'KON69/KP69'],
                ['KOFF70', 'KON70/KP70'],
                ['KOFF71', 'KON71/KP71'],
                ['KOFF72', 'KON72/KP72'],
                ['KOFF73', 'KON73/KP73'],
                ['KOFF74', 'KON74/KP74'],
                ['KOFF75', 'KON75/KP75'],
                ['KOFF76', 'KON76/KP76'],
                ['KOFF77', 'KON77/KP77'],
                ['KOFF78', 'KON78/KP78'],
                ['KOFF79', 'KON79/KP79'],
                ['KOFF80', 'KON80/KP80'],
                ['KOFF81', 'KON81/KP81'],
                ['KOFF82', 'KON82/KP82'],
                ['KOFF83', 'KON83/KP83'],
                ['KOFF84', 'KON84/KP84'],
                ['KOFF85', 'KON85/KP85'],
                ['KOFF86', 'KON86/KP86'],
                ['KOFF87', 'KON87/KP87'],
                ['KOFF88', 'KON88/KP88'],
                ['KOFF89', 'KON89/KP89'],
                ['KOFF90', 'KON90/KP90'],
                ['KOFF91', 'KON91/KP91'],
                ['KOFF92', 'KON92/KP92'],
                ['KOFF93', 'KON93/KP93'],
                ['KOFF94', 'KON94/KP94'],
                ['KOFF95', 'KON95/KP95'],
                ['KOFF96', 'KON96/KP96'],
                ['KOFF97', 'KON97/KP97'],
                ['KOFF98', 'KON98/KP98'],
                ['KOFF99', 'KON99/KP99'],
                ['KOFF100', 'KON100/KP100'],
                ['KOFF101', 'KON101/KP101'],
                ['KOFF102', 'KON102/KP102'],
                ['KOFF103', 'KON103/KP103'],
                ['KOFF104', 'KON104/KP104'],
                ['KOFF105', 'KON105/KP105'],
                ['KOFF106', 'KON106/KP106'],
                ['KOFF107', 'KON107/KP107'],
                ['KOFF108', 'KON108/KP108'],
                ['KOFF109', 'KON109/KP109'],
                ['KOFF110', 'KON110/KP110'],
                ['KOFF111', 'KON111/KP111'],
                ['KOFF112', 'KON112/KP112'],
                ['KOFF113', 'KON113/KP113'],
                ['KOFF114', 'KON114/KP114'],
                ['KOFF115', 'KON115/KP115'],
                ['KOFF116', 'KON116/KP116'],
                ['KOFF117', 'KON117/KP117'],
                ['KOFF118', 'KON118/KP118'],
                ['KOFF119', 'KON119/KP119'],
                ['KOFF120', 'KON120/KP120'],
                ['KOFF121', 'KON121/KP121'],
                ['KOFF122', 'KON122/KP122'],
                ['KOFF123', 'KON123/KP123'],
                ['KOFF124', 'KON124/KP124'],
                ['KOFF125', 'KON125/KP125'],
                ['KOFF126', 'KON126/KP126'],
                ['KOFF127', 'KON127/KP127'],
                ['KOFF128', 'KON128/KP128'],
                ['KOFF129', 'KON129/KP129'],
                ['KOFF130', 'KON130/KP130'],
                ['KOFF131', 'KON131/KP131'],
                ['KOFF132', 'KON132/KP132'],
                ['KOFF133', 'KON133/KP133'],
                ['KOFF134', 'KON134/KP134'],
                ['KOFF135', 'KON135/KP135'],
                ['KOFF136', 'KON136/KP136'],
                ['KOFF137', 'KON137/KP137'],
                ['KOFF138', 'KON138/KP138'],
                ['KOFF139', 'KON139/KP139'],
                ['KOFF140', 'KON140/KP140'],
                ['KOFF141', 'KON141/KP141'],
                ['KOFF142', 'KON142/KP142'],
                ['KOFF143', 'KON143/KP143'],
                ['KOFF144', 'KON144/KP144'],
                ['KOFF145', 'KON145/KP145'],
                ['KOFF146', 'KON146/KP146'],
                ['KOFF147', 'KON147/KP147'],
                ['KOFF148', 'KON148/KP148'],
                ['KOFF149', 'KON149/KP149'],
                ['KOFF150', 'KON150/KP150'],
                ['KOFF151', 'KON151/KP151'],
                ['KOFF152', 'KON152/KP152'],
                ['KOFF153', 'KON153/KP153'],
                ['KOFF154', 'KON154/KP154'],
                ['KOFF155', 'KON155/KP155'],
                ['KOFF156', 'KON156/KP156'],
                ['KOFF157', 'KON157/KP157'],
                ['KOFF158', 'KON158/KP158'],
                ['KOFF159', 'KON159/KP159'],
                ['KOFF160', 'KON160/KP160'],
                ['KOFF161', 'KON161/KP161'],
                ['KOFF162', 'KON162/KP162'],
                ['KOFF163', 'KON163/KP163'],
                ['KOFF164', 'KON164/KP164'],
                ['KOFF165', 'KON165/KP165'],
                ['KOFF166', 'KON166/KP166'],
                ['KOFF167', 'KON167/KP167'],
                ['KOFF168', 'KON168/KP168'],
                ['KOFF169', 'KON169/KP169'],
                ['KOFF170', 'KON170/KP170'],
                ['KOFF171', 'KON171/KP171'],
                ['KOFF172', 'KON172/KP172'],
                ['KOFF173', 'KON173/KP173'],
                ['KOFF174', 'KON174/KP174'],
                ['KOFF175', 'KON175/KP175'],
                ['KOFF176', 'KON176/KP176'],
                ['KOFF177', 'KON177/KP177'],
                ['KOFF178', 'KON178/KP178'],
                ['KOFF179', 'KON179/KP179'],
                ['KOFF180', 'KON180/KP180'],
                ['KOFF181', 'KON181/KP181'],
                ['KOFF182', 'KON182/KP182'],
                ['KOFF183', 'KON183/KP183'],
                ['KOFF184', 'KON184/KP184'],
                ['KOFF185', 'KON185/KP185'],
                ['KOFF186', 'KON186/KP186'],
                ['KOFF200', 'KON200/KP200'],
                ['KOFF201', 'KON201/KP201'],
                ['KOFF202', 'KON202/KP202'],
                ['KOFF203', 'KON203/KP203'],
                ['KOFF204', 'KON204/KP204'],
                ['KOFF205', 'KON205/KP205'],
                ['KOFF206', 'KON206/KP206'],
                ['KOFF207', 'KON207/KP207'],
                ['KOFF209', 'KON209/KP209'],
                ['KOFF210', 'KON210/KP210'],
                ['KOFF211', 'KON211/KP211'],
                ['KOFF212', 'KON212/KP212'],
                ['KOFF213', 'KON213/KP213'],
                ['KOFF214', 'KON214/KP214'],
                ['KOFF215', 'KON215/KP215'],
                ['KOFF216', 'KON216/KP216'],
                ['KOFF217', 'KON217/KP217'],
                ['KOFF218', 'KON218/KP218'],
                ['KOFF219', 'KON219/KP219'],
                ['KOFF220', 'KON220/KP220'],
                ['KOFF221', 'KON221/KP221'],
                ['KOFF222', 'KON222/KP222'],
                ['KOFF223', 'KON223/KP223'],
                ['KOFF224', 'KON224/KP224'],
                ['KOFF225', 'KON225/KP225'],
                ['KOFF226', 'KON226/KP226'],
                ['KOFF227', 'KON227/KP227'],
                ['KOFF228', 'KON228/KP228'],
                ['KOFF229', 'KON229/KP229'],
                ['KOFF230', 'KON230/KP230'],
                ['KOFF231', 'KON231/KP231'],
                ['KOFF232', 'KON232/KP232'],
                ['KOFF233', 'KON233/KP233'],
                ['KOFF234', 'KON234/KP234'],
                ['KOFF235', 'KON235/KP235'],
                ['KOFF236', 'KON236/KP236'],
                ['KOFF237', 'KON237/KP237'],
                ['KOFF238', 'KON238/KP238'],
                ['KOFF239', 'KON239/KP239'],
                ['KOFF240', 'KON240/KP240'],
                ['KOFF241', 'KON241/KP241'],
                ['KOFF242', 'KON242/KP242'],
                ['KOFF243', 'KON243/KP243'],
                ['KOFF244', 'KON244/KP244'],
                ['KOFF245', 'KON245/KP245'],
                ['KOFF246', 'KON246/KP246'],
                ['KOFF247', 'KON247/KP247'],
                ['KOFF248', 'KON248/KP248'],
                ['KOFF249', 'KON249/KP249'],
                ['KOFF250', 'KON250/KP250'],
                ['KOFF251', 'KON251/KP251'],
                ['KOFF252', 'KON252/KP252'],
                ['KOFF253', 'KON253/KP253'],
                ['KOFF254', 'KON254/KP254'],
                ['KOFF255', 'KON255/KP255'],
                ['KOFF256', 'KON256/KP256'],
                ['KOFF257', 'KON257/KP257'],
                ['KOFF258', 'KON258/KP258'],
                ['KOFF259', 'KON259/KP259'],
                ['KOFF260', 'KON260/KP260'],
                ['KOFF261', 'KON261/KP261'],
                ['KOFF262', 'KON262/KP262'],
                ['KOFF263', 'KON263/KP263'],
                ['KOFF264', 'KON264/KP264'],
                ['KOFF265', 'KON265/KP265'],
                ['KOFF266', 'KON266/KP266'],
                ['KOFF267', 'KON267/KP267'],
                ['KOFF268', 'KON268/KP268'],
                ['KOFF269', 'KON269/KP269'],
                ['KOFF270', 'KON270/KP270'],
                ['KOFF271', 'KON271/KP271'],
                ['KOFF272', 'KON272/KP272'],
                ['KOFF273', 'KON273/KP273'],
                ['KOFF274', 'KON274/KP274'],
                ['KOFF275', 'KON275/KP275'],
                ['KOFF276', 'KON276/KP276'],
                ['KOFF277', 'KON277/KP277'],
                ['KOFF278', 'KON278/KP278'],
                ['KOFF279', 'KON279/KP279'],
                ['KOFF280', 'KON280/KP280'],
                ['KOFF281', 'KON281/KP281'],
                ['KOFF282', 'KON282/KP282'],
                ['KOFF283', 'KON283/KP283'],
                ['KOFF284', 'KON284/KP284'],
                ['KOFF285', 'KON285/KP285'],
                ['KOFF286', 'KON286/KP286'],
                ['KOFF287', 'KON287/KP287'],
                ['KOFF288', 'KON288/KP288'],
                ['KOFF289', 'KON289/KP289'],
                ['KOFF290', 'KON290/KP290'],
                ['KOFF291', 'KON291/KP291'],
                ['KOFF292', 'KON292/KP292'],
                ['KOFF293', 'KON293/KP293'],
                ['KOFF294', 'KON294/KP294'],
                ['KOFF295', 'KON295/KP295'],
                ['KOFF296', 'KON296/KP296'],
                ['KOFF297', 'KON297/KP297'],
                ['KOFF298', 'KON298/KP298'],
                ['KOFF299', 'KON299/KP299'],
                ['KOFF300', 'KON300/KP300'],
                ['KOFF301', 'KON301/KP301'],
                ['KOFF302', 'KON302/KP302'],
                ['KOFF303', 'KON303/KP303'],
                ['KOFF304', 'KON304/KP304'],
                ['KOFF305', 'KON305/KP305'],
                ['KOFF306', 'KON306/KP306'],
                ['KOFF307', 'KON307/KP307'],
                ['KOFF308', 'KON308/KP308'],
                ['KOFF309', 'KON309/KP309'],
                ['KOFF310', 'KON310/KP310'],
                ['KOFF311', 'KON311/KP311'],
                ['KOFF312', 'KON312/KP312'],
                ['KOFF313', 'KON313/KP313'],
                ['KOFF314', 'KON314/KP314'],
                ['KOFF315', 'KON315/KP315'],
                ['KOFF316', 'KON316/KP316'],
                ['KOFF317', 'KON317/KP317'],
                ['KOFF318', 'KON318/KP318'],
                ['KOFF319', 'KON319/KP319'],
                ['KOFF320', 'KON320/KP320'],
                ['KOFF321', 'KON321/KP321'],
                ['KOFF322', 'KON322/KP322'],
                ['KOFF323', 'KON323/KP323'],
                ['KOFF324', 'KON324/KP324'],
                ['KOFF325', 'KON325/KP325'],
                ['KOFF326', 'KON326/KP326'],
                ['KOFF327', 'KON327/KP327'],
                ['KOFF350', 'KON350/KP350'],
                ['KOFF351', 'KON351/KP351'],
                ['KOFF352', 'KON352/KP352'],
                ['KOFF353', 'KON353/KP353'],
                ['KOFF354', 'KON354/KP354'],
                ['KOFF355', 'KON355/KP355'],
                ['KOFF356', 'KON356/KP356'],
                ['KOFF357', 'KON357/KP357'],
                ['KOFF358', 'KON358/KP358'],
                ['KOFF359', 'KON359/KP359'],
                ['KOFF360', 'KON360/KP360'],
                ['KOFF361', 'KON361/KP361'],
                ['KOFF362', 'KON362/KP362'],
                ['KOFF363', 'KON363/KP363'],
                ['KOFF364', 'KON364/KP364'],
                ['KOFF365', 'KON365/KP365'],
                ['KOFF366', 'KON366/KP366'],
                ['KOFF367', 'KON367/KP367'],
                ['KOFF368', 'KON368/KP368'],
                ['KOFF369', 'KON369/KP369'],
                ['KOFF370', 'KON370/KP370'],
                ['KOFF371', 'KON371/KP371'],
                ['KOFF372', 'KON372/KP372'],
                ['KOFF373', 'KON373/KP373'],
                ['KOFF374', 'KON374/KP374'],
                ['KOFF375', 'KON375/KP375'],
                ['KOFF376', 'KON376/KP376'],
                ['KOFF377', 'KON377/KP377'],
                ['KOFF378', 'KON378/KP378'],
                ['KOFF379', 'KON379/KP379'],
                ['KOFF380', 'KON380/KP380'],
                ['KOFF381', 'KON381/KP381'],
                ['KOFF382', 'KON382/KP382'],
                ['KOFF383', 'KON383/KP383'],
                ['KOFF384', 'KON384/KP384'],
                ['KOFF385', 'KON385/KP385'],
                ['KOFF386', 'KON386/KP386'],
                ['KOFF387', 'KON387/KP387'],
                ['KOFF388', 'KON388/KP388'],
                ['KOFF389', 'KON389/KP389'],
                ['KOFF390', 'KON390/KP390'],
                ['KOFF391', 'KON391/KP391'],
                ['KOFF392', 'KON392/KP392'],
                ['KOFF393', 'KON393/KP393'],
                ['KOFF394', 'KON394/KP394'],
                ['KOFF395', 'KON395/KP395'],
                ['KOFF396', 'KON396/KP396'],
                ['KOFF397', 'KON397/KP397'],
                ['KOFF398', 'KON398/KP398'],
                ['KOFF399', 'KON399/KP399'],
                ['KOFF400', 'KON400/KP400'],
                ['KOFF401', 'KON401/KP401'],
                ['KOFF402', 'KON402/KP402'],
                ['KOFF403', 'KON403/KP403'],
                ['KOFF404', 'KON404/KP404'],
                ['KOFF405', 'KON405/KP405'],
                ['KOFF406', 'KON406/KP406'],
                ['KOFF407', 'KON407/KP407'],
                ['KOFF408', 'KON408/KP408'],
                ['KOFF409', 'KON409/KP409'],
                ['KOFF410', 'KON410/KP410'],
                ['KOFF411', 'KON411/KP411'],
                ['KOFF412', 'KON412/KP412'],
                ['KOFF413', 'KON413/KP413'],
                ['KOFF414', 'KON414/KP414'],
                ['KOFF415', 'KON415/KP415'],
                ['KOFF416', 'KON416/KP416'],
                ['KOFF417', 'KON417/KP417'],
                ['KOFF418', 'KON418/KP418'],
                ['KOFF419', 'KON419/KP419'],
                ['KOFF420', 'KON420/KP420'],
                ['KOFF421', 'KON421/KP421'],
                ['KOFF422', 'KON422/KP422'],
                ['KOFF423', 'KON423/KP423'],
                ['KOFF424', 'KON424/KP424'],
                ['KOFF425', 'KON425/KP425'],
                ['KOFF426', 'KON426/KP426'],
                ['KOFF427', 'KON427/KP427'],
                ['KOFF428', 'KON428/KP428'],
                ['KOFF429', 'KON429/KP429'],
                ['KOFF430', 'KON430/KP430'],
                ['KOFF431', 'KON431/KP431'],
                ['KOFF432', 'KON432/KP432'],
                ['KOFF433', 'KON433/KP433'],
                ['KOFF434', 'KON434/KP434'],
                ['KOFF435', 'KON435/KP435'],
                ['KOFF436', 'KON436/KP436'],
                ['KOFF437', 'KON437/KP437'],
                ['KOFF438', 'KON438/KP438'],
                ['KOFF439', 'KON439/KP439'],
                ['KOFF440', 'KON440/KP440'],
                ['KOFF441', 'KON441/KP441'],
                ['KOFF442', 'KON442/KP442'],
                ['KOFF443', 'KON443/KP443'],
                ['KOFF444', 'KON444/KP444'],
                ['KOFF445', 'KON445/KP445'],
                ['KOFF446', 'KON446/KP446'],
                ['KOFF447', 'KON447/KP447'],
                ['KOFF448', 'KON448/KP448'],
                ['KOFF449', 'KON449/KP449'],
                ['KOFF450', 'KON450/KP450'],
                ['KOFF451', 'KON451/KP451'],
                ['KOFF452', 'KON452/KP452'],
                ['KOFF453', 'KON453/KP453'],
                ['KOFF454', 'KON454/KP454'],
                ['KOFF455', 'KON455/KP455'],
                ['KOFF456', 'KON456/KP456'],
                ['KOFF457', 'KON457/KP457'],
                ['KOFF458', 'KON458/KP458'],
                ['KOFF459', 'KON459/KP459'],
                ['KOFF460', 'KON460/KP460'],
                ['KOFF461', 'KON461/KP461'],
                ['KOFF462', 'KON462/KP462'],
                ['KOFF463', 'KON463/KP463'],
                ['KOFF464', 'KON464/KP464'],
                ['KOFF465', 'KON465/KP465'],
                ['KOFF466', 'KON466/KP466'],
                ['KOFF467', 'KON467/KP467'],
                ['KOFF468', 'KON468/KP468'],
                ['KOFF469', 'KON469/KP469'],
                ['KOFF470', 'KON470/KP470'],
                ['KOFF471', 'KON471/KP471'],
                ['KOFF472', 'KON472/KP472'],
                ['KOFF473', 'KON473/KP473'],
                ['KOFF474', 'KON474/KP474'],
                ['KOFF475', 'KON475/KP475'],
                ['KOFF476', 'KON476/KP476'],
                ['KOFF477', 'KON477/KP477'],
                ['KOFF478', 'KON478/KP478'],
                ['KOFF479', 'KON479/KP479'],
                ['KOFF480', 'KON480/KP480'],
                ['KOFF481', 'KON481/KP481'],
                ['KOFF482', 'KON482/KP482'],
                ['KOFF483', 'KON483/KP483'],
                ['KOFF484', 'KON484/KP484'],
                ['KOFF485', 'KON485/KP485'],
                ['KOFF486', 'KON486/KP486'],
                ['KOFF487', 'KON487/KP487'],
                ['KOFF488', 'KON488/KP488'],
                ['KOFF489', 'KON489/KP489'],
                ['KOFF490', 'KON490/KP490'],
                ['KOFF491', 'KON491/KP491'],
                ['KOFF492', 'KON492/KP492'],
                ['KOFF493', 'KON493/KP493'],
                ['KOFF494', 'KON494/KP494'],
                ['KOFF495', 'KON495/KP495'],
                ['KOFF496', 'KON496/KP496'],
                ['KOFF497', 'KON497/KP497'],
                ['KOFF498', 'KON498/KP498'],
                ['KOFF499', 'KON499/KP499'],
                ['KOFF500', 'KON500/KP500'],
                ['KOFF501', 'KON501/KP501'],
                ['KOFF502', 'KON502/KP502'],
                ['KOFF503', 'KON503/KP503'],
                ['KOFF504', 'KON504/KP504'],
                ['KOFF505', 'KON505/KP505'],
                ['KOFF506', 'KON506/KP506'],
                ['KOFF507', 'KON507/KP507'],
                ['KOFF508', 'KON508/KP508'],
                ['KOFF509', 'KON509/KP509'],
                ['KOFF510', 'KON510/KP510'],
                ['KOFF511', 'KON511/KP511'],
                ['KOFF512', 'KON512/KP512'],
                ['KOFF513', 'KON513/KP513'],
                ['KOFF514', 'KON514/KP514'],
                ['KOFF515', 'KON515/KP515'],
                ['KOFF516', 'KON516/KP516'],
                ['KOFF517', 'KON517/KP517'],
                ['KOFF518', 'KON518/KP518'],
                ['KOFF519', 'KON519/KP519'],
                ['KOFF520', 'KON520/KP520'],
                ['KOFF521', 'KON521/KP521'],
                ['KOFF522', 'KON522/KP522'],
                ['KOFF523', 'KON523/KP523'],
                ['KOFF524', 'KON524/KP524'],
                ['KOFF525', 'KON525/KP525'],
                ['KOFF526', 'KON526/KP526'],
                ['KOFF527', 'KON527/KP527'],
                ['KOFF528', 'KON528/KP528'],
                ['KOFF529', 'KON529/KP529'],
                ['KOFF530', 'KON530/KP530'],
                ['KOFF531', 'KON531/KP531'],
                ['KOFF532', 'KON532/KP532'],
                ['KOFF533', 'KON533/KP533'],
                ['KOFF534', 'KON534/KP534'],
                ['KOFF535', 'KON535/KP535'],
                ['KOFF536', 'KON536/KP536'],
                ['KOFF537', 'KON537/KP537'],
                ['KOFF538', 'KON538/KP538'],
                ['KOFF539', 'KON539/KP539'],
                ['KOFF540', 'KON540/KP540'],
                ['KOFF541', 'KON541/KP541'],
                ['KOFF542', 'KON542/KP542'],
                ['KOFF543', 'KON543/KP543'],
                ['KOFF544', 'KON544/KP544'],
                ['KOFF545', 'KON545/KP545'],
                ['KOFF546', 'KON546/KP546'],
                ['KOFF547', 'KON547/KP547'],
                ['KOFF548', 'KON548/KP548'],
                ['KOFF549', 'KON549/KP549'],
                ['KOFF550', 'KON550/KP550'],
                ['KOFF551', 'KON551/KP551'],
                ['KOFF552', 'KON552/KP552'],
                ['KOFF553', 'KON553/KP553'],
                ['KOFF554', 'KON554/KP554'],
                ['KOFF555', 'KON555/KP555'],
                ['KOFF556', 'KON556/KP556'],
                ['KOFF557', 'KON557/KP557'],
                ['KOFF558', 'KON558/KP558'],
                ['KOFF559', 'KON559/KP559'],
                ['KOFF560', 'KON560/KP560'],
                ['KOFF561', 'KON561/KP561'],
                ['KOFF562', 'KON562/KP562'],
                ['KOFF563', 'KON563/KP563'],
                ['KOFF564', 'KON564/KP564'],
                ['KOFF565', 'KON565/KP565'],
                ['KOFF566', 'KON566/KP566'],
                ['KOFF567', 'KON567/KP567'],
                ['KOFF568', 'KON568/KP568'],
                ['KOFF569', 'KON569/KP569'],
                ['KOFF570', 'KON570/KP570'],
                ['KOFF571', 'KON571/KP571'],
                ['KOFF572', 'KON572/KP572'],
                ['KOFF573', 'KON573/KP573'],
                ['KOFF574', 'KON574/KP574'],
                ['KOFF575', 'KON575/KP575'],
                ['KOFF576', 'KON576/KP576'],
                ['KOFF577', 'KON577/KP577'],
                ['KOFF578', 'KON578/KP578'],
                ['KOFF579', 'KON579/KP579'],
                ['KOFF580', 'KON580/KP580'],
                ['KOFF581', 'KON581/KP581'],
                ['KOFF582', 'KON582/KP582'],
                ['KOFF583', 'KON583/KP583'],
                ['KOFF584', 'KON584/KP584'],
                ['KOFF585', 'KON585/KP585'],
                ['KOFF586', 'KON586/KP586'],
                ['KOFF587', 'KON587/KP587'],
                ['KOFF588', 'KON588/KP588'],
                ['KOFF589', 'KON589/KP589'],
                ['KOFF590', 'KON590/KP590'],
                ['KOFF591', 'KON591/KP591'],
                ['KOFF592', 'KON592/KP592'],
                ['KOFF593', 'KON593/KP593'],
                ['KOFF594', 'KON594/KP594'],
                ['KOFF595', 'KON595/KP595'],
                ['KOFF596', 'KON596/KP596'],
                ['KOFF597', 'KON597/KP597'],
                ['KOFF598', 'KON598/KP598'],
                ['KOFF599', 'KON599/KP599'],
                ['KOFF600', 'KON600/KP600'],
                ['KOFF601', 'KON601/KP601'],
                ['KOFF602', 'KON602/KP602'],
                ['KOFF603', 'KON603/KP603'],
                ['KOFF604', 'KON604/KP604'],
                ['KOFF605', 'KON605/KP605'],
                ['KOFF606', 'KON606/KP606'],
                ['KOFF607', 'KON607/KP607'],
                ['KOFF608', 'KON608/KP608'],
                ['KOFF609', 'KON609/KP609'],
                ['KOFF610', 'KON610/KP610']]   
    
    off_dict={}
    for i in off_temp:
        x=i[1].split('/')
        x[0]=on_dict[x[0]]
        x[1]=on_dict[x[1]]
        off_dict[i[0]]='('+x[0]+')/('+x[1]+')'
    
    part_in=[['kacid*acidsum', 'LIMONONIC=PART1'],
            ['kacid*acidsum', 'LIMONIC=PART11'],
            ['kacid*acidsum', 'KLIMONONIC=PART13'],
            ['kacid*acidsum', 'KLIMONIC=PART23'],
            ['kacid*acidsum', 'C731CO2H=PART24'],
            ['kacid*acidsum', 'C822CO2H=PART25'],
            ['kacid*acidsum', 'HOPINONIC=PART64'],
            ['kacid*acidsum', 'H3C25CCO2H=PART66'],
            ['kacid*acidsum', 'PINIC=PART72'],
            ['kacid*acidsum', 'NORPINIC=PART85'],
            ['kacid*acidsum', 'H3C2C4CO2H=PART119'],
            ['kacid*acidsum', 'PINONIC=PART123'],
            ['kacid*acidsum', 'C89CO2H=PART132'],
            ['kacid*acidsum', 'PERPINONIC=PART137'],
            ['kacid*acidsum', 'CO13C3CO2H=PART157'],
            ['kacid*acidsum', 'C512CO2H=PART209'],
            ['kacid*acidsum', 'C615CO2H=PART226'],
            ['kacid*acidsum', 'C617CO2H=PART234'],
            ['kacid*acidsum', 'C618CO2H=PART239'],
            ['kacid*acidsum', 'C718CO2H=PART251'],
            ['kacid*acidsum', 'C87CO2H=PART258'],
            ['kacid*acidsum', 'C88CO2H=PART265'],
            ['kacid*acidsum', 'CO1M22CO2H=PART304'],
            ['kacid*acidsum', 'MC3ODBCO2H=PART354'],
            ['kacid*acidsum', 'HC4CCO2H=PART361'],
            ['kacid*acidsum', 'HC4ACO2H=PART362'],
            ['kacid*acidsum', 'CO2C4CO2H=PART363'],
            ['kacid*acidsum', 'C518CO2H=PART383'],
            ['kacid*acidsum', 'HMVKBCO2H=PART386'],
            ['kacid*acidsum', 'C624CO2H=PART407'],
            ['kacid*acidsum', 'C622CO2H=PART408'],
            ['kacid*acidsum', 'C23O3CCO2H=PART411'],
            ['kacid*acidsum', 'C519CO2H=PART416'],
            ['kacid*acidsum', 'C517CO2H=PART418'],
            ['kacid*acidsum', 'C729CO2H=PART438'],
            ['kacid*acidsum', 'CONM2CO2H=PART460'],
            ['kacid*acidsum', 'MMALNBCO2H=PART523'],
            ['kacid*acidsum', 'MMALNACO2H=PART524'],
            ['kacid*acidsum', 'C58NO3CO2H=PART530'],
            ['kacid*acidsum', 'C57NO3CO2H=PART531'],
            ['kacid*acidsum', 'INCNCO2H=PART590'],
            ['kacid*acidsum', 'INB1NBCO2H=PART591'],
            ['kacid*acidsum', 'INB1NACO2H=PART592'],
            ['KON1', 'LIMONONIC+SEED_1=PART1+SEED_1'],
            ['KON2A', 'LIMANO3+SEED_1=PART2A+SEED_1'],
            ['KON2B', 'LIMBNO3+SEED_1=PART2B+SEED_1'],
            ['KON3', 'LIMCNO3+SEED_1=PART3+SEED_1'],
            ['KON4', 'C923PAN+SEED_1=PART4+SEED_1'],
            ['KON5', 'C817PAN+SEED_1=PART5+SEED_1'],
            ['KON6', 'LMKANO3+SEED_1=PART6+SEED_1'],
            ['KON11', 'LIMONIC+SEED_1=PART11+SEED_1'],
            ['KON13', 'KLIMONONIC+SEED_1=PART13+SEED_1'],
            ['KON14', 'LIMAL+SEED_1=PART14+SEED_1'],
            ['KON15', 'LMLKET+SEED_1=PART15+SEED_1'],
            ['KON16', 'LIMALBOH+SEED_1=PART16+SEED_1'],
            ['KON17', 'LIMALACO+SEED_1=PART17+SEED_1'],
            ['KON22', 'C732PAN+SEED_1=PART22+SEED_1'],
            ['KON23', 'KLIMONIC+SEED_1=PART23+SEED_1'],
            ['KON24', 'C731CO2H+SEED_1=PART24+SEED_1'],
            ['KON25', 'C822CO2H+SEED_1=PART25+SEED_1'],
            ['KON26', 'LIMALOOH+SEED_1=PART26+SEED_1'],
            ['KON27', 'LIMCOOH+SEED_1=PART27+SEED_1'],
            ['KON28', 'C825OH+SEED_1=PART28+SEED_1'],
            ['KON29', 'LIMAOOH+SEED_1=PART29+SEED_1'],
            ['KON30', 'C826OOH+SEED_1=PART30+SEED_1'],
            ['KON31', 'C825CO+SEED_1=PART31+SEED_1'],
            ['KON32', 'LIMALOH+SEED_1=PART32+SEED_1'],
            ['KON33', 'C728OOH+SEED_1=PART33+SEED_1'],
            ['KON34', 'LIMALBOOH+SEED_1=PART34+SEED_1'],
            ['KON35', 'LIMALAOOH+SEED_1=PART35+SEED_1'],
            ['KON36', 'C924OOH+SEED_1=PART36+SEED_1'],
            ['KON37', 'C818OOH+SEED_1=PART37+SEED_1'],
            ['KON38', 'LMKAOOH+SEED_1=PART38+SEED_1'],
            ['KON39', 'NORLIMOOH+SEED_1=PART39+SEED_1'],
            ['KON40', 'LIMCOH+SEED_1=PART40+SEED_1'],
            ['KON41', 'C924OH+SEED_1=PART41+SEED_1'],
            ['KON42', 'LIMALAOH+SEED_1=PART42+SEED_1'],
            ['KON43', 'C925OOH+SEED_1=PART43+SEED_1'],
            ['KON44', 'LIMAOH+SEED_1=PART44+SEED_1'],
            ['KON45', 'C826OH+SEED_1=PART45+SEED_1'],
            ['KON46', 'C728OH+SEED_1=PART46+SEED_1'],
            ['KON47', 'C823OOH+SEED_1=PART47+SEED_1'],
            ['KON48', 'LIMBOOH+SEED_1=PART48+SEED_1'],
            ['KON49', 'LMLKAOH+SEED_1=PART49+SEED_1'],
            ['KON50', 'C922OOH+SEED_1=PART50+SEED_1'],
            ['KON51', 'C813OOH+SEED_1=PART51+SEED_1'],
            ['KON52', 'C516OOH+SEED_1=PART52+SEED_1'],
            ['KON53', 'C621OOH+SEED_1=PART53+SEED_1'],
            ['KON54', 'C813NO3+SEED_1=PART54+SEED_1'],
            ['KON55', 'C921OOH+SEED_1=PART55+SEED_1'],
            ['KON56', 'C812OOH+SEED_1=PART56+SEED_1'],
            ['KON57', 'C813OH+SEED_1=PART57+SEED_1'],
            ['KON58', 'NC72OOH+SEED_1=PART58+SEED_1'],
            ['KON59', 'NC61CO3H+SEED_1=PART59+SEED_1'],
            ['KON60', 'NC102OOH+SEED_1=PART60+SEED_1'],
            ['KON61', 'C719OOH+SEED_1=PART61+SEED_1'],
            ['KON62', 'C98OOH+SEED_1=PART62+SEED_1'],
            ['KON63', 'NC6PAN1+SEED_1=PART63+SEED_1'],
            ['KON64', 'HOPINONIC+SEED_1=PART64+SEED_1'],
            ['KON65', 'C812OH+SEED_1=PART65+SEED_1'],
            ['KON66', 'H3C25CCO2H+SEED_1=PART66+SEED_1'],
            ['KON67', 'C722OOH+SEED_1=PART67+SEED_1'],
            ['KON68', 'NC71OOH+SEED_1=PART68+SEED_1'],
            ['KON69', 'NC101OOH+SEED_1=PART69+SEED_1'],
            ['KON70', 'C719NO3+SEED_1=PART70+SEED_1'],
            ['KON71', 'C920CO3H+SEED_1=PART71+SEED_1'],
            ['KON72', 'PINIC+SEED_1=PART72+SEED_1'],
            ['KON73', 'C106OOH+SEED_1=PART73+SEED_1'],
            ['KON74', 'C108OOH+SEED_1=PART74+SEED_1'],
            ['KON75', 'H3C25CCO3H+SEED_1=PART75+SEED_1'],
            ['KON76', 'C98NO3+SEED_1=PART76+SEED_1'],
            ['KON77', 'C614OOH+SEED_1=PART77+SEED_1'],
            ['KON78', 'C920OOH+SEED_1=PART78+SEED_1'],
            ['KON79', 'H3C25C6OOH+SEED_1=PART79+SEED_1'],
            ['KON80', 'C811OOH+SEED_1=PART80+SEED_1'],
            ['KON81', 'C44OOH+SEED_1=PART81+SEED_1'],
            ['KON82', 'C719OH+SEED_1=PART82+SEED_1'],
            ['KON83', 'H3C25C6PAN+SEED_1=PART83+SEED_1'],
            ['KON84', 'C97OOH+SEED_1=PART84+SEED_1'],
            ['KON85', 'NORPINIC+SEED_1=PART85+SEED_1'],
            ['KON86', 'H1C23C4OOH+SEED_1=PART86+SEED_1'],
            ['KON87', 'C920PAN+SEED_1=PART87+SEED_1'],
            ['KON88', 'C98OH+SEED_1=PART88+SEED_1'],
            ['KON89', 'C811CO3H+SEED_1=PART89+SEED_1'],
            ['KON90', 'HC23C4CO3H+SEED_1=PART90+SEED_1'],
            ['KON91', 'C106NO3+SEED_1=PART91+SEED_1'],
            ['KON92', 'C108NO3+SEED_1=PART92+SEED_1'],
            ['KON93', 'C811PAN+SEED_1=PART93+SEED_1'],
            ['KON94', 'C716OOH+SEED_1=PART94+SEED_1'],
            ['KON95', 'C717OOH+SEED_1=PART95+SEED_1'],
            ['KON96', 'NAPINAOOH+SEED_1=PART96+SEED_1'],
            ['KON97', 'NAPINBOOH+SEED_1=PART97+SEED_1'],
            ['KON98', 'C721OOH+SEED_1=PART98+SEED_1'],
            ['KON99', 'C109OOH+SEED_1=PART99+SEED_1'],
            ['KON100', 'C614NO3+SEED_1=PART100+SEED_1'],
            ['KON101', 'H1C23C4PAN+SEED_1=PART101+SEED_1'],
            ['KON102', 'C721CO3H+SEED_1=PART102+SEED_1'],
            ['KON103', 'C235C6CO3H+SEED_1=PART103+SEED_1'],
            ['KON104', 'APINCOOH+SEED_1=PART104+SEED_1'],
            ['KON105', 'C811NO3+SEED_1=PART105+SEED_1'],
            ['KON106', 'APINAOOH+SEED_1=PART106+SEED_1'],
            ['KON107', 'C7PAN3+SEED_1=PART107+SEED_1'],
            ['KON108', 'C107OOH+SEED_1=PART108+SEED_1'],
            ['KON109', 'PINALOOH+SEED_1=PART109+SEED_1'],
            ['KON110', 'C106OH+SEED_1=PART110+SEED_1'],
            ['KON111', 'C108OH+SEED_1=PART111+SEED_1'],
            ['KON112', 'C811OH+SEED_1=PART112+SEED_1'],
            ['KON113', 'C614OH+SEED_1=PART113+SEED_1'],
            ['KON114', 'H3C25C6OH+SEED_1=PART114+SEED_1'],
            ['KON115', 'C721PAN+SEED_1=PART115+SEED_1'],
            ['KON116', 'C810OOH+SEED_1=PART116+SEED_1'],
            ['KON117', 'CO235C6OOH+SEED_1=PART117+SEED_1'],
            ['KON118', 'APINBOOH+SEED_1=PART118+SEED_1'],
            ['KON119', 'H3C2C4CO2H+SEED_1=PART119+SEED_1'],
            ['KON120', 'C717NO3+SEED_1=PART120+SEED_1'],
            ['KON121', 'NC71CO+SEED_1=PART121+SEED_1'],
            ['KON122', 'C97OH+SEED_1=PART122+SEED_1'],
            ['KON123', 'PINONIC+SEED_1=PART123+SEED_1'],
            ['KON124', 'APINCNO3+SEED_1=PART124+SEED_1'],
            ['KON125', 'C86OOH+SEED_1=PART125+SEED_1'],
            ['KON126', 'PINALNO3+SEED_1=PART126+SEED_1'],
            ['KON127', 'C109OH+SEED_1=PART127+SEED_1'],
            ['KON128', 'C810NO3+SEED_1=PART128+SEED_1'],
            ['KON129', 'APINANO3+SEED_1=PART129+SEED_1'],
            ['KON130', 'C720OOH+SEED_1=PART130+SEED_1'],
            ['KON131', 'H3C2C4CO3H+SEED_1=PART131+SEED_1'],
            ['KON132', 'C89CO2H+SEED_1=PART132+SEED_1'],
            ['KON133', 'C716OH+SEED_1=PART133+SEED_1'],
            ['KON134', 'C717OH+SEED_1=PART134+SEED_1'],
            ['KON135', 'APINBNO3+SEED_1=PART135+SEED_1'],
            ['KON136', 'C514OOH+SEED_1=PART136+SEED_1'],
            ['KON137', 'PERPINONIC+SEED_1=PART137+SEED_1'],
            ['KON138', 'C10PAN2+SEED_1=PART138+SEED_1'],
            ['KON139', 'C614CO+SEED_1=PART139+SEED_1'],
            ['KON140', 'APINCOH+SEED_1=PART140+SEED_1'],
            ['KON141', 'H3C2C4PAN+SEED_1=PART141+SEED_1'],
            ['KON142', 'C107OH+SEED_1=PART142+SEED_1'],
            ['KON143', 'PINALOH+SEED_1=PART143+SEED_1'],
            ['KON144', 'APINBOH+SEED_1=PART144+SEED_1'],
            ['KON145', 'C721CHO+SEED_1=PART145+SEED_1'],
            ['KON146', 'C89CO3H+SEED_1=PART146+SEED_1'],
            ['KON147', 'C96OOH+SEED_1=PART147+SEED_1'],
            ['KON148', 'CO2H3CO3H+SEED_1=PART148+SEED_1'],
            ['KON149', 'H3C25C5CHO+SEED_1=PART149+SEED_1'],
            ['KON150', 'NC101CO+SEED_1=PART150+SEED_1'],
            ['KON151', 'C810OH+SEED_1=PART151+SEED_1'],
            ['KON152', 'H1C23C4CHO+SEED_1=PART152+SEED_1'],
            ['KON153', 'C85CO3H+SEED_1=PART153+SEED_1'],
            ['KON154', 'C514NO3+SEED_1=PART154+SEED_1'],
            ['KON155', 'C109CO+SEED_1=PART155+SEED_1'],
            ['KON156', 'C9PAN2+SEED_1=PART156+SEED_1'],
            ['KON157', 'CO13C3CO2H+SEED_1=PART157+SEED_1'],
            ['KON158', 'CHOC3COOOH+SEED_1=PART158+SEED_1'],
            ['KON159', 'C720NO3+SEED_1=PART159+SEED_1'],
            ['KON160', 'C511OOH+SEED_1=PART160+SEED_1'],
            ['KON161', 'C4PAN6+SEED_1=PART161+SEED_1'],
            ['KON162', 'H1CO23CHO+SEED_1=PART162+SEED_1'],
            ['KON163', 'C89PAN+SEED_1=PART163+SEED_1'],
            ['KON164', 'C89OOH+SEED_1=PART164+SEED_1'],
            ['KON165', 'C5PAN9+SEED_1=PART165+SEED_1'],
            ['KON166', 'C96NO3+SEED_1=PART166+SEED_1'],
            ['KON167', 'CO235C6CHO+SEED_1=PART167+SEED_1'],
            ['KON168', 'CHOC3COPAN+SEED_1=PART168+SEED_1'],
            ['KON169', 'CO23C4CO3H+SEED_1=PART169+SEED_1'],
            ['KON170', 'C720OH+SEED_1=PART170+SEED_1'],
            ['KON171', 'C85OOH+SEED_1=PART171+SEED_1'],
            ['KON172', 'APINBCO+SEED_1=PART172+SEED_1'],
            ['KON173', 'C312COCO3H+SEED_1=PART173+SEED_1'],
            ['KON174', 'C514OH+SEED_1=PART174+SEED_1'],
            ['KON175', 'C96OH+SEED_1=PART175+SEED_1'],
            ['KON176', 'C312COPAN+SEED_1=PART176+SEED_1'],
            ['KON177', 'CO235C5CHO+SEED_1=PART177+SEED_1'],
            ['KON178', 'C89NO3+SEED_1=PART178+SEED_1'],
            ['KON179', 'PINAL+SEED_1=PART179+SEED_1'],
            ['KON180', 'HCC7CO+SEED_1=PART180+SEED_1'],
            ['KON181', 'C89OH+SEED_1=PART181+SEED_1'],
            ['KON182', 'CO13C4CHO+SEED_1=PART182+SEED_1'],
            ['KON183', 'NORPINAL+SEED_1=PART183+SEED_1'],
            ['KON184', 'CO2H3CHO+SEED_1=PART184+SEED_1'],
            ['KON185', 'C4CODIAL+SEED_1=PART185+SEED_1'],
            ['KON186', 'CO23C4CHO+SEED_1=PART186+SEED_1'],
            ['KON200', 'BPINANO3+SEED_1=PART200+SEED_1'],
            ['KON201', 'BPINAOH+SEED_1=PART201+SEED_1'],
            ['KON202', 'BPINAOOH+SEED_1=PART202+SEED_1'],
            ['KON203', 'BPINBNO3+SEED_1=PART203+SEED_1'],
            ['KON204', 'BPINBOOH+SEED_1=PART204+SEED_1'],
            ['KON205', 'BPINCNO3+SEED_1=PART205+SEED_1'],
            ['KON206', 'BPINCOH+SEED_1=PART206+SEED_1'],
            ['KON207', 'BPINCOOH+SEED_1=PART207+SEED_1'],
            ['KON209', 'C512CO2H+SEED_1=PART209+SEED_1'],
            ['KON210', 'C512CO3H+SEED_1=PART210+SEED_1'],
            ['KON211', 'C512NO3+SEED_1=PART211+SEED_1'],
            ['KON212', 'C512OH+SEED_1=PART212+SEED_1'],
            ['KON213', 'C512OOH+SEED_1=PART213+SEED_1'],
            ['KON214', 'C512PAN+SEED_1=PART214+SEED_1'],
            ['KON215', 'C513CO+SEED_1=PART215+SEED_1'],
            ['KON216', 'C513OH+SEED_1=PART216+SEED_1'],
            ['KON217', 'C513OOH+SEED_1=PART217+SEED_1'],
            ['KON218', 'C515CHO+SEED_1=PART218+SEED_1'],
            ['KON219', 'C515CO+SEED_1=PART219+SEED_1'],
            ['KON220', 'C515CO3H+SEED_1=PART220+SEED_1'],
            ['KON221', 'C515OOH+SEED_1=PART221+SEED_1'],
            ['KON222', 'C515PAN+SEED_1=PART222+SEED_1'],
            ['KON223', 'C55OOH+SEED_1=PART223+SEED_1'],
            ['KON224', 'C5PAN11+SEED_1=PART224+SEED_1'],
            ['KON225', 'C615CO+SEED_1=PART225+SEED_1'],
            ['KON226', 'C615CO2H+SEED_1=PART226+SEED_1'],
            ['KON227', 'C615CO3H+SEED_1=PART227+SEED_1'],
            ['KON228', 'C615OH+SEED_1=PART228+SEED_1'],
            ['KON229', 'C615OOH+SEED_1=PART229+SEED_1'],
            ['KON230', 'C615PAN+SEED_1=PART230+SEED_1'],
            ['KON231', 'C616OH+SEED_1=PART231+SEED_1'],
            ['KON232', 'C616OOH+SEED_1=PART232+SEED_1'],
            ['KON233', 'C617CHO+SEED_1=PART233+SEED_1'],
            ['KON234', 'C617CO2H+SEED_1=PART234+SEED_1'],
            ['KON235', 'C617CO3H+SEED_1=PART235+SEED_1'],
            ['KON236', 'C617OH+SEED_1=PART236+SEED_1'],
            ['KON237', 'C617OOH+SEED_1=PART237+SEED_1'],
            ['KON238', 'C617PAN+SEED_1=PART238+SEED_1'],
            ['KON239', 'C618CO2H+SEED_1=PART239+SEED_1'],
            ['KON240', 'C618CO3H+SEED_1=PART240+SEED_1'],
            ['KON241', 'C618OOH+SEED_1=PART241+SEED_1'],
            ['KON242', 'C618PAN+SEED_1=PART242+SEED_1'],
            ['KON243', 'C619CO+SEED_1=PART243+SEED_1'],
            ['KON244', 'C619OH+SEED_1=PART244+SEED_1'],
            ['KON245', 'C619OOH+SEED_1=PART245+SEED_1'],
            ['KON246', 'C620OH+SEED_1=PART246+SEED_1'],
            ['KON247', 'C620OOH+SEED_1=PART247+SEED_1'],
            ['KON248', 'C67CHO+SEED_1=PART248+SEED_1'],
            ['KON249', 'C67CO3H+SEED_1=PART249+SEED_1'],
            ['KON250', 'C6PAN9+SEED_1=PART250+SEED_1'],
            ['KON251', 'C718CO2H+SEED_1=PART251+SEED_1'],
            ['KON252', 'C718CO3H+SEED_1=PART252+SEED_1'],
            ['KON253', 'C718NO3+SEED_1=PART253+SEED_1'],
            ['KON254', 'C718OH+SEED_1=PART254+SEED_1'],
            ['KON255', 'C718OOH+SEED_1=PART255+SEED_1'],
            ['KON256', 'C718PAN+SEED_1=PART256+SEED_1'],
            ['KON257', 'C87CO+SEED_1=PART257+SEED_1'],
            ['KON258', 'C87CO2H+SEED_1=PART258+SEED_1'],
            ['KON259', 'C87CO3H+SEED_1=PART259+SEED_1'],
            ['KON260', 'C87OH+SEED_1=PART260+SEED_1'],
            ['KON261', 'C87OOH+SEED_1=PART261+SEED_1'],
            ['KON262', 'C87PAN+SEED_1=PART262+SEED_1'],
            ['KON263', 'C88CHO+SEED_1=PART263+SEED_1'],
            ['KON264', 'C88CO+SEED_1=PART264+SEED_1'],
            ['KON265', 'C88CO2H+SEED_1=PART265+SEED_1'],
            ['KON266', 'C88CO3H+SEED_1=PART266+SEED_1'],
            ['KON267', 'C88OH+SEED_1=PART267+SEED_1'],
            ['KON268', 'C88OOH+SEED_1=PART268+SEED_1'],
            ['KON269', 'C88PAN+SEED_1=PART269+SEED_1'],
            ['KON270', 'C8BC+SEED_1=PART270+SEED_1'],
            ['KON271', 'C8BCCO+SEED_1=PART271+SEED_1'],
            ['KON272', 'C8BCNO3+SEED_1=PART272+SEED_1'],
            ['KON273', 'C8BCOH+SEED_1=PART273+SEED_1'],
            ['KON274', 'C8BCOOH+SEED_1=PART274+SEED_1'],
            ['KON275', 'C914CO+SEED_1=PART275+SEED_1'],
            ['KON276', 'C914OH+SEED_1=PART276+SEED_1'],
            ['KON277', 'C914OOH+SEED_1=PART277+SEED_1'],
            ['KON278', 'C915NO3+SEED_1=PART278+SEED_1'],
            ['KON279', 'C915OH+SEED_1=PART279+SEED_1'],
            ['KON280', 'C915OOH+SEED_1=PART280+SEED_1'],
            ['KON281', 'C916NO3+SEED_1=PART281+SEED_1'],
            ['KON282', 'C916OH+SEED_1=PART282+SEED_1'],
            ['KON283', 'C916OOH+SEED_1=PART283+SEED_1'],
            ['KON284', 'C917NO3+SEED_1=PART284+SEED_1'],
            ['KON285', 'C917OH+SEED_1=PART285+SEED_1'],
            ['KON286', 'C917OOH+SEED_1=PART286+SEED_1'],
            ['KON287', 'C918CHO+SEED_1=PART287+SEED_1'],
            ['KON288', 'C918CO3H+SEED_1=PART288+SEED_1'],
            ['KON289', 'C918NO3+SEED_1=PART289+SEED_1'],
            ['KON290', 'C918OH+SEED_1=PART290+SEED_1'],
            ['KON291', 'C918OOH+SEED_1=PART291+SEED_1'],
            ['KON292', 'C918PAN+SEED_1=PART292+SEED_1'],
            ['KON293', 'C919NO3+SEED_1=PART293+SEED_1'],
            ['KON294', 'C919OH+SEED_1=PART294+SEED_1'],
            ['KON295', 'C919OOH+SEED_1=PART295+SEED_1'],
            ['KON296', 'C9DC+SEED_1=PART296+SEED_1'],
            ['KON297', 'C9DCCO+SEED_1=PART297+SEED_1'],
            ['KON298', 'C9DCNO3+SEED_1=PART298+SEED_1'],
            ['KON299', 'C9DCOH+SEED_1=PART299+SEED_1'],
            ['KON300', 'C9DCOOH+SEED_1=PART300+SEED_1'],
            ['KON301', 'CO123C5CHO+SEED_1=PART301+SEED_1'],
            ['KON302', 'CO12C4CHO+SEED_1=PART302+SEED_1'],
            ['KON303', 'CO1M22CHO+SEED_1=PART303+SEED_1'],
            ['KON304', 'CO1M22CO2H+SEED_1=PART304+SEED_1'],
            ['KON305', 'CO1M22CO3H+SEED_1=PART305+SEED_1'],
            ['KON306', 'CO1M22PAN+SEED_1=PART306+SEED_1'],
            ['KON307', 'H2M2C3CO3H+SEED_1=PART307+SEED_1'],
            ['KON308', 'MIBKHO4CHO+SEED_1=PART308+SEED_1'],
            ['KON309', 'NBPINAOOH+SEED_1=PART309+SEED_1'],
            ['KON310', 'NBPINBOOH+SEED_1=PART310+SEED_1'],
            ['KON311', 'NC91CHO+SEED_1=PART311+SEED_1'],
            ['KON312', 'NC91CO3H+SEED_1=PART312+SEED_1'],
            ['KON313', 'NC91PAN+SEED_1=PART313+SEED_1'],
            ['KON314', 'NOPINANO3+SEED_1=PART314+SEED_1'],
            ['KON315', 'NOPINAOH+SEED_1=PART315+SEED_1'],
            ['KON316', 'NOPINAOOH+SEED_1=PART316+SEED_1'],
            ['KON317', 'NOPINBCO+SEED_1=PART317+SEED_1'],
            ['KON318', 'NOPINBNO3+SEED_1=PART318+SEED_1'],
            ['KON319', 'NOPINBOH+SEED_1=PART319+SEED_1'],
            ['KON320', 'NOPINBOOH+SEED_1=PART320+SEED_1'],
            ['KON321', 'NOPINCNO3+SEED_1=PART321+SEED_1'],
            ['KON322', 'NOPINCOH+SEED_1=PART322+SEED_1'],
            ['KON323', 'NOPINCOOH+SEED_1=PART323+SEED_1'],
            ['KON324', 'NOPINDCO+SEED_1=PART324+SEED_1'],
            ['KON325', 'NOPINDOH+SEED_1=PART325+SEED_1'],
            ['KON326', 'NOPINDOOH+SEED_1=PART326+SEED_1'],
            ['KON327', 'NOPINONE+SEED_1=PART327+SEED_1'],
            ['kon350', 'M3F+SEED_1=PART350+SEED_1'],
            ['KON351', 'ISOPDOH+SEED_1=PART351+SEED_1'],
            ['KON352', 'ISOPAOH+SEED_1=PART352+SEED_1'],
            ['KON353', 'MMALANHY+SEED_1=PART353+SEED_1'],
            ['KON354', 'MC3ODBCO2H+SEED_1=PART354+SEED_1'],
            ['KON355', 'C532CO+SEED_1=PART355+SEED_1'],
            ['KON356', 'C624CO+SEED_1=PART356+SEED_1'],
            ['KON357', 'C518CHO+SEED_1=PART357+SEED_1'],
            ['KON358', 'IEB1CHO+SEED_1=PART358+SEED_1'],
            ['KON359', 'HO1CO34C5+SEED_1=PART359+SEED_1'],
            ['KON360', 'HMVKBCHO+SEED_1=PART360+SEED_1'],
            ['KON361', 'HC4CCO2H+SEED_1=PART361+SEED_1'],
            ['KON362', 'HC4ACO2H+SEED_1=PART362+SEED_1'],
            ['KON363', 'CO2C4CO2H+SEED_1=PART363+SEED_1'],
            ['KON364', 'C5HPALD2+SEED_1=PART364+SEED_1'],
            ['KON365', 'C624OH+SEED_1=PART365+SEED_1'],
            ['KON366', 'C622OH+SEED_1=PART366+SEED_1'],
            ['KON367', 'ISOPDOOH+SEED_1=PART367+SEED_1'],
            ['KON368', 'ISOPCOOH+SEED_1=PART368+SEED_1'],
            ['KON369', 'IEPOXC+SEED_1=PART369+SEED_1'],
            ['KON370', 'IEPOXB+SEED_1=PART370+SEED_1'],
            ['KON371', 'HO13CO4C5+SEED_1=PART371+SEED_1'],
            ['KON372', 'C517OH+SEED_1=PART372+SEED_1'],
            ['KON373', 'C531CO+SEED_1=PART373+SEED_1'],
            ['KON374', 'CO2C4GLYOX+SEED_1=PART374+SEED_1'],
            ['KON375', 'C511CHO+SEED_1=PART375+SEED_1'],
            ['KON376', 'C624CHO+SEED_1=PART376+SEED_1'],
            ['KON377', 'C622CHO+SEED_1=PART377+SEED_1'],
            ['KON378', 'C5PACALD2+SEED_1=PART378+SEED_1'],
            ['KON379', 'C5PACALD1+SEED_1=PART379+SEED_1'],
            ['KON380', 'C23O3CCHO+SEED_1=PART380+SEED_1'],
            ['KON381', 'C627OH+SEED_1=PART381+SEED_1'],
            ['KON382', 'C519CHO+SEED_1=PART382+SEED_1'],
            ['KON383', 'C518CO2H+SEED_1=PART383+SEED_1'],
            ['KON384', 'C517CHO+SEED_1=PART384+SEED_1'],
            ['KON385', 'PXYFUOH+SEED_1=PART385+SEED_1'],
            ['KON386', 'HMVKBCO2H+SEED_1=PART386+SEED_1'],
            ['KON387', 'HC4CCO3H+SEED_1=PART387+SEED_1'],
            ['KON388', 'HC4ACO3H+SEED_1=PART388+SEED_1'],
            ['KON389', 'CO2C4CO3H+SEED_1=PART389+SEED_1'],
            ['KON390', 'C520OH+SEED_1=PART390+SEED_1'],
            ['KON391', 'C4M2AL2OH+SEED_1=PART391+SEED_1'],
            ['KON392', 'C624OOH+SEED_1=PART392+SEED_1'],
            ['KON393', 'C622OOH+SEED_1=PART393+SEED_1'],
            ['KON394', 'C58OH+SEED_1=PART394+SEED_1'],
            ['KON395', 'C57OH+SEED_1=PART395+SEED_1'],
            ['KON396', 'C519OOH+SEED_1=PART396+SEED_1'],
            ['KON397', 'C517OOH+SEED_1=PART397+SEED_1'],
            ['KON398', 'LIMKET+SEED_1=PART398+SEED_1'],
            ['KON399', 'C816CO+SEED_1=PART399+SEED_1'],
            ['KON400', 'C729CHO+SEED_1=PART400+SEED_1'],
            ['KON401', 'CO25C6CHO+SEED_1=PART401+SEED_1'],
            ['KON402', 'C727CO+SEED_1=PART402+SEED_1'],
            ['KON403', 'C626CHO+SEED_1=PART403+SEED_1'],
            ['KON404', 'C822OH+SEED_1=PART404+SEED_1'],
            ['KON405', 'C731OH+SEED_1=PART405+SEED_1'],
            ['KON406', 'C729OOH+SEED_1=PART406+SEED_1'],
            ['KON407', 'C624CO2H+SEED_1=PART407+SEED_1'],
            ['KON408', 'C622CO2H+SEED_1=PART408+SEED_1'],
            ['KON409', 'MMALNHY2OH+SEED_1=PART409+SEED_1'],
            ['KON410', 'C531OOH+SEED_1=PART410+SEED_1'],
            ['KON411', 'C23O3CCO2H+SEED_1=PART411+SEED_1'],
            ['KON412', 'C629OH+SEED_1=PART412+SEED_1'],
            ['KON413', 'C628OH+SEED_1=PART413+SEED_1'],
            ['KON414', 'C627OOH+SEED_1=PART414+SEED_1'],
            ['KON415', 'C626OOH+SEED_1=PART415+SEED_1'],
            ['KON416', 'C519CO2H+SEED_1=PART416+SEED_1'],
            ['KON417', 'C518CO3H+SEED_1=PART417+SEED_1'],
            ['KON418', 'C517CO2H+SEED_1=PART418+SEED_1'],
            ['KON419', 'ISOPDNO3+SEED_1=PART419+SEED_1'],
            ['KON420', 'ISOPCNO3+SEED_1=PART420+SEED_1'],
            ['KON421', 'PXYFUOOH+SEED_1=PART421+SEED_1'],
            ['KON422', 'IECCO3H+SEED_1=PART422+SEED_1'],
            ['KON423', 'IEC2OOH+SEED_1=PART423+SEED_1'],
            ['KON424', 'HMVKBCO3H+SEED_1=PART424+SEED_1'],
            ['KON425', 'C520OOH+SEED_1=PART425+SEED_1'],
            ['KON426', 'C4MALOHOOH+SEED_1=PART426+SEED_1'],
            ['KON427', 'C625OH+SEED_1=PART427+SEED_1'],
            ['KON428', 'C623OH+SEED_1=PART428+SEED_1'],
            ['KON429', 'C59OOH+SEED_1=PART429+SEED_1'],
            ['KON430', 'C58OOH+SEED_1=PART430+SEED_1'],
            ['KON431', 'C58AOOH+SEED_1=PART431+SEED_1'],
            ['KON432', 'C57OOH+SEED_1=PART432+SEED_1'],
            ['KON433', 'C57AOOH+SEED_1=PART433+SEED_1'],
            ['KON434', 'NORLIMAL+SEED_1=PART434+SEED_1'],
            ['KON435', 'C824CO+SEED_1=PART435+SEED_1'],
            ['KON436', 'C823CO+SEED_1=PART436+SEED_1'],
            ['KON437', 'C817CO+SEED_1=PART437+SEED_1'],
            ['KON438', 'C729CO2H+SEED_1=PART438+SEED_1'],
            ['KON439', 'C923OH+SEED_1=PART439+SEED_1'],
            ['KON440', 'C823OH+SEED_1=PART440+SEED_1'],
            ['KON441', 'C822OOH+SEED_1=PART441+SEED_1'],
            ['KON442', 'C817OH+SEED_1=PART442+SEED_1'],
            ['KON443', 'C816OOH+SEED_1=PART443+SEED_1'],
            ['KON444', 'C511CO3H+SEED_1=PART444+SEED_1'],
            ['KON445', 'C733OH+SEED_1=PART445+SEED_1'],
            ['KON446', 'C732OH+SEED_1=PART446+SEED_1'],
            ['KON447', 'C731OOH+SEED_1=PART447+SEED_1'],
            ['KON448', 'C727OOH+SEED_1=PART448+SEED_1'],
            ['KON449', 'C624CO3H+SEED_1=PART449+SEED_1'],
            ['KON450', 'C622CO3H+SEED_1=PART450+SEED_1'],
            ['KON451', 'C624NO3+SEED_1=PART451+SEED_1'],
            ['KON452', 'C622NO3+SEED_1=PART452+SEED_1'],
            ['KON453', 'MMALNHYOOH+SEED_1=PART453+SEED_1'],
            ['KON454', 'C23O3CCO3H+SEED_1=PART454+SEED_1'],
            ['KON455', 'C629OOH+SEED_1=PART455+SEED_1'],
            ['KON456', 'C628OOH+SEED_1=PART456+SEED_1'],
            ['KON457', 'C519CO3H+SEED_1=PART457+SEED_1'],
            ['KON458', 'C517CO3H+SEED_1=PART458+SEED_1'],
            ['KON459', 'C730OH+SEED_1=PART459+SEED_1'],
            ['KON460', 'CONM2CO2H+SEED_1=PART460+SEED_1'],
            ['KON461', 'C517NO3+SEED_1=PART461+SEED_1'],
            ['KON462', 'C533OOH+SEED_1=PART462+SEED_1'],
            ['KON463', 'C625OOH+SEED_1=PART463+SEED_1'],
            ['KON464', 'C623OOH+SEED_1=PART464+SEED_1'],
            ['KON465', 'HPC52OOH+SEED_1=PART465+SEED_1'],
            ['KON466', 'C527OOH+SEED_1=PART466+SEED_1'],
            ['KON467', 'LIMBCO+SEED_1=PART467+SEED_1'],
            ['KON468', 'LMKBCO+SEED_1=PART468+SEED_1'],
            ['KON469', 'C924CO+SEED_1=PART469+SEED_1'],
            ['KON470', 'C818CO+SEED_1=PART470+SEED_1'],
            ['KON471', 'C729CO3H+SEED_1=PART471+SEED_1'],
            ['KON472', 'LMKAOH+SEED_1=PART472+SEED_1'],
            ['KON473', 'C923OOH+SEED_1=PART473+SEED_1'],
            ['KON474', 'C729NO3+SEED_1=PART474+SEED_1'],
            ['KON475', 'CO25C6CO3H+SEED_1=PART475+SEED_1'],
            ['KON476', 'C821OOH+SEED_1=PART476+SEED_1'],
            ['KON477', 'C735OOH+SEED_1=PART477+SEED_1'],
            ['KON478', 'C734CO+SEED_1=PART478+SEED_1'],
            ['KON479', 'C626CO3H+SEED_1=PART479+SEED_1'],
            ['KON480', 'C824OOH+SEED_1=PART480+SEED_1'],
            ['KON481', 'C818OH+SEED_1=PART481+SEED_1'],
            ['KON482', 'C817OOH+SEED_1=PART482+SEED_1'],
            ['KON483', 'MC3CODBPAN+SEED_1=PART483+SEED_1'],
            ['KON484', 'C3MCODBPAN+SEED_1=PART484+SEED_1'],
            ['KON485', 'C626NO3+SEED_1=PART485+SEED_1'],
            ['KON486', 'C734OH+SEED_1=PART486+SEED_1'],
            ['KON487', 'C733OOH+SEED_1=PART487+SEED_1'],
            ['KON488', 'C732OOH+SEED_1=PART488+SEED_1'],
            ['KON489', 'INCGLYOX+SEED_1=PART489+SEED_1'],
            ['KON490', 'C5PAN2+SEED_1=PART490+SEED_1'],
            ['KON491', 'C5PAN19+SEED_1=PART491+SEED_1'],
            ['KON492', 'C5PAN17+SEED_1=PART492+SEED_1'],
            ['KON493', 'C4M2ALOHNO3+SEED_1=PART493+SEED_1'],
            ['KON494', 'C47CHO+SEED_1=PART494+SEED_1'],
            ['KON495', 'C730OOH+SEED_1=PART495+SEED_1'],
            ['KON496', 'INDHCHO+SEED_1=PART496+SEED_1'],
            ['KON497', 'INCCO+SEED_1=PART497+SEED_1'],
            ['KON498', 'C58NO3+SEED_1=PART498+SEED_1'],
            ['KON499', 'C58ANO3+SEED_1=PART499+SEED_1'],
            ['KON500', 'C57NO3+SEED_1=PART500+SEED_1'],
            ['KON501', 'C535OOH+SEED_1=PART501+SEED_1'],
            ['KON502', 'C534OOH+SEED_1=PART502+SEED_1'],
            ['KON503', 'INDOH+SEED_1=PART503+SEED_1'],
            ['KON504', 'INCOH+SEED_1=PART504+SEED_1'],
            ['KON505', 'C537OOH+SEED_1=PART505+SEED_1'],
            ['KON506', 'LIMALBCO+SEED_1=PART506+SEED_1'],
            ['KON507', 'LMLKBCO+SEED_1=PART507+SEED_1'],
            ['KON508', 'LMLKACO+SEED_1=PART508+SEED_1'],
            ['KON509', 'LMLKBOH+SEED_1=PART509+SEED_1'],
            ['KON510', 'C926OH+SEED_1=PART510+SEED_1'],
            ['KON511', 'C822CO3H+SEED_1=PART511+SEED_1'],
            ['KON512', 'C816CO3H+SEED_1=PART512+SEED_1'],
            ['KON513', 'C822NO3+SEED_1=PART513+SEED_1'],
            ['KON514', 'C731CO3H+SEED_1=PART514+SEED_1'],
            ['KON515', 'C727CO3H+SEED_1=PART515+SEED_1'],
            ['KON516', 'LMKBOOH+SEED_1=PART516+SEED_1'],
            ['KON517', 'C731NO3+SEED_1=PART517+SEED_1'],
            ['KON518', 'C825OOH+SEED_1=PART518+SEED_1'],
            ['KON519', 'C819OOH+SEED_1=PART519+SEED_1'],
            ['KON520', 'C518PAN+SEED_1=PART520+SEED_1'],
            ['KON521', 'C734OOH+SEED_1=PART521+SEED_1'],
            ['KON522', 'NPXYFUOOH+SEED_1=PART522+SEED_1'],
            ['KON523', 'MMALNBCO2H+SEED_1=PART523+SEED_1'],
            ['KON524', 'MMALNACO2H+SEED_1=PART524+SEED_1'],
            ['KON525', 'IECPAN+SEED_1=PART525+SEED_1'],
            ['KON526', 'HMVKBPAN+SEED_1=PART526+SEED_1'],
            ['KON527', 'NC623OH+SEED_1=PART527+SEED_1'],
            ['KON528', 'C623NO3+SEED_1=PART528+SEED_1'],
            ['KON529', 'INDHPCHO+SEED_1=PART529+SEED_1'],
            ['KON530', 'C58NO3CO2H+SEED_1=PART530+SEED_1'],
            ['KON531', 'C57NO3CO2H+SEED_1=PART531+SEED_1'],
            ['KON532', 'C527NO3+SEED_1=PART532+SEED_1'],
            ['KON533', 'INDOOH+SEED_1=PART533+SEED_1'],
            ['KON534', 'INCOOH+SEED_1=PART534+SEED_1'],
            ['KON535', 'HPC52CO3H+SEED_1=PART535+SEED_1'],
            ['KON536', 'C923CO3H+SEED_1=PART536+SEED_1'],
            ['KON537', 'C923NO3+SEED_1=PART537+SEED_1'],
            ['KON538', 'LMLKBOOH+SEED_1=PART538+SEED_1'],
            ['KON539', 'LMLKAOOH+SEED_1=PART539+SEED_1'],
            ['KON540', 'C926OOH+SEED_1=PART540+SEED_1'],
            ['KON541', 'C823CO3H+SEED_1=PART541+SEED_1'],
            ['KON542', 'C817CO3H+SEED_1=PART542+SEED_1'],
            ['KON543', 'C823NO3+SEED_1=PART543+SEED_1'],
            ['KON544', 'C817NO3+SEED_1=PART544+SEED_1'],
            ['KON545', 'C820OOH+SEED_1=PART545+SEED_1'],
            ['KON546', 'C732CO3H+SEED_1=PART546+SEED_1'],
            ['KON547', 'C511PAN+SEED_1=PART547+SEED_1'],
            ['KON548', 'C732NO3+SEED_1=PART548+SEED_1'],
            ['KON549', 'C624PAN+SEED_1=PART549+SEED_1'],
            ['KON550', 'C622PAN+SEED_1=PART550+SEED_1'],
            ['KON551', 'C23O3CPAN+SEED_1=PART551+SEED_1'],
            ['KON552', 'C519PAN+SEED_1=PART552+SEED_1'],
            ['KON553', 'C517PAN+SEED_1=PART553+SEED_1'],
            ['KON554', 'NC730OH+SEED_1=PART554+SEED_1'],
            ['KON555', 'NC728OH+SEED_1=PART555+SEED_1'],
            ['KON556', 'C730NO3+SEED_1=PART556+SEED_1'],
            ['KON557', 'C728NO3+SEED_1=PART557+SEED_1'],
            ['KON558', 'MMALNBCO3H+SEED_1=PART558+SEED_1'],
            ['KON559', 'MMALNACO3H+SEED_1=PART559+SEED_1'],
            ['KON560', 'C47CO3H+SEED_1=PART560+SEED_1'],
            ['KON561', 'NC623OOH+SEED_1=PART561+SEED_1'],
            ['KON562', 'INDHCO3H+SEED_1=PART562+SEED_1'],
            ['KON563', 'C58NO3CO3H+SEED_1=PART563+SEED_1'],
            ['KON564', 'C57NO3CO3H+SEED_1=PART564+SEED_1'],
            ['KON565', 'C729PAN+SEED_1=PART565+SEED_1'],
            ['KON566', 'LMKBNO3+SEED_1=PART566+SEED_1'],
            ['KON567', 'C627PAN+SEED_1=PART567+SEED_1'],
            ['KON568', 'C626PAN+SEED_1=PART568+SEED_1'],
            ['KON569', 'NC826OH+SEED_1=PART569+SEED_1'],
            ['KON570', 'C826NO3+SEED_1=PART570+SEED_1'],
            ['KON571', 'NC730OOH+SEED_1=PART571+SEED_1'],
            ['KON572', 'NC728OOH+SEED_1=PART572+SEED_1'],
            ['KON573', 'CONM2PAN+SEED_1=PART573+SEED_1'],
            ['KON574', 'CO2N3PAN+SEED_1=PART574+SEED_1'],
            ['KON575', 'INCNCHO+SEED_1=PART575+SEED_1'],
            ['KON576', 'INB1NBCHO+SEED_1=PART576+SEED_1'],
            ['KON577', 'INB1NACHO+SEED_1=PART577+SEED_1'],
            ['KON578', 'MACRNPAN+SEED_1=PART578+SEED_1'],
            ['KON579', 'MACRNBPAN+SEED_1=PART579+SEED_1'],
            ['KON580', 'INCNO3+SEED_1=PART580+SEED_1'],
            ['KON581', 'INB1NO3+SEED_1=PART581+SEED_1'],
            ['KON582', 'INDHPCO3H+SEED_1=PART582+SEED_1'],
            ['KON583', 'C822PAN+SEED_1=PART583+SEED_1'],
            ['KON584', 'C816PAN+SEED_1=PART584+SEED_1'],
            ['KON585', 'NLIMOOH+SEED_1=PART585+SEED_1'],
            ['KON586', 'C731PAN+SEED_1=PART586+SEED_1'],
            ['KON587', 'C727PAN+SEED_1=PART587+SEED_1'],
            ['KON588', 'NLMKAOOH+SEED_1=PART588+SEED_1'],
            ['KON589', 'NC826OOH+SEED_1=PART589+SEED_1'],
            ['KON590', 'INCNCO2H+SEED_1=PART590+SEED_1'],
            ['KON591', 'INB1NBCO2H+SEED_1=PART591+SEED_1'],
            ['KON592', 'INB1NACO2H+SEED_1=PART592+SEED_1'],
            ['KON593', 'HPC52PAN+SEED_1=PART593+SEED_1'],
            ['KON594', 'C823PAN+SEED_1=PART594+SEED_1'],
            ['KON595', 'NLIMALOH+SEED_1=PART595+SEED_1'],
            ['KON596', 'LIMALNO3+SEED_1=PART596+SEED_1'],
            ['KON597', 'MMALNBPAN+SEED_1=PART597+SEED_1'],
            ['KON598', 'MMALNAPAN+SEED_1=PART598+SEED_1'],
            ['KON599', 'C47PAN+SEED_1=PART599+SEED_1'],
            ['KON600', 'INDHPAN+SEED_1=PART600+SEED_1'],
            ['KON601', 'INCNCO3H+SEED_1=PART601+SEED_1'],
            ['KON602', 'INB1NBCO3H+SEED_1=PART602+SEED_1'],
            ['KON603', 'INB1NACO3H+SEED_1=PART603+SEED_1'],
            ['KON604', 'C58NO3PAN+SEED_1=PART604+SEED_1'],
            ['KON605', 'C57NO3PAN+SEED_1=PART605+SEED_1'],
            ['KON606', 'NLIMALOOH+SEED_1=PART606+SEED_1'],
            ['KON607', 'INDHPPAN+SEED_1=PART607+SEED_1'],
            ['KON608', 'INCNPAN+SEED_1=PART608+SEED_1'],
            ['KON609', 'INB1NBPAN+SEED_1=PART609+SEED_1'],
            ['KON610', 'INB1NAPAN+SEED_1=PART610+SEED_1'],
            ['KON1', 'LIMONONIC+TSP=PART1'],
            ['KON2A', 'LIMANO3+TSP=PART2A'],
            ['KON2B', 'LIMBNO3+TSP=PART2B'],
            ['KON3', 'LIMCNO3+TSP=PART3'],
            ['KON4', 'C923PAN+TSP=PART4'],
            ['KON5', 'C817PAN+TSP=PART5'],
            ['KON6', 'LMKANO3+TSP=PART6'],
            ['KON11', 'LIMONIC+TSP=PART11'],
            ['KON13', 'KLIMONONIC+TSP=PART13'],
            ['KON14', 'LIMAL+TSP=PART14'],
            ['KON15', 'LMLKET+TSP=PART15'],
            ['KON16', 'LIMALBOH+TSP=PART16'],
            ['KON17', 'LIMALACO+TSP=PART17'],
            ['KON22', 'C732PAN+TSP=PART22'],
            ['KON23', 'KLIMONIC+TSP=PART23'],
            ['KON24', 'C731CO2H+TSP=PART24'],
            ['KON25', 'C822CO2H+TSP=PART25'],
            ['KON26', 'LIMALOOH+TSP=PART26'],
            ['KON27', 'LIMCOOH+TSP=PART27'],
            ['KON28', 'C825OH+TSP=PART28'],
            ['KON29', 'LIMAOOH+TSP=PART29'],
            ['KON30', 'C826OOH+TSP=PART30'],
            ['KON31', 'C825CO+TSP=PART31'],
            ['KON32', 'LIMALOH+TSP=PART32'],
            ['KON33', 'C728OOH+TSP=PART33'],
            ['KON34', 'LIMALBOOH+TSP=PART34'],
            ['KON35', 'LIMALAOOH+TSP=PART35'],
            ['KON36', 'C924OOH+TSP=PART36'],
            ['KON37', 'C818OOH+TSP=PART37'],
            ['KON38', 'LMKAOOH+TSP=PART38'],
            ['KON39', 'NORLIMOOH+TSP=PART39'],
            ['KON40', 'LIMCOH+TSP=PART40'],
            ['KON41', 'C924OH+TSP=PART41'],
            ['KON42', 'LIMALAOH+TSP=PART42'],
            ['KON43', 'C925OOH+TSP=PART43'],
            ['KON44', 'LIMAOH+TSP=PART44'],
            ['KON45', 'C826OH+TSP=PART45'],
            ['KON46', 'C728OH+TSP=PART46'],
            ['KON47', 'C823OOH+TSP=PART47'],
            ['KON48', 'LIMBOOH+TSP=PART48'],
            ['KON49', 'LMLKAOH+TSP=PART49'],
            ['KON50', 'C922OOH+TSP=PART50'],
            ['KON51', 'C813OOH+TSP=PART51'],
            ['KON52', 'C516OOH+TSP=PART52'],
            ['KON53', 'C621OOH+TSP=PART53'],
            ['KON54', 'C813NO3+TSP=PART54'],
            ['KON55', 'C921OOH+TSP=PART55'],
            ['KON56', 'C812OOH+TSP=PART56'],
            ['KON57', 'C813OH+TSP=PART57'],
            ['KON58', 'NC72OOH+TSP=PART58'],
            ['KON59', 'NC61CO3H+TSP=PART59'],
            ['KON60', 'NC102OOH+TSP=PART60'],
            ['KON61', 'C719OOH+TSP=PART61'],
            ['KON62', 'C98OOH+TSP=PART62'],
            ['KON63', 'NC6PAN1+TSP=PART63'],
            ['KON64', 'HOPINONIC+TSP=PART64'],
            ['KON65', 'C812OH+TSP=PART65'],
            ['KON66', 'H3C25CCO2H+TSP=PART66'],
            ['KON67', 'C722OOH+TSP=PART67'],
            ['KON68', 'NC71OOH+TSP=PART68'],
            ['KON69', 'NC101OOH+TSP=PART69'],
            ['KON70', 'C719NO3+TSP=PART70'],
            ['KON71', 'C920CO3H+TSP=PART71'],
            ['KON72', 'PINIC+TSP=PART72'],
            ['KON73', 'C106OOH+TSP=PART73'],
            ['KON74', 'C108OOH+TSP=PART74'],
            ['KON75', 'H3C25CCO3H+TSP=PART75'],
            ['KON76', 'C98NO3+TSP=PART76'],
            ['KON77', 'C614OOH+TSP=PART77'],
            ['KON78', 'C920OOH+TSP=PART78'],
            ['KON79', 'H3C25C6OOH+TSP=PART79'],
            ['KON80', 'C811OOH+TSP=PART80'],
            ['KON81', 'C44OOH+TSP=PART81'],
            ['KON82', 'C719OH+TSP=PART82'],
            ['KON83', 'H3C25C6PAN+TSP=PART83'],
            ['KON84', 'C97OOH+TSP=PART84'],
            ['KON85', 'NORPINIC+TSP=PART85'],
            ['KON86', 'H1C23C4OOH+TSP=PART86'],
            ['KON87', 'C920PAN+TSP=PART87'],
            ['KON88', 'C98OH+TSP=PART88'],
            ['KON89', 'C811CO3H+TSP=PART89'],
            ['KON90', 'HC23C4CO3H+TSP=PART90'],
            ['KON91', 'C106NO3+TSP=PART91'],
            ['KON92', 'C108NO3+TSP=PART92'],
            ['KON93', 'C811PAN+TSP=PART93'],
            ['KON94', 'C716OOH+TSP=PART94'],
            ['KON95', 'C717OOH+TSP=PART95'],
            ['KON96', 'NAPINAOOH+TSP=PART96'],
            ['KON97', 'NAPINBOOH+TSP=PART97'],
            ['KON98', 'C721OOH+TSP=PART98'],
            ['KON99', 'C109OOH+TSP=PART99'],
            ['KON100', 'C614NO3+TSP=PART100'],
            ['KON101', 'H1C23C4PAN+TSP=PART101'],
            ['KON102', 'C721CO3H+TSP=PART102'],
            ['KON103', 'C235C6CO3H+TSP=PART103'],
            ['KON104', 'APINCOOH+TSP=PART104'],
            ['KON105', 'C811NO3+TSP=PART105'],
            ['KON106', 'APINAOOH+TSP=PART106'],
            ['KON107', 'C7PAN3+TSP=PART107'],
            ['KON108', 'C107OOH+TSP=PART108'],
            ['KON109', 'PINALOOH+TSP=PART109'],
            ['KON110', 'C106OH+TSP=PART110'],
            ['KON111', 'C108OH+TSP=PART111'],
            ['KON112', 'C811OH+TSP=PART112'],
            ['KON113', 'C614OH+TSP=PART113'],
            ['KON114', 'H3C25C6OH+TSP=PART114'],
            ['KON115', 'C721PAN+TSP=PART115'],
            ['KON116', 'C810OOH+TSP=PART116'],
            ['KON117', 'CO235C6OOH+TSP=PART117'],
            ['KON118', 'APINBOOH+TSP=PART118'],
            ['KON119', 'H3C2C4CO2H+TSP=PART119'],
            ['KON120', 'C717NO3+TSP=PART120'],
            ['KON121', 'NC71CO+TSP=PART121'],
            ['KON122', 'C97OH+TSP=PART122'],
            ['KON123', 'PINONIC+TSP=PART123'],
            ['KON124', 'APINCNO3+TSP=PART124'],
            ['KON125', 'C86OOH+TSP=PART125'],
            ['KON126', 'PINALNO3+TSP=PART126'],
            ['KON127', 'C109OH+TSP=PART127'],
            ['KON128', 'C810NO3+TSP=PART128'],
            ['KON129', 'APINANO3+TSP=PART129'],
            ['KON130', 'C720OOH+TSP=PART130'],
            ['KON131', 'H3C2C4CO3H+TSP=PART131'],
            ['KON132', 'C89CO2H+TSP=PART132'],
            ['KON133', 'C716OH+TSP=PART133'],
            ['KON134', 'C717OH+TSP=PART134'],
            ['KON135', 'APINBNO3+TSP=PART135'],
            ['KON136', 'C514OOH+TSP=PART136'],
            ['KON137', 'PERPINONIC+TSP=PART137'],
            ['KON138', 'C10PAN2+TSP=PART138'],
            ['KON139', 'C614CO+TSP=PART139'],
            ['KON140', 'APINCOH+TSP=PART140'],
            ['KON141', 'H3C2C4PAN+TSP=PART141'],
            ['KON142', 'C107OH+TSP=PART142'],
            ['KON143', 'PINALOH+TSP=PART143'],
            ['KON144', 'APINBOH+TSP=PART144'],
            ['KON145', 'C721CHO+TSP=PART145'],
            ['KON146', 'C89CO3H+TSP=PART146'],
            ['KON147', 'C96OOH+TSP=PART147'],
            ['KON148', 'CO2H3CO3H+TSP=PART148'],
            ['KON149', 'H3C25C5CHO+TSP=PART149'],
            ['KON150', 'NC101CO+TSP=PART150'],
            ['KON151', 'C810OH+TSP=PART151'],
            ['KON152', 'H1C23C4CHO+TSP=PART152'],
            ['KON153', 'C85CO3H+TSP=PART153'],
            ['KON154', 'C514NO3+TSP=PART154'],
            ['KON155', 'C109CO+TSP=PART155'],
            ['KON156', 'C9PAN2+TSP=PART156'],
            ['KON157', 'CO13C3CO2H+TSP=PART157'],
            ['KON158', 'CHOC3COOOH+TSP=PART158'],
            ['KON159', 'C720NO3+TSP=PART159'],
            ['KON160', 'C511OOH+TSP=PART160'],
            ['KON161', 'C4PAN6+TSP=PART161'],
            ['KON162', 'H1CO23CHO+TSP=PART162'],
            ['KON163', 'C89PAN+TSP=PART163'],
            ['KON164', 'C89OOH+TSP=PART164'],
            ['KON165', 'C5PAN9+TSP=PART165'],
            ['KON166', 'C96NO3+TSP=PART166'],
            ['KON167', 'CO235C6CHO+TSP=PART167'],
            ['KON168', 'CHOC3COPAN+TSP=PART168'],
            ['KON169', 'CO23C4CO3H+TSP=PART169'],
            ['KON170', 'C720OH+TSP=PART170'],
            ['KON171', 'C85OOH+TSP=PART171'],
            ['KON172', 'APINBCO+TSP=PART172'],
            ['KON173', 'C312COCO3H+TSP=PART173'],
            ['KON174', 'C514OH+TSP=PART174'],
            ['KON175', 'C96OH+TSP=PART175'],
            ['KON176', 'C312COPAN+TSP=PART176'],
            ['KON177', 'CO235C5CHO+TSP=PART177'],
            ['KON178', 'C89NO3+TSP=PART178'],
            ['KON179', 'PINAL+TSP=PART179'],
            ['KON180', 'HCC7CO+TSP=PART180'],
            ['KON181', 'C89OH+TSP=PART181'],
            ['KON182', 'CO13C4CHO+TSP=PART182'],
            ['KON183', 'NORPINAL+TSP=PART183'],
            ['KON184', 'CO2H3CHO+TSP=PART184'],
            ['KON185', 'C4CODIAL+TSP=PART185'],
            ['KON186', 'CO23C4CHO+TSP=PART186'],
            ['KON200', 'BPINANO3+TSP=PART200'],
            ['KON201', 'BPINAOH+TSP=PART201'],
            ['KON202', 'BPINAOOH+TSP=PART202'],
            ['KON203', 'BPINBNO3+TSP=PART203'],
            ['KON204', 'BPINBOOH+TSP=PART204'],
            ['KON205', 'BPINCNO3+TSP=PART205'],
            ['KON206', 'BPINCOH+TSP=PART206'],
            ['KON207', 'BPINCOOH+TSP=PART207'],
            ['KON209', 'C512CO2H+TSP=PART209'],
            ['KON210', 'C512CO3H+TSP=PART210'],
            ['KON211', 'C512NO3+TSP=PART211'],
            ['KON212', 'C512OH+TSP=PART212'],
            ['KON213', 'C512OOH+TSP=PART213'],
            ['KON214', 'C512PAN+TSP=PART214'],
            ['KON215', 'C513CO+TSP=PART215'],
            ['KON216', 'C513OH+TSP=PART216'],
            ['KON217', 'C513OOH+TSP=PART217'],
            ['KON218', 'C515CHO+TSP=PART218'],
            ['KON219', 'C515CO+TSP=PART219'],
            ['KON220', 'C515CO3H+TSP=PART220'],
            ['KON221', 'C515OOH+TSP=PART221'],
            ['KON222', 'C515PAN+TSP=PART222'],
            ['KON223', 'C55OOH+TSP=PART223'],
            ['KON224', 'C5PAN11+TSP=PART224'],
            ['KON225', 'C615CO+TSP=PART225'],
            ['KON226', 'C615CO2H+TSP=PART226'],
            ['KON227', 'C615CO3H+TSP=PART227'],
            ['KON228', 'C615OH+TSP=PART228'],
            ['KON229', 'C615OOH+TSP=PART229'],
            ['KON230', 'C615PAN+TSP=PART230'],
            ['KON231', 'C616OH+TSP=PART231'],
            ['KON232', 'C616OOH+TSP=PART232'],
            ['KON233', 'C617CHO+TSP=PART233'],
            ['KON234', 'C617CO2H+TSP=PART234'],
            ['KON235', 'C617CO3H+TSP=PART235'],
            ['KON236', 'C617OH+TSP=PART236'],
            ['KON237', 'C617OOH+TSP=PART237'],
            ['KON238', 'C617PAN+TSP=PART238'],
            ['KON239', 'C618CO2H+TSP=PART239'],
            ['KON240', 'C618CO3H+TSP=PART240'],
            ['KON241', 'C618OOH+TSP=PART241'],
            ['KON242', 'C618PAN+TSP=PART242'],
            ['KON243', 'C619CO+TSP=PART243'],
            ['KON244', 'C619OH+TSP=PART244'],
            ['KON245', 'C619OOH+TSP=PART245'],
            ['KON246', 'C620OH+TSP=PART246'],
            ['KON247', 'C620OOH+TSP=PART247'],
            ['KON248', 'C67CHO+TSP=PART248'],
            ['KON249', 'C67CO3H+TSP=PART249'],
            ['KON250', 'C6PAN9+TSP=PART250'],
            ['KON251', 'C718CO2H+TSP=PART251'],
            ['KON252', 'C718CO3H+TSP=PART252'],
            ['KON253', 'C718NO3+TSP=PART253'],
            ['KON254', 'C718OH+TSP=PART254'],
            ['KON255', 'C718OOH+TSP=PART255'],
            ['KON256', 'C718PAN+TSP=PART256'],
            ['KON257', 'C87CO+TSP=PART257'],
            ['KON258', 'C87CO2H+TSP=PART258'],
            ['KON259', 'C87CO3H+TSP=PART259'],
            ['KON260', 'C87OH+TSP=PART260'],
            ['KON261', 'C87OOH+TSP=PART261'],
            ['KON262', 'C87PAN+TSP=PART262'],
            ['KON263', 'C88CHO+TSP=PART263'],
            ['KON264', 'C88CO+TSP=PART264'],
            ['KON265', 'C88CO2H+TSP=PART265'],
            ['KON266', 'C88CO3H+TSP=PART266'],
            ['KON267', 'C88OH+TSP=PART267'],
            ['KON268', 'C88OOH+TSP=PART268'],
            ['KON269', 'C88PAN+TSP=PART269'],
            ['KON270', 'C8BC+TSP=PART270'],
            ['KON271', 'C8BCCO+TSP=PART271'],
            ['KON272', 'C8BCNO3+TSP=PART272'],
            ['KON273', 'C8BCOH+TSP=PART273'],
            ['KON274', 'C8BCOOH+TSP=PART274'],
            ['KON275', 'C914CO+TSP=PART275'],
            ['KON276', 'C914OH+TSP=PART276'],
            ['KON277', 'C914OOH+TSP=PART277'],
            ['KON278', 'C915NO3+TSP=PART278'],
            ['KON279', 'C915OH+TSP=PART279'],
            ['KON280', 'C915OOH+TSP=PART280'],
            ['KON281', 'C916NO3+TSP=PART281'],
            ['KON282', 'C916OH+TSP=PART282'],
            ['KON283', 'C916OOH+TSP=PART283'],
            ['KON284', 'C917NO3+TSP=PART284'],
            ['KON285', 'C917OH+TSP=PART285'],
            ['KON286', 'C917OOH+TSP=PART286'],
            ['KON287', 'C918CHO+TSP=PART287'],
            ['KON288', 'C918CO3H+TSP=PART288'],
            ['KON289', 'C918NO3+TSP=PART289'],
            ['KON290', 'C918OH+TSP=PART290'],
            ['KON291', 'C918OOH+TSP=PART291'],
            ['KON292', 'C918PAN+TSP=PART292'],
            ['KON293', 'C919NO3+TSP=PART293'],
            ['KON294', 'C919OH+TSP=PART294'],
            ['KON295', 'C919OOH+TSP=PART295'],
            ['KON296', 'C9DC+TSP=PART296'],
            ['KON297', 'C9DCCO+TSP=PART297'],
            ['KON298', 'C9DCNO3+TSP=PART298'],
            ['KON299', 'C9DCOH+TSP=PART299'],
            ['KON300', 'C9DCOOH+TSP=PART300'],
            ['KON301', 'CO123C5CHO+TSP=PART301'],
            ['KON302', 'CO12C4CHO+TSP=PART302'],
            ['KON303', 'CO1M22CHO+TSP=PART303'],
            ['KON304', 'CO1M22CO2H+TSP=PART304'],
            ['KON305', 'CO1M22CO3H+TSP=PART305'],
            ['KON306', 'CO1M22PAN+TSP=PART306'],
            ['KON307', 'H2M2C3CO3H+TSP=PART307'],
            ['KON308', 'MIBKHO4CHO+TSP=PART308'],
            ['KON309', 'NBPINAOOH+TSP=PART309'],
            ['KON310', 'NBPINBOOH+TSP=PART310'],
            ['KON311', 'NC91CHO+TSP=PART311'],
            ['KON312', 'NC91CO3H+TSP=PART312'],
            ['KON313', 'NC91PAN+TSP=PART313'],
            ['KON314', 'NOPINANO3+TSP=PART314'],
            ['KON315', 'NOPINAOH+TSP=PART315'],
            ['KON316', 'NOPINAOOH+TSP=PART316'],
            ['KON317', 'NOPINBCO+TSP=PART317'],
            ['KON318', 'NOPINBNO3+TSP=PART318'],
            ['KON319', 'NOPINBOH+TSP=PART319'],
            ['KON320', 'NOPINBOOH+TSP=PART320'],
            ['KON321', 'NOPINCNO3+TSP=PART321'],
            ['KON322', 'NOPINCOH+TSP=PART322'],
            ['KON323', 'NOPINCOOH+TSP=PART323'],
            ['KON324', 'NOPINDCO+TSP=PART324'],
            ['KON325', 'NOPINDOH+TSP=PART325'],
            ['KON326', 'NOPINDOOH+TSP=PART326'],
            ['KON327', 'NOPINONE+TSP=PART327'],
            ['KON350', 'M3F+TSP=PART350'],
            ['KON351', 'ISOPDOH+TSP=PART351'],
            ['KON352', 'ISOPAOH+TSP=PART352'],
            ['KON353', 'MMALANHY+TSP=PART353'],
            ['KON354', 'MC3ODBCO2H+TSP=PART354'],
            ['KON355', 'C532CO+TSP=PART355'],
            ['KON356', 'C624CO+TSP=PART356'],
            ['KON357', 'C518CHO+TSP=PART357'],
            ['KON358', 'IEB1CHO+TSP=PART358'],
            ['KON359', 'HO1CO34C5+TSP=PART359'],
            ['KON360', 'HMVKBCHO+TSP=PART360'],
            ['KON361', 'HC4CCO2H+TSP=PART361'],
            ['KON362', 'HC4ACO2H+TSP=PART362'],
            ['KON363', 'CO2C4CO2H+TSP=PART363'],
            ['KON364', 'C5HPALD2+TSP=PART364'],
            ['KON365', 'C624OH+TSP=PART365'],
            ['KON366', 'C622OH+TSP=PART366'],
            ['KON367', 'ISOPDOOH+TSP=PART367'],
            ['KON368', 'ISOPCOOH+TSP=PART368'],
            ['KON369', 'IEPOXC+TSP=PART369'],
            ['KON370', 'IEPOXB+TSP=PART370'],
            ['KON371', 'HO13CO4C5+TSP=PART371'],
            ['KON372', 'C517OH+TSP=PART372'],
            ['KON373', 'C531CO+TSP=PART373'],
            ['KON374', 'CO2C4GLYOX+TSP=PART374'],
            ['KON375', 'C511CHO+TSP=PART375'],
            ['KON376', 'C624CHO+TSP=PART376'],
            ['KON377', 'C622CHO+TSP=PART377'],
            ['KON378', 'C5PACALD2+TSP=PART378'],
            ['KON379', 'C5PACALD1+TSP=PART379'],
            ['KON380', 'C23O3CCHO+TSP=PART380'],
            ['KON381', 'C627OH+TSP=PART381'],
            ['KON382', 'C519CHO+TSP=PART382'],
            ['KON383', 'C518CO2H+TSP=PART383'],
            ['KON384', 'C517CHO+TSP=PART384'],
            ['KON385', 'PXYFUOH+TSP=PART385'],
            ['KON386', 'HMVKBCO2H+TSP=PART386'],
            ['KON387', 'HC4CCO3H+TSP=PART387'],
            ['KON388', 'HC4ACO3H+TSP=PART388'],
            ['KON389', 'CO2C4CO3H+TSP=PART389'],
            ['KON390', 'C520OH+TSP=PART390'],
            ['KON391', 'C4M2AL2OH+TSP=PART391'],
            ['KON392', 'C624OOH+TSP=PART392'],
            ['KON393', 'C622OOH+TSP=PART393'],
            ['KON394', 'C58OH+TSP=PART394'],
            ['KON395', 'C57OH+TSP=PART395'],
            ['KON396', 'C519OOH+TSP=PART396'],
            ['KON397', 'C517OOH+TSP=PART397'],
            ['KON398', 'LIMKET+TSP=PART398'],
            ['KON399', 'C816CO+TSP=PART399'],
            ['KON400', 'C729CHO+TSP=PART400'],
            ['KON401', 'CO25C6CHO+TSP=PART401'],
            ['KON402', 'C727CO+TSP=PART402'],
            ['KON403', 'C626CHO+TSP=PART403'],
            ['KON404', 'C822OH+TSP=PART404'],
            ['KON405', 'C731OH+TSP=PART405'],
            ['KON406', 'C729OOH+TSP=PART406'],
            ['KON407', 'C624CO2H+TSP=PART407'],
            ['KON408', 'C622CO2H+TSP=PART408'],
            ['KON409', 'MMALNHY2OH+TSP=PART409'],
            ['KON410', 'C531OOH+TSP=PART410'],
            ['KON411', 'C23O3CCO2H+TSP=PART411'],
            ['KON412', 'C629OH+TSP=PART412'],
            ['KON413', 'C628OH+TSP=PART413'],
            ['KON414', 'C627OOH+TSP=PART414'],
            ['KON415', 'C626OOH+TSP=PART415'],
            ['KON416', 'C519CO2H+TSP=PART416'],
            ['KON417', 'C518CO3H+TSP=PART417'],
            ['KON418', 'C517CO2H+TSP=PART418'],
            ['KON419', 'ISOPDNO3+TSP=PART419'],
            ['KON420', 'ISOPCNO3+TSP=PART420'],
            ['KON421', 'PXYFUOOH+TSP=PART421'],
            ['KON422', 'IECCO3H+TSP=PART422'],
            ['KON423', 'IEC2OOH+TSP=PART423'],
            ['KON424', 'HMVKBCO3H+TSP=PART424'],
            ['KON425', 'C520OOH+TSP=PART425'],
            ['KON426', 'C4MALOHOOH+TSP=PART426'],
            ['KON427', 'C625OH+TSP=PART427'],
            ['KON428', 'C623OH+TSP=PART428'],
            ['KON429', 'C59OOH+TSP=PART429'],
            ['KON430', 'C58OOH+TSP=PART430'],
            ['KON431', 'C58AOOH+TSP=PART431'],
            ['KON432', 'C57OOH+TSP=PART432'],
            ['KON433', 'C57AOOH+TSP=PART433'],
            ['KON434', 'NORLIMAL+TSP=PART434'],
            ['KON435', 'C824CO+TSP=PART435'],
            ['KON436', 'C823CO+TSP=PART436'],
            ['KON437', 'C817CO+TSP=PART437'],
            ['KON438', 'C729CO2H+TSP=PART438'],
            ['KON439', 'C923OH+TSP=PART439'],
            ['KON440', 'C823OH+TSP=PART440'],
            ['KON441', 'C822OOH+TSP=PART441'],
            ['KON442', 'C817OH+TSP=PART442'],
            ['KON443', 'C816OOH+TSP=PART443'],
            ['KON444', 'C511CO3H+TSP=PART444'],
            ['KON445', 'C733OH+TSP=PART445'],
            ['KON446', 'C732OH+TSP=PART446'],
            ['KON447', 'C731OOH+TSP=PART447'],
            ['KON448', 'C727OOH+TSP=PART448'],
            ['KON449', 'C624CO3H+TSP=PART449'],
            ['KON450', 'C622CO3H+TSP=PART450'],
            ['KON451', 'C624NO3+TSP=PART451'],
            ['KON452', 'C622NO3+TSP=PART452'],
            ['KON453', 'MMALNHYOOH+TSP=PART453'],
            ['KON454', 'C23O3CCO3H+TSP=PART454'],
            ['KON455', 'C629OOH+TSP=PART455'],
            ['KON456', 'C628OOH+TSP=PART456'],
            ['KON457', 'C519CO3H+TSP=PART457'],
            ['KON458', 'C517CO3H+TSP=PART458'],
            ['KON459', 'C730OH+TSP=PART459'],
            ['KON460', 'CONM2CO2H+TSP=PART460'],
            ['KON461', 'C517NO3+TSP=PART461'],
            ['KON462', 'C533OOH+TSP=PART462'],
            ['KON463', 'C625OOH+TSP=PART463'],
            ['KON464', 'C623OOH+TSP=PART464'],
            ['KON465', 'HPC52OOH+TSP=PART465'],
            ['KON466', 'C527OOH+TSP=PART466'],
            ['KON467', 'LIMBCO+TSP=PART467'],
            ['KON468', 'LMKBCO+TSP=PART468'],
            ['KON469', 'C924CO+TSP=PART469'],
            ['KON470', 'C818CO+TSP=PART470'],
            ['KON471', 'C729CO3H+TSP=PART471'],
            ['KON472', 'LMKAOH+TSP=PART472'],
            ['KON473', 'C923OOH+TSP=PART473'],
            ['KON474', 'C729NO3+TSP=PART474'],
            ['KON475', 'CO25C6CO3H+TSP=PART475'],
            ['KON476', 'C821OOH+TSP=PART476'],
            ['KON477', 'C735OOH+TSP=PART477'],
            ['KON478', 'C734CO+TSP=PART478'],
            ['KON479', 'C626CO3H+TSP=PART479'],
            ['KON480', 'C824OOH+TSP=PART480'],
            ['KON481', 'C818OH+TSP=PART481'],
            ['KON482', 'C817OOH+TSP=PART482'],
            ['KON483', 'MC3CODBPAN+TSP=PART483'],
            ['KON484', 'C3MCODBPAN+TSP=PART484'],
            ['KON485', 'C626NO3+TSP=PART485'],
            ['KON486', 'C734OH+TSP=PART486'],
            ['KON487', 'C733OOH+TSP=PART487'],
            ['KON488', 'C732OOH+TSP=PART488'],
            ['KON489', 'INCGLYOX+TSP=PART489'],
            ['KON490', 'C5PAN2+TSP=PART490'],
            ['KON491', 'C5PAN19+TSP=PART491'],
            ['KON492', 'C5PAN17+TSP=PART492'],
            ['KON493', 'C4M2ALOHNO3+TSP=PART493'],
            ['KON494', 'C47CHO+TSP=PART494'],
            ['KON495', 'C730OOH+TSP=PART495'],
            ['KON496', 'INDHCHO+TSP=PART496'],
            ['KON497', 'INCCO+TSP=PART497'],
            ['KON498', 'C58NO3+TSP=PART498'],
            ['KON499', 'C58ANO3+TSP=PART499'],
            ['KON500', 'C57NO3+TSP=PART500'],
            ['KON501', 'C535OOH+TSP=PART501'],
            ['KON502', 'C534OOH+TSP=PART502'],
            ['KON503', 'INDOH+TSP=PART503'],
            ['KON504', 'INCOH+TSP=PART504'],
            ['KON505', 'C537OOH+TSP=PART505'],
            ['KON506', 'LIMALBCO+TSP=PART506'],
            ['KON507', 'LMLKBCO+TSP=PART507'],
            ['KON508', 'LMLKACO+TSP=PART508'],
            ['KON509', 'LMLKBOH+TSP=PART509'],
            ['KON510', 'C926OH+TSP=PART510'],
            ['KON511', 'C822CO3H+TSP=PART511'],
            ['KON512', 'C816CO3H+TSP=PART512'],
            ['KON513', 'C822NO3+TSP=PART513'],
            ['KON514', 'C731CO3H+TSP=PART514'],
            ['KON515', 'C727CO3H+TSP=PART515'],
            ['KON516', 'LMKBOOH+TSP=PART516'],
            ['KON517', 'C731NO3+TSP=PART517'],
            ['KON518', 'C825OOH+TSP=PART518'],
            ['KON519', 'C819OOH+TSP=PART519'],
            ['KON520', 'C518PAN+TSP=PART520'],
            ['KON521', 'C734OOH+TSP=PART521'],
            ['KON522', 'NPXYFUOOH+TSP=PART522'],
            ['KON523', 'MMALNBCO2H+TSP=PART523'],
            ['KON524', 'MMALNACO2H+TSP=PART524'],
            ['KON525', 'IECPAN+TSP=PART525'],
            ['KON526', 'HMVKBPAN+TSP=PART526'],
            ['KON527', 'NC623OH+TSP=PART527'],
            ['KON528', 'C623NO3+TSP=PART528'],
            ['KON529', 'INDHPCHO+TSP=PART529'],
            ['KON530', 'C58NO3CO2H+TSP=PART530'],
            ['KON531', 'C57NO3CO2H+TSP=PART531'],
            ['KON532', 'C527NO3+TSP=PART532'],
            ['KON533', 'INDOOH+TSP=PART533'],
            ['KON534', 'INCOOH+TSP=PART534'],
            ['KON535', 'HPC52CO3H+TSP=PART535'],
            ['KON536', 'C923CO3H+TSP=PART536'],
            ['KON537', 'C923NO3+TSP=PART537'],
            ['KON538', 'LMLKBOOH+TSP=PART538'],
            ['KON539', 'LMLKAOOH+TSP=PART539'],
            ['KON540', 'C926OOH+TSP=PART540'],
            ['KON541', 'C823CO3H+TSP=PART541'],
            ['KON542', 'C817CO3H+TSP=PART542'],
            ['KON543', 'C823NO3+TSP=PART543'],
            ['KON544', 'C817NO3+TSP=PART544'],
            ['KON545', 'C820OOH+TSP=PART545'],
            ['KON546', 'C732CO3H+TSP=PART546'],
            ['KON547', 'C511PAN+TSP=PART547'],
            ['KON548', 'C732NO3+TSP=PART548'],
            ['KON549', 'C624PAN+TSP=PART549'],
            ['KON550', 'C622PAN+TSP=PART550'],
            ['KON551', 'C23O3CPAN+TSP=PART551'],
            ['KON552', 'C519PAN+TSP=PART552'],
            ['KON553', 'C517PAN+TSP=PART553'],
            ['KON554', 'NC730OH+TSP=PART554'],
            ['KON555', 'NC728OH+TSP=PART555'],
            ['KON556', 'C730NO3+TSP=PART556'],
            ['KON557', 'C728NO3+TSP=PART557'],
            ['KON558', 'MMALNBCO3H+TSP=PART558'],
            ['KON559', 'MMALNACO3H+TSP=PART559'],
            ['KON560', 'C47CO3H+TSP=PART560'],
            ['KON561', 'NC623OOH+TSP=PART561'],
            ['KON562', 'INDHCO3H+TSP=PART562'],
            ['KON563', 'C58NO3CO3H+TSP=PART563'],
            ['KON564', 'C57NO3CO3H+TSP=PART564'],
            ['KON565', 'C729PAN+TSP=PART565'],
            ['KON566', 'LMKBNO3+TSP=PART566'],
            ['KON567', 'C627PAN+TSP=PART567'],
            ['KON568', 'C626PAN+TSP=PART568'],
            ['KON569', 'NC826OH+TSP=PART569'],
            ['KON570', 'C826NO3+TSP=PART570'],
            ['KON571', 'NC730OOH+TSP=PART571'],
            ['KON572', 'NC728OOH+TSP=PART572'],
            ['KON573', 'CONM2PAN+TSP=PART573'],
            ['KON574', 'CO2N3PAN+TSP=PART574'],
            ['KON575', 'INCNCHO+TSP=PART575'],
            ['KON576', 'INB1NBCHO+TSP=PART576'],
            ['KON577', 'INB1NACHO+TSP=PART577'],
            ['KON578', 'MACRNPAN+TSP=PART578'],
            ['KON579', 'MACRNBPAN+TSP=PART579'],
            ['KON580', 'INCNO3+TSP=PART580'],
            ['KON581', 'INB1NO3+TSP=PART581'],
            ['KON582', 'INDHPCO3H+TSP=PART582'],
            ['KON583', 'C822PAN+TSP=PART583'],
            ['KON584', 'C816PAN+TSP=PART584'],
            ['KON585', 'NLIMOOH+TSP=PART585'],
            ['KON586', 'C731PAN+TSP=PART586'],
            ['KON587', 'C727PAN+TSP=PART587'],
            ['KON588', 'NLMKAOOH+TSP=PART588'],
            ['KON589', 'NC826OOH+TSP=PART589'],
            ['KON590', 'INCNCO2H+TSP=PART590'],
            ['KON591', 'INB1NBCO2H+TSP=PART591'],
            ['KON592', 'INB1NACO2H+TSP=PART592'],
            ['KON593', 'HPC52PAN+TSP=PART593'],
            ['KON594', 'C823PAN+TSP=PART594'],
            ['KON595', 'NLIMALOH+TSP=PART595'],
            ['KON596', 'LIMALNO3+TSP=PART596'],
            ['KON597', 'MMALNBPAN+TSP=PART597'],
            ['KON598', 'MMALNAPAN+TSP=PART598'],
            ['KON599', 'C47PAN+TSP=PART599'],
            ['KON600', 'INDHPAN+TSP=PART600'],
            ['KON601', 'INCNCO3H+TSP=PART601'],
            ['KON602', 'INB1NBCO3H+TSP=PART602'],
            ['KON603', 'INB1NACO3H+TSP=PART603'],
            ['KON604', 'C58NO3PAN+TSP=PART604'],
            ['KON605', 'C57NO3PAN+TSP=PART605'],
            ['KON606', 'NLIMALOOH+TSP=PART606'],
            ['KON607', 'INDHPPAN+TSP=PART607'],
            ['KON608', 'INCNPAN+TSP=PART608'],
            ['KON609', 'INB1NBPAN+TSP=PART609'],
            ['KON610', 'INB1NAPAN+TSP=PART610'],
            ['KOFF1', 'PART1=LIMONONIC'],
            ['KOFF2a', 'PART2A=LIMANO3'],
            ['KOFF2b', 'PART2B=LIMBNO3'],
            ['KOFF3', 'PART3=LIMCNO3'],
            ['KOFF4', 'PART4=C923PAN'],
            ['KOFF5', 'PART5=C817PAN'],
            ['KOFF6', 'PART6=LMKANO3'],
            ['KOFF11', 'PART11=LIMONIC'],
            ['KOFF13', 'PART13=KLIMONONIC'],
            ['KOFF14', 'PART14=LIMAL'],
            ['KOFF15', 'PART15=LMLKET'],
            ['KOFF16', 'PART16=LIMALBOH'],
            ['KOFF17', 'PART17=LIMALACO'],
            ['KOFF22', 'PART22=C732PAN'],
            ['KOFF23', 'PART23=KLIMONIC'],
            ['KOFF24', 'PART24=C731CO2H'],
            ['KOFF25', 'PART25=C822CO2H'],
            ['KOFF26', 'PART26=LIMALOOH'],
            ['KOFF27', 'PART27=LIMCOOH'],
            ['KOFF28', 'PART28=C825OH'],
            ['KOFF29', 'PART29=LIMAOOH'],
            ['KOFF30', 'PART30=C826OOH'],
            ['KOFF31', 'PART31=C825CO'],
            ['KOFF32', 'PART32=LIMALOH'],
            ['KOFF33', 'PART33=C728OOH'],
            ['KOFF34', 'PART34=LIMALBOOH'],
            ['KOFF35', 'PART35=LIMALAOOH'],
            ['KOFF36', 'PART36=C924OOH'],
            ['KOFF37', 'PART37=C818OOH'],
            ['KOFF38', 'PART38=LMKAOOH'],
            ['KOFF39', 'PART39=NORLIMOOH'],
            ['KOFF40', 'PART40=LIMCOH'],
            ['KOFF41', 'PART41=C924OH'],
            ['KOFF42', 'PART42=LIMALAOH'],
            ['KOFF43', 'PART43=C925OOH'],
            ['KOFF44', 'PART44=LIMAOH'],
            ['KOFF45', 'PART45=C826OH'],
            ['KOFF46', 'PART46=C728OH'],
            ['KOFF47', 'PART47=C823OOH'],
            ['KOFF48', 'PART48=LIMBOOH'],
            ['KOFF49', 'PART49=LMLKAOH'],
            ['KOFF50', 'PART50=C922OOH'],
            ['KOFF51', 'PART51=C813OOH'],
            ['KOFF52', 'PART52=C516OOH'],
            ['KOFF53', 'PART53=C621OOH'],
            ['KOFF54', 'PART54=C813NO3'],
            ['KOFF55', 'PART55=C921OOH'],
            ['KOFF56', 'PART56=C812OOH'],
            ['KOFF57', 'PART57=C813OH'],
            ['KOFF58', 'PART58=NC72OOH'],
            ['KOFF59', 'PART59=NC61CO3H'],
            ['KOFF60', 'PART60=NC102OOH'],
            ['KOFF61', 'PART61=C719OOH'],
            ['KOFF62', 'PART62=C98OOH'],
            ['KOFF63', 'PART63=NC6PAN1'],
            ['KOFF64', 'PART64=HOPINONIC'],
            ['KOFF65', 'PART65=C812OH'],
            ['KOFF66', 'PART66=H3C25CCO2H'],
            ['KOFF67', 'PART67=C722OOH'],
            ['KOFF68', 'PART68=NC71OOH'],
            ['KOFF69', 'PART69=NC101OOH'],
            ['KOFF70', 'PART70=C719NO3'],
            ['KOFF71', 'PART71=C920CO3H'],
            ['KOFF72', 'PART72=PINIC'],
            ['KOFF73', 'PART73=C106OOH'],
            ['KOFF74', 'PART74=C108OOH'],
            ['KOFF75', 'PART75=H3C25CCO3H'],
            ['KOFF76', 'PART76=C98NO3'],
            ['KOFF77', 'PART77=C614OOH'],
            ['KOFF78', 'PART78=C920OOH'],
            ['KOFF79', 'PART79=H3C25C6OOH'],
            ['KOFF80', 'PART80=C811OOH'],
            ['KOFF81', 'PART81=C44OOH'],
            ['KOFF82', 'PART82=C719OH'],
            ['KOFF83', 'PART83=H3C25C6PAN'],
            ['KOFF84', 'PART84=C97OOH'],
            ['KOFF85', 'PART85=NORPINIC'],
            ['KOFF86', 'PART86=H1C23C4OOH'],
            ['KOFF87', 'PART87=C920PAN'],
            ['KOFF88', 'PART88=C98OH'],
            ['KOFF89', 'PART89=C811CO3H'],
            ['KOFF90', 'PART90=HC23C4CO3H'],
            ['KOFF91', 'PART91=C106NO3'],
            ['KOFF92', 'PART92=C108NO3'],
            ['KOFF93', 'PART93=C811PAN'],
            ['KOFF94', 'PART94=C716OOH'],
            ['KOFF95', 'PART95=C717OOH'],
            ['KOFF96', 'PART96=NAPINAOOH'],
            ['KOFF97', 'PART97=NAPINBOOH'],
            ['KOFF98', 'PART98=C721OOH'],
            ['KOFF99', 'PART99=C109OOH'],
            ['KOFF100', 'PART100=C614NO3'],
            ['KOFF101', 'PART101=H1C23C4PAN'],
            ['KOFF102', 'PART102=C721CO3H'],
            ['KOFF103', 'PART103=C235C6CO3H'],
            ['KOFF104', 'PART104=APINCOOH'],
            ['KOFF105', 'PART105=C811NO3'],
            ['KOFF106', 'PART106=APINAOOH'],
            ['KOFF107', 'PART107=C7PAN3'],
            ['KOFF108', 'PART108=C107OOH'],
            ['KOFF109', 'PART109=PINALOOH'],
            ['KOFF110', 'PART110=C106OH'],
            ['KOFF111', 'PART111=C108OH'],
            ['KOFF112', 'PART112=C811OH'],
            ['KOFF113', 'PART113=C614OH'],
            ['KOFF114', 'PART114=H3C25C6OH'],
            ['KOFF115', 'PART115=C721PAN'],
            ['KOFF116', 'PART116=C810OOH'],
            ['KOFF117', 'PART117=CO235C6OOH'],
            ['KOFF118', 'PART118=APINBOOH'],
            ['KOFF119', 'PART119=H3C2C4CO2H'],
            ['KOFF120', 'PART120=C717NO3'],
            ['KOFF121', 'PART121=NC71CO'],
            ['KOFF122', 'PART122=C97OH'],
            ['KOFF123', 'PART123=PINONIC'],
            ['KOFF124', 'PART124=APINCNO3'],
            ['KOFF125', 'PART125=C86OOH'],
            ['KOFF126', 'PART126=PINALNO3'],
            ['KOFF127', 'PART127=C109OH'],
            ['KOFF128', 'PART128=C810NO3'],
            ['KOFF129', 'PART129=APINANO3'],
            ['KOFF130', 'PART130=C720OOH'],
            ['KOFF131', 'PART131=H3C2C4CO3H'],
            ['KOFF132', 'PART132=C89CO2H'],
            ['KOFF133', 'PART133=C716OH'],
            ['KOFF134', 'PART134=C717OH'],
            ['KOFF135', 'PART135=APINBNO3'],
            ['KOFF136', 'PART136=C514OOH'],
            ['KOFF137', 'PART137=PERPINONIC'],
            ['KOFF138', 'PART138=C10PAN2'],
            ['KOFF139', 'PART139=C614CO'],
            ['KOFF140', 'PART140=APINCOH'],
            ['KOFF141', 'PART141=H3C2C4PAN'],
            ['KOFF142', 'PART142=C107OH'],
            ['KOFF143', 'PART143=PINALOH'],
            ['KOFF144', 'PART144=APINBOH'],
            ['KOFF145', 'PART145=C721CHO'],
            ['KOFF146', 'PART146=C89CO3H'],
            ['KOFF147', 'PART147=C96OOH'],
            ['KOFF148', 'PART148=CO2H3CO3H'],
            ['KOFF149', 'PART149=H3C25C5CHO'],
            ['KOFF150', 'PART150=NC101CO'],
            ['KOFF151', 'PART151=C810OH'],
            ['KOFF152', 'PART152=H1C23C4CHO'],
            ['KOFF153', 'PART153=C85CO3H'],
            ['KOFF154', 'PART154=C514NO3'],
            ['KOFF155', 'PART155=C109CO'],
            ['KOFF156', 'PART156=C9PAN2'],
            ['KOFF157', 'PART157=CO13C3CO2H'],
            ['KOFF158', 'PART158=CHOC3COOOH'],
            ['KOFF159', 'PART159=C720NO3'],
            ['KOFF160', 'PART160=C511OOH'],
            ['KOFF161', 'PART161=C4PAN6'],
            ['KOFF162', 'PART162=H1CO23CHO'],
            ['KOFF163', 'PART163=C89PAN'],
            ['KOFF164', 'PART164=C89OOH'],
            ['KOFF165', 'PART165=C5PAN9'],
            ['KOFF166', 'PART166=C96NO3'],
            ['KOFF167', 'PART167=CO235C6CHO'],
            ['KOFF168', 'PART168=CHOC3COPAN'],
            ['KOFF169', 'PART169=CO23C4CO3H'],
            ['KOFF170', 'PART170=C720OH'],
            ['KOFF171', 'PART171=C85OOH'],
            ['KOFF172', 'PART172=APINBCO'],
            ['KOFF173', 'PART173=C312COCO3H'],
            ['KOFF174', 'PART174=C514OH'],
            ['KOFF175', 'PART175=C96OH'],
            ['KOFF176', 'PART176=C312COPAN'],
            ['KOFF177', 'PART177=CO235C5CHO'],
            ['KOFF178', 'PART178=C89NO3'],
            ['KOFF179', 'PART179=PINAL'],
            ['KOFF180', 'PART180=HCC7CO'],
            ['KOFF181', 'PART181=C89OH'],
            ['KOFF182', 'PART182=CO13C4CHO'],
            ['KOFF183', 'PART183=NORPINAL'],
            ['KOFF184', 'PART184=CO2H3CHO'],
            ['KOFF185', 'PART185=C4CODIAL'],
            ['KOFF186', 'PART186=CO23C4CHO'],
            ['KOFF200', 'PART200=BPINANO3'],
            ['KOFF201', 'PART201=BPINAOH'],
            ['KOFF202', 'PART202=BPINAOOH'],
            ['KOFF203', 'PART203=BPINBNO3'],
            ['KOFF204', 'PART204=BPINBOOH'],
            ['KOFF205', 'PART205=BPINCNO3'],
            ['KOFF206', 'PART206=BPINCOH'],
            ['KOFF207', 'PART207=BPINCOOH'],
            ['KOFF209', 'PART209=C512CO2H'],
            ['KOFF210', 'PART210=C512CO3H'],
            ['KOFF211', 'PART211=C512NO3'],
            ['KOFF212', 'PART212=C512OH'],
            ['KOFF213', 'PART213=C512OOH'],
            ['KOFF214', 'PART214=C512PAN'],
            ['KOFF215', 'PART215=C513CO'],
            ['KOFF216', 'PART216=C513OH'],
            ['KOFF217', 'PART217=C513OOH'],
            ['KOFF218', 'PART218=C515CHO'],
            ['KOFF219', 'PART219=C515CO'],
            ['KOFF220', 'PART220=C515CO3H'],
            ['KOFF221', 'PART221=C515OOH'],
            ['KOFF222', 'PART222=C515PAN'],
            ['KOFF223', 'PART223=C55OOH'],
            ['KOFF224', 'PART224=C5PAN11'],
            ['KOFF225', 'PART225=C615CO'],
            ['KOFF226', 'PART226=C615CO2H'],
            ['KOFF227', 'PART227=C615CO3H'],
            ['KOFF228', 'PART228=C615OH'],
            ['KOFF229', 'PART229=C615OOH'],
            ['KOFF230', 'PART230=C615PAN'],
            ['KOFF231', 'PART231=C616OH'],
            ['KOFF232', 'PART232=C616OOH'],
            ['KOFF233', 'PART233=C617CHO'],
            ['KOFF234', 'PART234=C617CO2H'],
            ['KOFF235', 'PART235=C617CO3H'],
            ['KOFF236', 'PART236=C617OH'],
            ['KOFF237', 'PART237=C617OOH'],
            ['KOFF238', 'PART238=C617PAN'],
            ['KOFF239', 'PART239=C618CO2H'],
            ['KOFF240', 'PART240=C618CO3H'],
            ['KOFF241', 'PART241=C618OOH'],
            ['KOFF242', 'PART242=C618PAN'],
            ['KOFF243', 'PART243=C619CO'],
            ['KOFF244', 'PART244=C619OH'],
            ['KOFF245', 'PART245=C619OOH'],
            ['KOFF246', 'PART246=C620OH'],
            ['KOFF247', 'PART247=C620OOH'],
            ['KOFF248', 'PART248=C67CHO'],
            ['KOFF249', 'PART249=C67CO3H'],
            ['KOFF250', 'PART250=C6PAN9'],
            ['KOFF251', 'PART251=C718CO2H'],
            ['KOFF252', 'PART252=C718CO3H'],
            ['KOFF253', 'PART253=C718NO3'],
            ['KOFF254', 'PART254=C718OH'],
            ['KOFF255', 'PART255=C718OOH'],
            ['KOFF256', 'PART256=C718PAN'],
            ['KOFF257', 'PART257=C87CO'],
            ['KOFF258', 'PART258=C87CO2H'],
            ['KOFF259', 'PART259=C87CO3H'],
            ['KOFF260', 'PART260=C87OH'],
            ['KOFF261', 'PART261=C87OOH'],
            ['KOFF262', 'PART262=C87PAN'],
            ['KOFF263', 'PART263=C88CHO'],
            ['KOFF264', 'PART264=C88CO'],
            ['KOFF265', 'PART265=C88CO2H'],
            ['KOFF266', 'PART266=C88CO3H'],
            ['KOFF267', 'PART267=C88OH'],
            ['KOFF268', 'PART268=C88OOH'],
            ['KOFF269', 'PART269=C88PAN'],
            ['KOFF270', 'PART270=C8BC'],
            ['KOFF271', 'PART271=C8BCCO'],
            ['KOFF272', 'PART272=C8BCNO3'],
            ['KOFF273', 'PART273=C8BCOH'],
            ['KOFF274', 'PART274=C8BCOOH'],
            ['KOFF275', 'PART275=C914CO'],
            ['KOFF276', 'PART276=C914OH'],
            ['KOFF277', 'PART277=C914OOH'],
            ['KOFF278', 'PART278=C915NO3'],
            ['KOFF279', 'PART279=C915OH'],
            ['KOFF280', 'PART280=C915OOH'],
            ['KOFF281', 'PART281=C916NO3'],
            ['KOFF282', 'PART282=C916OH'],
            ['KOFF283', 'PART283=C916OOH'],
            ['KOFF284', 'PART284=C917NO3'],
            ['KOFF285', 'PART285=C917OH'],
            ['KOFF286', 'PART286=C917OOH'],
            ['KOFF287', 'PART287=C918CHO'],
            ['KOFF288', 'PART288=C918CO3H'],
            ['KOFF289', 'PART289=C918NO3'],
            ['KOFF290', 'PART290=C918OH'],
            ['KOFF291', 'PART291=C918OOH'],
            ['KOFF292', 'PART292=C918PAN'],
            ['KOFF293', 'PART293=C919NO3'],
            ['KOFF294', 'PART242=C919OH'],
            ['KOFF295', 'PART295=C919OOH'],
            ['KOFF296', 'PART296=C9DC'],
            ['KOFF297', 'PART297=C9DCCO'],
            ['KOFF298', 'PART298=C9DCNO3'],
            ['KOFF299', 'PART299=C9DCOH'],
            ['KOFF300', 'PART300=C9DCOOH'],
            ['KOFF301', 'PART301=CO123C5CHO'],
            ['KOFF302', 'PART302=CO12C4CHO'],
            ['KOFF303', 'PART303=CO1M22CHO'],
            ['KOFF304', 'PART304=CO1M22CO2H'],
            ['KOFF305', 'PART305=CO1M22CO3H'],
            ['KOFF306', 'PART306=CO1M22PAN'],
            ['KOFF307', 'PART307=H2M2C3CO3H'],
            ['KOFF308', 'PART308=MIBKHO4CHO'],
            ['KOFF309', 'PART309=NBPINAOOH'],
            ['KOFF310', 'PART310=NBPINBOOH'],
            ['KOFF311', 'PART311=NC91CHO'],
            ['KOFF312', 'PART312=NC91CO3H'],
            ['KOFF313', 'PART313=NC91PAN'],
            ['KOFF314', 'PART314=NOPINANO3'],
            ['KOFF315', 'PART315=NOPINAOH'],
            ['KOFF316', 'PART316=NOPINAOOH'],
            ['KOFF317', 'PART317=NOPINBCO'],
            ['KOFF318', 'PART318=NOPINBNO3'],
            ['KOFF319', 'PART319=NOPINBOH'],
            ['KOFF320', 'PART320=NOPINBOOH'],
            ['KOFF321', 'PART321=NOPINCNO3'],
            ['KOFF322', 'PART322=NOPINCOH'],
            ['KOFF323', 'PART323=NOPINCOOH'],
            ['KOFF324', 'PART324=NOPINDCO'],
            ['KOFF325', 'PART325=NOPINDOH'],
            ['KOFF326', 'PART326=NOPINDOOH'],
            ['KOFF327', 'PART327=NOPINONE'],
            ['KOFF350', 'PART350=M3F'],
            ['KOFF351', 'PART351=ISOPDOH'],
            ['KOFF352', 'PART352=ISOPAOH'],
            ['KOFF353', 'PART353=MMALANHY'],
            ['KOFF354', 'PART354=MC3ODBCO2H'],
            ['KOFF355', 'PART355=C532CO'],
            ['KOFF356', 'PART356=C624CO'],
            ['KOFF357', 'PART357=C518CHO'],
            ['KOFF358', 'PART358=IEB1CHO'],
            ['KOFF359', 'PART359=HO1CO34C5'],
            ['KOFF360', 'PART360=HMVKBCHO'],
            ['KOFF361', 'PART361=HC4CCO2H'],
            ['KOFF362', 'PART362=HC4ACO2H'],
            ['KOFF363', 'PART363=CO2C4CO2H'],
            ['KOFF364', 'PART364=C5HPALD2'],
            ['KOFF365', 'PART365=C624OH'],
            ['KOFF366', 'PART366=C622OH'],
            ['KOFF367', 'PART367=ISOPDOOH'],
            ['KOFF368', 'PART368=ISOPCOOH'],
            ['KOFF369', 'PART369=IEPOXC'],
            ['KOFF370', 'PART370=IEPOXB'],
            ['KOFF371', 'PART371=HO13CO4C5'],
            ['KOFF372', 'PART372=C517OH'],
            ['KOFF373', 'PART373=C531CO'],
            ['KOFF374', 'PART374=CO2C4GLYOX'],
            ['KOFF375', 'PART375=C511CHO'],
            ['KOFF376', 'PART376=C624CHO'],
            ['KOFF377', 'PART377=C622CHO'],
            ['KOFF378', 'PART378=C5PACALD2'],
            ['KOFF379', 'PART379=C5PACALD1'],
            ['KOFF380', 'PART380=C23O3CCHO'],
            ['KOFF381', 'PART381=C627OH'],
            ['KOFF382', 'PART382=C519CHO'],
            ['KOFF383', 'PART383=C518CO2H'],
            ['KOFF384', 'PART384=C517CHO'],
            ['KOFF385', 'PART385=PXYFUOH'],
            ['KOFF386', 'PART386=HMVKBCO2H'],
            ['KOFF387', 'PART387=HC4CCO3H'],
            ['KOFF388', 'PART388=HC4ACO3H'],
            ['KOFF389', 'PART389=CO2C4CO3H'],
            ['KOFF390', 'PART390=C520OH'],
            ['KOFF391', 'PART391=C4M2AL2OH'],
            ['KOFF392', 'PART392=C624OOH'],
            ['KOFF393', 'PART393=C622OOH'],
            ['KOFF394', 'PART394=C58OH'],
            ['KOFF395', 'PART395=C57OH'],
            ['KOFF396', 'PART396=C519OOH'],
            ['KOFF397', 'PART397=C517OOH'],
            ['KOFF398', 'PART398=LIMKET'],
            ['KOFF399', 'PART399=C816CO'],
            ['KOFF400', 'PART400=C729CHO'],
            ['KOFF401', 'PART401=CO25C6CHO'],
            ['KOFF402', 'PART402=C727CO'],
            ['KOFF403', 'PART403=C626CHO'],
            ['KOFF404', 'PART404=C822OH'],
            ['KOFF405', 'PART405=C731OH'],
            ['KOFF406', 'PART406=C729OOH'],
            ['KOFF407', 'PART407=C624CO2H'],
            ['KOFF408', 'PART408=C622CO2H'],
            ['KOFF409', 'PART409=MMALNHY2OH'],
            ['KOFF410', 'PART410=C531OOH'],
            ['KOFF411', 'PART411=C23O3CCO2H'],
            ['KOFF412', 'PART412=C629OH'],
            ['KOFF413', 'PART413=C628OH'],
            ['KOFF414', 'PART414=C627OOH'],
            ['KOFF415', 'PART415=C626OOH'],
            ['KOFF416', 'PART416=C519CO2H'],
            ['KOFF417', 'PART417=C518CO3H'],
            ['KOFF418', 'PART418=C517CO2H'],
            ['KOFF419', 'PART419=ISOPDNO3'],
            ['KOFF420', 'PART420=ISOPCNO3'],
            ['KOFF421', 'PART421=PXYFUOOH'],
            ['KOFF422', 'PART422=IECCO3H'],
            ['KOFF423', 'PART423=IEC2OOH'],
            ['KOFF424', 'PART424=HMVKBCO3H'],
            ['KOFF425', 'PART425=C520OOH'],
            ['KOFF426', 'PART426=C4MALOHOOH'],
            ['KOFF427', 'PART427=C625OH'],
            ['KOFF428', 'PART428=C623OH'],
            ['KOFF429', 'PART429=C59OOH'],
            ['KOFF430', 'PART430=C58OOH'],
            ['KOFF431', 'PART431=C58AOOH'],
            ['KOFF432', 'PART432=C57OOH'],
            ['KOFF433', 'PART433=C57AOOH'],
            ['KOFF434', 'PART434=NORLIMAL'],
            ['KOFF435', 'PART435=C824CO'],
            ['KOFF436', 'PART436=C823CO'],
            ['KOFF437', 'PART437=C817CO'],
            ['KOFF438', 'PART438=C729CO2H'],
            ['KOFF439', 'PART439=C923OH'],
            ['KOFF440', 'PART440=C823OH'],
            ['KOFF441', 'PART441=C822OOH'],
            ['KOFF442', 'PART442=C817OH'],
            ['KOFF443', 'PART443=C816OOH'],
            ['KOFF444', 'PART444=C511CO3H'],
            ['KOFF445', 'PART445=C733OH'],
            ['KOFF446', 'PART446=C732OH'],
            ['KOFF447', 'PART447=C731OOH'],
            ['KOFF448', 'PART448=C727OOH'],
            ['KOFF449', 'PART449=C624CO3H'],
            ['KOFF450', 'PART450=C622CO3H'],
            ['KOFF451', 'PART451=C624NO3'],
            ['KOFF452', 'PART452=C622NO3'],
            ['KOFF453', 'PART453=MMALNHYOOH'],
            ['KOFF454', 'PART454=C23O3CCO3H'],
            ['KOFF455', 'PART455=C629OOH'],
            ['KOFF456', 'PART456=C628OOH'],
            ['KOFF457', 'PART457=C519CO3H'],
            ['KOFF458', 'PART458=C517CO3H'],
            ['KOFF459', 'PART459=C730OH'],
            ['KOFF460', 'PART460=CONM2CO2H'],
            ['KOFF461', 'PART461=C517NO3'],
            ['KOFF462', 'PART462=C533OOH'],
            ['KOFF463', 'PART463=C625OOH'],
            ['KOFF464', 'PART464=C623OOH'],
            ['KOFF465', 'PART465=HPC52OOH'],
            ['KOFF466', 'PART466=C527OOH'],
            ['KOFF467', 'PART467=LIMBCO'],
            ['KOFF468', 'PART468=LMKBCO'],
            ['KOFF469', 'PART469=C924CO'],
            ['KOFF470', 'PART470=C818CO'],
            ['KOFF471', 'PART471=C729CO3H'],
            ['KOFF472', 'PART472=LMKAOH'],
            ['KOFF473', 'PART473=C923OOH'],
            ['KOFF474', 'PART474=C729NO3'],
            ['KOFF475', 'PART475=CO25C6CO3H'],
            ['KOFF476', 'PART476=C821OOH'],
            ['KOFF477', 'PART477=C735OOH'],
            ['KOFF478', 'PART478=C734CO'],
            ['KOFF479', 'PART479=C626CO3H'],
            ['KOFF480', 'PART480=C824OOH'],
            ['KOFF481', 'PART481=C818OH'],
            ['KOFF482', 'PART482=C817OOH'],
            ['KOFF483', 'PART483=MC3CODBPAN'],
            ['KOFF484', 'PART484=C3MCODBPAN'],
            ['KOFF485', 'PART485=C626NO3'],
            ['KOFF486', 'PART486=C734OH'],
            ['KOFF487', 'PART487=C733OOH'],
            ['KOFF488', 'PART488=C732OOH'],
            ['KOFF489', 'PART489=INCGLYOX'],
            ['KOFF490', 'PART490=C5PAN2'],
            ['KOFF491', 'PART491=C5PAN19'],
            ['KOFF492', 'PART492=C5PAN17'],
            ['KOFF493', 'PART493=C4M2ALOHNO3'],
            ['KOFF494', 'PART494=C47CHO'],
            ['KOFF495', 'PART495=C730OOH'],
            ['KOFF496', 'PART496=INDHCHO'],
            ['KOFF497', 'PART497=INCCO'],
            ['KOFF498', 'PART498=C58NO3'],
            ['KOFF499', 'PART499=C58ANO3'],
            ['KOFF500', 'PART500=C57NO3'],
            ['KOFF501', 'PART501=C535OOH'],
            ['KOFF502', 'PART502=C534OOH'],
            ['KOFF503', 'PART503=INDOH'],
            ['KOFF504', 'PART504=INCOH'],
            ['KOFF505', 'PART505=C537OOH'],
            ['KOFF506', 'PART506=LIMALBCO'],
            ['KOFF507', 'PART507=LMLKBCO'],
            ['KOFF508', 'PART508=LMLKACO'],
            ['KOFF509', 'PART509=LMLKBOH'],
            ['KOFF510', 'PART510=C926OH'],
            ['KOFF511', 'PART511=C822CO3H'],
            ['KOFF512', 'PART512=C816CO3H'],
            ['KOFF513', 'PART513=C822NO3'],
            ['KOFF514', 'PART514=C731CO3H'],
            ['KOFF515', 'PART515=C727CO3H'],
            ['KOFF516', 'PART516=LMKBOOH'],
            ['KOFF517', 'PART517=C731NO3'],
            ['KOFF518', 'PART518=C825OOH'],
            ['KOFF519', 'PART519=C819OOH'],
            ['KOFF520', 'PART520=C518PAN'],
            ['KOFF521', 'PART521=C734OOH'],
            ['KOFF522', 'PART522=NPXYFUOOH'],
            ['KOFF523', 'PART523=MMALNBCO2H'],
            ['KOFF524', 'PART524=MMALNACO2H'],
            ['KOFF525', 'PART525=IECPAN'],
            ['KOFF526', 'PART526=HMVKBPAN'],
            ['KOFF527', 'PART527=NC623OH'],
            ['KOFF528', 'PART528=C623NO3'],
            ['KOFF529', 'PART529=INDHPCHO'],
            ['KOFF530', 'PART530=C58NO3CO2H'],
            ['KOFF531', 'PART531=C57NO3CO2H'],
            ['KOFF532', 'PART532=C527NO3'],
            ['KOFF533', 'PART533=INDOOH'],
            ['KOFF534', 'PART534=INCOOH'],
            ['KOFF535', 'PART535=HPC52CO3H'],
            ['KOFF536', 'PART536=C923CO3H'],
            ['KOFF537', 'PART537=C923NO3'],
            ['KOFF538', 'PART538=LMLKBOOH'],
            ['KOFF539', 'PART539=LMLKAOOH'],
            ['KOFF540', 'PART540=C926OOH'],
            ['KOFF541', 'PART541=C823CO3H'],
            ['KOFF542', 'PART542=C817CO3H'],
            ['KOFF543', 'PART543=C823NO3'],
            ['KOFF544', 'PART544=C817NO3'],
            ['KOFF545', 'PART545=C820OOH'],
            ['KOFF546', 'PART546=C732CO3H'],
            ['KOFF547', 'PART547=C511PAN'],
            ['KOFF548', 'PART548=C732NO3'],
            ['KOFF549', 'PART549=C624PAN'],
            ['KOFF550', 'PART550=C622PAN'],
            ['KOFF551', 'PART551=C23O3CPAN'],
            ['KOFF552', 'PART552=C519PAN'],
            ['KOFF553', 'PART553=C517PAN'],
            ['KOFF554', 'PART554=NC730OH'],
            ['KOFF555', 'PART555=NC728OH'],
            ['KOFF556', 'PART556=C730NO3'],
            ['KOFF557', 'PART557=C728NO3'],
            ['KOFF558', 'PART558=MMALNBCO3H'],
            ['KOFF559', 'PART559=MMALNACO3H'],
            ['KOFF560', 'PART560=C47CO3H'],
            ['KOFF561', 'PART561=NC623OOH'],
            ['KOFF562', 'PART562=INDHCO3H'],
            ['KOFF563', 'PART563=C58NO3CO3H'],
            ['KOFF564', 'PART564=C57NO3CO3H'],
            ['KOFF565', 'PART565=C729PAN'],
            ['KOFF566', 'PART566=LMKBNO3'],
            ['KOFF567', 'PART567=C627PAN'],
            ['KOFF568', 'PART568=C626PAN'],
            ['KOFF569', 'PART569=NC826OH'],
            ['KOFF570', 'PART570=C826NO3'],
            ['KOFF571', 'PART571=NC730OOH'],
            ['KOFF572', 'PART572=NC728OOH'],
            ['KOFF573', 'PART573=CONM2PAN'],
            ['KOFF574', 'PART574=CO2N3PAN'],
            ['KOFF575', 'PART575=INCNCHO'],
            ['KOFF576', 'PART576=INB1NBCHO'],
            ['KOFF577', 'PART577=INB1NACHO'],
            ['KOFF578', 'PART578=MACRNPAN'],
            ['KOFF579', 'PART579=MACRNBPAN'],
            ['KOFF580', 'PART580=INCNO3'],
            ['KOFF581', 'PART581=INB1NO3'],
            ['KOFF582', 'PART582=INDHPCO3H'],
            ['KOFF583', 'PART583=C822PAN'],
            ['KOFF584', 'PART584=C816PAN'],
            ['KOFF585', 'PART585=NLIMOOH'],
            ['KOFF586', 'PART586=C731PAN'],
            ['KOFF587', 'PART587=C727PAN'],
            ['KOFF588', 'PART588=NLMKAOOH'],
            ['KOFF589', 'PART589=NC826OOH'],
            ['KOFF590', 'PART590=INCNCO2H'],
            ['KOFF591', 'PART591=INB1NBCO2H'],
            ['KOFF592', 'PART592=INB1NACO2H'],
            ['KOFF593', 'PART593=HPC52PAN'],
            ['KOFF594', 'PART594=C823PAN'],
            ['KOFF595', 'PART595=NLIMALOH'],
            ['KOFF596', 'PART596=LIMALNO3'],
            ['KOFF597', 'PART597=MMALNBPAN'],
            ['KOFF598', 'PART598=MMALNAPAN'],
            ['KOFF599', 'PART599=C47PAN'],
            ['KOFF600', 'PART600=INDHPAN'],
            ['KOFF601', 'PART601=INCNCO3H'],
            ['KOFF602', 'PART602=INB1NBCO3H'],
            ['KOFF603', 'PART603=INB1NACO3H'],
            ['KOFF604', 'PART604=C58NO3PAN'],
            ['KOFF605', 'PART605=C57NO3PAN'],
            ['KOFF606', 'PART606=NLIMALOOH'],
            ['KOFF607', 'PART607=INDHPPAN'],
            ['KOFF608', 'PART608=INCNPAN'],
            ['KOFF609', 'PART609=INB1NBPAN'],
            ['KOFF610', 'PART610=INB1NAPAN'],
            ['0.0001', 'HNO3S=HNO3'],
            ['0.0001', 'PART14S=PART14'],
            ['0.0001', 'PART15S=PART15'],
            ['0.0001', 'PART1S=PART1'],
            ['0.0001', 'PART17S=PART17'],
            ['0.0001', 'PART13S=PART13'],
            ['0.0001', 'PART15S=PART25'],
            ['0.8E-14', 'PART14+PART1=DIMER1'],
            ['0.8E-14', 'PART14+PART11=DIMER2'],
            ['0.8E-14', 'PART14+PART13=DIMER3'],
            ['0.8E-14', 'PART14+PART14=DIMER4'],
            ['0.8E-14', 'PART14+PART15=DIMER5'],
            ['0.8E-14', 'PART14+PART23=DIMER6'],
            ['0.8E-14', 'PART14+PART24=DIMER7'],
            ['0.8E-14', 'PART14+PART25=DIMER8'],
            ['0.8E-14', 'PART15+PART1=DIMER9'],
            ['0.8E-14', 'PART15+PART11=DIMER10'],
            ['0.8E-14', 'PART15+PART13=DIMER11'],
            ['0.8E-14', 'PART15+PART15=DIMER12'],
            ['0.8E-14', 'PART15+PART23=DIMER13'],
            ['0.8E-14', 'PART15+PART24=DIMER14'],
            ['0.8E-14', 'PART15+PART25=DIMER15'],
            ['0.8E-14', 'PART13+PART1=DIMER16'],
            ['0.8E-14', 'PART13+PART11=DIMER17'],
            ['0.8E-14', 'PART13+PART13=DIMER18'],
            ['0.8E-14', 'PART13+PART23=DIMER19'],
            ['0.8E-14', 'PART13+PART24=DIMER20'],
            ['0.8E-14', 'PART13+PART25=DIMER21'],
            ['0.0001', 'DIMER1=PART14+PART1'],
            ['0.0001', 'DIMER2=PART14+PART11'],
            ['0.0001', 'DIMER3=PART14+PART13'],
            ['0.0001', 'DIMER4=PART14+PART14'],
            ['0.0001', 'DIMER5=PART14+PART15'],
            ['0.0001', 'DIMER6=PART14+PART23'],
            ['0.0001', 'DIMER7=PART14+PART24'],
            ['0.0001', 'DIMER8=PART14+PART25'],
            ['0.0001', 'DIMER9=PART15+PART1'],
            ['0.0001', 'DIMER10=PART15+PART11'],
            ['0.0001', 'DIMER11=PART15+PART13'],
            ['0.0001', 'DIMER12=PART15+PART15'],
            ['0.0001', 'DIMER13=PART15+PART23'],
            ['0.0001', 'DIMER14=PART15+PART24'],
            ['0.0001', 'DIMER15=PART15+PART25'],
            ['0.0001', 'DIMER16=PART13+PART1'],
            ['0.0001', 'DIMER17=PART13+PART11'],
            ['0.0001', 'DIMER18=PART13+PART13'],
            ['0.0001', 'DIMER19=PART13+PART23'],
            ['0.0001', 'DIMER20=PART13+PART24'],
            ['0.0001', 'DIMER21=PART13+PART25'],
            ['3.0E-18', 'O3+TSP='],
            ['J15*0.5', 'PART14=C923O2+HO2+CO'],
            ['J15*0.5', 'PART14=C923CO3+HO2'],
            ['1.2*1.78E9*numba_exp(-8550/temp)', 'PART4=C923CO3+NO2'],
            ['J53', 'PART3=LIMKET+HCHO+HO2+NO2'],
            ['J53', 'PART2A=LIMAL+NO2+HO2'],
            ['J53', 'PART2B=LIMAL+NO2+HO2'],
            ['1.2*1.78E9*numba_exp(-8550/temp)', 'PART5=C817CO3+NO2'],
            ['1.20D-15', 'LIMBOO + CO = LIMAL'],
            ['1.00D-14', 'LIMBOO + NO = LIMAL + NO2'],
            ['1.00D-15', 'LIMBOO + NO2 = LIMAL + NO3'],
            ['7.00D-14', 'LIMBOO + SO2 = LIMAL + SO3'],
            ['1.40D-17*H2O', 'LIMBOO = LIMAL + H2O2'],
            ['2.00D-18*H2O', 'LIMBOO = LIMONONIC'],
            ['4e-16', 'LIMBOO + HCHO = LIMONONIC + HCHO'],
            ['2E-14', 'LIMBOO + LIMAL = SEED'],
            ['2E-14', 'LIMBOO + LMLKET = SEED'],
            ['2e-14', 'LIMBOO + LIMALBOH = SEED'],
            ['2e-14', 'LIMBOO + C825CO = SEED'],
            ['2e-14', 'LIMBOO + HCOOH = SEED'],
            ['5.3E-13', 'LIMBOO + KLIMONONIC = SEED'],
            ['5.3E-13', 'LIMBOO + LIMONONIC = SEED'],
            ['5.3e-13', 'LIMBOO + LIMONIC = SEED'],
            ['2e-14', 'LMKBOO + LIMAL = SEED'],
            ['2e-14', 'LMKBOO + LMLKET = SEED'],
            ['2e-14', 'LMKBOO + LIMALBOH = SEED'],
            ['2e-14', 'LMKBOO + C825CO = SEED'],
            ['2e-14', 'LMKBOO + HCOOH = SEED'],
            ['5.3e-13', 'LMKBOO + KLIMONONIC = SEED'],
            ['5.3e-13', 'LMKBOO + LIMONONIC = SEED'],
            ['0.8E-14','HNO3 + SEED = HNO3S + SEED'],
            ['0.8E-14','PART14 + SEED = PART14S + SEED'],
            ['0.8E-14','PART15 + SEED = PART15S + SEED'],
            ['0.8E-14','PART1 + SEED = PART1S + SEED'],
            ['0.8E-14','PART17 + SEED = PART17S + SEED'],
            ['0.8E-14','PART13 + SEED = PART13S + SEED']]
            
    full_dict={**on_dict,**off_dict}
    
    for i,s in enumerate(part_in):
        if s[0].upper() in full_dict.keys():
            part_in[i][0] = full_dict[part_in[i][0].upper()]       
    return part_in

def part_vap_pres():
    '''
    returns:
        vap_pres_dict = dictionary of particle vapour pressures
    '''
    vap_pres_dict={}
    vap_pres_dict['P1']=1.81e-4
    vap_pres_dict['P2A']=5.19e-4
    vap_pres_dict['P2B']=8.03e-4
    vap_pres_dict['P3']=1.09e-4
    vap_pres_dict['P4']=7.99e-4
    vap_pres_dict['P5']=1.25e-4
    vap_pres_dict['P6']=7.02e-5
    vap_pres_dict['P11']=1.71E-6
    vap_pres_dict['P13']=2.27E-5
    vap_pres_dict['P14']=4.63E-2
    vap_pres_dict['P15']=8.63E-3
    vap_pres_dict['P16']=2.41E-4
    vap_pres_dict['P17']=5.69E-3
    vap_pres_dict['P22']=1.03E-6
    vap_pres_dict['P23']=7.57E-8
    vap_pres_dict['P24']=4.36E-5
    vap_pres_dict['P25']=3.51E-4
    vap_pres_dict['P26']=4.91E-8
    vap_pres_dict['P27']=1.31E-5
    vap_pres_dict['P28']=1.92E-7
    vap_pres_dict['P29']=7.82E-5
    vap_pres_dict['P30']=1.74E-7
    vap_pres_dict['P31']=3.92E-6
    vap_pres_dict['P32']=1.72E-6
    vap_pres_dict['P33']=2.32E-8
    vap_pres_dict['P34']=2.21E-5
    vap_pres_dict['P35']=4.43E-5
    vap_pres_dict['P36']=6.31E-6
    vap_pres_dict['P37']=6.37E-7
    vap_pres_dict['P38']=9.38E-6
    vap_pres_dict['P39']=1.68E-7
    vap_pres_dict['P40']=3.46E-4
    vap_pres_dict['P41']=1.12E-4
    vap_pres_dict['P42']=6.45E-4
    vap_pres_dict['P43']=2.22E-10
    vap_pres_dict['P44']=1.93E-3
    vap_pres_dict['P45']=6.42E-6
    vap_pres_dict['P46']=1.15E-6
    vap_pres_dict['P47']=3.59E-6
    vap_pres_dict['P48']=1.28E-4
    vap_pres_dict['P49']=8.75E-5
    #
    vap_pres_dict['P50']=2.22E-10
    vap_pres_dict['P51']=2.43E-10
    vap_pres_dict['P52']=2.10E-09
    vap_pres_dict['P53']=2.13E-09
    vap_pres_dict['P54']=5.01E-09
    vap_pres_dict['P55']=9.27E-09
    vap_pres_dict['P56']=1.04E-08
    vap_pres_dict['P57']=1.37E-08
    vap_pres_dict['P58']=8.90E-08
    vap_pres_dict['P59']=1.12E-07
    vap_pres_dict['P60']=1.17E-07
    vap_pres_dict['P61']=1.64E-07
    vap_pres_dict['P62']=3.21E-07
    vap_pres_dict['P63']=3.40E-07
    vap_pres_dict['P64']=4.89E-07
    vap_pres_dict['P65']=5.12E-07
    vap_pres_dict['P66']=5.38E-07
    vap_pres_dict['P67']=7.18E-07
    vap_pres_dict['P68']=1.41E-06
    vap_pres_dict['P69']=2.10E-06
    vap_pres_dict['P70']=2.12E-06
    vap_pres_dict['P71']=2.37E-06
    vap_pres_dict['P72']=2.50E-06
    vap_pres_dict['P73']=2.64E-06
    vap_pres_dict['P74']=2.64E-06
    vap_pres_dict['P75']=2.85E-06
    vap_pres_dict['P76']=2.98E-06
    vap_pres_dict['P77']=3.41E-06
    vap_pres_dict['P78']=4.25E-06
    vap_pres_dict['P79']=5.10E-06
    vap_pres_dict['P80']=5.24E-06
    vap_pres_dict['P81']=6.82E-06
    vap_pres_dict['P82']=7.55E-06
    vap_pres_dict['P83']=8.71E-06
    vap_pres_dict['P84']=8.74E-06
    vap_pres_dict['P85']=8.92E-06
    vap_pres_dict['P86']=9.33E-06
    vap_pres_dict['P87']=9.93E-06
    vap_pres_dict['P88']=1.06E-05
    vap_pres_dict['P89']=1.11E-05
    vap_pres_dict['P90']=1.14E-05
    vap_pres_dict['P91']=1.79E-05
    vap_pres_dict['P92']=1.79E-05
    vap_pres_dict['P93']=2.34E-05
    vap_pres_dict['P94']=2.83E-05
    vap_pres_dict['P95']=2.83E-05
    vap_pres_dict['P96']=2.99E-05
    vap_pres_dict['P97']=2.99E-05
    vap_pres_dict['P98']=3.00E-05
    vap_pres_dict['P99']=3.11E-05
    vap_pres_dict['P100']=3.30E-05
    vap_pres_dict['P101']=3.35E-05
    vap_pres_dict['P102']=3.84E-05
    vap_pres_dict['P103']=4.23E-05
    vap_pres_dict['P104']=4.28E-05
    vap_pres_dict['P105']=5.53E-05
    vap_pres_dict['P106']=5.78E-05
    vap_pres_dict['P107']=5.90E-05
    vap_pres_dict['P108']=5.97E-05
    vap_pres_dict['P109']=5.97E-05
    vap_pres_dict['P110']=6.81E-05
    vap_pres_dict['P111']=6.81E-05
    vap_pres_dict['P112']=6.96E-05
    vap_pres_dict['P113']=7.48E-05
    vap_pres_dict['P114']=7.48E-05
    vap_pres_dict['P115']=7.49E-05
    vap_pres_dict['P116']=8.65E-05
    vap_pres_dict['P117']=8.75E-05
    vap_pres_dict['P118']=9.49E-05
    vap_pres_dict['P119']=1.00E-04
    vap_pres_dict['P120']=1.86E-04
    vap_pres_dict['P121']=2.31E-04
    vap_pres_dict['P122']=2.49E-04
    vap_pres_dict['P123']=2.50E-04
    vap_pres_dict['P124']=3.05E-04
    vap_pres_dict['P125']=3.22E-04
    vap_pres_dict['P126']=3.28E-04
    vap_pres_dict['P127']=3.31E-04
    vap_pres_dict['P128']=3.49E-04
    vap_pres_dict['P129']=3.99E-04
    vap_pres_dict['P130']=4.18E-04
    vap_pres_dict['P131']=4.84E-04
    vap_pres_dict['P132']=4.85E-04
    vap_pres_dict['P133']=5.07E-04
    vap_pres_dict['P134']=5.07E-04
    vap_pres_dict['P135']=6.19E-04
    vap_pres_dict['P136']=6.91E-04
    vap_pres_dict['P137']=8.41E-04
    vap_pres_dict['P138']=1.06E-03
    vap_pres_dict['P139']=1.09E-03
    vap_pres_dict['P140']=1.10E-03
    vap_pres_dict['P141']=1.30E-03
    vap_pres_dict['P142']=1.33E-03
    vap_pres_dict['P143']=1.33E-03
    vap_pres_dict['P144']=1.44E-03
    vap_pres_dict['P145']=1.56E-03
    vap_pres_dict['P146']=1.68E-03
    vap_pres_dict['P147']=1.68E-03
    vap_pres_dict['P148']=1.76E-03
    vap_pres_dict['P149']=1.81E-03
    vap_pres_dict['P150']=1.89E-03
    vap_pres_dict['P151']=2.12E-03
    vap_pres_dict['P152']=2.16E-03
    vap_pres_dict['P153']=2.60E-03
    vap_pres_dict['P154']=2.66E-03
    vap_pres_dict['P155']=2.68E-03
    vap_pres_dict['P156']=2.94E-03
    vap_pres_dict['P157']=3.16E-03
    vap_pres_dict['P158']=3.35E-03
    vap_pres_dict['P159']=3.37E-03
    vap_pres_dict['P160']=3.82E-03
    vap_pres_dict['P161']=4.21E-03
    vap_pres_dict['P162']=4.51E-03
    vap_pres_dict['P163']=4.56E-03
    vap_pres_dict['P164']=4.95E-03
    vap_pres_dict['P165']=5.06E-03
    vap_pres_dict['P166']=5.15E-03
    vap_pres_dict['P167']=5.33E-03
    vap_pres_dict['P168']=5.40E-03
    vap_pres_dict['P169']=5.52E-03
    vap_pres_dict['P170']=7.48E-03
    vap_pres_dict['P171']=7.97E-03
    vap_pres_dict['P172']=1.09E-02
    vap_pres_dict['P173']=1.19E-02
    vap_pres_dict['P174']=1.19E-02
    vap_pres_dict['P175']=1.56E-02
    vap_pres_dict['P176']=1.66E-02
    vap_pres_dict['P177']=1.82E-02
    vap_pres_dict['P178']=2.06E-02
    vap_pres_dict['P179']=5.98E-02
    vap_pres_dict['P180']=5.99E-02
    vap_pres_dict['P181']=6.90E-02
    vap_pres_dict['P182']=1.31E-01
    vap_pres_dict['P183']=1.78E-01
    vap_pres_dict['P184']=2.58E-01
    vap_pres_dict['P185']=4.31E-01
    vap_pres_dict['P186']=5.84E-01
    #
    vap_pres_dict['P200']=2.66e-4
    vap_pres_dict['P201']=8.27E-4
    vap_pres_dict['P202']=3.53E-5
    vap_pres_dict['P203']=5.5E-04
    vap_pres_dict['P204']=8.12E-5
    vap_pres_dict['P205']=2.03E-04
    vap_pres_dict['P206']=6.27E-4
    vap_pres_dict['P207']=2.61E-5
    vap_pres_dict['P208']=8.09E-5
    vap_pres_dict['P209']=4.43E-4
    vap_pres_dict['P210']=1.7E-3
    vap_pres_dict['P211']=1.77E-2
    vap_pres_dict['P212']=3.55E-2
    vap_pres_dict['P213']=3.16E-03
    vap_pres_dict['P214']=3.06E-3
    vap_pres_dict['P215']=3.70E-03
    vap_pres_dict['P216']=2.68E-4
    vap_pres_dict['P217']=1.22E-5
    vap_pres_dict['P218']=1.04E-2
    vap_pres_dict['P219']=3.39E-2
    vap_pres_dict['P220']=1.59E-04
    vap_pres_dict['P221']=3.03E-04
    vap_pres_dict['P222']=2.90E-04
    vap_pres_dict['P223']=1.51E-03
    vap_pres_dict['P224']=1.06E-01
    vap_pres_dict['P225']=2.36E-01
    vap_pres_dict['P226']=1.96E-04
    vap_pres_dict['P227']=8.30E-04
    vap_pres_dict['P228']=2.87E-02
    vap_pres_dict['P229']=2.02E-03
    vap_pres_dict['P230']=3.00E-03
    vap_pres_dict['P231']=9.85E-04
    vap_pres_dict['P232']=5.71E-05
    vap_pres_dict['P233']=7.95E-02
    vap_pres_dict['P234']=6.36E-04
    vap_pres_dict['P235']=2.22E-03
    vap_pres_dict['P236']=4.33E-02
    vap_pres_dict['P237']=4.28E-03
    vap_pres_dict['P238']=3.85E-03
    vap_pres_dict['P239']=6.36E-04
    vap_pres_dict['P240']=2.22E-03
    vap_pres_dict['P241']=3.86E-03
    vap_pres_dict['P242']=3.85E-03
    vap_pres_dict['P243']=1.39E-01
    vap_pres_dict['P244']=1.91E-02
    vap_pres_dict['P245']=1.29E-03
    vap_pres_dict['P246']=9.85E-04
    vap_pres_dict['P247']=5.71E-05
    vap_pres_dict['P248']=9.25E-02
    vap_pres_dict['P249']=8.72E-04
    vap_pres_dict['P250']=2.11E-03
    vap_pres_dict['P251']=1.95E-04
    vap_pres_dict['P252']=7.04E-04
    vap_pres_dict['P253']=6.71E-03
    vap_pres_dict['P254']=1.33E-02
    vap_pres_dict['P255']=1.33E-03
    vap_pres_dict['P256']=1.37E-03
    vap_pres_dict['P257']=1.31E-03
    vap_pres_dict['P258']=2.50E-06
    vap_pres_dict['P259']=1.12E-05
    vap_pres_dict['P260']=1.98E-04
    vap_pres_dict['P261']=1.84E-05
    vap_pres_dict['P262']=3.95E-05
    vap_pres_dict['P263']=1.82E-02
    vap_pres_dict['P264']=5.86E-02
    vap_pres_dict['P265']=6.32E-05
    vap_pres_dict['P266']=2.29E-04
    vap_pres_dict['P267']=8.90E-03
    vap_pres_dict['P268']=6.77E-04
    vap_pres_dict['P269']=3.23E-04
    vap_pres_dict['P270']=2.14E+01
    vap_pres_dict['P271']=2.25E+00
    vap_pres_dict['P272']=2.50E-01
    vap_pres_dict['P273']=9.25E-01
    vap_pres_dict['P274']=7.76E-02
    vap_pres_dict['P275']=2.05E-03
    vap_pres_dict['P276']=2.49E-04
    vap_pres_dict['P277']=1.70E-05
    vap_pres_dict['P278']=1.05E-03
    vap_pres_dict['P279']=2.63E-03
    vap_pres_dict['P280']=1.97E-04
    vap_pres_dict['P281']=4.05E-05
    vap_pres_dict['P282']=1.61E-04
    vap_pres_dict['P283']=6.52E-06
    vap_pres_dict['P284']=7.29E-04
    vap_pres_dict['P285']=2.76E-03
    vap_pres_dict['P286']=1.36E-04
    vap_pres_dict['P287']=1.23E-02
    vap_pres_dict['P288']=1.42E-04
    vap_pres_dict['P289']=1.44E-03
    vap_pres_dict['P290']=3.87E-03
    vap_pres_dict['P291']=2.85E-04
    vap_pres_dict['P292']=8.15E-04
    vap_pres_dict['P293']=4.05E-05
    vap_pres_dict['P294']=1.61E-04
    vap_pres_dict['P295']=6.52E-06
    vap_pres_dict['P296']=1.39E-01
    vap_pres_dict['P297']=1.80E-02
    vap_pres_dict['P298']=9.94E-04
    vap_pres_dict['P299']=2.56E-03
    vap_pres_dict['P300']=1.95E-04
    vap_pres_dict['P301']=1.04E-02
    vap_pres_dict['P302']=1.98E-01
    vap_pres_dict['P303']=1.41E+00
    vap_pres_dict['P304']=6.42E-02
    vap_pres_dict['P305']=1.99E-01
    vap_pres_dict['P306']=3.38E-01
    vap_pres_dict['P307']=3.23E-02
    vap_pres_dict['P308']=9.25E-02
    vap_pres_dict['P309']=2.80E-05
    vap_pres_dict['P310']=2.80E-05
    vap_pres_dict['P311']=3.23E-03
    vap_pres_dict['P312']=4.58E-05
    vap_pres_dict['P313']=1.62E-04
    vap_pres_dict['P314']=6.07E-03
    vap_pres_dict['P315']=2.37E-02
    vap_pres_dict['P316']=1.97E-03
    vap_pres_dict['P317']=1.39E-01
    vap_pres_dict['P318']=6.07E-03
    vap_pres_dict['P319']=2.37E-02
    vap_pres_dict['P320']=1.97E-03
    vap_pres_dict['P321']=5.46E-03
    vap_pres_dict['P322']=3.17E-02
    vap_pres_dict['P323']=1.75E-03
    vap_pres_dict['P324']=1.39E-01
    vap_pres_dict['P325']=2.37E-02
    vap_pres_dict['P326']=1.97E-03
    vap_pres_dict['P327']=6.29E-01
    #
    vap_pres_dict['P350']=4.392E+02
    vap_pres_dict['P351']=1.267E-01
    vap_pres_dict['P352']=3.700E-02
    vap_pres_dict['P353']=2.012E+05
    vap_pres_dict['P354']=1.799E-02
    vap_pres_dict['P355']=1.099E+00
    vap_pres_dict['P356']=2.468E-01
    vap_pres_dict['P357']=4.323E-01
    vap_pres_dict['P358']=7.769E-02
    vap_pres_dict['P359']=6.793E-02
    vap_pres_dict['P360']=8.326E-02
    vap_pres_dict['P361']=1.161E-03
    vap_pres_dict['P362']=1.161E-03
    vap_pres_dict['P363']=3.094E-02
    vap_pres_dict['P364']=5.121E-02
    vap_pres_dict['P365']=4.025E-02
    vap_pres_dict['P366']=2.604E-02
    vap_pres_dict['P367']=7.653E-03
    vap_pres_dict['P368']=3.466E-03
    vap_pres_dict['P369']=8.040E-03
    vap_pres_dict['P370']=5.103E-03
    vap_pres_dict['P371']=6.153E-03
    vap_pres_dict['P372']=3.998E-03
    vap_pres_dict['P373']=2.220E-01
    vap_pres_dict['P374']=2.833E-01
    vap_pres_dict['P375']=1.413E-01
    vap_pres_dict['P376']=1.364E-01
    vap_pres_dict['P377']=1.364E-01
    vap_pres_dict['P378']=6.330E-02
    vap_pres_dict['P379']=6.330E-02
    vap_pres_dict['P380']=4.316E-01
    vap_pres_dict['P381']=2.065E-02
    vap_pres_dict['P382']=2.481E-02
    vap_pres_dict['P383']=1.255E-03
    vap_pres_dict['P384']=2.481E-02
    vap_pres_dict['P385']=3.420E-04
    vap_pres_dict['P386']=1.537E-04
    vap_pres_dict['P387']=5.515E-03
    vap_pres_dict['P388']=5.515E-03
    vap_pres_dict['P389']=9.810E-02
    vap_pres_dict['P390']=1.248E-03
    vap_pres_dict['P391']=1.134E-03
    vap_pres_dict['P392']=2.483E-03
    vap_pres_dict['P393']=2.501E-03
    vap_pres_dict['P394']=8.254E-05
    vap_pres_dict['P395']=8.254E-05
    vap_pres_dict['P396']=3.357E-04
    vap_pres_dict['P397']=3.391E-04
    vap_pres_dict['P398']=6.743E-01
    vap_pres_dict['P399']=4.408E-01
    vap_pres_dict['P400']=1.082E-01
    vap_pres_dict['P401']=8.746E-02
    vap_pres_dict['P402']=1.309E-01
    vap_pres_dict['P403']=4.747E-02
    vap_pres_dict['P404']=4.410E-02
    vap_pres_dict['P405']=7.619E-03
    vap_pres_dict['P406']=1.495E-02
    vap_pres_dict['P407']=3.872E-04
    vap_pres_dict['P408']=3.872E-04
    vap_pres_dict['P409']=2.369E-03
    vap_pres_dict['P410']=1.405E-03
    vap_pres_dict['P411']=2.143E-03
    vap_pres_dict['P412']=3.608E-04
    vap_pres_dict['P413']=3.608E-04
    vap_pres_dict['P414']=2.026E-03
    vap_pres_dict['P415']=2.382E-03
    vap_pres_dict['P416']=4.595E-05
    vap_pres_dict['P417']=5.256E-03
    vap_pres_dict['P418']=4.595E-05
    vap_pres_dict['P419']=6.189E-02
    vap_pres_dict['P420']=3.164E-02
    vap_pres_dict['P421']=1.122E-05
    vap_pres_dict['P422']=1.730E-03
    vap_pres_dict['P423']=3.582E-05
    vap_pres_dict['P424']=7.255E-04
    vap_pres_dict['P425']=3.582E-05
    vap_pres_dict['P426']=3.268E-05
    vap_pres_dict['P427']=1.218E-05
    vap_pres_dict['P428']=1.096E-05
    vap_pres_dict['P429']=9.439E-07
    vap_pres_dict['P430']=1.827E-06
    vap_pres_dict['P431']=3.385E-06
    vap_pres_dict['P432']=1.827E-06
    vap_pres_dict['P433']=3.385E-06
    vap_pres_dict['P434']=2.420E-01
    vap_pres_dict['P435']=5.165E-03
    vap_pres_dict['P436']=2.439E-03
    vap_pres_dict['P437']=5.040E-02
    vap_pres_dict['P438']=2.439E-03
    vap_pres_dict['P439']=2.252E-02
    vap_pres_dict['P440']=1.202E-04
    vap_pres_dict['P441']=4.869E-03
    vap_pres_dict['P442']=3.927E-03
    vap_pres_dict['P443']=7.735E-03
    vap_pres_dict['P444']=4.104E-03
    vap_pres_dict['P445']=6.331E-05
    vap_pres_dict['P446']=1.384E-05
    vap_pres_dict['P447']=7.395E-04
    vap_pres_dict['P448']=1.242E-03
    vap_pres_dict['P449']=1.623E-03
    vap_pres_dict['P450']=1.623E-03
    vap_pres_dict['P451']=5.416E+01
    vap_pres_dict['P452']=5.397E+01
    vap_pres_dict['P453']=7.337E-05
    vap_pres_dict['P454']=7.571E-03
    vap_pres_dict['P455']=1.067E-05
    vap_pres_dict['P456']=1.067E-05
    vap_pres_dict['P457']=2.177E-04
    vap_pres_dict['P458']=2.177E-04
    vap_pres_dict['P459']=3.324E-06
    vap_pres_dict['P460']=4.906E-04
    vap_pres_dict['P461']=1.209E+01
    vap_pres_dict['P462']=5.921E-05
    vap_pres_dict['P463']=2.878E-07
    vap_pres_dict['P464']=2.544E-07
    vap_pres_dict['P465']=1.142E-07
    vap_pres_dict['P466']=7.054E-08
    vap_pres_dict['P467']=2.675E-02
    vap_pres_dict['P468']=4.844E-03
    vap_pres_dict['P469']=2.690E-03
    vap_pres_dict['P470']=4.203E-04
    vap_pres_dict['P471']=8.004E-03
    vap_pres_dict['P472']=6.159E-04
    vap_pres_dict['P473']=2.604E-03
    vap_pres_dict['P474']=6.707E+01
    vap_pres_dict['P475']=1.045E-03
    vap_pres_dict['P476']=1.244E-04
    vap_pres_dict['P477']=4.865E-05
    vap_pres_dict['P478']=1.085E-06
    vap_pres_dict['P479']=1.272E-03
    vap_pres_dict['P480']=2.997E-05
    vap_pres_dict['P481']=3.348E-05
    vap_pres_dict['P482']=3.997E-04
    vap_pres_dict['P483']=1.339E-01
    vap_pres_dict['P484']=1.339E-01
    vap_pres_dict['P485']=2.429E+01
    vap_pres_dict['P486']=4.936E-08
    vap_pres_dict['P487']=3.256E-06
    vap_pres_dict['P488']=1.011E-06
    vap_pres_dict['P489']=7.516E-04
    vap_pres_dict['P490']=7.985E-02
    vap_pres_dict['P491']=2.842E-02
    vap_pres_dict['P492']=2.842E-02
    vap_pres_dict['P493']=2.685E-04
    vap_pres_dict['P494']=3.486E+00
    vap_pres_dict['P495']=7.870E-08
    vap_pres_dict['P496']=4.577E-05
    vap_pres_dict['P497']=3.609E-05
    vap_pres_dict['P498']=2.685E-05
    vap_pres_dict['P499']=8.144E-01
    vap_pres_dict['P500']=2.685E-05
    vap_pres_dict['P501']=3.246E-07
    vap_pres_dict['P502']=3.246E-07
    vap_pres_dict['P503']=1.552E-06
    vap_pres_dict['P504']=2.439E-06
    vap_pres_dict['P505']=4.165E-09
    vap_pres_dict['P506']=4.106E-03
    vap_pres_dict['P507']=8.264E-04
    vap_pres_dict['P508']=1.995E-03
    vap_pres_dict['P509']=7.611E-05
    vap_pres_dict['P510']=3.243E-04
    vap_pres_dict['P511']=2.650E-03
    vap_pres_dict['P512']=4.032E-03
    vap_pres_dict['P513']=2.511E+01
    vap_pres_dict['P514']=4.011E-04
    vap_pres_dict['P515']=6.406E-04
    vap_pres_dict['P516']=4.028E-05
    vap_pres_dict['P517']=8.442E+00
    vap_pres_dict['P518']=2.519E-08
    vap_pres_dict['P519']=1.814E-06
    vap_pres_dict['P520']=7.142E+02
    vap_pres_dict['P521']=1.817E-09
    vap_pres_dict['P522']=8.397E-06
    vap_pres_dict['P523']=8.127E-07
    vap_pres_dict['P524']=8.127E-07
    vap_pres_dict['P525']=6.782E-03
    vap_pres_dict['P526']=1.973E+02
    vap_pres_dict['P527']=1.886E-01
    vap_pres_dict['P528']=8.956E-02
    vap_pres_dict['P529']=1.316E-06
    vap_pres_dict['P530']=2.024E-08
    vap_pres_dict['P531']=2.024E-08
    vap_pres_dict['P532']=4.229E-02
    vap_pres_dict['P533']=3.510E-08
    vap_pres_dict['P534']=1.007E-07
    vap_pres_dict['P535']=3.404E-10
    vap_pres_dict['P536']=1.351E-03
    vap_pres_dict['P537']=9.741E+00
    vap_pres_dict['P538']=6.801E-06
    vap_pres_dict['P539']=1.383E-05
    vap_pres_dict['P540']=1.359E-05
    vap_pres_dict['P541']=2.035E-05
    vap_pres_dict['P542']=2.057E-04
    vap_pres_dict['P543']=5.952E-01
    vap_pres_dict['P544']=3.536E+00
    vap_pres_dict['P545']=1.350E-07
    vap_pres_dict['P546']=1.264E-06
    vap_pres_dict['P547']=2.755E+02
    vap_pres_dict['P548']=1.171E-01
    vap_pres_dict['P549']=2.501E+02
    vap_pres_dict['P550']=2.501E+02
    vap_pres_dict['P551']=7.226E-03
    vap_pres_dict['P552']=6.853E+01
    vap_pres_dict['P553']=6.853E+01
    vap_pres_dict['P554']=5.720E-02
    vap_pres_dict['P555']=5.720E-02
    vap_pres_dict['P556']=2.742E-02
    vap_pres_dict['P557']=2.742E-02
    vap_pres_dict['P558']=4.102E-06
    vap_pres_dict['P559']=4.102E-06
    vap_pres_dict['P560']=1.244E-01
    vap_pres_dict['P561']=9.985E-03
    vap_pres_dict['P562']=2.391E-07
    vap_pres_dict['P563']=1.333E-07
    vap_pres_dict['P564']=1.333E-07
    vap_pres_dict['P565']=2.508E+02
    vap_pres_dict['P566']=8.104E-01
    vap_pres_dict['P567']=7.256E+01
    vap_pres_dict['P568']=1.017E+02
    vap_pres_dict['P569']=9.980E-02
    vap_pres_dict['P570']=5.127E-02
    vap_pres_dict['P571']=3.043E-03
    vap_pres_dict['P572']=3.043E-03
    vap_pres_dict['P573']=4.666E-03
    vap_pres_dict['P574']=1.658E-03
    vap_pres_dict['P575']=2.899E-05
    vap_pres_dict['P576']=1.252E-05
    vap_pres_dict['P577']=1.252E-05
    vap_pres_dict['P578']=3.531E-04
    vap_pres_dict['P579']=1.223E-03
    vap_pres_dict['P580']=1.271E-06
    vap_pres_dict['P581']=5.062E-07
    vap_pres_dict['P582']=5.344E-09
    vap_pres_dict['P583']=1.002E+02
    vap_pres_dict['P584']=1.004E+02
    vap_pres_dict['P585']=3.237E-01
    vap_pres_dict['P586']=3.814E+01
    vap_pres_dict['P587']=4.020E+01
    vap_pres_dict['P588']=6.900E-02
    vap_pres_dict['P589']=6.715E-03
    vap_pres_dict['P590']=3.512E-08
    vap_pres_dict['P591']=1.328E-08
    vap_pres_dict['P592']=1.328E-08
    vap_pres_dict['P593']=3.752E-02
    vap_pres_dict['P594']=4.153E+00
    vap_pres_dict['P595']=2.318E-02
    vap_pres_dict['P596']=1.237E-02
    vap_pres_dict['P597']=2.363E-05
    vap_pres_dict['P598']=2.363E-05
    vap_pres_dict['P599']=1.614E+03
    vap_pres_dict['P600']=2.543E-06
    vap_pres_dict['P601']=1.755E-07
    vap_pres_dict['P602']=7.085E-08
    vap_pres_dict['P603']=7.085E-08
    vap_pres_dict['P604']=1.544E-06
    vap_pres_dict['P605']=1.544E-06
    vap_pres_dict['P606']=1.614E-03
    vap_pres_dict['P607']=8.865E-08
    vap_pres_dict['P608']=1.425E-06
    vap_pres_dict['P609']=6.731E-07
    vap_pres_dict['P610']=6.731E-07
    #
    return vap_pres_dict

def particle_calc_dict():
    '''
    returns:
        part_calc_dict = dictionary of summations used in particle calculations
    '''
    part_calc_dict={     
    'TSP' : compile('SEED + PART1 + PART2A + PART2B + PART3 + PART4 + PART5 + PART6 + PART11 \
    + PART13 + PART14 + PART15 + PART16 + PART17 + PART22 + PART23 + PART24 + PART25 \
    + PART26 + PART27 + PART28 + PART29 + PART30 + PART31 + PART32 + PART33 + PART34 \
    + PART35 + PART36 + PART37 + PART38 + PART39 + PART40 + PART41 + PART42 + PART43 \
    + PART44 + PART45 + PART46 + PART47 + PART48 + PART49 + NA + PART50 + PART51 \
    + PART52 + PART53 + PART54 + PART55 + PART56 + PART57 + PART58 + PART59 + PART60 \
    + PART61 + PART62 + PART63 + PART64 + PART65 + PART66 + PART67 + PART68 + PART69 \
    + PART70 + PART71 + PART72 + PART73 + PART74 + PART75 + PART76 + PART77 + PART78 \
    + PART79 + PART80 + PART81 + PART82 + PART83 + PART84 + PART85 + PART86 + PART87 \
    + PART88 + PART89 + PART90 + PART91 + PART92 + PART93 + PART94 + PART95 + PART96 \
    + PART97 + PART98 + PART99 + PART100 + PART101 + PART102 + PART103 + PART104 \
    + PART105 + PART106 + PART107 + PART108 + PART109 + PART110 + PART111 + PART112 \
    + PART113 + PART114 + PART115 + PART116 + PART117 + PART118 + PART119 + PART120 \
    + PART121 + PART122 + PART123 + PART124 + PART125 + PART126 + PART127 + PART128 \
    + PART129 + PART130 + PART131 + PART132 + PART133 + PART134 + PART135 + PART136 \
    + PART137 + PART138 + PART139 + PART140 + PART141 + PART142 + PART143 + PART144 \
    + PART145 + PART146 + PART147 + PART148 + PART149 + PART150 + PART151 + PART152 \
    + PART153 + PART154 + PART155 + PART156 + PART157 + PART158 + PART159 + PART160 \
    + PART161 + PART162 + PART163 + PART164 + PART165 + PART166 + PART167 + PART168 \
    + PART169 + PART170 + PART171 + PART172 + PART173 + PART174 + PART175 + PART176 \
    + PART177 + PART178 + PART179 + PART180 + PART181 + PART182 + PART183 + PART184 \
    + PART185 + PART186 + PART200 + PART201 + PART202 + PART203 + PART204 + PART205 \
    + PART206 + PART207 + PART209 + PART210 + PART211 + PART212 + PART213 + PART214 \
    + PART215 + PART216 + PART217 + PART218 + PART219 + PART220 + PART221 + PART222 \
    + PART223 + PART224 + PART225 + PART226 + PART227 + PART228 + PART229 + PART230 \
    + PART231 + PART232 + PART233 + PART234 + PART235 + PART236 + PART237 + PART238 \
    + PART239 + PART240 + PART241 + PART242 + PART243 + PART244 + PART245 + PART246 \
    + PART247 + PART248 + PART249 + PART250 + PART251 + PART252 + PART253 + PART254 \
    + PART255 + PART256 + PART257 + PART258 + PART259 + PART260 + PART261 + PART262 \
    + PART263 + PART264 + PART265 + PART266 + PART267 + PART268 + PART269 + PART270 \
    + PART271 + PART272 + PART273 + PART274 + PART275 + PART276 + PART277 + PART278 \
    + PART279 + PART280 + PART281 + PART282 + PART283 + PART284 + PART285 + PART286 \
    + PART287 + PART288 + PART289 + PART290 + PART291 + PART292 + PART293 + PART294 \
    + PART295 + PART296 + PART297 + PART298 + PART299 + PART300 + PART301 + PART302 \
    + PART303 + PART304 + PART305 + PART306 + PART307 + PART308 + PART309 + PART310 \
    + PART311 + PART312 + PART313 + PART314 + PART315 + PART316 + PART317 + PART318 \
    + PART319 + PART320 + PART321 + PART322 + PART323 + PART324 + PART325 + PART326 \
    + PART327 + PART350 + PART351 + PART352 + PART353 + PART354 + PART355 \
    + PART356 + PART357 + PART358 + PART359 + PART360 + PART361 + PART362 \
    + PART363 + PART364 + PART365 + PART366 + PART367 + PART368 + PART369 \
    + PART370 + PART371 + PART372 + PART373 + PART374 + PART375 + PART376 \
    + PART377 + PART378 + PART379 + PART380 + PART381 + PART382 + PART383 \
    + PART384 + PART385 + PART386 + PART387 + PART388 + PART389 + PART390 \
    + PART391 + PART392 + PART393 + PART394 + PART395 + PART396 + PART397 \
    + PART398 + PART399 + PART400 + PART401 + PART402 + PART403 + PART404 \
    + PART405 + PART406 + PART407 + PART408 + PART409 + PART410 + PART411 \
    + PART412 + PART413 + PART414 + PART415 + PART416 + PART417 + PART418 \
    + PART419 + PART420 + PART421 + PART422 + PART423 + PART424 + PART425 \
    + PART426 + PART427 + PART428 + PART429 + PART430 + PART431 + PART432 \
    + PART433 + PART434 + PART435 + PART436 + PART437 + PART438 + PART439 \
    + PART440 + PART441 + PART442 + PART443 + PART444 + PART445 + PART446 \
    + PART447 + PART448 + PART449 + PART450 + PART451 + PART452 + PART453 \
    + PART454 + PART455 + PART456 + PART457 + PART458 + PART459 + PART460 \
    + PART461 + PART462 + PART463 + PART464 + PART465 + PART466 + PART467 \
    + PART468 + PART469 + PART470 + PART471 + PART472 + PART473 + PART474 \
    + PART475 + PART476 + PART477 + PART478 + PART479 + PART480 + PART481 \
    + PART482 + PART483 + PART484 + PART485 + PART486 + PART487 + PART488 \
    + PART489 + PART490 + PART491 + PART492 + PART493 + PART494 + PART495 \
    + PART496 + PART497 + PART498 + PART499 + PART500 + PART501 + PART502 \
    + PART503 + PART504 + PART505 + PART506 + PART507 + PART508 + PART509 \
    + PART510 + PART511 + PART512 + PART513 + PART514 + PART515 + PART516 \
    + PART517 + PART518 + PART519 + PART520 + PART521 + PART522 + PART523 \
    + PART524 + PART525 + PART526 + PART527 + PART528 + PART529 + PART530 \
    + PART531 + PART532 + PART533 + PART534 + PART535 + PART536 + PART537 \
    + PART538 + PART539 + PART540 + PART541 + PART542 + PART543 + PART544 \
    + PART545 + PART546 + PART547 + PART548 + PART549 + PART550 + PART551 \
    + PART552 + PART553 + PART554 + PART555 + PART556 + PART557 + PART558 \
    + PART559 + PART560 + PART561 + PART562 + PART563 + PART564 + PART565 \
    + PART566 + PART567 + PART568 + PART569 + PART570 + PART571 + PART572 \
    + PART573 + PART574 + PART575 + PART576 + PART577 + PART578 + PART579 \
    + PART580 + PART581 + PART582 + PART583 + PART584 + PART585 + PART586 \
    + PART587 + PART588 + PART589 + PART590 + PART591 + PART592 + PART593 \
    + PART594 + PART595 + PART596 + PART597 + PART598 + PART599 + PART600 \
    + PART601 + PART602 + PART603 + PART604 + PART605 + PART606 + PART607 \
    + PART608 + PART609 + PART610 + NA','<string>','eval'),
    #    
    'TSPx' : compile('(1e12/6.02E23)*((SEED_1*120) + (TSPNONORG*mwom) + (SEED*360) \
    + (PART1*184.26) + (PART2A*215.25) + (PART2B*215.25) + (PART3*215.25) \
    + (PART4*245.23) + (PART5*247.2) + (PART6*217.22) + (PART11*186.21) \
    + (PART13*186.21) + (PART14*168.23) + (PART15*170.21) + (PART16*184.23) \
    + (PART17*182.22) + (PART22*249.17) + (PART23*188.18) + (PART24*172.18) \
    + (PART25*170.21) + (PART26*218.28) + (PART27*186.28) + (PART28*174.22) \
    + (PART29*186.28) + (PART30*190.22) + (PART31*172.2) + (PART32*202.28) \
    + (PART33*178.21) + (PART34*200.26) + (PART35*200.26) + (PART36*188.25) \
    + (PART37*190.22) + (PART38*188.25) + (PART39*204.25) + (PART40*170.28) \
    + (PART41*172.25) + (PART42*184.26) + (PART43*220.25) + (PART44*170.28) \
    + (PART45*174.22) + (PART46*162.21) + (PART47*174.22) + (PART48*186.28) \
    + (PART49*186.23) + (NA*62.01) + (PART50*220.22) + (PART51*206.19) \
    + (PART52*164.11) + (PART53*178.14) + (PART54*235.19) + (PART55*204.22) \
    + (PART56*190.19) + (PART57*190.19) + (PART58*233.13) + (PART59*249.13) \
    + (PART60*261.23) + (PART61*176.17) + (PART62*204.22) + (PART63*294.13) \
    + (PART64*200.23) + (PART65*174.19) + (PART66*174.15) + (PART67*176.17) \
    + (PART68*219.15) + (PART69*245.23) + (PART70*205.17) + (PART71*216.23) \
    + (PART72*186.21) + (PART73*216.23) + (PART74*216.23) + (PART75*190.15) \
    + (PART76*233.22) + (PART77*162.14) + (PART78*188.22) + (PART79*162.14) \
    + (PART80*174.19) + (PART81*134.09) + (PART82*160.17) + (PART83*235.15) \
    + (PART84*188.22) + (PART85*172.18) + (PART86*134.09) + (PART87*261.23) \
    + (PART88*188.22) + (PART89*202.20) + (PART90*162.10) + (PART91*245.23) \
    + (PART92*245.23) + (PART93*247.20) + (PART94*174.15) + (PART95*174.15) \
    + (PART96*231.25) + (PART97*231.25) + (PART98*160.17) + (PART99*200.23) \
    + (PART100*191.14) + (PART101*207.10) + (PART102*188.18) + (PART103*188.14) \
    + (PART104*186.25) + (PART105*203.19) + (PART106*186.25) + (PART107*233.13) \
    + (PART108*200.23) + (PART109*200.23) + (PART110*200.23) + (PART111*200.23) \
    + (PART112*158.20) + (PART113*146.14) + (PART114*146.14) + (PART115*160.12) \
    + (PART116*174.19) + (PART117*160.12) + (PART118*186.25) + (PART119*132.12) \
    + (PART120*203.15) + (PART121*201.13) + (PART122*172.22) + (PART123*184.23) \
    + (PART124*215.25) + (PART125*174.19) + (PART126*229.23) + (PART127*184.23) \
    + (PART128*203.19) + (PART129*215.25) + (PART130*144.17) + (PART131*148.11) \
    + (PART132*170.21) + (PART133*158.15) + (PART134*215.25) + (PART135*215.25) \
    + (PART136*132.11) + (PART137*200.23) + (PART138*245.23) + (PART139*144.13) \
    + (PART140*170.25) + (PART141*193.11) + (PART142*184.23) + (PART143*184.23) \
    + (PART144*170.25) + (PART145*156.18) + (PART146*186.21) + (PART147*172.22) \
    + (PART148*134.09) + (PART149*213.23) + (PART150*213.23) + (PART151*158.20) \
    + (PART152*130.10) + (PART153*186.21) + (PART154*161.11) + (PART155*182.22) \
    + (PART156*231.20) + (PART157*116.07) + (PART158*146.10) + (PART159*173.17) \
    + (PART160*132.11) + (PART161*179.09) + (PART162*116.07) + (PART163*231.20) \
    + (PART164*158.20) + (PART165*191.10) + (PART166*201.22) + (PART167*156.14) \
    + (PART168*191.10) + (PART169*146.10) + (PART170*128.17) + (PART171*158.20) \
    + (PART172*168.23) + (PART173*132.07) + (PART174*116.12) + (PART175*156.22) \
    + (PART176*177.07) + (PART177*142.11) + (PART178*187.19) + (PART179*168.23) \
    + (PART180*126.15) + (PART181*142.20) + (PART182*114.10) + (PART183*154.21) \
    + (PART184*102.09) + (PART185*100.07) + (PART186*114.10) + (PART200*215.2463) \
    + (PART201*170.2487) + (PART202*186.2481) + (PART203*215.2463) + (PART204*186.2481) \
    + (PART205*215.2463) + (PART206*170.2487) + (PART207*186.2481)  + (PART209*144.1253) \
    + (PART210*160.1247) + (PART211*161.1128) + (PART212*116.1152) + (PART213*132.1146) \
    + (PART214*205.1223) + (PART215*130.0987) + (PART216*132.1146) + (PART217*148.114) \
    + (PART218*142.1094) + (PART219*128.0829) + (PART220*174.1082) + (PART221*146.0981) \
    + (PART222*219.1058) + (PART223*134.1305) + (PART224*179.1281) + (PART225*128.1259) \
    + (PART226*158.1519) + (PART227*174.1513) + (PART228*130.1418) + (PART229*146.1412) \
    + (PART230*219.1489) + (PART231*144.1253) + (PART232*160.1247) + (PART233*142.1525) \
    + (PART234*158.1519) + (PART235*174.1513) + (PART236*130.1418) + (PART237*146.1412) \
    + (PART238*219.1489) + (PART239*158.1519) + (PART240*174.1513) + (PART241*146.1412) \
    + (PART242*219.1489) + (PART243*126.11) + (PART244*128.1259) + (PART245*144.1253) \
    + (PART246*144.1253) + (PART247*160.1247) + (PART248*130.1418) + (PART249*162.1406) \
    + (PART250*207.1382) + (PART251*172.1785) + (PART252*188.1779) + (PART253*189.1659) \
    + (PART254*144.1684) + (PART255*160.1678) + (PART256*233.1754) + (PART257*170.1626) \
    + (PART258*200.1886) + (PART259*216.188) + (PART260*172.1785) + (PART261*188.1779) \
    + (PART262*261.1855) + (PART263*168.1898) + (PART264*154.1632) + (PART265*184.1892) \
    + (PART266*200.1886) + (PART267*156.1791) + (PART268*172.1785) + (PART269*245.1861) \
    + (PART270*110.1968) + (PART271*124.1803) + (PART272*171.1937) + (PART273*126.1962) \
    + (PART274*142.1956) + (PART275*182.1733) + (PART276*184.1892) + (PART277*200.1886) \
    + (PART278*215.2032) + (PART279*170.2057) + (PART280*186.2051) + (PART281*213.2026) \
    + (PART282*186.2051) + (PART283*202.2045) + (PART284*215.2032) + (PART285*170.2057) \
    + (PART286*186.2051) + (PART287*168.2328) + (PART288*200.2316) + (PART289*215.2032) \
    + (PART290*170.2057) + (PART291*186.2051) + (PART292*245.2292) + (PART293*231.2026) \
    + (PART294*186.2051) + (PART295*202.2045) + (PART296*152.1904) + (PART297*166.1739) \
    + (PART298*213.1873) + (PART299*168.1898) + (PART300*184.1892) + (PART301*142.1094) \
    + (PART302*114.0993) + (PART303*100.1158) + (PART304*116.1152) + (PART305*132.1146) \
    + (PART306*177.1122) + (PART307*134.1305) + (PART308*130.1418) + (PART309*231.2457) \
    + (PART310*231.2457) + (PART311*213.2304) + (PART312*245.2292) + (PART313*290.2268) \
    + (PART314*199.2038) + (PART315*154.2063) + (PART316*170.2057) + (PART317*152.1904) \
    + (PART318*199.2038) + (PART319*154.2063) + (PART320*170.2057) + (PART321*199.2038) \
    + (PART322*154.2063) + (PART323*170.2057) + (PART324*152.1904) + (PART325*154.2063) \
    + (PART326*170.2057) + (PART327*138.2069) + (PART350*82.1005) + (PART351*102.1317) \
    + (PART352*102.1317) + (PART353*112.0835) + (PART354*114.0993) + (PART355*114.0993) \
    + (PART356*114.1424) + (PART357*114.1424) + (PART358*116.1152) + (PART359*116.1152) \
    + (PART360*116.1152) + (PART361*116.1152) + (PART362*116.1152) + (PART363*116.1152) \
    + (PART364*116.1152) + (PART365*116.1583) + (PART366*116.1583) + (PART367*118.1311) \
    + (PART368*118.1311) + (PART369*118.1311) + (PART370*118.1311) + (PART371*118.1311) \
    + (PART372*118.1311) + (PART373*128.0829) + (PART374*128.1259) + (PART375*128.1259) \
    + (PART376*128.169) + (PART377*128.169) + (PART378*130.0987) + (PART379*130.0987) \
    + (PART380*130.0987) + (PART381*130.1418) + (PART382*130.1418) + (PART383*130.1418) \
    + (PART384*130.1418) + (PART385*132.1146) + (PART386*132.1146) + (PART387*132.1146) \
    + (PART388*132.1146) + (PART389*132.1146) + (PART390*132.1146) + (PART391*132.1146) \
    + (PART392*132.1577) + (PART393*132.1577) + (PART394*134.1305) + (PART395*134.1305) \
    + (PART396*134.1305) + (PART397*134.1305) + (PART398*138.2069) + (PART399*140.1797) \
    + (PART400*140.1797) + (PART401*142.1525) + (PART402*142.1525) + (PART403*142.1525) \
    + (PART404*142.1956) + (PART405*144.1684) + (PART406*144.1684) + (PART407*144.1684) \
    + (PART408*144.1684) + (PART409*146.0981) + (PART410*146.0981) + (PART411*146.0981) \
    + (PART412*146.1412) + (PART413*146.1412) + (PART414*146.1412) + (PART415*146.1412) \
    + (PART416*146.1412) + (PART417*146.1412) + (PART418*146.1412) + (PART419*147.1293) \
    + (PART420*147.1293) + (PART421*148.114) + (PART422*148.114) + (PART423*148.114) \
    + (PART424*148.114) + (PART425*148.114) + (PART426*148.114) + (PART427*148.1571) \
    + (PART428*148.1571) + (PART429*150.1299) + (PART430*150.1299) + (PART431*150.1299) \
    + (PART432*150.1299) + (PART433*150.1299) + (PART434*154.2063) + (PART435*156.1791) \
    + (PART436*156.1791) + (PART437*156.1791) + (PART438*156.1791) + (PART439*156.2221) \
    + (PART440*158.195) + (PART441*158.195) + (PART442*158.195) + (PART443*158.195) \
    + (PART444*160.1247) + (PART445*160.1678) + (PART446*160.1678) + (PART447*160.1678) \
    + (PART448*160.1678) + (PART449*160.1678) + (PART450*160.1678) + (PART451*161.1558) \
    + (PART452*161.1558) + (PART453*162.0975) + (PART454*162.0975) + (PART455*162.1406) \
    + (PART456*162.1406) + (PART457*162.1406) + (PART458*162.1406) + (PART459*162.1837) \
    + (PART460*163.0856) + (PART461*163.1287) + (PART462*164.1134) + (PART463*164.1565) \
    + (PART464*164.1565) + (PART465*166.1293) + (PART466*166.1293) + (PART467*168.2328) \
    + (PART468*170.2057) + (PART469*170.2057) + (PART470*172.1785) + (PART471*172.1785) \
    + (PART472*172.2215) + (PART473*172.2215) + (PART474*173.1665) + (PART475*174.1513) \
    + (PART476*174.1513) + (PART477*174.1513) + (PART478*174.1513) + (PART479*174.1513) \
    + (PART480*174.1944) + (PART481*174.1944) + (PART482*174.1944) + (PART483*175.0963) \
    + (PART484*175.0963) + (PART485*175.1394) + (PART486*176.1672) + (PART487*176.1672) \
    + (PART488*176.1672) + (PART489*177.1122) + (PART490*177.1122) + (PART491*177.1122) \
    + (PART492*177.1122) + (PART493*177.1122) + (PART494*177.1122) + (PART495*178.1831) \
    + (PART496*179.1281) + (PART497*179.1281) + (PART498*179.1281) + (PART499*179.1281) \
    + (PART500*179.1281) + (PART501*180.1128) + (PART502*180.1128) + (PART503*181.1439) \
    + (PART504*181.1439) + (PART505*182.0426) + (PART506*182.2164) + (PART507*184.1892) \
    + (PART508*184.1892) + (PART509*186.2051) + (PART510*186.2051) + (PART511*186.2051) \
    + (PART512*186.2051) + (PART513*187.1931) + (PART514*188.1779) + (PART515*188.1779) \
    + (PART516*188.2209) + (PART517*189.1659) + (PART518*190.1938) + (PART519*190.1938) \
    + (PART520*191.1388) + (PART521*192.1666) + (PART522*193.1116) + (PART523*193.1116) \
    + (PART524*193.1116) + (PART525*193.1116) + (PART526*193.1116) + (PART527*193.1546) \
    + (PART528*193.1546) + (PART529*195.1275) + (PART530*195.1275) + (PART531*195.1275) \
    + (PART532*195.1275) + (PART533*197.1433) + (PART534*197.1433) + (PART535*198.1281) \
    + (PART536*200.2316) + (PART537*201.2197) + (PART538*202.2045) + (PART539*202.2045) \
    + (PART540*202.2045) + (PART541*202.2045) + (PART542*202.2045) + (PART543*203.1925) \
    + (PART544*203.1925) + (PART545*204.1773) + (PART546*204.1773) + (PART547*205.1223) \
    + (PART548*205.1653) + (PART549*205.1653) + (PART550*205.1653) + (PART551*207.0951) \
    + (PART552*207.1382) + (PART553*207.1382) + (PART554*207.1812) + (PART555*207.1812) \
    + (PART556*207.1812) + (PART557*207.1812) + (PART558*209.111) + (PART559*209.111) \
    + (PART560*209.111) + (PART561*209.154) + (PART562*211.1269) + (PART563*211.1269) \
    + (PART564*211.1269) + (PART565*217.176) + (PART566*217.2191) + (PART567*219.1489) \
    + (PART568*219.1489) + (PART569*219.1919) + (PART570*219.1919) + (PART571*223.1806) \
    + (PART572*223.1806) + (PART573*224.0826) + (PART574*224.0826) + (PART575*224.1256) \
    + (PART576*224.1256) + (PART577*224.1256) + (PART578*226.0984) + (PART579*226.0984) \
    + (PART580*226.1415) + (PART581*226.1415) + (PART582*227.1263) + (PART583*231.2026) \
    + (PART584*231.2026) + (PART585*231.2457) + (PART586*233.1754) + (PART587*233.1754) \
    + (PART588*233.2185) + (PART589*235.1913) + (PART590*240.125) + (PART591*240.125) \
    + (PART592*240.125) + (PART593*243.1257) + (PART594*247.202) + (PART595*247.2451) \
    + (PART596*247.2451) + (PART597*254.1085) + (PART598*254.1085) + (PART599*254.1085) \
    + (PART600*256.1244) + (PART601*256.1244) + (PART602*256.1244) + (PART603*256.1244) \
    + (PART604*256.1244) + (PART605*256.1244) + (PART606*263.2445) + (PART607*272.1238) \
    + (PART608*301.122) + (PART609*301.122) + (PART610*301.122) + (NA*62.1))','<string>','eval'),
    #
    'acidsum' : compile('LIMONONIC + LIMONIC + KLIMONONIC + KLIMONIC + C731CO2H + C822CO2H \
    + HOPINONIC + H3C25CCO2H + PINIC + NORPINIC + H3C2C4CO2H + PINONIC \
    + C89CO2H + PERPINONIC + CO13C3CO2H + C512CO2H + C615CO2H + C617CO2H \
    + C618CO2H + C718CO2H + C87CO2H + C88CO2H + CO1M22CO2H + MC3ODBCO2H \
    + HC4CCO2H + HC4ACO2H + CO2C4CO2H + C518CO2H + HMVKBCO2H + C624CO2H \
    + C622CO2H + C23O3CCO2H + C519CO2H + C517CO2H + C729CO2H + CONM2CO2H \
    + MMALNBCO2H + MMALNACO2H + C58NO3CO2H + C57NO3CO2H + INCNCO2H \
    + INB1NBCO2H + INB1NACO2H','<string>','eval'),
    #
    'mwomv' : compile('(1e12/6.02E23)*((TSPNONORG/TSPx*mwom**2) +\
    (SEED_1/TSPx*120**2) + (SEED/TSPx*360**2) +\
    (PART1/TSPx*184.26**2) + (PART2A/TSPx*215.25**2) +\
    (PART2B/TSPx*215.25**2) + (PART3/TSPx*215.25**2) +\
    (PART4/TSPx*245.23**2) + (PART5/TSPx*247.2**2) +\
    (PART6/TSPx*217.22**2) + (PART11/TSPx*186.21**2) +\
    (PART13/TSPx*186.21**2) + (PART14/TSPx*168.23**2) +\
    (PART15/TSPx*170.21**2) + (PART16/TSPx*184.23**2) +\
    (PART17/TSPx*182.22**2) + (PART22/TSPx*249.17**2) +\
    (PART23/TSPx*188.18**2) + (PART24/TSPx*172.18**2) +\
    (PART25/TSPx*170.21**2) + (PART26/TSPx*218.28**2) +\
    (PART27/TSPx*186.28**2) + (PART28/TSPx*174.22**2) +\
    (PART29/TSPx*186.28**2) + (PART30/TSPx*190.22**2) +\
    (PART31/TSPx*172.2**2) + (PART32/TSPx*202.28**2) +\
    (PART33/TSPx*178.21**2) + (PART34/TSPx*200.26**2) +\
    (PART35/TSPx*200.26**2) + (PART36/TSPx*188.25**2) +\
    (PART37/TSPx*190.22**2) + (PART38/TSPx*188.25**2) +\
    (PART39/TSPx*204.25**2) + (PART40/TSPx*170.28**2) +\
    (PART41/TSPx*172.25**2) + (PART42/TSPx*184.26**2) +\
    (PART43/TSPx*220.25**2) + (PART44/TSPx*170.28**2) +\
    (PART45/TSPx*174.22**2) + (PART46/TSPx*162.21**2) +\
    (PART47/TSPx*174.22**2) + (PART48/TSPx*186.28**2) +\
    (PART49/TSPx*186.23**2) + (PART50/TSPx*220.22**2) +\
    (PART51/TSPx*206.19**2) + (PART52/TSPx*164.11**2) +\
    (PART53/TSPx*178.14**2) + (PART54/TSPx*235.19**2) +\
    (PART55/TSPx*204.22**2) + (PART56/TSPx*190.19**2) +\
    (PART57/TSPx*190.19**2) + (PART58/TSPx*233.13**2) +\
    (PART59/TSPx*249.13**2) + (PART60/TSPx*261.23**2) +\
    (PART61/TSPx*176.17**2) + (PART62/TSPx*204.22**2) +\
    (PART63/TSPx*294.13**2) + (PART64/TSPx*200.23**2) +\
    (PART65/TSPx*174.19**2) + (PART66/TSPx*174.15**2) +\
    (PART67/TSPx*176.17**2) + (PART68/TSPx*219.15**2) +\
    (PART69/TSPx*245.23**2) + (PART70/TSPx*205.17**2) +\
    (PART71/TSPx*216.23**2) + (PART72/TSPx*186.21**2) +\
    (PART73/TSPx*216.23**2) + (PART74/TSPx*216.23**2) +\
    (PART75/TSPx*190.15**2) + (PART76/TSPx*233.22**2) +\
    (PART77/TSPx*162.14**2) + (PART78/TSPx*188.22**2) +\
    (PART79/TSPx*162.14**2) + (PART80/TSPx*174.19**2) +\
    (PART81/TSPx*134.09**2) + (PART82/TSPx*160.17**2) +\
    (PART83/TSPx*235.15**2) + (PART84/TSPx*188.22**2) +\
    (PART85/TSPx*172.18**2) + (PART86/TSPx*134.09**2) +\
    (PART87/TSPx*261.23**2) + (PART88/TSPx*188.22**2) +\
    (PART89/TSPx*202.20**2) + (PART90/TSPx*162.10**2) +\
    (PART91/TSPx*245.23**2) + (PART92/TSPx*245.23**2) +\
    (PART93/TSPx*247.20**2) + (PART94/TSPx*174.15**2) +\
    (PART95/TSPx*174.15**2) + (PART96/TSPx*231.25**2) +\
    (PART97/TSPx*231.25**2) + (PART98/TSPx*160.17**2) +\
    (PART99/TSPx*200.23**2) + (PART100/TSPx*191.14**2) +\
    (PART101/TSPx*207.10**2) + (PART102/TSPx*188.18**2) +\
    (PART103/TSPx*188.14**2) + (PART104/TSPx*186.25**2) +\
    (PART105/TSPx*203.19**2) + (PART106/TSPx*186.25**2) +\
    (PART107/TSPx*233.13**2) + (PART108/TSPx*200.23**2) +\
    (PART109/TSPx*200.23**2) + (PART110/TSPx*200.23**2) +\
    (PART111/TSPx*200.23**2) + (PART112/TSPx*158.20**2) +\
    (PART113/TSPx*146.14**2) + (PART114/TSPx*146.14**2) +\
    (PART115/TSPx*160.12**2) + (PART116/TSPx*174.19**2) +\
    (PART117/TSPx*160.12**2) + (PART118/TSPx*186.25**2) +\
    (PART119/TSPx*132.12**2) + (PART120/TSPx*203.15**2) +\
    (PART121/TSPx*201.13**2) + (PART122/TSPx*172.22**2) +\
    (PART123/TSPx*184.23**2) + (PART124/TSPx*215.25**2) +\
    (PART125/TSPx*174.19**2) + (PART126/TSPx*229.23**2) +\
    (PART127/TSPx*184.23**2) + (PART128/TSPx*203.19**2) +\
    (PART129/TSPx*215.25**2) + (PART130/TSPx*144.17**2) +\
    (PART131/TSPx*148.11**2) + (PART132/TSPx*170.21**2) +\
    (PART133/TSPx*158.15**2) + (PART134/TSPx*215.25**2) +\
    (PART135/TSPx*215.25**2) + (PART136/TSPx*132.11**2) +\
    (PART137/TSPx*200.23**2) + (PART138/TSPx*245.23**2) +\
    (PART139/TSPx*144.13**2) + (PART140/TSPx*170.25**2) +\
    (PART141/TSPx*193.11**2) + (PART142/TSPx*184.23**2) +\
    (PART143/TSPx*184.23**2) + (PART144/TSPx*170.25**2) +\
    (PART145/TSPx*156.18**2) + (PART146/TSPx*186.21**2) +\
    (PART147/TSPx*172.22**2) + (PART148/TSPx*134.09**2) +\
    (PART149/TSPx*213.23**2) + (PART150/TSPx*213.23**2) +\
    (PART151/TSPx*158.20**2) + (PART152/TSPx*130.10**2) +\
    (PART153/TSPx*186.21**2) + (PART154/TSPx*161.11**2) +\
    (PART155/TSPx*182.22**2) + (PART156/TSPx*231.20**2) +\
    (PART157/TSPx*116.07**2) + (PART158/TSPx*146.10**2) +\
    (PART159/TSPx*173.17**2) + (PART160/TSPx*132.11**2) +\
    (PART161/TSPx*179.09**2) + (PART162/TSPx*116.07**2) +\
    (PART163/TSPx*231.20**2) + (PART164/TSPx*158.20**2) +\
    (PART165/TSPx*191.10**2) + (PART166/TSPx*201.22**2) +\
    (PART167/TSPx*156.14**2) + (PART168/TSPx*191.10**2) +\
    (PART169/TSPx*146.10**2) + (PART170/TSPx*128.17**2) +\
    (PART171/TSPx*158.20**2) + (PART172/TSPx*168.23**2) +\
    (PART173/TSPx*132.07**2) + (PART174/TSPx*116.12**2) +\
    (PART175/TSPx*156.22**2) + (PART176/TSPx*177.07**2) +\
    (PART177/TSPx*142.11**2) + (PART178/TSPx*187.19**2) +\
    (PART179/TSPx*168.23**2) + (PART180/TSPx*126.15**2) +\
    (PART181/TSPx*142.20**2) + (PART182/TSPx*114.10**2) +\
    (PART183/TSPx*154.21**2) + (PART184/TSPx*102.09**2) +\
    (PART185/TSPx*100.07**2) + (PART186/TSPx*114.10**2) +\
    (PART200/TSPx*215.2463**2) + (PART201/TSPx*170.2487**2) +\
    (PART202/TSPx*186.2481**2) + (PART203/TSPx*215.2463**2) +\
    (PART204/TSPx*186.2481**2) + (PART205/TSPx*215.2463**2) +\
    (PART206/TSPx*170.2487**2) + (PART207/TSPx*186.2481**2) +\
    (PART209/TSPx*144.1253**2) + (PART210/TSPx*160.1247**2) +\
    (PART211/TSPx*161.1128**2) + (PART212/TSPx*116.1152**2) +\
    (PART213/TSPx*132.1146**2) + (PART214/TSPx*205.1223**2) +\
    (PART215/TSPx*130.0987**2) + (PART216/TSPx*132.1146**2) +\
    (PART217/TSPx*148.114**2) + (PART218/TSPx*142.1094**2) +\
    (PART219/TSPx*128.0829**2) + (PART220/TSPx*174.1082**2) +\
    (PART221/TSPx*146.0981**2) + (PART222/TSPx*219.1058**2) +\
    (PART223/TSPx*134.1305**2) + (PART224/TSPx*179.1281**2) +\
    (PART225/TSPx*128.1259**2) + (PART226/TSPx*158.1519**2) +\
    (PART227/TSPx*174.1513**2) + (PART228/TSPx*130.1418**2) +\
    (PART229/TSPx*146.1412**2) + (PART230/TSPx*219.1489**2) +\
    (PART231/TSPx*144.1253**2) + (PART232/TSPx*160.1247**2) +\
    (PART233/TSPx*142.1525**2) + (PART234/TSPx*158.1519**2) +\
    (PART235/TSPx*174.1513**2) + (PART236/TSPx*130.1418**2) +\
    (PART237/TSPx*146.1412**2) + (PART238/TSPx*219.1489**2) +\
    (PART239/TSPx*158.1519**2) + (PART240/TSPx*174.1513**2) +\
    (PART241/TSPx*146.1412**2) + (PART242/TSPx*219.1489**2) +\
    (PART243/TSPx*126.11**2) + (PART244/TSPx*128.1259**2) +\
    (PART245/TSPx*144.1253**2) + (PART246/TSPx*144.1253**2) +\
    (PART247/TSPx*160.1247**2) + (PART248/TSPx*130.1418**2) +\
    (PART249/TSPx*162.1406**2) + (PART250/TSPx*207.1382**2) +\
    (PART251/TSPx*172.1785**2) + (PART252/TSPx*188.1779**2) +\
    (PART253/TSPx*189.1659**2) + (PART254/TSPx*144.1684**2) +\
    (PART255/TSPx*160.1678**2) + (PART256/TSPx*233.1754**2) +\
    (PART257/TSPx*170.1626**2) + (PART258/TSPx*200.1886**2) +\
    (PART259/TSPx*216.188**2) + (PART260/TSPx*172.1785**2) +\
    (PART261/TSPx*188.1779**2) + (PART262/TSPx*261.1855**2) +\
    (PART263/TSPx*168.1898**2) + (PART264/TSPx*154.1632**2)+\
    (PART265/TSPx*184.1892**2) + (PART266/TSPx*200.1886**2) +\
    (PART267/TSPx*156.1791**2) + (PART268/TSPx*172.1785**2) +\
    (PART269/TSPx*245.1861**2) + (PART270/TSPx*110.1968**2) +\
    (PART271/TSPx*124.1803**2) + (PART272/TSPx*171.1937**2) +\
    (PART273/TSPx*126.1962**2) + (PART274/TSPx*142.1956**2) +\
    (PART275/TSPx*182.1733**2) + (PART276/TSPx*184.1892**2) +\
    (PART277/TSPx*200.1886**2) + (PART278/TSPx*215.2032**2) +\
    (PART279/TSPx*170.2057**2) + (PART280/TSPx*186.2051**2) +\
    (PART281/TSPx*213.2026**2) + (PART282/TSPx*186.2051**2) +\
    (PART283/TSPx*202.2045**2) + (PART284/TSPx*215.2032**2) +\
    (PART285/TSPx*170.2057**2) + (PART286/TSPx*186.2051**2) +\
    (PART287/TSPx*168.2328**2) + (PART288/TSPx*200.2316**2) +\
    (PART289/TSPx*215.2032**2) + (PART290/TSPx*170.2057**2) +\
    (PART291/TSPx*186.2051**2) + (PART292/TSPx*245.2292**2) +\
    (PART293/TSPx*231.2026**2) + (PART294/TSPx*186.2051**2) +\
    (PART295/TSPx*202.2045**2) + (PART296/TSPx*152.1904**2) +\
    (PART297/TSPx*166.1739**2) + (PART298/TSPx*213.1873**2) +\
    (PART299/TSPx*168.1898**2) + (PART300/TSPx*184.1892**2) +\
    (PART301/TSPx*142.1094**2) + (PART302/TSPx*114.0993**2) +\
    (PART303/TSPx*100.1158**2) + (PART304/TSPx*116.1152**2) +\
    (PART305/TSPx*132.1146**2) + (PART306/TSPx*177.1122**2) +\
    (PART307/TSPx*134.1305**2) + (PART308/TSPx*130.1418**2) +\
    (PART309/TSPx*231.2457**2) + (PART310/TSPx*231.2457**2) +\
    (PART311/TSPx*213.2304**2) + (PART312/TSPx*245.2292**2) +\
    (PART313/TSPx*290.2268**2) + (PART314/TSPx*199.2038**2) +\
    (PART315/TSPx*154.2063**2) + (PART316/TSPx*170.2057**2) +\
    (PART317/TSPx*152.1904**2) + (PART318/TSPx*199.2038**2) +\
    (PART319/TSPx*154.2063**2) + (PART320/TSPx*170.2057**2) +\
    (PART321/TSPx*199.2038**2) + (PART322/TSPx*154.2063**2) +\
    (PART323/TSPx*170.2057**2) + (PART324/TSPx*152.1904**2) +\
    (PART325/TSPx*154.2063**2) + (PART326/TSPx*170.2057**2) +\
    (PART327/TSPx*138.2069**2) + (PART350/TSPx*82.1005**2) +\
    (PART351/TSPx*102.1317**2) + (PART352/TSPx*102.1317**2) +\
    (PART353/TSPx*112.0835**2) + (PART354/TSPx*114.0993**2) +\
    (PART355/TSPx*114.0993**2) + (PART356/TSPx*114.1424**2) +\
    (PART357/TSPx*114.1424**2) + (PART358/TSPx*116.1152**2) +\
    (PART359/TSPx*116.1152**2) + (PART360/TSPx*116.1152**2) +\
    (PART361/TSPx*116.1152**2) + (PART362/TSPx*116.1152**2) +\
    (PART363/TSPx*116.1152**2) + (PART364/TSPx*116.1152**2) +\
    (PART365/TSPx*116.1583**2) + (PART366/TSPx*116.1583**2) +\
    (PART367/TSPx*118.1311**2) + (PART368/TSPx*118.1311**2) +\
    (PART369/TSPx*118.1311**2) + (PART370/TSPx*118.1311**2) +\
    (PART371/TSPx*118.1311**2) + (PART372/TSPx*118.1311**2) +\
    (PART373/TSPx*128.0829**2) + (PART374/TSPx*128.1259**2) +\
    (PART375/TSPx*128.1259**2) + (PART376/TSPx*128.169**2) +\
    (PART377/TSPx*128.169**2) + (PART378/TSPx*130.0987**2) +\
    (PART379/TSPx*130.0987**2) + (PART380/TSPx*130.0987**2) +\
    (PART381/TSPx*130.1418**2) + (PART382/TSPx*130.1418**2) +\
    (PART383/TSPx*130.1418**2) + (PART384/TSPx*130.1418**2) +\
    (PART385/TSPx*132.1146**2) + (PART386/TSPx*132.1146**2) +\
    (PART387/TSPx*132.1146**2) + (PART388/TSPx*132.1146**2) +\
    (PART389/TSPx*132.1146**2) + (PART390/TSPx*132.1146**2) +\
    (PART391/TSPx*132.1146**2) + (PART392/TSPx*132.1577**2) +\
    (PART393/TSPx*132.1577**2) + (PART394/TSPx*134.1305**2) +\
    (PART395/TSPx*134.1305**2) + (PART396/TSPx*134.1305**2) +\
    (PART397/TSPx*134.1305**2) + (PART398/TSPx*138.2069**2) +\
    (PART399/TSPx*140.1797**2) + (PART400/TSPx*140.1797**2) +\
    (PART401/TSPx*142.1525**2) + (PART402/TSPx*142.1525**2) +\
    (PART403/TSPx*142.1525**2) + (PART404/TSPx*142.1956**2) +\
    (PART405/TSPx*144.1684**2) + (PART406/TSPx*144.1684**2) +\
    (PART407/TSPx*144.1684**2) + (PART408/TSPx*144.1684**2) +\
    (PART409/TSPx*146.0981**2) + (PART410/TSPx*146.0981**2) +\
    (PART411/TSPx*146.0981**2) + (PART412/TSPx*146.1412**2) +\
    (PART413/TSPx*146.1412**2) + (PART414/TSPx*146.1412**2) +\
    (PART415/TSPx*146.1412**2) + (PART416/TSPx*146.1412**2) +\
    (PART417/TSPx*146.1412**2) + (PART418/TSPx*146.1412**2) +\
    (PART419/TSPx*147.1293**2) + (PART420/TSPx*147.1293**2) +\
    (PART421/TSPx*148.114**2) + (PART422/TSPx*148.114**2) +\
    (PART423/TSPx*148.114**2) + (PART424/TSPx*148.114**2) +\
    (PART425/TSPx*148.114**2) + (PART426/TSPx*148.114**2) +\
    (PART427/TSPx*148.1571**2) + (PART428/TSPx*148.1571**2) +\
    (PART429/TSPx*150.1299**2) + (PART430/TSPx*150.1299**2) +\
    (PART431/TSPx*150.1299**2) + (PART432/TSPx*150.1299**2) +\
    (PART433/TSPx*150.1299**2) + (PART434/TSPx*154.2063**2) +\
    (PART435/TSPx*156.1791**2) + (PART436/TSPx*156.1791**2) +\
    (PART437/TSPx*156.1791**2) + (PART438/TSPx*156.1791**2) +\
    (PART439/TSPx*156.2221**2) + (PART440/TSPx*158.195**2) +\
    (PART441/TSPx*158.195**2) + (PART442/TSPx*158.195**2) +\
    (PART443/TSPx*158.195**2) + (PART444/TSPx*160.1247**2) +\
    (PART445/TSPx*160.1678**2) + (PART446/TSPx*160.1678**2) +\
    (PART447/TSPx*160.1678**2) + (PART448/TSPx*160.1678**2) +\
    (PART449/TSPx*160.1678**2) + (PART450/TSPx*160.1678**2) +\
    (PART451/TSPx*161.1558**2) + (PART452/TSPx*161.1558**2) +\
    (PART453/TSPx*162.0975**2) + (PART454/TSPx*162.0975**2) +\
    (PART455/TSPx*162.1406**2) + (PART456/TSPx*162.1406**2) +\
    (PART457/TSPx*162.1406**2) + (PART458/TSPx*162.1406**2) +\
    (PART459/TSPx*162.1837**2) + (PART460/TSPx*163.0856**2) +\
    (PART461/TSPx*163.1287**2) + (PART462/TSPx*164.1134**2) +\
    (PART463/TSPx*164.1565**2) + (PART464/TSPx*164.1565**2) +\
    (PART465/TSPx*166.1293**2) + (PART466/TSPx*166.1293**2) +\
    (PART467/TSPx*168.2328**2) + (PART468/TSPx*170.2057**2) +\
    (PART469/TSPx*170.2057**2) + (PART470/TSPx*172.1785**2) +\
    (PART471/TSPx*172.1785**2) + (PART472/TSPx*172.2215**2) +\
    (PART473/TSPx*172.2215**2) + (PART474/TSPx*173.1665**2) +\
    (PART475/TSPx*174.1513**2) + (PART476/TSPx*174.1513**2) +\
    (PART477/TSPx*174.1513**2) + (PART478/TSPx*174.1513**2) +\
    (PART479/TSPx*174.1513**2) + (PART480/TSPx*174.1944**2) +\
    (PART481/TSPx*174.1944**2) + (PART482/TSPx*174.1944**2) +\
    (PART483/TSPx*175.0963**2) + (PART484/TSPx*175.0963**2) +\
    (PART485/TSPx*175.1394**2) + (PART486/TSPx*176.1672**2) +\
    (PART487/TSPx*176.1672**2) + (PART488/TSPx*176.1672**2) +\
    (PART489/TSPx*177.1122**2) + (PART490/TSPx*177.1122**2) +\
    (PART491/TSPx*177.1122**2) + (PART492/TSPx*177.1122**2) +\
    (PART493/TSPx*177.1122**2) + (PART494/TSPx*177.1122**2) +\
    (PART495/TSPx*178.1831**2) + (PART496/TSPx*179.1281**2) +\
    (PART497/TSPx*179.1281**2) + (PART498/TSPx*179.1281**2) +\
    (PART499/TSPx*179.1281**2) + (PART500/TSPx*179.1281**2) +\
    (PART501/TSPx*180.1128**2) + (PART502/TSPx*180.1128**2) +\
    (PART503/TSPx*181.1439**2) + (PART504/TSPx*181.1439**2) +\
    (PART505/TSPx*182.0426**2) + (PART506/TSPx*182.2164**2) +\
    (PART507/TSPx*184.1892**2) + (PART508/TSPx*184.1892**2) +\
    (PART509/TSPx*186.2051**2) + (PART510/TSPx*186.2051**2) +\
    (PART511/TSPx*186.2051**2) + (PART512/TSPx*186.2051**2) +\
    (PART513/TSPx*187.1931**2) + (PART514/TSPx*188.1779**2) +\
    (PART515/TSPx*188.1779**2) + (PART516/TSPx*188.2209**2) +\
    (PART517/TSPx*189.1659**2) + (PART518/TSPx*190.1938**2) +\
    (PART519/TSPx*190.1938**2) + (PART520/TSPx*191.1388**2) +\
    (PART521/TSPx*192.1666**2) + (PART522/TSPx*193.1116**2) +\
    (PART523/TSPx*193.1116**2) + (PART524/TSPx*193.1116**2) +\
    (PART525/TSPx*193.1116**2) + (PART526/TSPx*193.1116**2) +\
    (PART527/TSPx*193.1546**2) + (PART528/TSPx*193.1546**2) +\
    (PART529/TSPx*195.1275**2) + (PART530/TSPx*195.1275**2) +\
    (PART531/TSPx*195.1275**2) + (PART532/TSPx*195.1275**2) +\
    (PART533/TSPx*197.1433**2) + (PART534/TSPx*197.1433**2) +\
    (PART535/TSPx*198.1281**2) + (PART536/TSPx*200.2316**2) +\
    (PART537/TSPx*201.2197**2) + (PART538/TSPx*202.2045**2) +\
    (PART539/TSPx*202.2045**2) + (PART540/TSPx*202.2045**2) +\
    (PART541/TSPx*202.2045**2) + (PART542/TSPx*202.2045**2) +\
    (PART543/TSPx*203.1925**2) + (PART544/TSPx*203.1925**2) +\
    (PART545/TSPx*204.1773**2) + (PART546/TSPx*204.1773**2) +\
    (PART547/TSPx*205.1223**2) + (PART548/TSPx*205.1653**2) +\
    (PART549/TSPx*205.1653**2) + (PART550/TSPx*205.1653**2) +\
    (PART551/TSPx*207.0951**2) + (PART552/TSPx*207.1382**2) +\
    (PART553/TSPx*207.1382**2) + (PART554/TSPx*207.1812**2) +\
    (PART555/TSPx*207.1812**2) + (PART556/TSPx*207.1812**2) +\
    (PART557/TSPx*207.1812**2) + (PART558/TSPx*209.111**2) +\
    (PART559/TSPx*209.111**2) + (PART560/TSPx*209.111**2) +\
    (PART561/TSPx*209.154**2) + (PART562/TSPx*211.1269**2) +\
    (PART563/TSPx*211.1269**2) + (PART564/TSPx*211.1269**2) +\
    (PART565/TSPx*217.176**2) + (PART566/TSPx*217.2191**2) +\
    (PART567/TSPx*219.1489**2) + (PART568/TSPx*219.1489**2) +\
    (PART569/TSPx*219.1919**2) + (PART570/TSPx*219.1919**2) +\
    (PART571/TSPx*223.1806**2) + (PART572/TSPx*223.1806**2) +\
    (PART573/TSPx*224.0826**2) + (PART574/TSPx*224.0826**2) +\
    (PART575/TSPx*224.1256**2) + (PART576/TSPx*224.1256**2) +\
    (PART577/TSPx*224.1256**2) + (PART578/TSPx*226.0984**2) +\
    (PART579/TSPx*226.0984**2) + (PART580/TSPx*226.1415**2) +\
    (PART581/TSPx*226.1415**2) + (PART582/TSPx*227.1263**2) +\
    (PART583/TSPx*231.2026**2) + (PART584/TSPx*231.2026**2) +\
    (PART585/TSPx*231.2457**2) + (PART586/TSPx*233.1754**2) +\
    (PART587/TSPx*233.1754**2) + (PART588/TSPx*233.2185**2) +\
    (PART589/TSPx*235.1913**2) + (PART590/TSPx*240.125**2) +\
    (PART591/TSPx*240.125**2) + (PART592/TSPx*240.125**2) +\
    (PART593/TSPx*243.1257**2) + (PART594/TSPx*247.202**2) +\
    (PART595/TSPx*247.2451**2) + (PART596/TSPx*247.2451**2) +\
    (PART597/TSPx*254.1085**2) + (PART598/TSPx*254.1085**2) +\
    (PART599/TSPx*254.1085**2) + (PART600/TSPx*256.1244**2) +\
    (PART601/TSPx*256.1244**2) + (PART602/TSPx*256.1244**2) +\
    (PART603/TSPx*256.1244**2) + (PART604/TSPx*256.1244**2) +\
    (PART605/TSPx*256.1244**2) + (PART606/TSPx*263.2445**2) +\
    (PART607/TSPx*272.1238**2) + (PART608/TSPx*301.122**2) +\
    (PART609/TSPx*301.122**2) + (PART610/TSPx*301.122**2) +\
    (NA/TSPx*62.01**2))','<string>','eval'),
    #
    "soacalc" : compile("TSPx-(NA*62.01*1e12/6.02E23)",'<string>','eval')}
    return part_calc_dict

def particle_import():
    '''
    Importing the particle chemistry, not from the MCM download. Created by 
    Nic Carslaw as part of the INDCM 
    
    returns:
        particle_species = list of particle species
        particle_reactions = dictionary of particle reactions
        particle_vapour_pressure = dictionary of particle vapour pressures
        part_calc_dict = dictionary of compiled summations used in particle calculations
    '''
    particle_species = particle_species_def()
    particle_reactions = particle_reactions_in()
    particle_vapour_pressure=part_vap_pres()
    part_calc_dict=particle_calc_dict()   
    return particle_species,particle_reactions,particle_vapour_pressure,part_calc_dict

def particle_calcs(part_calc_dict,density_dict):
    '''
    calculations specific to the particles during the integration
    
    inputs:
        part_calc_dict = dictionary of compiled summations used in particle calculations
        density_dict = dictionary of current concentrations
        
    returns:
        particle_dict = dictionary of constants and calculated values for use in
                        particle calculations
    '''
    particle_dict={'mwom' : 120,
               'ACTIVITY' : 1,
               'SCALINGFAC' : 120}
    particle_dict['acidsum'] = eval(part_calc_dict['acidsum'],density_dict,particle_dict)
    particle_dict['TSP'] = eval(part_calc_dict['TSP'],density_dict,particle_dict)
    particle_dict['TSPx'] =  eval(part_calc_dict['TSPx'],density_dict,particle_dict)
    particle_dict['mwomv'] = eval(part_calc_dict['mwomv'],density_dict,particle_dict)
    particle_dict['soacalc'] = eval(part_calc_dict['soacalc'],density_dict,particle_dict)

    return particle_dict


def reactions_check(reactions_numba,particle_reactions,species):
    '''
    Need to check that species in the particle reactions actually exist in the species list
    and remove reactions that don't
    
    inputs:
        reactions_numba = full list of included chemical reactions [rate, reaction]
                          with reaction calculations in numba format
        particle_reactions = dictionary of particle reactions
        species = list of species
        
    returns:
        reactions_numba = full list of included chemical reactions [rate, reaction]
                          with reaction calculations in numba format
    '''
    temp=[]
    particle_reactions_temp=[]
    for i,s in enumerate(particle_reactions):
        temp.append(re.split('[=+]',s[1]))
        if set(temp[i]).issubset(species + ['TSP','RO2','O2','N2','']):
            particle_reactions_temp.append(s)
    reactions_numba = reactions_numba + particle_reactions_temp
    return reactions_numba