#!/usr/bin/python3
"""Uses GitHub API to display a user's ID."""
import sys

import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    print(response.json().get("id"))
