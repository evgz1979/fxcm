from fxcmpy.fxcmpy import fxcmpy as fxcmpy  
from fxcmpy.fxcmpy_open_position import fxcmpy_open_position 
from fxcmpy.fxcmpy_closed_position import fxcmpy_closed_position 
from fxcmpy.fxcmpy_order import fxcmpy_order 
from fxcmpy.fxcmpy_oco_order import fxcmpy_oco_order 
from fxcmpy.fxcmpy_data_reader import fxcmpy_candles_data_reader
from fxcmpy.fxcmpy_data_reader import fxcmpy_tick_data_reader
from pkg_resources import get_distribution, DistributionNotFound
try:
	__version__ = get_distribution(__name__).version
except DistributionNotFound:
	# package is not installed
	__version__ = 'package is not installed'
	pass