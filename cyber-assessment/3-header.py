#!/usr/bin/python3

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as url_obj:
    headers = url_obj.headers
    next = False
    for h in headers:
        if (h == "X-Request-Id"):
            print(headers[h])



