#!/usr/bin/python3
"""Package to use for requesting url"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    try:
        req = Request(sys.argv[1])
        with urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
