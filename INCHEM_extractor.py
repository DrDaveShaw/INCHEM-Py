# -*- coding: utf-8 -*-
"""
Output extraction and plotting script for INCHEM-Py. 
A detailed description of this file can be found within the user manual.

Copyright (C) 2019-2021 
David Shaw : david.shaw@york.ac.uk
Nicola Carslaw : nicola.carslaw@york.ac.uk

All rights reserved.

This file is additional to INCHEM-Py.

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

This script inputs the out_data.pickle files from model runs of INCHEM-Py
from specified output directories, saves and plots the species given in
species_to_plot in a csv and a png respectively. These are saved in the 
output_folder 
"""

'''
Variables to change
'''
#directories of data to extract and plot
out_directories=[
    '20210211_152040_test1',
    '20210212_151525_test2',
    '20210212_153517_test3']

#species to extract and plot
species_to_extract=['LIMONENE','BENZENE','TOLUENE','OH_reactivity',
                 'OH_production','J1']
#All species will be saved to a seperate csv for each input directory.
#A maximum of three seperate graphs will be made; species concentrations, 
#reactivity, and production. 

#times to plot from and to
start_time = 0
end_time = 3600*72

scale = "hours"
#can be "hours", "minutes", "seconds"

#folder to save csv and png graphs to output_folder. Can already exist or
#it will be created
output_folder = "extracted_outputs"

#should the y scale be log or not. Boolean
log_plot = False

'''
Extract and plot the data
'''
#import required packages
import pickle
import os
import matplotlib.pyplot as plt
import numpy as np

#define dictionary of output dataframes from out_directories
out_data={}
for i in out_directories:
    with open("%s/out_data.pickle" % i,'rb') as handle:
        out_data[i]=pickle.load(handle)

#get the current working directory and create the output folder 
#if it doesn't exist        
path=os.getcwd()
if not os.path.exists('%s/%s' % (path,output_folder)):
    os.mkdir('%s/%s' % (path,output_folder))

#create and save csvs
for i in out_data:
    out_data[i].to_csv("%s/%s/%s.csv" % (path,output_folder,i), 
                       columns = species_to_extract, index_label='Time (s)')
    
#plotting function
def plotting_function(plot_species,out_data,units,start_time,end_time,name,log_plot):
    #figure resolution and size
    plt.figure(dpi=600,figsize=(8,4))
    
    #set time conversion factor and labels
    if scale == "hours":
        factor = 3600
        plt.xlabel("Time (hours)")
    elif scale == "minutes":
        factor = 60
        plt.xlabel("Time (mins)")
    else:
        factor = 1
        plt.xlabel("Time (mins)")
    
    #unique colours
    colour=iter(plt.cm.gist_rainbow(np.linspace(0,1,len(plot_species)*len(out_data))))
    for k in out_data:
        time_step = out_data[k].index[1]-out_data[k].index[0]
        start_time = int( time_step * round( start_time / time_step ))
        end_time = int( time_step * round( end_time / time_step ))
        for l in plot_species: 
            c=next(colour)
            plt.plot(list(out_data[k][l][start_time:end_time].index/factor),
                     list(out_data[k][l][start_time:end_time]),
                     label="%s_%s" % (k,l),c=c)
    if log_plot == True:
        if name != "Photolysis":        
            plt.yscale("log") #can be commented out for a non-log plot
    plt.ylabel(units)
    plt.legend(loc='upper center', bbox_to_anchor=(0.45, -0.15),
      fancybox=True, shadow=True, ncol=2)
    plt.savefig('%s/%s/out_graph_%s.png' % (path,output_folder,name),
                bbox_inches='tight')
    return None

#units for the graphs
units = ["Concentration (molecule/cm\N{SUPERSCRIPT THREE})",
"Reactivity (s\N{SUPERSCRIPT MINUS}\N{SUPERSCRIPT ONE})",
"Production (molecule/cm\N{SUPERSCRIPT THREE}s\N{SUPERSCRIPT MINUS}\N{SUPERSCRIPT ONE})",
"Photolysis coefficient (s\N{SUPERSCRIPT MINUS}\N{SUPERSCRIPT ONE})"]

#additional name for graphs
name = ['Concentration','Reactivity','Production','Photolysis']

photolysis_names = ['J%s' % x for x in range(75)]

#extract concentrations, production, and reactivity
production = []
reactivity = []
concentration = []
photolysis = []
for i in species_to_extract: 
    if i.endswith("production"):
        production.append(i)
    elif i.endswith("reactivity"):
        reactivity.append(i)
    elif i in photolysis_names:
        photolysis.append(i)
    else:
        concentration.append(i)
 
#plot graphs
if len(production) > 0:
    plotting_function(production,out_data,units[2],start_time,end_time,name[2],log_plot)
if len(reactivity) > 0:
    plotting_function(reactivity,out_data,units[1],start_time,end_time,name[1],log_plot)
if len(concentration) > 0:
    plotting_function(concentration,out_data,units[0],start_time,end_time,name[0],log_plot)
if len(photolysis) > 0:
    plotting_function(photolysis,out_data,units[3],start_time,end_time,name[3],log_plot)
