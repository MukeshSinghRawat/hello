#!/usr/bin/python3

# import modules
import os

# Importing all variables exposed to the environment
# list = []
# list.append(os.environ['DDL_SCRIPT_PATH'])
# list.append(os.environ['DML_SCRIPT_PATH'])

ddl_script_path = os.environ['DDL_SCRIPT_PATH']
dml_script_path = os.environ['DML_SCRIPT_PATH']
auth_mechanism = os.environ['AUTH_MECHANISM']
mongo_connection_string = os.environ['MONGO_CONNECTION_STRING']
tls_certificate_key_file = os.environ['TLS_CERTIFICATE_KEY_FILE']
tls_certificate_key_file_password = os.environ['TLS_CERTIFICATE_KEY_FILE_PASSWORD']

# Define functions to execute ddl and dml
def execute_ddl(mongo_connection_string, tls_certificate_key_file, tls_certificate_key_file_password, auth_mechanism, ddl_script_path):
  if os.path.exists(ddl_script_path):
    ddl_shell_command = "mongosh '"+mongo_connection_string+"' --tls --tlsCertificateKeyFile "+tls_certificate_key_file+" --tlsCertificateKeyFilePassword "+tls_certificate_key_file_password+" --authenticationMechanism "+auth_mechanism < ddl_script_path
    os.system(ddl_shell_command)   
  else:
    print(ddl_script_path+" doesn't exist...")
    
def execute_dml(mongo_connection_string, tls_certificate_key_file, tls_certificate_key_file_password, auth_mechanism, dml_script_path):
  if os.path.exists(dml_script_path):
    dml_shell_command = "mongosh '"+mongo_connection_string+"' --tls --tlsCertificateKeyFile "+tls_certificate_key_file+" --tlsCertificateKeyFilePassword "+tls_certificate_key_file_password+" --authenticationMechanism "+auth_mechanism < dml_script_path
    os.system(dml_shell_command)   
  else:
    print(dml_script_path+" doesn't exist...")
  
# Calling the functions
try:
  execute_ddl(mongo_connection_string, tls_certificate_key_file, tls_certificate_key_file_password, auth_mechanism, ddl_script_path)
  execute_dml(mongo_connection_string, tls_certificate_key_file, tls_certificate_key_file_password, auth_mechanism, dml_script_path)
 
except:
  print("script execution failed...")
