#!/usr/bin/python3
"""writing a Python script using module requests"""

import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        r_json = response.json()
        if r_json:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
