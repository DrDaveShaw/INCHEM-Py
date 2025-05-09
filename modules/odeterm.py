"""
Additional tools for importing and interpolating an input file of concentrations
with time. Also for updating internal dictionaries with these concentrations.

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

File created by Neil Butcher
"""

class SpeciesODETerm:
    """
    A single term in the ode function, or it's jacobian

    It stores a list of contributions to a single function term, in the form of compiled, evals.
    It constructs the full result by summing these at calltime.
    """

    def __init__(self, contributions):
        """
        inputs:
            contributions = list of strings which are compiled, then summed to give the full

        """
        self.compiled_contributions = [compile(c, '<string>', 'eval') for c in contributions]

    def __call__(self, full_dict):
        """
        Computes the numerical value of this term in the ODE equation (jacobian or function)

        inputs:
            full_dict = accumulated dictionary including concentrations, deposition rates and reaction rates
        """
        result = 0.0
        for contribution in self.compiled_contributions:
            result += eval(contribution, {}, full_dict)
        return result
