#!/usr/bin/python3
"""write a Python script that takes in a URL, sends a request to the URL and displays the value"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode()


    with urllib.request.urlopen(url, data=data) as response:
        html = response.read()
        decoded_html = html.decode('utf-8')
        print(decoded_html)

