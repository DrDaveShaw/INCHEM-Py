from typing import Union, List, Dict, Optional


class DefaultTestSettings:
    """
        @brief A class recording, and weakly documenting, all the settings from an unchanged inchempy_main run

    """

    def __init__(self,
                 filename: str = 'mcm_v331.fac',
                 particles: bool = True,
                 INCHEM_additional: bool = True,
                 custom: bool = False,
                 custom_filename: str = 'custom_input.txt',
                 spline: Union[str, float] = 293.0,
                 temperatures: Optional[List[List[float]]] = None,
                 rel_humidity: float = 50.,
                 M: float = 2.51e+19,
                 const_dict: Optional[Dict[str, float]] = None,
                 ACRate: Optional[Dict[int, float]] = None,
                 diurnal: bool = True,
                 city: str = "Bergen_urban",
                 date: str = "21-06-2020",
                 lat: float = 45,
                 light_type: str = "Incand",
                 light_on_times: Optional[List[List[int]]] = None,
                 glass: str = "glass_C",
                 volume: float = 2.97e7,
                 surface_area: Optional[Dict[str, float]] = None,
                 H2O2_dep: bool = True,
                 O3_dep: bool = True,
                 adults: int = 0,
                 children: int = 0,
                 initials_from_run: bool = False,
                 initial_conditions_gas: str = 'initial_concentrations.txt',
                 timed_emissions: bool = False,
                 timed_inputs: Optional[Dict[str, List[List[Union[int, float]]]]] = None,
                 constrained_file: Optional[str] = None,
                 dt: int = 60,
                 t0: int = 0,
                 seconds_to_integrate: int = 86400,
                 custom_name: str = "Bergen_urban",
                 reactions_output: bool = True,
                 output_graph: bool = True,
                 output_species: Optional[List[str]] = None,
                 settings_file: str = __file__):
        """
        @brief Initialize the InChemPySettings class with simulation parameters.

        This class holds all configuration values for an INCHEM-Py simulation, including
        environmental settings, reaction setup, emissions, lighting, deposition, and output control.

        For further details refer to the INCHEM-Py documentation

        @param filename Input FACSIMILE format filename.
        @param particles Boolean flag to include particle modeling.
        @param INCHEM_additional Include additional INCHEM reactions not in the MCM download.
        @param custom Include custom reactions.
        @param custom_filename Filename for custom reaction input.
        @param spline Method of temperature interpolation or a constant temperature.
        @param temperatures List of [time, temperature] pairs for interpolation.
        @param rel_humidity Relative humidity (in %).
        @param M Number density of air in molecules/cm³.
        @param const_dict Dictionary of species to hold constant with their values.
        @param ACRate Dictionary of air change rates {time (s): rate (1/s)}.
        @param diurnal Enable diurnal variation of outdoor concentrations.
        @param city City for outdoor concentration profiles.
        @param date Simulation date in format "DD-MM-YYYY".
        @param lat Latitude of the simulation location.
        @param light_type Indoor light source type.
        @param light_on_times Schedule for indoor lighting (on/off in hours).
        @param glass Type of glass for light attenuation.
        @param volume Volume of the simulation room in cm³.
        @param surface_area Dictionary of surface areas by material in cm².
        @param H2O2_dep Enable surface deposition modeling for H2O2.
        @param O3_dep Enable surface deposition modeling for O3.
        @param adults Number of adults in the room.
        @param children Number of children (age 10) in the room.
        @param initials_from_run If True, use previous model output for initial conditions.
        @param initial_conditions_gas Filename with initial concentrations if not using previous output.
        @param timed_emissions Enable time-dependent emissions of species.
        @param timed_inputs Dictionary of species and their emission schedules.
        @param constrained_file CSV file to constrain species or rates over time.
        @param dt Time step for integration (seconds).
        @param t0 Start time in seconds from midnight.
        @param seconds_to_integrate Duration of the simulation in seconds.
        @param custom_name Label for output files and folders.
        @param reactions_output Save detailed reaction rates and constants.
        @param output_graph Output concentration plots and CSVs.
        @param output_species List of species to include in output graphs.
        @param settings_file Optional name of the settings file used.
        """

        self.filename: str = filename
        self.particles: bool = particles
        self.INCHEM_additional: bool = INCHEM_additional
        self.custom: bool = custom
        self.custom_filename: str = custom_filename

        self.spline: Union[str, float] = spline
        self.temperatures: List[List[float]] = temperatures or [[25200, 288.15], [50400, 294.15]]
        self.rel_humidity: float = rel_humidity
        self.M: float = M

        self.const_dict: Dict[str, float] = const_dict or {
            'O2': 0.2095 * self.M,
            'N2': 0.7809 * self.M,
            'H2': 550e-9 * self.M,
            'saero': 1.3e-2
        }

        self.ACRate: Dict[int, float] = ACRate or {
            0: 0.5 / 3600,
            3600 * 24: 1 / 3600,
            3600 * 48: 2 / 3600
        }

        self.diurnal: bool = diurnal
        self.city: str = city

        self.date: str = date
        self.lat: float = lat
        self.light_type: str = light_type

        self.light_on_times: List[List[int]] = light_on_times or [[7, 19], [31, 43], [55, 67], [79, 91]]

        self.glass: str = glass

        self.volume: float = volume

        self.surface_area: Dict[str, float] = surface_area or {
            'SOFT': 10.42e4,
            'PAINT': 33.76e4,
            'WOOD': 18.23e4,
            'METAL': 7.46e4,
            'CONCRETE': 0.391e4,
            'PAPER': 1.89e4,
            'LINO': 0,
            'PLASTIC': 14.18e4,
            'GLASS': 2.61e4,
            'HUMAN': 0,
            'OTHER': 0
        }

        self.H2O2_dep: bool = H2O2_dep
        self.O3_dep: bool = O3_dep

        self.adults: int = adults
        self.children: int = children

        self.initials_from_run: bool = initials_from_run
        self.initial_conditions_gas: str = initial_conditions_gas

        self.timed_emissions: bool = timed_emissions
        self.timed_inputs: Dict[str, List[List[Union[int, float]]]] = timed_inputs or {
            "LIMONENE": [[46800, 47400, 5e10], [107600, 108000, 5e8]],
            "BPINENE": [[46800, 47400, 5e10]]
        }

        self.constrained_file: Optional[str] = constrained_file

        self.dt: int = dt
        self.t0: int = t0
        self.seconds_to_integrate: int = seconds_to_integrate

        self.custom_name: str = custom_name
        self.reactions_output: bool = reactions_output
        self.output_graph: bool = output_graph
        self.output_species: List[str] = output_species or ['LIMONENE', 'BPINENE']

        self.settings_file: Optional[str] = settings_file