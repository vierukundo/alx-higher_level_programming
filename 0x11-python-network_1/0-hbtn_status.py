#!/usr/bin/python3
"""Package to use for requesting url"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        page = response.read()
    print("Body response:")
    print("\t- type:", type(page))
    print("\t- content:", page)
    print("\t- utf8 content:", page.decode('utf-8'))
