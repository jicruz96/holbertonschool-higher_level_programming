#!/usr/bin/python3
""" displays Github user id """

import requests
from sys import argv

if __name__ == "__main__":

    url = 'api.github.com/user'
    user = argv[1]
    pw = argv[2]

    try:
        out = requests.get(url, auth=(user, pw))
        id = out.json()['id']
        print(id)
    except:
        print('None')
