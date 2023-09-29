#!/usr/bin/python3
"""Require modules"""
import requests
import sys

if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]

    try:
        response = requests.get(
            f"https://api.github.com/users/{user_name}",
            headers={"Authorization": f"token {password}"},
        )

        user_id = response.json().get("id")
        print(user_id)

    except requests.exceptions.RequestException as e:
        pass
