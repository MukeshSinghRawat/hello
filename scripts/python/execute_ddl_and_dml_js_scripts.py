#!/usr/bin/python3

# import modules
import os

# block 1
mongo_username = os.environ['MY_SECRET_USERNAME']
print(mongo_username)

# block 2
javascript_path=os.environment['JS_PATH']
def execute_js(js_path):
  execution = "node "+js_path
  os.system(execution)
  
execute_js(javascript_path)
