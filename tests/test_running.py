import unittest
from modules.inchem_main_class import InChemPyMainClass
from .default_test_settings import DefaultTestSettings


class TestInChemPyMainClass(unittest.TestCase):

    def test_inchempy_runs(self):

        default_settings = DefaultTestSettings()

        inchem_main_class: InChemPyMainClass = InChemPyMainClass(
            filename=default_settings.filename,
            INCHEM_additional=default_settings.INCHEM_additional,
            particles=default_settings.particles,
            constrained_file=default_settings.constrained_file,
            output_folder=None,
            dt=default_settings.dt,
            volume=default_settings.volume,
            surface_area=default_settings.surface_area,
            const_dict=default_settings.const_dict,
            H2O2_dep=default_settings.H2O2_dep,
            O3_dep=default_settings.O3_dep,
            custom=default_settings.custom,
            timed_emissions=default_settings.timed_emissions,
            timed_inputs=default_settings.timed_inputs,
            custom_filename=default_settings.custom_filename)

        output_concentrations, times = inchem_main_class.run(
            t0=0,
            seconds_to_integrate=60,  # smaller for the test to run
            dt=default_settings.dt,
            timed_emissions=default_settings.timed_emissions,
            timed_inputs=default_settings.timed_inputs,
            spline=default_settings.spline,
            temperatures=default_settings.temperatures,
            rel_humidity=default_settings.rel_humidity,
            const_dict=default_settings.const_dict,
            M=default_settings.M,
            light_type=default_settings.light_type,
            glass=default_settings.glass,
            diurnal=default_settings.diurnal,
            city=default_settings.city,
            date=default_settings.date,
            lat=default_settings.lat,
            ACRate_dict=default_settings.ACRate,
            light_on_times=default_settings.light_on_times,
            initial_conditions_gas=default_settings.initial_conditions_gas,
            initials_from_run=default_settings.initials_from_run,
            path=None,
            adults=default_settings.adults,
            children=default_settings.children,
            output_folder=None,
            reactions_output=default_settings.reactions_output,
            initial_dataframe=None
        )

        self.assertEqual(2, len(output_concentrations))
        self.assertEqual(4, output_concentrations[60]["O3"])


if __name__ == '__main__':
    unittest.main()
