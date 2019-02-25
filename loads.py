import sys
import importlib
import json
class Loads(object):
	 
	 def __init__(self, module_name,config):
	   self.moduleName=module_name
	   self.module=load_module(module_name)
	 
	 def load_module(modulename):
		module=None
		try:
			module=importlib.import_module(modulename)
		except ImportError:
			print("Failed to load {module}".format(module=modulename),file=sys.stderr)
		return module
	 
	 def load_config(self):
		 config=None
		 with open('config.json') as conf:
			 config=json.loa(conf)
	   	 return config

	 def get(self):
		return self.module