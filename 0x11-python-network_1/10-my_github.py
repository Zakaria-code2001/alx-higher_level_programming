#!/usr/bin/python3
"""writing a Python script using module requests for git id"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    author = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    request = requests.get("https://api.github.com/user", auth=author)
    print(request.json().get("id"))
