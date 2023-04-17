#!/usr/bin/python3

# import modules
import os
import sys

# Importing all variables exposed to the environment
list = []
list.append(os.environ['DDL_SCRIPT_PATH'])
list.append(os.environ['DML_SCRIPT_PATH'])

# ddl_script_path = os.environ['DDL_SCRIPT_PATH']
# dml_script_path = os.environ['DML_SCRIPT_PATH']
auth_mechanism = os.environ['AUTH_MECHANISM']
mongo_connection_string = os.environ['MONGO_CONNECTION_STRING']
tls_certificate_key_file = os.environ['TLS_CERTIFICATE_KEY_FILE']
tls_certificate_key_file_password = os.environ['TLS_CERTIFICATE_KEY_FILE_PASSWORD']

# Define functions to execute ddl and dml    
def execute_js_scripts(mongo_connection_string, tls_certificate_key_file, tls_certificate_key_file_password, auth_mechanism, js_script_path):
  dml_shell_command = "mongosh '"+mongo_connection_string+"' --tls --tlsCertificateKeyFile "+tls_certificate_key_file+" --tlsCertificateKeyFilePassword "+tls_certificate_key_file_password+" --authenticationMechanism "+auth_mechanism < js_script_path
  os.system(dml_shell_command)
  
# Calling the functions
for js_files in list:
  if os.path.exists(js_files):  
    execute_js_scripts(mongo_connection_string, tls_certificate_key_file, tls_certificate_key_file_password, auth_mechanism, js_files)
  else:
      sys.exit(js_files+" doesn't exist...")
