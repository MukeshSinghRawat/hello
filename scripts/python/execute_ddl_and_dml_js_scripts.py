#!/usr/bin/python3

# import modules
import os

# block 1
mongo_username = os.environ['MY_SECRET_USERNAME']
print(mongo_username)

# block 2
javascript_path_1=os.environ['JS_PATH_1']
javascript_path_2=os.environ['JS_PATH_2']

def execute_js(js_path_1, js_path_2):
  execution = "node "+js_path_1+" \nnode "+js_path_2
  os.system(execution)
  
execute_js(javascript_path_1, javascript_path_2)
