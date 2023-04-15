#!/usr/bin/python3

# import modules
import os

# Testing the env variables
# mongo_username = os.environ['MY_SECRET_USERNAME']
# print(mongo_username)

# Run the js script on the mongo
js_list = []
js_list.append(os.environ['DDL_SCRIPT_PATH'])
js_list.append(os.environ['DML_SCRIPT_PATH'])
auth_mechanism = os.environ['AUTH_MECHANISM']
mongo_connection_string = os.environ['MONGO_CONNECTION_STRING']
tls_certificate_key_file = os.environ['TLS_CERTIFICATE_KEY_FILE']
tls_certificate_key_file_password = os.environ['TLS_CERTIFICATE_KEY_FILE_PASSWORD']
# container_id = os.environ['CONTAINER_ID']

# def execute_js(con_id, list):
def execute_js(list):
  for paths in list:
#     basename = os.path.basename(paths)
#     execution = "docker cp "+paths+" "+con_id+":/"+basename+"\ndocker exec "+con_id+" mongosh "+basename+"\ndocker exec "+con_id+" mongosh --eval 'db.getMongo().getDBNames()'"
    execution = ###############################
    os.system(execution)   
    
# execute_js(container_id, js_list)
execute_js(js_list)
