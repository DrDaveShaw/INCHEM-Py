

class SpeciesODETerm:
    def __init__(self, contributions):
        self.compiled_contributions = [compile(c,'<string>','eval') for c in contributions]

    def __call__(self, full_dict):
        result = 0.0
        for contribution in self.compiled_contributions:
            result += eval(contribution,{},full_dict)
        return result
