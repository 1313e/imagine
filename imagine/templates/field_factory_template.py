from imagine import GeneralFieldFactory

class YourField_Factory(GeneralFieldFactory):
    """Example: field factory for YourFieldClass"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.field_class = YourFieldClass

        # Default values are used for inactive parameters
        self.default_parameters = {'param_A': param_A_value,
                                   'param_B': param_B_value,
                                   ... }
        # All parameters should have a range
        self.parameter_ranges = {'param_A': [A_min, A_max],
                                 'param_B': [B_min, B_max],
                                 ... }
        # Note that both ranges and default values should include units

        # Any parameters ommitted in the prior dictionary will use a flat prior
        self.priors = {'param_A': PriorA(prior_args, interval=[A_min, A_max])
                       ... }
