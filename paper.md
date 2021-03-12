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

In developed countries, people spend over 90% of their time indoors, where they are exposed to airborne pollutants that are generated indoors or outdoors, and some of which are harmful to human health. Occupant activities indoors such as cooking and cleaning can generate numerous chemical compounds and some of these can undergo further reaction to produce a large range of complex chemical reactions. Current instrumental techniques are unable to measure many of these compounds at present, so models provide the means to try and understand these processes and their impacts. The INdoor CHEMical model in Python (INCHEM-Py) is an open source and accessible box-model that has been refactored from the detailed chemical model developed by @Carslaw2007 to give researchers deeper insight into the chemical mechanisms behind indoor air chemistry. The detailed chemical model by Carslaw relies on proprietary software and requires a high level of chemistry expertise and Fortran knowledge. INCHEM-Py has therefore been built to address these issues and is intended to be used and further developed by academics and students of all abilities. It is open source, has no black box processes, and all inputs can be tracked through the model allowing for complete understanding of the system.

INCHEM-Py creates and solves a system of coupled Ordinary Differential Equations (ODEs) to progress indoor atmospheric chemical species concentrations through time. It can be used to investigate numerous indoor air chemistry events in world-wide locales providing key insights into the chemical processes involved. INCHEM-Py utilises the Master Chemical Mechanism (MCM) at its core [@Jenkin1997], which is near explicit and contains no lumping or use of species surrogates. INCHEM-Py also employs additional chemical mechanisms developed specifically for indoor air. These include gas-to-particle partitioning for three of the commonly encountered terpenes indoors (limonene and alpha- and beta-pinene), novel indoor photolysis parameterisation, indoor-outdoor air exchange and deposition to surfaces. 

The mechanisms contained within the model have been utilised in a significant number of published studies, these include: indoor air chemistry following cleaning with terpene based mixtures [@Carslaw2012; @Carslaw2017; @Carslaw2013; @Terry2014]; indoor air chemistry following cleaning with chlorine containing bleach [@Wong2017]; the impact of outdoor vegetation on indoor air chemistry [@Carslaw2015]; the importance of surface interactions for secondary pollutant formation [@Kruza2017]; ranking of harmful volatile organic compounds (VOCs) [@Carslaw2019]; improved model representation of the formation and composition of aerosols [@Kruza2020]; and photolysis of indoor air chemistry following high-concentration hospital/industrial cleaning events [@Wang2020]. INCHEM-Py has already been used to determine production rates and reactivity of indoor radical species, to assess the spatial and temporal scales of variability for indoor air constituents [@Lakey2021], and is currently being used to probe the impact of indoor air chemistry on ambient air, as well as to compare the differential secondary pollutant formation potential for different cleaning formulations.  

# Acknowledgements

The development of this model has been funded by a grant from the Alfred P. Sloan Foundation, grant number 2018-10083. Conclusions reached or positions taken by researchers or other grantees represent the views of the grantees themselves and not those of the Alfred P. Sloan Foundation or its trustees, officers, or staff.

# References