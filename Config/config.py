# Version
version = '0.0.1'

# Data aqcuisition parameters
__DEFAULT_DATA__ = 'data_generation'
__DATA_PATHS__ = {'data_generation': 'DataGeneration.data_generation.DataGeneration'
                  }

# Bids' parameters
__DEFAULT_NB_BIDS__ = 20
__DEFAULT_MAX_Q__ = 60
__DEFAULT_MIN_Q__ = 10
__DEFAULT_MAX_P__ = 200
__DEFAULT_MIN_P__ = 10
__DEFAULT_NB_CLASSES__ = 3
__DEFAULT_NB_GROUPS__ = 2

# Optimization parameters
__DEFAULT_ALGO__ = 'brute_force'
__ALGS_PATHS__ = {'brute_force': 'OptimizationAlgorithms.brute_force.BruteForce',
                  }
