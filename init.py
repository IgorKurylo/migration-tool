import sys
import json
from src.database.client_database import ClientDatabase
from src.database.loads import Loads

def read_args(arguments):
	try:
	  if len(arguments)>1:
	   db_server=arguments[1]
	   db_user=arguments[2]
	   db_pass=arguments[3]
	   db_name=arguments[4]
	  else:
		  filepath='./src/database/utils/args.json'
		  argsjson=Loads.load_config(filepath=filepath)
		  db_server=argsjson['host']
		  db_user=argsjson['user']
		  db_pass=argsjson['pass']
		  db_name=argsjson['db']
	  config={}
	  config['server']=db_server
	  config['user']=db_user
	  config['password']=db_pass
	  config['dbname']=db_name
	  conn=ClientDatabase(config).connection()
	  cursor=conn.cursor()
	  cursor.excute("SELECT * FROM t1")
	  numrows=cursor.rowcount
	  print(numrows)
	except IndexError:
		print("Error numbers of arguments ")
          	

read_args(sys.argv)
