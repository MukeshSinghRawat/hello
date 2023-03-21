#!/usr/bin/python3

# import modules
import os

# Testing the env variables
# mongo_username = os.environ['MY_SECRET_USERNAME']
# print(mongo_username)

# Run the js script on the mongo
js_list = []
js_list.append(os.environ['JS_PATH_1'])
js_list.append(os.environ['JS_PATH_2'])
container_id=os.environ['CONTAINER_ID']

def execute_js(con_id):
  for paths in js_list:
    execution = "docker cp "+paths+" "+con_id+":/"+paths+"\ndocker exec "+con_id+" mongosh "+paths+"\ndocker exec "+con_id+" mongosh --eval 'printjson(db.adminCommand("listDatabases"))'"
    os.system(execution)
       
    
execute_js(container_id)
