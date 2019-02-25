
from src.database.loads import Loads
class ClientDatabase(object):


	def __init__(self, config):
	 self.config=config
	 

	def connection(self):
	 moduleConf=Loads().load_config('config.json')
	 db=moduleConf['databases']
	 connector=None
	 if self.config['dbtype']=='mysql':
		  moduleName=moduleConf['databases'][0]['module_name']
		  varalibles=moduleConf['databases'][0]['connection_string']
		  module = Loads.load_module(moduleName)
		  host=varalibles['host']
		  user=varalibles['user']
		  passwd=varalibles['passwd']
		  db=varalibles['db']
		  connector = module.connect(host = self.config['server'],
		  user=self.config['user'],passwd=self.config['password'],db=self.config['dbname'])
	 return connector	
		 
		

		