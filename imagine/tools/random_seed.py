"""
This module provides a time-thread dependent seed value.

For the testing suites, please turn to "imagine/tests/tools_tests.py".
"""

# %% IMPORTS
# Built-in imports
import logging as log
import threading
import time

# Package imports
import numpy as np

# All declaration
__all__ = ['ensemble_seed_generator', 'seed_generator']


# %% FUNCTION DEFINITIONS
def seed_generator(trigger):
    """
    Sets trigger as 0 will generate time-thread dependent method
    otherwise returns the trigger as seed.

    Parameters
    ----------
    trigger : int
        Non-negative pre-fixed seed.

    Returns
    -------
    seed : int
        A random seed value.
    """
    log.debug('@ random_seed::seed_generator')
    if trigger > 0:
        return int(trigger)
    elif trigger == 0:
        return round(time.time()*1E+9) % int(1E+8) + threading.get_ident() % int(1E+8)
    else:
        raise ValueError('unsupported random seed value')

def ensemble_seed_generator(size):
    """
    Generates fixed random seed values for each realization in ensemble.

    Parameters
    ----------
    size : int
        Number of realizations in ensemble.

    Returns
    -------
    seeds : numpy.ndarray
        An array of random seeds.
    """
    log.debug('@ random_seed::ensemble_seed_generator')
    # the uint32 is defined by the random generator's capacity
    return np.random.randint(low=1, high=np.uint32(-1)//3, size=np.uint64(size))
