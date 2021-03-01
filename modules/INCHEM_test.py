# -*- coding: utf-8 -*-
"""
Unit testing for modules and functions used in INCHEM-Py

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

import unittest
import os
import numpy as np

'''
testing the Import module
'''
from Import import custom_import, speciesin, rate_coeff, ppool_in,\
    reactionslist, numba_rate, numba_reactions, import_all

class TestImport(unittest.TestCase):
    
    def test_custom(self):
        filename = "test_files/custom_input_test.txt"
        species = ["species1","species5"]
        custom_rates, custom_reactions,\
            custom_species, custom_RO2,\
                sums = custom_import(filename,species)
        self.assertEqual(custom_rates, [["k1","x+y"]],
                         "rate parsed incorrectly")
        self.assertEqual(custom_reactions, [['reaction_rate',
                                             'species1+species2=species3+species4']],
                         "reaction parsed incorrectly")
        self.assertEqual(custom_species,["species2","species3","species4"],
                         "species parsed incorrectly")
        self.assertEqual(custom_RO2, ['species1', 'species5'],
                         "RO2 summation parsed incorrectly")
        self.assertEqual(sums, [['sum_name', 'species1+species2+species3+species4']],
                         "custom summation parsed incorrectly")
        
    def test_speciesin(self):
        filename = "test_files/mcm_parse_test.fac"
        species = speciesin(filename)
        self.assertTrue(len(species) == 722, "there are 722 species in the test input")
        self.assertTrue(species[1] == "NC826OH", "incorrect species parsed from test")
        
    def test_rate_coeff(self):
        filename = "test_files/mcm_parse_test.fac"
        rates_in = rate_coeff(filename)
        self.assertTrue(len(rates_in) == 139, "there are 139 rates in the test file")
        self.assertTrue(rates_in[0] == ['KRO2NO', '2.7e-12*exp(360/TEMP)'], 
                        "incorrect rate parsed")
        
    def test_ppool_in(self):
        filename = "test_files/mcm_parse_test.fac"
        ppool = ppool_in(filename)
        self.assertTrue(len(ppool) == 146, "there are 146 peroxy radicals in the test file")
        self.assertTrue(ppool[0] == 'NLIMO2', "incorrect radical parsed")
        
    def test_reactionslist(self):
        filename = "test_files/mcm_parse_test.fac"
        reactions_in = reactionslist(filename)
        self.assertTrue(len(reactions_in) == 2189,
                        "there are 2189 reactions in the test file")
        self.assertTrue(len(reactions_in[0]) == 2,
                        "each reaction should consist of two parts")
        self.assertEqual(reactions_in[0][1], "O = O3",
                         "incorrect reaction parsed")
        
    def test_numba_rate(self):
        rates_in = [["rate1","exp(x)+log10(y)*TEMP/sqrt(z)"],
                    ["rate2","exp(x)+log10(y)*TEMP/sqrt(z)"]]
        numbarates = numba_rate(rates_in)
        self.assertTrue(len(numbarates) == 2,
                        "two rates provided for test")
        self.assertTrue(numbarates[0][1] == "numba_exp(x)+numba_log10(y)*temp/numba_sqrt(z)",
                        "numba conversions parsed incorrectly")
        
    def test_numba_reactions(self):
        reactions_in = [["exp(x)+log10(y)*TEMP/sqrt(z)","spec1=spec2+spec3"],
                        ["exp(x)+log10(y)*TEMP/sqrt(z)","=spec2"],
                        ["exp(x)+log10(y)*TEMP/sqrt(z)","spec1="]]
        numbareactions = numba_reactions(reactions_in)
        self.assertEqual(numbareactions[0],
                          ['numba_exp(x)+numba_log10(y)*temp/numba_sqrt(z)',
                           'spec1=spec2+spec3'],
                          "numba conversions parsed incorrectly")
        self.assertTrue(len(numbareactions) == 3,
                        "3 reactions given for test")
        
    def test_import_all(self):
        filename = "test_files/mcm_parse_test.fac"
        species,ppool,numbarates,numbareactions = import_all(filename)
        self.assertTrue(len(species) == 721,
                        "721 species in test input")
        self.assertTrue(species[0] == "ACETOL",
                        "species missing or in incorrect order")
        self.assertTrue(len(ppool) == 146,
                        "146 peroxy radicals in test input")
        self.assertTrue(ppool[0] == 'NLIMO2', "incorrect species parsed")
        self.assertTrue(len(numbarates) == 139,
                        "139 rates in test input")
        self.assertTrue(len(numbareactions) == 2189,
                        "2189 reactions in test input")


'''
test intial_dictionaries module
'''       
from initial_dictionaries import initial_conditions, master_calc, \
    write_jacobian_build, INDCM_species_calc
 
class TestInitial(unittest.TestCase):
    
    def test_initial_conditions_infile(self):
        filename = "test_files/initial_test.txt"
        species = ['species1','species2','species3','species4','HONO']
        rate_numba = [["rate1","2*numba_exp(4)"],["rate2","20"]]
        calc_dict = {'numba_exp':np.exp}
        path = os.getcwd()+"/test_files"
        density_dict, calc_dict = initial_conditions(filename,10,species,
                                                     rate_numba,calc_dict,
                                                     1,0,0,path)
        self.assertTrue(calc_dict["rate2"] == 20,
                        "rate 2 should be parsed as 20")
        self.assertTrue(len(calc_dict) == 3,
                        "incorrect length calc_dict (3)")
        self.assertTrue("seed" in density_dict,
                        "seed value missing")
        self.assertTrue(len(density_dict) == 7,
                        "7 species total in test")
        
    def test_initial_conditions_pickle(self):
        filename = "test_files/initial_test.txt"
        species = ['species1','species2','species3','species4','HONO']
        rate_numba = [["rate1","2*numba_exp(4)"],["rate2","20"]]
        calc_dict = {'numba_exp':np.exp}
        path = os.getcwd()+"/test_files"
        density_dict, calc_dict = initial_conditions(filename,10,species,
                                                     rate_numba,calc_dict,
                                                     1,1,900,path)
        self.assertTrue(calc_dict["rate2"] == 20,
                        "rate 2 should be parsed as 20")
        self.assertTrue(len(calc_dict) == 3,
                        "incorrect length calc_dict (3)")
        self.assertTrue("seed" in density_dict,
                        "seed value missing")
        self.assertTrue(len(density_dict) == 7,
                        "7 species total in test")
        self.assertTrue(density_dict["HONO"] == 4639743671.834778,
                        "HONO value parsed incorrectly at 900 seconds")
        
    def test_master_calc(self):
        reactions_in = [['5.5e-12*numba_exp(188/temp)', 'O + NO2 = NO'],
                        ['KMT03', 'NO2 + NO3 = N2O5'],
                        ['J15*2', 'C626CHO = C626O2 + CO + HO2'],
                        ['Part_rate', "PART1 + PART2 = PART3"],
                        ['test_rate','NO2 =']]
        species = ['O','NO2','NO','NO3','N2O5','C626CHO','C626O2','CO','HO2']
        reaction_number = np.linspace(1,5,5)
        particle_species = ['PART1','PART2','PART3']
        timed_densities = 0
        master_array_dict = master_calc(reactions_in,species,reaction_number,
                                        1,particle_species,
                                        timed_densities)
        self.assertEqual(len(master_array_dict), 9,
                         "9 species in test")
        self.assertEqual(master_array_dict['NO2'][2], ['5.0', '-1', 'NO2'],
                         "Equations parsed incorrectly")
        self.assertEqual(list(master_array_dict.keys()), species,
                         "species input do not match master array keys")
        
    def test_write_jacobian(self):
        master_array_dict = {"species1" : [['2.0', '-1', 'species3', 'species2'],
                                   ['species1OUT', 'AER'],
                                   ['species1', 'AER', '-1'],
                                   ['species1_SURF', 'species1', '-1']],
                     "species2" : [['1.0', '-1', 'species1', 'species2'],
                                   ['2.0', '-1', 'species2', 'species3'],
                                   ['5.0', '-1', 'species2'],
                                   ['species2OUT', 'AER'],
                                   ['species2', 'AER', '-1'],
                                   ['species2_SURF', 'species2', '-1']],
                     "species3" : [['a','-1','species3']]}
        species = ['species1','species2','species3']
        output_folder = "test_files"
        path = path = os.getcwd()
        write_jacobian_build(master_array_dict,species,output_folder,path)
        with open("test_files/Jacobian.py") as created_file:
            created_str = created_file.read().replace('\n', '')
        with open("test_files/Jacobian_test.txt") as test_file:
            test_str = test_file.read().replace('\n', '')
        self.assertMultiLineEqual(created_str, test_str, "files are not the same")
        os.remove("test_files/Jacobian.py") #clean up
    
    def test_INDCM_species_calc(self):
        from test_files.INDCM_test import INDCM_reactions
        species = ["species1","OH","NO"]
        INDCM_species = INDCM_species_calc(INDCM_reactions,species)
        self.assertFalse(any(item in species for item in INDCM_species),\
                         "Did not remove current species from new species")
        self.assertEqual(len(INDCM_species), 15, "15 species in list")
'''
test outdoor concentration module
'''
from outdoor_concentrations import outdoor_rates
    
class TestOutdoor(unittest.TestCase):
    
    def test_outdoor_rates(self):
        AER = 100
        particles = 1
        species = ["NO","NO2","test_species1"]
        outdoor_dict = outdoor_rates(AER,particles,species)
        self.assertEqual(outdoor_dict["test_species1OUT"],0,
                         "test_species value should be 0")
        species_out = ["NOOUT","NO2OUT","test_species1OUT"]
        self.assertTrue(set(species_out).issubset(list(outdoor_dict.keys())),
                        "not all species from test present in dictionary") 
        
if __name__ == '__main__':
    unittest.main()   