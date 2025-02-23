#!/usr/bin/python3
"""Fetches the 10 most recent commits of my GitHub repository."""
import sys

import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/CollinsOmwoyo/alx-higher_level_programming/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Fetch only the latest 10 commits
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name", "Unknown")
            print(f"{sha}: {author}")
    else:
        print("Error:", response.status_code)
