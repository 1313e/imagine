from imagine import Simulator
import numpy as np
import MY_SIMULATOR
class SimulatorTemplate(Simulator):
    """ 
    Detailed description of the simulator
    """
    def __init__(self, measurements, extra_args):
        # Send the measurenents to parent class
        super().__init__(measurements)
        
        # Any initialization task involving extra_args
        ...
    
    @property
    def simulated_quantities(self):
        return {'my_observable_quantity'}
    @property
    def required_field_types(self):
        return {'field_type_1', 'field_type_2'}
    @property
    def allowed_grid_types(self):
        return {'grid_type'}
    
    def simulate(self, key, coords_dict, Nside, output_units):
        """
        This is the main function you need to override to create your simulator.
        The simulator will cycle through a series of Measurements and create
        mock data using this `simulate` function for each of them. 
        
        Parameters
        ----------
        key : tuple
            Information about the observable one is trying to simulate
        coords_dict : dictionary
            If the trying to simulate data associated with discrite positions
            in the sky, this dictionary contains arrays of coordinates. 
        Nside : int
            If simulating a HEALPix map, the HEALPix Nside of the map. 
        output_units : astropy.units.Unit
            The requested output units.
        """
        # The argument key provide extra information about the specific
        # measurement one is trying to simulate
        obs_quantity, freq_Ghz , Nside , tag = key
        
        # If the simulator is working on tabular data, the observed 
        # coordinates can be accesd from coords_dict, e.g.
        lat, lon = coords_dict['lat'], coords_dict['lon']
        
        # Fields can be accessed from a dictionary stored in self.fields
        my_field = self.fields['field_type_1']
        # If a common grid is used, it can be accessed from
        grid = self.grid
        # If fields are allowed to use different grids, 
        # one can get the grid from
        grid_my_field = my_field.grid
    
        # SIMULATE
        results = MY_SIMULATOR.simulate(args)
        # The results should be in a 1-D array of size compatible with 
        # your dataset. I.e. for tabular data: results.size = lat.size
        # and for HEALPix data  results.size = 12*(Nside**2)
    
        return results