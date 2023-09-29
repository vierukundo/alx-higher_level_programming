#!/usr/bin/python3
"""Required modules"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': q}

    try:
        response = requests.post(url, data=params)
        response.raise_for_status()
        data = response.json()
        if data:
            user_id = data.get('id')
            user_name = data.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
