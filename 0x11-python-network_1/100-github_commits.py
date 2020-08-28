#!/usr/bin/python3
""" Task 100 """

import requests
from sys import argv

if __name__ == "__main__":

    repo = argv[1]
    owner = argv[2]
    url = 'http://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    commits = requests.get(url).json()[:10]
    for commit in commits:
        sha = commit['sha']
        name = commit['commit']['author']['name']
        print("{}: {}".format(sha, name))
