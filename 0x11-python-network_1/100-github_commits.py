#!/usr/bin/python3
"""Required modules"""
import requests
import sys


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repository_name)

    try:
        response = requests.get(url)

        commits = response.json()[:10]

        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        pass
