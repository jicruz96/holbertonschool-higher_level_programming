#!/usr/bin/python3
""" Task 5 """

import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    header = 'X-Request-Id'

    header_value = requests.get(url).headers.get(header)

    if header_value:
        print(header_value)
