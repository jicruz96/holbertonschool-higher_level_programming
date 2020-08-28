#!/usr/bin/python3
""" displays Github user id """

import requests
from sys import argv

if __name__ == "__main__":

    user = argv[1]
    pw = argv[2]

    print(requests.get('api.github.com/user', auth=(user, pw)).json()['id'])
