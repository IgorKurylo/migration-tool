import sys
import importlib
import json
class Loads(object):

	 def __init__(self):
		 pass
	 def load_module(modulename):
	  module=None
	  try:
		  module=importlib.import_module(modulename)
	  except ImportError:
		  print("Failed to load {module}".format(module=modulename),file=sys.stderr)
	  return module
	 
	 def load_config(filepath):
	  config=None
	  with open(filepath) as conf:
	   config=json.load(conf)
	   return config
