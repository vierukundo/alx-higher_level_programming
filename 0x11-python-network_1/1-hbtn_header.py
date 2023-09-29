#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response"""
from urllib.request import Request, urlopen
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
