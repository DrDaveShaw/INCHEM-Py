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

Humans spend over 90% of their time indoors and it is here that they are exposed to the majority of harmful airborne pollutants. Understanding the chemical processes that occur indoors is therefore vital to decrease the harmful chemistry created by indoor activities such as cooking and cleaning. The INdoor CHEMical model in Python (INCHEM-Py) is an open source and accessible box-model that has been refactored from the detailed chemical model developed by @Carslaw2007 to give researchers deeper insight into the chemical mechanisms of indoor air. The detailed chemical model by Carslaw relies on proprietary software and requires a high level of chemistry expertise and Fortran knowledge. INCHEM-Py addresses these issues and is intended to be used and further developed by academics and students of all abilities.

INCHEM-Py creates and solves a system of coupled Ordinary Differential Equations (ODEs) to progress indoor atmospheric chemical reactions through time. It can be used to investigate numerous indoor air chemistry events in world-wide locales providing key insights into the chemical processes involved. INCHEM-Py utilises the Master Chemical Mechanism (MCM) at its core [@Jenkin1997], which is near explicit; containing no lumping or use of species surrogates. INCHEM-Py also employs additional chemical mechanisms developed specifically for indoor air. These include gas-particle partitioning, photolysis from indoor and outdoor sources, indoor-outdoor air exchange, surface deposition, and reaction mechanisms for chemical species created during indoor events such as cooking and cleaning. 

The mechanisms contained within the model have been utilised in a significant number of published studies, these include: Indoor air chemistry following cleaning with terpene based mixtures [@Carslaw2012; @Carslaw2017; @Carslaw2013; @Terry2014]; indoor air chemistry following cleaning with chlorine containing bleach [@Wong2017]; the impact of outdoor vegetation on indoor air chemistry [@Carslaw2015]; the importance of surface interactions for secondary pollutant formation [@Kruza2017]; ranking of harmful volatile organic compounds (VOCs) [@Carslaw2019]; improved model representation of the formation and composition of aerosols [@Kruza2020]; and photolysis of indoor air chemistry following cleaning events [@Wang2020]. INCHEM-Py has been used to determine production rates and reactivity of species to assess the spatial and temporal scales of variability for indoor air constituents [@Lakey2021], and continues to be used in numerous other exciting studies.  

# Acknowledgements

The development of this model has been funded by a grant from the Alfred P. Sloan Foundation, grant number 2018-10083. Conclusions reached or positions taken by researchers or other grantees represent the views of the grantees themselves and not those of the Alfred P. Sloan Foundation or its trustees, officers, or staff.

# References