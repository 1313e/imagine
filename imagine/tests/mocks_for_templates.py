import sys
import numpy as np
import astropy.units as u
from imagine.fields import DummyField

# --------------------------------------------------------------------------
# For testing the magnetic_field_template
def MY_GMF_MODEL_compute_B(param_A, param_B, x_coord, y_coord, z_coord, seed):
    # Checks interface with physical parameters
    Bx = param_A
    # Checks interface with dimensionless parameters
    By = param_B * 1e-10 *u.tesla # This will also test unit conversions..
    # Checks cartesian coordinates
    Bz = 42*(x_coord.value*y_coord.value*z_coord.value) * u.microgauss
    return Bx, By, Bz

MY_GMF_MODEL = type(sys)('MY_GMF_MODEL')
MY_GMF_MODEL.compute_B = MY_GMF_MODEL_compute_B


# --------------------------------------------------------------------------
# For testing the thermal_electrons_template
def MY_GALAXY_MODEL_compute_ne(param_A, param_B, r, theta, phi, seed):
    # Checks interface with physical parameters
    A = param_A.to_value(u.kpc)
    # Checks interface with dimensionless parameters
    B = param_B * 1*u.cm**-3
    # Checks spherical coordinates
    return A*B*(r.value*theta.value*phi.value)*seed

MY_GALAXY_MODEL = type(sys)('MY_GALAXY_MODEL')
MY_GALAXY_MODEL.compute_ne = MY_GALAXY_MODEL_compute_ne

# --------------------------------------------------------------------------
# For testing the simulator_template
def MY_SIMULATOR_simulate():
    pass

MY_SIMULATOR = type(sys)('MY_SIMULATOR')
MY_SIMULATOR.simulate = MY_SIMULATOR_simulate



# --------------------------------------------------------------------------
# For testing the field_factory_template
class MY_PACKAGE_MY_FIELD_CLASS(DummyField):

    # Class attributes
    NAME = 'name_of_the_dummy_field'

    @property
    def field_checklist(self):
        return {'Parameter_A': 'parameter_A_settings',
                'Parameter_B': None}

MY_PACKAGE = type(sys)('MY_PACKAGE')
MY_PACKAGE.MY_FIELD_CLASS = MY_PACKAGE_MY_FIELD_CLASS
MY_PACKAGE.A_std_val = 1
MY_PACKAGE.B_std_val = 1
MY_PACKAGE.A_min = 0
MY_PACKAGE.A_max = 2
MY_PACKAGE.B_min = 0
MY_PACKAGE.B_max = 2
MY_PACKAGE.B_sig = 1


# --------------------------------------------------------------------------
# For testing the pipeline_template
class MY_SAMPLER_Sampler:
    def __init__(param_names=None, loglike=None, prior_transform=None,
                 prior_pdf=None):
        pass

    def run(**kwargs):
        return {'samples': [0.5,0.5], 'logz': 42, 'logzerr': 17}

MY_SAMPLER = type(sys)('MY_SAMPLER')
MY_SAMPLER.Sampler = MY_SAMPLER_Sampler
