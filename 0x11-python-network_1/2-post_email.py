#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = sys.argv[2]
    params = {'email': value}
    data = urlencode(params)
    data = data.encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        page = response.read().decode('utf-8')
    print(page)
