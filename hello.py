#!/usr/bin/env python3

import os
import json
import templates

# Create an empty dictionary
env = {}

for key, value in os.environ.items():
    env[key] = value
    print(key, value)

print("Content-Type: application/json")
print()

print(json.dumps(env, indent=4))

print()
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
message = "\nQuery string:{}".format(os.environ.get('QUERY_STRING'))
print(message)

print("<br>")
#print('Content-Type: text/html; charset=UTF-8')
message = "\nBrowser:{}".format(os.environ.get("HTTP_USER_AGENT"))
print(message)
print("<br>")