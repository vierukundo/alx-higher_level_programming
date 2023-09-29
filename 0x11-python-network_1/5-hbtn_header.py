#!/usr/bin/python3
"""module used to fetch url"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    x_Request_Id = response.headers.get('X-Request-Id')
    if x_Request_Id:
        print(x_Request_Id)
