#!/usr/bin/python3

# import modules
import os

# Import all variables exposed to the environment
list = []
list.append(os.environ['DDL_SCRIPT_PATH'])
list.append(os.environ['DML_SCRIPT_PATH'])
auth_mechanism = os.environ['AUTH_MECHANISM']
mongo_connection_string = os.environ['MONGO_CONNECTION_STRING']
tls_certificate_key_file = os.environ['TLS_CERTIFICATE_KEY_FILE']
tls_certificate_key_file_password = os.environ['TLS_CERTIFICATE_KEY_FILE_PASSWORD']

def execute_js(mongo_connection_string, tls_certificate_key_file, tls_certificate_key_file_password, auth_mechanism, list):
  for paths in list:
    execution = "mongosh "+mongo_connection_string+" --tls --tlsCertificateKeyFile "+tls_certificate_key_file+" --tlsCertificateKeyFilePassword "+tls_certificate_key_file_password+" --authenticationMechanism "+auth_mechanism < paths
    os.system(execution)   
    
# Calling the function here
try:
  execute_js(mongo_connection_string, tls_certificate_key_file, tls_certificate_key_file_password, auth_mechanism, list)
 
except:
  print("script execution failed...")
