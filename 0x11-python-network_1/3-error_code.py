#!/usr/bin/python3
"""write a Python script that takes in a URL,
sends a request to the URL and displays the value
"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
