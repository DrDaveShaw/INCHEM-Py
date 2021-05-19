---
title: 'INCHEM-Py: An open source Python box model for indoor air chemistry'
tags:
  - Python
  - atmospheric chemistry
  - indoor air
  - air pollution
  - box model
authors:
  - name: David Shaw^[corresponding author]
    orcid: 0000-0001-5542-0334
    affiliation: 1
  - name: Nicola Carslaw
    orcid: 0000-0002-5290-4779
    affiliation: 1
affiliations:
 - name: Department of Environment and Geography, University of York, Wentworth Way, York, YO10 5NG, United Kingdom
   index: 1
date: 12 March 2021
bibliography: paper.bib
---

# Summary

In developed countries people spend over 90% of their time indoors where they are exposed to airborne pollutants that are generated indoors or outdoors, some of which are harmful to human health. Occupant activities indoors such as cooking and cleaning can generate numerous chemical compounds and some of these can undergo further reactions to produce a large range of complex chemicals. Current instrumental techniques are unable to measure many of these compounds at present, so models provide the means to try and understand these processes and their impacts. The INdoor CHEMical model in Python (INCHEM-Py) is an open source and accessible box-model that has been re-factored from the indoor detailed chemical model developed by @Carslaw2007 to give researchers deeper insight into the chemical mechanisms behind indoor air chemistry. 

# Statement of need

Over the last 15 years, the INdoor Detailed Chemical Model (INDCM) has been used to successfully probe the chemistry of indoor air [@Carslaw2007]. However, it relies on proprietary software and requires a high level of chemistry expertise and some Fortran knowledge to edit and use the code. Software tools such as Pybox [@Topping2018], PyCHAM [@OMeara2020] and AtChem2 [@Sommariva2020] facilitate the use of chemical mechanisms to model atmospheric chemistry, but with a focus on chamber studies or ambient conditions. INCHEM-Py has been designed with a unique set of tools for the specific purpose of modelling indoor air chemistry. As well as a detailed gas-phase chemical mechanism, the new model includes gas-to-particle partitioning for three of the commonly encountered terpenes indoors (limonene and alpha- and beta-pinene), novel indoor photolysis parameterisation, indoor-outdoor air exchange and deposition to internal surfaces. INCHEM-Py is open source, has no black box processes and all inputs can be tracked through the model, allowing for complete understanding of the system. It has been designed to be easy to install for use by academics and students of all abilities, and is sufficiently accessible for further development by the wider indoor air community. The functionality embedded within INCHEM-Py will allow for a wide range of uses including in-depth analysis of experimental measurements, development and testing of new chemical mechanisms and probing numerous indoor scenarios, with the impacts on simulated indoor air pollutant concentrations from variations in parameters such as photolysis, ventilation and deposition rates, outdoor pollutant concentrations, time of year, and building location. 

# INCHEM-Py

INCHEM-Py creates and solves a system of coupled Ordinary Differential Equations (ODEs) to progress indoor atmospheric chemical species concentrations through time. It can be used to investigate numerous indoor air chemistry events in world-wide locales providing key insights into the chemical processes involved. INCHEM-Py utilises the Master Chemical Mechanism (MCM) at its core [@Jenkin1997; @Saunders2003], which is near explicit and contains no lumping or use of species surrogates. 

ICHEM-Py does not solve for spatial dimensions and assumes a well mixed atmosphere [@Carslaw2007]. Gas-to-particle partitioning is implemented using absorptive partitioning from @Pankow1994 with relevant reactions between particle and gas phase species included within the mechanism [@Carslaw2012]. Surface deposition is treated as an irreversible process with rates dependant on the simulated surface area to volume ratio and species deposition velocities [@Carslaw2012]. Photolysis rates can be calculated for several indoor lighting sources with different spectral profiles and also for attenuation of sunlight through multiple glass compositions [@Wang2021]. Daylight hours are derived from latitude and time of year.

The additional chemical mechanisms developed specifically for indoor air scenarios contained within the model have been utilised in a numerous published studies. These include: indoor air chemistry following cleaning with terpene based mixtures [@Carslaw2012; @Carslaw2017; @Carslaw2013; @Terry2014]; indoor air chemistry following cleaning with chlorine containing bleach [@Wong2017]; the impact of outdoor vegetation on indoor air chemistry [@Carslaw2015]; the importance of surface interactions for secondary pollutant formation [@Kruza2017]; ranking of harmful volatile organic compounds (VOCs) [@Carslaw2019]; improved model representation of the formation and composition of aerosols [@Kruza2020]; and photolysis of indoor air chemistry following high-concentration hospital/industrial cleaning events [@Wang2020]. INCHEM-Py has already been used to determine production rates and reactivity of indoor radical species, to assess the spatial and temporal scales of variability for indoor air constituents [@Lakey2021], and is currently being used to probe the impact of indoor air chemistry on ambient air, as well as to compare the differential secondary pollutant formation potential for different cleaning formulations.

At publication the current stable release of INCHEM-Py is v1.1.  

# Acknowledgements

The development of this model has been funded by a grant from the Alfred P. Sloan Foundation, grant number 2018-10083. Conclusions reached or positions taken by researchers or other grantees represent the views of the grantees themselves and not those of the Alfred P. Sloan Foundation or its trustees, officers, or staff.

# References
