#!/usr/bin/python3

# import modules
import os

# block 1
mongo_username = os.environ['MY_SECRET_USERNAME']
print(mongo_username)

# block 2
js_list = []
js_list.append(os.environ['JS_PATH_1'])
js_list.append(os.environ['JS_PATH_2'])

# javascript_path_1=os.environ['JS_PATH_1']
# javascript_path_2=os.environ['JS_PATH_2']

def execute_js():
  for paths in js_list:
    execution = "node "+paths
    os.system(execution)

execute_js()
