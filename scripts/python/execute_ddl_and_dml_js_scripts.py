#!/usr/bin/python3

# import the modules
import os
# import sys 
# import json
# import pymongo

mongo_url = os.environ['MY_SECRET_HOSTNAME']

def print_hostname(hostname):
  new_hostname = hostname + '-custom'
  print(new_hostname)
  
print_hostname(mongo_url)
