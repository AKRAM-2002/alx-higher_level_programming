#!/usr/bin/python3
"""

"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    i = 0

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    
    response = get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Get the 10 most recent commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")