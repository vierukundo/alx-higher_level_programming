#!/usr/bin/python3
"""Package to use for requesting url"""
import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(res.content.decode('utf-8')))
    print("\t- content:", res.content.decode('utf-8'))
