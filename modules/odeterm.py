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
