
from  utils.loads import Loads
class ClientDatabase(object):


	def __init__(self, config):
	 self.config=config
	 self.connection(config)
	
	def connection(self,config):
		moduleConf=Loads.load_config()
		db=moduleConf['databases']
		connector=None

		if config['dbtype']=='mysql':
		 	moduleName=moduleConf['databases'][0]['module_name']
		 	varalibles=moduleConf['databases'][0]['connection_string']
			module = Loads.load_module(moduleName)
		 	host=varalibles['host']
		 	user=varalibles['user']
		 	passwd=varalibles['passwd']
		 	db=varalibles['db']
		 	connector = module.connect(host = config['server'],
		 	user=config['user'],passwd=config['password'],db=config['dbname'])
		return connector	
		 
		

		