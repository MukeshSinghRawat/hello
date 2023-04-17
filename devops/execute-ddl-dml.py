#!/usr/bin/python3

# import modules
import os
import os.path
import sys

# Importing all variables exposed to the environment
list = []
list.append(os.environ['DDL_SCRIPT_PATH'])
list.append(os.environ['DML_SCRIPT_PATH'])

# ddl_script_path = os.environ['DDL_SCRIPT_PATH']
# dml_script_path = os.environ['DML_SCRIPT_PATH']
# auth_mechanism = os.environ['AUTH_MECHANISM']
mongo_connection_string = os.environ['MONGO_CONNECTION_STRING']
# tls_certificate_key_file = os.environ['TLS_CERTIFICATE_KEY_FILE']
# tls_certificate_key_file_password = os.environ['TLS_CERTIFICATE_KEY_FILE_PASSWORD']

# Define functions to execute ddl and dml    
def execute_js_scripts(mongo_connection_string, js_script_path):
  shell_command = "mongosh '"+mongo_connection_string+"'" < js_script_path
  os.system(shell_command)
  
# Calling the functions
for js_files_path in list:
  if os.path.exists(js_files_path): 
    execute_js_scripts(mongo_connection_string, js_files_path)
  else:
    sys.exit(js_files_path+" doesn't exist...")
