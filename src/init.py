import sys
import json
from src.database.client_database import ClientDatabase
def read_args(arguments):
	try:
	  db_server=arguments[1]
	  db_user=arguments[2]
	  db_pass=arguments[3]
	  db_name=arguments[4]
	  config=json.dumps({})
	  config['server']=db_server
	  config['user']=db_user
	  config['password']=db_pass
	  db_name['dbname']=db_name
	  conn=ClientDatabase.connection(config)
	  print(conn)
	except IndexError:
		print("Error numbers of arguments ")
          	

read_args(sys.argv)
