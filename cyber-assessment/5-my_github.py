#!/usr/bin/python3

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

api_request = requests.get('https://api.github.com/user', auth=(username, password))
if (api_request.status_code == 401):
    print(None)
else:
    info = api_request.json()
    print(info["id"])
