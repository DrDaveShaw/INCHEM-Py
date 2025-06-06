from modules.inchem_import import import_all, custom_import
from modules.particle_input import particle_import, particle_calcs, reactions_check, HOMS_chemistry, \
    particle_calc_dict
from modules.photolysis import photolysis_J, Zixu_photolysis, Zixu_photolysis_compiled
from modules.initial_dictionaries import initial_conditions, master_calc, master_compiler, \
    reaction_rate_compile, reaction_eval, construct_jacobian, INCHEM_species_calc, timed_import, \
    undefined_species_dict
from modules.outdoor_concentrations import outdoor_rates, outdoor_rates_diurnal, outdoor_rates_calc, \
    ACRate_updater
from modules.constraints import constraints_import, constrained_update
import numpy as np
import numba as nb
from scipy.integrate import ode
from scipy import interpolate
from modules.surface_dictionary import surface_deposition, O3_deposition, H2O2_deposition, breath_emissions
from threadpoolctl import threadpool_limits
# import importlib.util
import pandas as pd
import datetime
import math
import time as timing
from modules.reactivity import reactivity_summation, reactivity_calc, production_calc
import bisect


class InChemPyMainClass:

    save_rate = 1  # sets the rate at which outputs are saved within the integrator.
    # Useful if the timestep has to be reduced but an output at a specific interval
    # is still required. A save rate of 1 will save every dt, a save rate of 2 will
    # save every 2*dt

    def __init__(self, filename, INCHEM_additional, particles, constrained_file, output_folder, dt, volume, surface_area, adults, children,
                 const_dict, H2O2_dep, O3_dep, custom, timed_emissions, timed_inputs, custom_filename):

        # constrained species
        # changes start and end time of simulation to be only within the constrained inputs
        self.constrained_file = constrained_file
        if constrained_file:
            self.interp_inputs, self.constrained_variables, seconds_to_integrate, start_time = constraints_import(constrained_file,
                                                                                                                  output_folder, dt)
            self.constrained_min_time = start_time
            self.constrained_max_time = start_time+seconds_to_integrate

        # import from MCM download
        self.species, self.ppool, self.rate_numba, self.reactions_numba = import_all(filename)

        pi = math.pi

        # Calculate area to volume ratio for surface deposition
        surfaces_AV, AV = self.AV_calc(volume, surface_area)

        # dictionary for evaluating the reaction rates
        self.calc_dict = {
            'numba_exp': self.numba_exp,
            'numba_log10': self.numba_log10,
            'numba_sqrt': self.numba_sqrt,
            'PI': pi,
            'AV': AV,
            'numba_abs': self.numba_abs,
            'adults': adults,
            'children': children,
            'volume': volume}

        self.calc_dict.update(const_dict)  # add constants from settings to calc_dict

        # If we have surface emissions we need the individual A/V
        if H2O2_dep == True or O3_dep == True:
            self.calc_dict.update(surfaces_AV)

        '''
        Custom reactions and rates. Those not in the MCM download, the code does not
        check this so please make sure you are not adding any reactions that already
        exist as it will just duplicate them.
        '''
        self.sums = []
        if custom == True:
            custom_rates, custom_reactions, custom_species, custom_RO2, custom_sums = \
                custom_import(custom_filename, self.species)
            # Check that rates/constants/RO2 have not been added as species
            custom_species = [item for item in custom_species
                              if item not in (['RO2'] + list(self.calc_dict.keys()) +
                                              [name[0] for name in self.rate_numba])]
            self.species = self.species + custom_species
            self.rate_numba = self.rate_numba + custom_rates
            self.reactions_numba = self.reactions_numba + custom_reactions
            self.ppool = self.ppool + custom_RO2
            self.sums.extend(custom_sums)

        '''
        INCHEM reactions and rates that are not included in MCM download.
        '''
        if INCHEM_additional == True:
            from modules.inchem_chemistry import INCHEM_RO2, INCHEM_reactions, \
                INCHEM_rates, INCHEM_sums
            INCHEM_species = INCHEM_species_calc(INCHEM_reactions, self.species)
            self.species = self.species + INCHEM_species
            self.ppool = self.ppool + INCHEM_RO2
            self.reactions_numba = self.reactions_numba + INCHEM_reactions
            self.rate_numba = self.rate_numba + INCHEM_rates
            self.sums.extend(INCHEM_sums)

        '''
        Particles
        '''
        particle_species = []
        HOMS_species = []
        self.particles = particles
        if particles == True:
            # if the full MCM is not being used then the calcuations for TSP and anything involving TSP
            # will fail so particles can only be used with the full MCM at the moment 04/2020
            particle_species, particle_reactions, particle_vap_dict, part_compile_dict = particle_import()
            self.species = self.species + particle_species  # add particle species to species list
            self.reactions_numba = reactions_check(self.reactions_numba, particle_reactions, self.species)
            self.rate_numba = self.rate_numba + [['kacid', '1.5e-32*numba_exp(14770/temp)']]
            self.calc_dict.update(particle_vap_dict)
            if INCHEM_additional == True:
                # HOMS Chemistry
                self.reactions_numba, HOMS_species, part_compile_dict, HOMRO2 = HOMS_chemistry(self.reactions_numba,
                                                                                               part_compile_dict)
                self.species = self.species + HOMS_species
                self.ppool = self.ppool + HOMRO2
                self.calc_dict['PHOMS'] = 2.11e-7  # HOMS vapour pressure (Torr)
                self.calc_dict['PHOMSD'] = 7.6e-13  # HOMS dimer vapour pressure (Torr)
            self.part_calc_dict = particle_calc_dict(part_compile_dict)

        '''
        Optional H2O2 and O3 deposition
        '''
        if H2O2_dep == True:
            H2O2_rates, H2O2_reactions = H2O2_deposition()
            self.reactions_numba = self.reactions_numba + H2O2_reactions
            self.rate_numba = self.rate_numba + H2O2_rates
        if O3_dep == True:
            O3_rates, O3_reactions = O3_deposition()
            self.reactions_numba = self.reactions_numba + O3_reactions
            self.rate_numba = self.rate_numba + O3_rates
        if adults+children > 0:
            breath_rates, breath_reactions = breath_emissions(volume)
            self.reactions_numba = self.reactions_numba + breath_reactions
            self.rate_numba = self.rate_numba + breath_rates

        '''
        timed concentrations
        '''

        self.emission_group = {}
        if timed_emissions == True:
            timed_reactions, self.emission_group = timed_import(timed_inputs)
            self.reactions_numba = self.reactions_numba + timed_reactions

        '''
        Constrained species, remove from integration
        '''
        if constrained_file:
            self.constrained_species = []
            for i in self.constrained_variables:
                if i in self.species:
                    self.constrained_species.append(i)
                    self.species.remove(i)

        '''
        Additional clean up, checking for summations from custom inputs
        '''
        self.summations = False
        if custom == True or INCHEM_additional == True:
            if len(self.sums) >= 1:
                self.summations = True

        self.reaction_number = []
        for i in range(len(self.reactions_numba)):  # for assigning within the master array
            self.reaction_number.append('r%s' % i)

        # if it's in the calc dict it shouldn't be calculated in any of the integrations
        for i in self.calc_dict.keys():
            if i in self.species:
                self.species.remove(i)
            for j in self.rate_numba:
                if j[0] == i:
                    self.rate_numba.remove(j)
                    print("%s from custom_input.txt ignored. Defined elsewhere." % i)

        '''
        Surface deposition
        '''
        self.surface_dict = surface_deposition(AV, H2O2_dep, O3_dep)
        for specie in self.species:
            if particles == True and specie in particle_species:
                self.surface_dict['%s_SURF' % specie] = 0.004*AV
            elif '%s_SURF' % specie not in self.surface_dict.keys():
                self.surface_dict['%s_SURF' % specie] = 0

        # creating the master array
        self.master_array_dict = master_calc(self.reactions_numba, self.species, self.reaction_number, particles,
                                             particle_species, timed_emissions)

        # compiling the master array
        self.master_compiled = master_compiler(self.master_array_dict, self.species)

        # Create the jacobian
        self.dy_dy_dict = construct_jacobian(self.master_array_dict)

    def run(self, t0, seconds_to_integrate, dt, timed_emissions, timed_inputs, spline, temperatures, rel_humidity,
            M, light_type, glass, diurnal, city, date, lat, ACRate_dict, light_on_times,
            initial_conditions_gas, initials_from_run, path,
            output_folder, reactions_output, initial_dataframe=None):

        start_time = timing.time()  # program start time

        pi = math.pi

        def dydt(t, y0, events):
            '''
            The function to calculate dydt that is fed to the integrator

            inputs:
                t = time
                y0 = concentration of species

            returns:
                dy = dictionary of change in species concentration with change in time
            '''
            # Update density dictionary
            for i in range(num_species):
                density_dict[self.species[i]] = y0[i]
            density_dict['RO2'] = self.ppool_density_calc(density_dict, self.ppool)

            # if summations are included they need to be updated to the density dictionary also
            if self.summations == True:
                sums_dict = self.summations_eval(summations_dict, density_dict, calc_dict)
                density_dict.update(sums_dict)

            # n = time in seconds from midnight for each day
            n = t-((int(t/86400))*86400)

            # recalculate photolysis
            # COSX and SECX involve local hour angles dependant on position and time
            # of year (latitude of location and declination of sun)

            lha = (1+((n)/4.32E+4))*math.pi     # local hour angle, radians. Midnight start
            cosx = ((self.numba_cos(lha)*cosld)+sinld)       # solar zenith angle

            # Set negative cosx to zero and calculate the inverse
            # (secx=1/cosx). The MCM photolysis parameterisation
            # (http://mcm.leeds.ac.uk/MCM/parameters/photolysis_param.htt)
            # requires cosx and secx to calculate the photolysis rates.
            if cosx <= 1E-15:
                cosx = 0.0
                secx = 1.0E+15
            else:
                secx = 1.0 / (((cosx + self.numba_abs(cosx))/2)+1.0E-30)  # no divison by 0

            # updates the relevant dictionary whether lights are on or off
            if events[0] == True:
                lighting_input.update(indoor_photo_dict)
            else:
                lighting_input.update(indoor_photo_dict_off)

            lighting_input["cosx"] = cosx
            lighting_input["secx"] = secx
            photolysis_J(lighting_input, photo_dict, J_dict)

            # ACRate update
            ACRate_updater(t, ACRate_dict, outdoor_dict)

            # diurnal outdoor rates
            if diurnal == True:
                out_calc_dict["n"] = n
                out_calc_dict["cosx"] = cosx
                out_calc_dict["secx"] = secx
                outdoor_rates_calc(outdoor_dict, outdoor_dict_diurnal, out_calc_dict)

            # constrained inputs
            if self.constrained_file:
                constrained_update(t, self.interp_inputs, self.constrained_variables, constrained_J, self.constrained_species,
                                   constrained_out, calc_dict, J_dict, outdoor_dict, constrained_rates, rel_humidity)

            # recalculate humidity,water
            if constant_temperature is False:
                calc_dict['temp'] = self.variable_temperature(t, temperatures, spline, tck)
            h2o, rh = self.h2o_rh(t, calc_dict['temp'], rel_humidity, self.numba_exp)
            calc_dict['H2O'] = h2o

            # recalculate particle sums
            if self.particles == True:
                particle_dict = particle_calcs(self.part_calc_dict, density_dict)
                density_dict.update(particle_dict)

            # checks time, if between times set for a forced density change the rate
            # is applied to the specific species
            if timed_emissions == True:
                for i, key in enumerate(self.emission_group.keys()):
                    if events[i+1] == True:
                        timed_dict[key] = 1
                    else:
                        timed_dict[key] = 0

            # recalculate reaction rates
            reaction_eval(reaction_rate_dict, self.reaction_number, J_dict, calc_dict,
                          density_dict, dt, reaction_compiled_dict,
                          outdoor_dict, self.surface_dict,
                          timed_dict)

            # evaluate the mater array to recalculate concentrations
            dy_dict = self.dy_calc(self.master_compiled, reaction_rate_dict, calc_dict, density_dict,
                                   outdoor_dict, self.surface_dict, self.species, timed_dict)

            # output the new concentration values
            dy = [dy_dict[i] for i in self.species]
            return dy

        def dydy(t, y0, events):
            '''
            The function to calculate the jacobian that is fed to the integrator

            inputs:
                t = time
                y0 = concentration of species

            returns:
                dydy = array of change in species concentration with change
                    in other species concentrations
            '''
            # Update density dictionary
            for i in range(num_species):
                density_dict[self.species[i]] = y0[i]
            density_dict['RO2'] = self.ppool_density_calc(density_dict, self.ppool)

            # if summations are included they need to be updated to the density dictionary also
            if self.summations == True:
                sums_dict = self.summations_eval(summations_dict, density_dict, calc_dict)
                density_dict.update(sums_dict)

            # n = time in seconds from midnight for each day
            n = t-((int(t/86400))*86400)

            # recalculate photolysis
            # COSX and SECX involve local hour angles dependant on position and time
            # of year (latitude of location and declination of sun)

            lha = (1+((n)/4.32E+4))*math.pi     # local hour angle, radians. Midnight start
            cosx = ((self.numba_cos(lha)*cosld)+sinld)       # solar zenith angle

            # Set negative cosx to zero and calculate the inverse
            # (secx=1/cosx). The MCM photolysis parameterisation
            # (http://mcm.leeds.ac.uk/MCM/parameters/photolysis_param.htt)
            # requires cosx and secx to calculate the photolysis rates.
            if cosx <= 1E-15:
                cosx = 0.0
                secx = 1.0E+15
            else:
                secx = 1.0 / (((cosx + self.numba_abs(cosx))/2)+1.0E-30)  # no division by 0

            # updates the relevant dictionary whether lights are on or off
            if events[0] == True:
                lighting_input.update(indoor_photo_dict)
            else:
                lighting_input.update(indoor_photo_dict_off)

            lighting_input["cosx"] = cosx
            lighting_input["secx"] = secx
            photolysis_J(lighting_input, photo_dict, J_dict)

            # ACRate update
            ACRate_updater(t, ACRate_dict, outdoor_dict)

            # diurnal outdoor rates
            if diurnal == True:
                out_calc_dict["n"] = n
                out_calc_dict["cosx"] = cosx
                out_calc_dict["secx"] = secx
                outdoor_rates_calc(outdoor_dict, outdoor_dict_diurnal, out_calc_dict)

            # constrained inputs
            if self.constrained_file:
                constrained_update(t, self.interp_inputs, self.constrained_variables, constrained_J, self.constrained_species,
                                   constrained_out, calc_dict, J_dict, outdoor_dict, constrained_rates, rel_humidity)

            # recalculate temp,humidity,water
            if constant_temperature is False:
                calc_dict['temp'] = self.variable_temperature(t, temperatures, spline, tck)
            h2o, rh = self.h2o_rh(t, calc_dict['temp'], rel_humidity, self.numba_exp)
            calc_dict['H2O'] = h2o

            # recalculate particle sums
            if self.particles == True:
                particle_dict = particle_calcs(self.part_calc_dict, density_dict)
                density_dict.update(particle_dict)

            # checks time, if between times set for a forced density change the rate
            # is applied to the specific species
            if timed_emissions == True:
                for i, key in enumerate(self.emission_group.keys()):
                    if events[i+1] == True:
                        timed_dict[key] = 1
                    else:
                        timed_dict[key] = 0

            # recalculate reaction rates
            reaction_eval(reaction_rate_dict, self.reaction_number, J_dict, calc_dict, density_dict,
                          dt, reaction_compiled_dict, outdoor_dict,
                          self.surface_dict, timed_dict)

            # recalculate jacobian
            dydy_jac = self.dy_dy_calc(self.dy_dy_dict, J_dict, calc_dict, density_dict, self.species,
                                       outdoor_dict, self.surface_dict, num_species,
                                       timed_dict, reaction_rate_dict)
            return dydy_jac

        def integrate_function(iters, t_bound_internal, y0, t0, ret, save_rate, num_species,
                               total_iter, dt, events):
            '''
            Using lsoda to calculate density evolution and output as n_new

            inputs:
                iters = number of iterations that have already been performed
                        through the integrator, used to calculate when an output
                        is saved
                t_bound_internal = the time to integrate to within this function (s)
                y0 = initial species concentration
                t0 = start time (s)
                ret = integrator return code from scipy.integrate.ode.get_return_code
                    set as 1 prior to calling the integrator
                save_rate = how many iterations to perform before saving an output
                num_species = the total number of species
                total_iter = the total number of iterations to be completed
                dt = time step (s)

            returns:
                dt_out = list of output times
                n_new = array of output concentrations for each species at each time
                iters = total number of iterations completed
                ret = integrator return code from scipy.integrate.ode.get_return_code
                iter_time = list of time stamps for the completion of each integration
                            over dt
                calculated_output = dictionary of lists of calculated values for each
                                    iteration. These are calculations done using the species
                                    concentrations and are only for output purposes
            '''
            # assign arrays to populate
            n_new = [[] for i in range(num_species)]
            dt_out = []
            iter_time = []

            calculated_output = {}
            calculated_output['RO2'] = []
            if self.particles == True:
                calculated_output['TSP'] = []
                calculated_output['acidsum'] = []
                calculated_output['TSPx'] = []
                calculated_output['mwomv'] = []
                calculated_output['soacalc'] = []
                calculated_output['SOA'] = []
            for i in reactivity_dict:
                calculated_output[i] = []
            for i in production_dict:
                calculated_output[i] = []
            for i in J_dict:
                calculated_output[i] = []
            for i in outdoor_dict:
                calculated_output[i] = []
            if self.summations == True:
                for i in sums_dict:
                    calculated_output[i] = []

            if reactions_output == True:
                for i in reaction_rate_dict:
                    calculated_output[i] = []  # reaction rates
                for i in self.surface_dict:
                    calculated_output[i] = []  # surface deposition values

            for i in calc_dict:
                if "numba" not in i:
                    calculated_output[i] = []

            # set integrator args
            atol = [1e-6]*num_species  # Default 1e-6
            rtol = 1e-6  # Default 1e-6
            first_step = 1e-10  # size of first integration step to try (s)
            nsteps = 2000  # max number of internal timesteps
            max_step = dt

            # set the integrator and arguments
            r = ode(dydt, dydy).set_integrator('lsoda', atol=atol, rtol=rtol,
                                               first_step=first_step, nsteps=nsteps, max_step=max_step)

            r.set_initial_value(y0, t0).set_f_params(events).set_jac_params(events)

            # integrate
            while r.successful() and r.t < t_bound_internal:
                print('Iteration ', iters+1, '/', total_iter, '¦', r.t, ' to ', r.t+dt)
                r.integrate(r.t+dt)
                iters = iters+1
                ret = r.get_return_code()
                if iters % save_rate == 0:  # output every save_rate iterations
                    dt_out.append(int(r.t))
                    iter_time.append(timing.time()-start_time)
                    calculated_output['RO2'].append(density_dict["RO2"])
                    reactivity_calc(reactivity_dict, reactivity_compiled, reaction_rate_dict,
                                    calc_dict, density_dict)
                    production_calc(production_dict, production_compiled, reaction_rate_dict,
                                    calc_dict, density_dict)
                    for i in reactivity_dict:
                        calculated_output[i].append(reactivity_dict[i])
                    for i in production_dict:
                        calculated_output[i].append(production_dict[i])
                    if self.particles == True:
                        calculated_output['TSP'].append(density_dict['TSP'])
                        calculated_output['acidsum'].append(density_dict['acidsum'])
                        calculated_output['TSPx'].append(density_dict['TSPx'])
                        calculated_output['mwomv'].append(density_dict['mwomv'])
                        calculated_output['soacalc'].append(density_dict['soacalc'])
                        calculated_output['SOA'].append(density_dict['SOA'])
                    for i in range(num_species):
                        n_new[i].append(r.y[i].copy())
                    for i in J_dict:
                        calculated_output[i].append(J_dict[i])
                    for i in outdoor_dict:
                        calculated_output[i].append(outdoor_dict[i])
                    if self.summations == True:
                        for i in sums_dict:
                            calculated_output[i].append(density_dict[i])
                    if reactions_output == True:
                        for i in reaction_rate_dict:
                            calculated_output[i].append(reaction_rate_dict[i])
                        for i in self.surface_dict:
                            calculated_output[i].append(self.surface_dict[i])
                    for i in calc_dict:
                        if "numba" not in i:
                            calculated_output[i].append(calc_dict[i])

            return dt_out, n_new, iters, ret, iter_time, calculated_output

        # setting integration envelopes and integration parameters
        # needs to happen before light on times and timed emissions are parsed
        # by the functions that call them
        t_bound = t0+seconds_to_integrate  # Maximum time to integrate to

        # check the constraints on times
        if self.constrained_file:
            assert (t0 >= self.constrained_min_time)
            assert (t_bound <= self.constrained_max_time)

        iters = 0  # the number of iterations that have been performed already (leave as 0)
        total_iter = math.ceil(int(t_bound-t0)/dt)  # calculated to show the user how long is left
        print('total iterations:', total_iter)

        # list of integration times
        integration_envelopes = []
        integration_envelopes.extend([t0, t_bound])

        light_on_times = [[j * 3600 for j in i]for i in light_on_times]  # conversion to seconds

        for light_envelopes in light_on_times:
            integration_envelopes.extend(light_envelopes)

        if timed_emissions == True:
            for input_species in timed_inputs:
                for sublist in timed_inputs[input_species]:
                    integration_envelopes.extend(sublist[:-1])

        # remove repeated values
        integration_envelopes = list(set(integration_envelopes))
        # sort by size
        integration_envelopes = sorted(integration_envelopes, key=lambda x: x)
        # remove times before and after start and end of simulation
        start_pos = bisect.bisect_right(integration_envelopes, t0)  # removes t0
        end_pos = bisect.bisect_right(integration_envelopes, t_bound)
        integration_envelopes = integration_envelopes[start_pos:end_pos]

        '''
        calculate initial values
        '''
        temperatures_length = len(temperatures)
        if type(spline) == int or type(spline) == float:  # determine if constant temperature should be used
            constant_temperature = True
            temp = spline
        elif temperatures_length == 1:
            constant_temperature = True
            temp = temperatures[0][1]
        else:  # else use a variable temperature
            constant_temperature = False
            # extend the temperatures given to cover the entire simulation
            while temperatures[-1][0] < t0+seconds_to_integrate:
                # duplicate temperatures in lengths of a day
                temporary_temperatures = temperatures[temperatures_length*-1:]
                temporary_temperatures = [[item[0]+86400, item[1]] for item in temporary_temperatures]
                temperatures.extend(temporary_temperatures)

            if temperatures[0][0] > t0:
                # make sure a value for the temperature exists before t0
                temporary_temperatures = temperatures[:temperatures_length]
                temporary_temperatures = [[item[0]-86400, item[1]] for item in temporary_temperatures]
                temporary_temperatures.extend(temperatures)
                temperatures = temporary_temperatures

            tck = interpolate.splrep([item[0]for item in temperatures], [item[1] for item in temperatures], s=0)
            temp = self.variable_temperature(t0, temperatures, spline, tck)

        h2o, rh = self.h2o_rh(t0, temp, rel_humidity, self.numba_exp)

        calc_dict = {'M': M,
                     'temp': temp,
                     'H2O': h2o
                     }
        calc_dict.update(self.calc_dict)

        '''
        importing initial concentrations
        '''
        density_dict, calc_dict = initial_conditions(initial_conditions_gas, M, self.species,
                                                     self.rate_numba, calc_dict, self.particles,
                                                     initials_from_run, t0, path, initial_dataframe)
        density_dict['RO2'] = self.ppool_density_calc(density_dict, self.ppool)

        '''
        timed concentrations
        '''

        timed_dict = {}
        if timed_emissions == True:
            for key, value in self.emission_group.items():
                if value[0] <= t0 <= value[1]:
                    timed_dict[key] = 1
                else:
                    timed_dict[key] = 0

        '''
        Photolysis

        The simulation works on solar time of day and does not require any input
        of longitude.
        '''
        # calculations for determining solar position given time of year
        if type(date) == str:
            day, month, year = map(int, date.split('-'))
            date = datetime.date(year, month, day)
        year_day = (date - datetime.date(year, 1, 1)).days + 1
        days_in_year = (datetime.date(year, 12, 31) - datetime.date(year, 1, 1)).days + 1
        radian = 180.0/pi
        dec = -23.45 * np.cos(((360/days_in_year)/radian)*(year_day+10))

        lat = lat/radian  # conversion to radians
        dec = dec/radian  # conversion to radians

        # calculations for spherical law of cosines for solar zenith angle
        sinld = self.numba_sin(lat)*self.numba_sin(dec)
        cosld = self.numba_cos(lat)*self.numba_cos(dec)

        photo_dict = Zixu_photolysis_compiled()  # compiled equations

        # full dictionary of attenuation factors for different lights/glass
        light_dict = Zixu_photolysis(self.numba_abs, self.numba_exp)

        indoor_photo_dict = {**light_dict[light_type], **light_dict[glass]}
        indoor_photo_dict_off = {**light_dict["off"], **light_dict[glass]}

        n = t0-((int(t0/86400))*86400)  # keeps time within 24 hour cycle

        # COSX and SECX involve local hour angles dependant on position and time
        # of year (latitude of location and declination of sun)
        lha = (1+((n)/4.32E+4))*pi    # local hour angle, radians. Midnight start
        cosx = ((self.numba_cos(lha)*cosld)+sinld)  # solar zenith angle

        # (http://mcm.york.ac.uk/parameters/photolysis_param.htt)
        # Keep cosx 0 or positive, we don't have negative photolysis
        if cosx <= 1E-15:
            cosx = 0.0
            secx = 1.0E+15
        else:
            secx = 1.0 / (((cosx + self.numba_abs(cosx))/2)+1.0E-30)

        # light_on_times = [[j * 3600 for j in i]for i in light_on_times] #conversion to seconds

        J_dict = {}
        lighting_input = {}

        condition = False
        for i in light_on_times:
            if i[0] <= t0 <= i[1]:
                condition = True
                lighting_input.update(indoor_photo_dict)
                break
        if not condition:
            lighting_input.update(indoor_photo_dict_off)

        lighting_input["cosx"] = cosx
        lighting_input["secx"] = secx
        photolysis_J(lighting_input, photo_dict, J_dict)

        '''
        MOCCIE inputs updating photolysis
        '''
        if self.constrained_file:
            constrained_J = []
            for i in self.constrained_variables:
                if i in J_dict.keys():
                    J_dict[i] = float(self.interp_inputs[i](t0))
                    constrained_J.append(i)

        '''
        Outdoor species concentration calculations
        '''
        out_calc_dict = {"numba_abs": self.numba_abs,
                         "numba_exp": self.numba_exp,
                         "numba_cos": self.numba_cos,
                         "numba_sin": self.numba_sin,
                         "n": n,
                         "cosx": cosx,
                         "secx": secx}

        # Outdoor dictionaries
        outdoor_dict = outdoor_rates(self.particles, self.species)
        # ACRate update
        ACRate_updater(t0, ACRate_dict, outdoor_dict)
        # Diurnal variation
        if diurnal == True:
            outdoor_dict_diurnal = outdoor_rates_diurnal(city)
            outdoor_rates_calc(outdoor_dict, outdoor_dict_diurnal, out_calc_dict)
            # diurnal rates will overide static rates if species shown in both

        '''
        constrained inputs updating outdoor concentrations
        '''
        if self.constrained_file:
            constrained_out = []
            for i in self.constrained_variables:
                if i in outdoor_dict.keys():
                    outdoor_dict[i] = float(self.interp_inputs[i](t0))
                    constrained_out.append(i)

        '''
        MOCCIE inputs updating initial concentrations
        '''
        if self.constrained_file:
            constrained_rates = []
            for i in self.constrained_variables:
                if i not in self.constrained_species + constrained_J + constrained_out + \
                        ["H2O", "TEMP", "rh"]:
                    print("%s not found as species, including as rates for potential custom calculations" % i)
                    constrained_rates.append(i)
                    calc_dict[i] = float(self.interp_inputs[i](t0))
            constrained_update(t0, self.interp_inputs, self.constrained_variables, constrained_J, self.constrained_species,
                               constrained_out, calc_dict, J_dict, outdoor_dict, constrained_rates, rel_humidity)

        # calculating t0 summations
        summations_dict = {}
        if self.summations == True:
            summations_dict = self.summations_compile(self.sums)
            undefined_dict = undefined_species_dict(summations_dict, density_dict, calc_dict)
            density_dict.update(undefined_dict)
            sums_dict = self.summations_eval(summations_dict, density_dict, calc_dict)
            density_dict.update(sums_dict)

        if self.particles == True:
            undefined_dict = undefined_species_dict(self.part_calc_dict, density_dict, calc_dict)
            density_dict.update(undefined_dict)
            particle_dict = particle_calcs(self.part_calc_dict, density_dict)
            density_dict.update(particle_dict)

        '''
        saving initial conditions to an output directory for reference
        '''
        if output_folder is not None:
            f = open("%s/%s/initial_concentrations.txt" % (path, output_folder), "w")
            for i in self.species:
                f.write('%s=%s ;\n' % (i, density_dict[i]))
            f.close()

        '''
        Calculating the reaction rates and compiling the master array of ODEs
        '''
        num_species = len(self.species)  # some calculations ask for the number of species
        # better to calculate it once rather than every time

        reaction_compiled_dict = reaction_rate_compile(self.reactions_numba, self.reaction_number)
        reaction_rate_dict = {}

        full_dict = {**J_dict, **density_dict, **outdoor_dict, **self.surface_dict, **timed_dict}
        undefined_dict = undefined_species_dict(reaction_compiled_dict, full_dict, calc_dict)
        density_dict.update(undefined_dict)

        reaction_eval(reaction_rate_dict, self.reaction_number, J_dict, calc_dict, density_dict,
                      dt, reaction_compiled_dict, outdoor_dict,
                      self.surface_dict, timed_dict)

        # reactivity and production calculations, details in the reactivity.py script
        reactivity_compiled, production_compiled = reactivity_summation(self.master_array_dict)
        reactivity_dict = {}
        reactivity_calc(reactivity_dict, reactivity_compiled, reaction_rate_dict, calc_dict,
                        density_dict)
        production_dict = {}
        production_calc(production_dict, production_compiled, reaction_rate_dict, calc_dict,
                        density_dict)

        '''
        #Integration
        '''
        # Create an array of concentrations to be updated during the integration. This
        # can then be used to repopulate the dictionaries with updated values
        y0 = [[] for i in range(num_species)]
        for i in range(num_species):
            y0[i] = density_dict[self.species[i]]

        # Create arrays for storing the output.
        n_new = np.array([[y0[i]] for i in range(num_species)])
        dt_out = np.array([])
        dt_out = np.append(dt_out, int(t0))
        iter_time_tot = [timing.time()-start_time]
        calculated_output_tot = {}
        calculated_output_tot['RO2'] = [density_dict['RO2']]
        if self.particles == True:
            calculated_output_tot['TSP'] = [density_dict['TSP']]
            calculated_output_tot['acidsum'] = [density_dict['acidsum']]
            calculated_output_tot['TSPx'] = [density_dict['TSPx']]
            calculated_output_tot['mwomv'] = [density_dict['mwomv']]
            calculated_output_tot['soacalc'] = [density_dict['soacalc']]
            calculated_output_tot['SOA'] = [density_dict['SOA']]
        for i in reactivity_dict:
            calculated_output_tot[i] = [reactivity_dict[i]]
        for i in production_dict:
            calculated_output_tot[i] = [production_dict[i]]
        for i in J_dict:
            calculated_output_tot[i] = [J_dict[i]]
        for i in outdoor_dict:
            calculated_output_tot[i] = [outdoor_dict[i]]
        if self.summations == True:
            for i in sums_dict:
                calculated_output_tot[i] = [density_dict[i]]

        if reactions_output == True:
            for i in reaction_rate_dict:
                calculated_output_tot[i] = [reaction_rate_dict[i]]  # reaction rates
            for i in self.surface_dict:
                calculated_output_tot[i] = [self.surface_dict[i]]  # surface deposition values

        for i in calc_dict:
            if "numba" not in i:
                calculated_output_tot[i] = [calc_dict[i]]

        ret = 1  # if ret=2 success. ODE return code

        print('Integration starting')

        env_loop_index = 0

        with threadpool_limits(limits=4, user_api='blas'):  # limits threads used by integration
            while iters < total_iter and ret > 0:
                end_time = integration_envelopes[env_loop_index]
                print('Integration to', end_time)
                n_new_in = n_new[:, -1]
                dt_out_in = dt_out[-1]
                events = self.event_creator(dt_out_in, light_on_times, timed_emissions, self.emission_group)
                dt_out_temp, n_new_temp, iters, ret, iter_time, calculated_output =\
                    integrate_function(iters, end_time, n_new_in, dt_out_in, ret, self.save_rate,
                                       num_species, total_iter, dt, events)
                dt_out = np.append(dt_out, dt_out_temp)
                n_new = np.append(n_new, n_new_temp, axis=1)
                iter_time_tot.extend(iter_time)
                env_loop_index += 1
                for x in calculated_output:
                    calculated_output_tot[x].extend(calculated_output[x])

        output_data = pd.DataFrame(np.transpose(n_new), columns=self.species, index=dt_out)
        output_data = output_data.join(pd.DataFrame(calculated_output_tot, index=dt_out))

        integration_times = pd.DataFrame(np.transpose(iter_time_tot), index=dt_out)

        end_time = timing.time()
        delta = datetime.timedelta(seconds=(end_time-start_time))
        print('Return code:', ret)  # ODE return code
        print('Total run time =', str(delta - datetime.timedelta(microseconds=delta.microseconds)))

        return output_data, integration_times

    @staticmethod
    def summations_compile(sums):
        '''
        compiles any custom summations

        inputs:
            sums = list of summations [name of sum, calculation]

        returns:
            summation_dict = dictionary of summations {name of sum : compiled calculation}
        '''
        summation_dict = {}
        for i in sums:
            summation_dict[i[0]] = compile(i[1], '<string>', 'eval')
        return summation_dict

    def summations_eval(self, summation_dict, density_dict, calc_dict):
        '''
        evaluates custom summations

        inputs:
            summation_dict = dictionary of summations {name of sum : compiled calculation}
            density_dict = dictionary of current species concentrations {species : concentration}
            calc_dict = dictionary of constants and variables for use in calculations

        returns:
            sums_dict = dictionary of evaluated sum calculations {name of sum : value}
        '''
        sums_dict = {}
        full_dict = {**density_dict, **calc_dict}
        for spec in summation_dict.keys():
            sums_dict[spec] = (eval(summation_dict[spec], {}, full_dict))
        return sums_dict

    @staticmethod
    def h2o_rh(time, temp, rel_humidity, numba_exp):
        '''
        calculates relative humidity and water at a given time and temperature

        inputs:
            time = current simulation time (s)
            temp = current temperature value (K)
            rel_humidity = current relative humidity (%), can be calculation
            numba_exp = exponent

        returns:
            h20 = water vapour
            rh = relative humidity (%)
        '''
        rh = rel_humidity
        h2o = 6.1078*numba_exp(-1.0e+0*(597.3-0.57*(temp-273.16))*18.0/1.986 *
                               (1.0/temp-1.0/273.16))*10./(1.38e-16*temp)*rh
        return h2o, rh

    @staticmethod
    def variable_temperature(time, temperatures, spline, tck):
        '''
        Interpolates a value for temperature given sparse temperature inputs

        inputs:
            time = current simulation time
            temperatures = input of temperatures at times in the form [[time (s),temp (K)],[...]]
            spline = input of type of spline to use, BSpline or Linear
            tck = A tuple containing a vector of knots, B-spline coefficients
                  and degree of the spline
        '''

        if spline == "Linear":
            temp = np.interp(time, [item[0]for item in temperatures], [item[1] for item in temperatures])
        elif spline == "BSpline":
            temp = float(interpolate.BSpline(*tck)(time))
        return temp

    @staticmethod
    def ppool_density_calc(density_dict, ppool):
        '''
        peroxy radical summation evaluation

        inputs:
            density_dict = dictionary of current concentrations
            ppool = list of species to be summed for RO2

        returns:
            RO2 = summed peroxy radical species
        '''
        RO2 = 0.
        for p in ppool:
            RO2 += eval(p, {}, density_dict)
        return RO2

    @staticmethod
    def dy_calc(master_compiled, reaction_rate_dict, calc_dict, density_dict, outdoor_dict,
                surface_dict, species, timed_dict):
        '''
        evaluating the master array of species

        inputs:
            master_compiled = dictionary of compiled ODEs
            reaction_rate_dict = dictionary of reaction rate values at current time
            calc_dict = dictionary of constants and variables for use in calculations
            density_dict = dictionary of current concentrations
            outdoor_dict = dictionary of outdoor species concentrations
            surface_dict = dictionary of surface deposition rates for each species
            species = list of species
            timed_dict = dictionary of rates for any timed inputs for current time

        returns:
            dy_dict = dictionary of changes in concentration for each species per second
        '''
        dy_dict = {}
        full_dict = {**reaction_rate_dict, **calc_dict, **density_dict, **outdoor_dict,
                     **surface_dict, **timed_dict}

        for specie in species:
            dy_dict[specie] = master_compiled[specie](full_dict)
        return dy_dict

    @staticmethod
    def dy_dy_calc(dy_dy_dict, J_dict, calc_dict, density_dict, species, outdoor_dict,
                   surface_dict, num_species, timed_dict, reaction_rate_dict):
        '''
        Evaluating the Jacobian during integration

        inputs:
            dy_dy_dict = dictionary jacobian {index:[x,y,compiled calculation]}
            J_dict = dictionary of current photolysys values
            reaction_rate_dict = dictionary of reaction rate values at current time
            calc_dict = dictionary of constants and variables for use in calculations
            density_dict = dictionary of current concentrations
            outdoor_dict = dictionary of outdoor species concentrations
            surface_dict = dictionary of surface deposition rates for each species
            num_species = number of species

        returns:
            dy_dy = dictionary of values of species change with species per second
        '''

        full_dict = {**reaction_rate_dict, **density_dict, **outdoor_dict, **surface_dict,
                     **calc_dict, **timed_dict}

        dy_dy = np.zeros((num_species, num_species), dtype=np.float32)

        for jacobian_term in dy_dy_dict.keys():
            k, k2 = jacobian_term
            dy_dy[int(k), int(k2)] = dy_dy_dict[jacobian_term](full_dict)
        return dy_dy

    @staticmethod
    def event_creator(t, light_on_times, timed_emissions, emission_group):
        '''
        inputs:
            t = current time (s)
            light_on_times = list of light on and off times of internal lighting
            timed_emissions = True or False for timed emissions being included
            timed_inputs = Dictionary of emission times and rates of species

        outputs:
            events =    a list of true or false statements that turn on or off events
                        within the integration. A method of dealing with discontinuities.
        '''
        events = []
        # updates the relevant dictionary whether lights are on or off
        condition = False
        for i in light_on_times:
            if i[0] <= t < i[1]:
                condition = True
                break
        events.append(condition)

        if timed_emissions == True:
            for emission in emission_group.values():
                if emission[0] <= t < emission[1]:
                    condition = True
                else:
                    condition = False
                events.append(condition)

        return events

    @staticmethod
    def AV_calc(volume, surface_area):
        '''
        Calculates the area to volume ratio for surface deposition

        inputs:
            volume = volume of the simulated space (cm^3)
            surface_areas = dictionary of surface areas of surfaces in the space (cm2^)

        outputs:
            AV_dict = dictionary of surface area to volume ratios (cm^-1)
            AV = total surface to volume ratio (cm^-1)
        '''
        AV = sum(surface_area.values())/volume

        surfaces_AV = {}
        for key in surface_area:
            surfaces_AV['AV%s' % key] = surface_area[key]/volume

        return surfaces_AV, AV

    '''
    numba functions to increase speed of mathamatical operations
    '''
    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_exp(x):
        return np.exp(x)

    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_cos(x):
        return np.cos(x)

    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_arctan(x):
        return np.arctan(x)

    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_sin(x):
        return np.sin(x)

    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_arccos(x):
        return np.arccos(x)

    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_sqrt(x):
        return np.sqrt(x)

    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_abs(x):
        return np.abs(x)

    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_log(x):
        return np.log(x)

    @staticmethod
    @nb.jit(nb.f8(nb.f8), nopython=True)
    def numba_log10(x):
        return np.log10(x)
