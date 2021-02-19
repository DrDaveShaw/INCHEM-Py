![INCHEM-Py](https://raw.githubusercontent.com/DrDaveShaw/INCHEM-Py/main/INCHEMPY_logo.png "INCHEM-Py logo")

# INCHEM-Py

The INdoor CHEMical model in Python (INCHEM-Py) is an open source 1D box model that creates and solves a system of coupled Ordinary Differential Equations (ODEs) to progress indoor air chemistry reactions through time. It is a refactor of the indoor detailed chemical model, developed by [Carslaw, 2007](https://doi.org/10.1016/j.atmosenv.2006.09.038), that has additional improvements in form, function, and accessibility. INCHEM-Py utilises gas phase chemistry from the [Master Chemical Mechanism (MCM)](http://mcm.leeds.ac.uk/MCM/) alongside additional mechanisms developed specifically for indoor air processes.

INCHEM-Py was created for the indoor air community to provide them with a useful tool with which to gain detailed insight into the chemistry occurring in internal atmospheres.

A full pdf manual is included within this repository, this README is not intended to cover every aspect of INCHEM-Py but should be sufficiant for users to get started.

A copy of the GNU General Public License v3.0 under which this project is licenced is included in this repository. 

# Table of contents
1. [Model overview](#Model-overview)
2. [Installation](#Installation)
3. [Running the model](#Running-the-model)
	* [Spyder](#Spyder)
	* [Command line](#cmd-line)
5. [Tests](#Tests)
6. [Community](#Community)

## Model overview<a name="Model-overview"></a>

INCHEM-Py takes multiple input files containing various mechanisms including: gas-phase chemical reactions, gas-particle partitioning, photolysis from both indoor and outdoor sources, indoor-outdoor air exchange including diurnal outdoor species concentrations, surface deposition, and optional custom reactions input by the user. These are parsed by the model into a series of stiff and highly-coupled ordinary differential equations and their Jacobian which are subsequently passed to the LSODA integration engine from ode in the scipy.integrate library which evolves the chemical concentrations with time. 

## Installation<a name="Installation"></a>

INCHEM-Py has been developed in Python 3 using the [Anaconda environment](https://www.anaconda.com/products/individual) and as such we recommend its use for installing Python and running the model. The Anaconda environment contains all of the python packages required. The graphical installer from the above link should be used to download and install Anaconda 3 which will contain Python 3 and other useful tools.

If you have chosen not to use the Anaconda environment then any Python 3 installation can be used and the following non-default packages will need to be installed:
* numpy
* numba
* pandas
* tqdm
* scipy
* threadpoolctl
* matplotlib

Downloading the INCHEM-Py repository and extracting it to the location within your computer from which you would like to run the model will complete the installation. Multiple files are produced by INCHEM-Py during a model run. The output folder is named automatically using the current date and time in the format YYYYMMDD_hhmmss, and an additional custom title can be set within the settings.py file. Therefore you must have write permission to the directory in which INCHEM-Py is extracted. Further details are included in the user manual.

## Running the model<a name="Running-the-model"></a>

INCHEM-Py is run using the included settings.py script. Within this script are variables that can be adjusted and a full description of how to modify these is discussed in the user manual. For now the following instructions will be to run the model in its default downloaded state. No editing of files is necessary for this.

### Spyder<a name="Spyder"></a>

INCHEM-Py was written using the IDE (integrated developer environment) Spyder. Spyder can be installed both with the Anaconda install or from the Anaconda Navigator. Instructions on how to both install and run Spyder can be found [here](https://docs.anaconda.com/anaconda/user-guide/getting-started/)

Once Spyder is open you can set the INCHEM-Py directory as your working directory using the folder icon in the top right. Then by selecting the files tab at the bottom of that top right window the settings.py file, or any other you wish to edit, can be opened to the window on the left by double clicking on it.

Once you are ready the model can be run by opening the settings.py file in the left hand window and either clicking on the green arrow in the toolbar or by pressing F5 on your keyboard. The model will then run in the bottom right console window.

### Command line<a name="cmd-line"></a>

Assuming you have installed python as recommended via Anaconda it is possible to run INCHEM-Py from the Anaconda prompt from within the Anaconda Navigator on Windows, or from the terminal in MacOS or Linux. Once Anaconda prompt or the terminal is open simply navigate to the INCHEM-Py directory using the change directory command, inputting your file path

    cd C:/Directory/AnotherDirectory/INCHEM-Py/

and run the settings.py script with Python

    python settings.py

## Tests<a name="Tests"></a>

Included within INCHEM-Py within the module folder is INCHEM_test.py. This script can be run to test some functions of INCHEM-Py that manipulate the input data into useful formats within the model. It uses preset inputs, found within the test_files folder, to check function outputs are expected. 

When entering new species or chemical mechanisms via the custom_input.txt file (details in the user manual) users should be careful that names are correct and reactions are not duplicated. The model cannot check intentions of the user as entering duplicate species or new species are both valid inputs. Many outputs are produced by INCHEM-Py that can be used to check that the model is working as expected or that custom chemistry has been entered correctly. The master_array can be viewed to validate reactions, the Jacobian is saved for a similar purpose. Any user entered mechanisms are also saved alongside mechanisms provided by the INCHEM-Py team which can be checked.

## Community<a name="Community"></a>

We welcome any contributions to INCHEM-Py and look forward to working with a community of people to develop the model further. 

Please contact us if you require any support.

david.shaw@york.ac.uk

nicola.carslaw@york.ac.uk

INCHEM-Py is free software, but since it is a scientific code we also ask that you show professional courtesy when using this code:
* Since you are benefiting from work on INCHEM-Py, we ask that you submit any improvements you make to the code to us by emailing us at david.shaw@york.ac.uk. Issues should be reported using the issue tracker.
* If you use INCHEM-Py results in a paper or professional publication, we ask that it includes an appropriate reference. It is understood that in most cases if one or more of the INCHEM-Py team are involved in preparing results then they should appear as co-authors.
* The INCHEM-Py logo is included with the model and may optionally be used in any oral or poster presentations.
