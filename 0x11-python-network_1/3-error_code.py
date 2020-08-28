#!/usr/bin/python3
""" takes in a URL, sends a request (that fails) and displays the error """

from urllib import request
from urllib.error import HTTPError
from sys import argv

url = argv[1]

if __name__ == "__main__":
    try:
        with request.urlopen(url) as response:
            print(response)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
