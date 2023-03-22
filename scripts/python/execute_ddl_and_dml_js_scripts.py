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
container_id = os.environ['CONTAINER_ID']

def execute_js(con_id, list):
  for paths in list:
    basename = os.path.basename(paths)
    execution = "docker cp "+paths+" "+con_id+":/"+basename+"\ndocker exec "+con_id+" mongosh "+basename+"\ndocker exec "+con_id+" mongosh --eval 'db.getMongo().getDBNames()'"
    os.system(execution)   
    
execute_js(container_id, js_list)
