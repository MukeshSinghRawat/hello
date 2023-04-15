#!/usr/bin/python3

# import modules
import os

# Import all variables exposed to the environment
js_list = []
js_list.append(os.environ['DDL_SCRIPT_PATH'])
js_list.append(os.environ['DML_SCRIPT_PATH'])
auth_mechanism = os.environ['AUTH_MECHANISM']
mongo_connection_string = os.environ['MONGO_CONNECTION_STRING']
tls_certificate_key_file = os.environ['TLS_CERTIFICATE_KEY_FILE']
tls_certificate_key_file_password = os.environ['TLS_CERTIFICATE_KEY_FILE_PASSWORD']

# def execute_js(con_id, list):
def execute_js(list):
  for paths in list:
#     basename = os.path.basename(paths)
#     execution = "docker cp "+paths+" "+con_id+":/"+basename+"\ndocker exec "+con_id+" mongosh "+basename+"\ndocker exec "+con_id+" mongosh --eval 'db.getMongo().getDBNames()'"
    execution = ###############################
    os.system(execution)   
    
# execute_js(container_id, js_list)
execute_js(js_list)
