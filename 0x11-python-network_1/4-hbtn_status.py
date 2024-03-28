#!/usr/bin/python3
"""What's my status"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    
    response = requests.get(url)
    html = response.text
    
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
