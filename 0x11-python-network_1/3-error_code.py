#!/usr/bin/python3
""" takes in a URL, sends a request (that fails) and displays the error """

from urllib.error import HTTPError
from urllib.request import urlopen
from sys import argv

url = argv[1]

if __name__ == "__main__":
    try:
        with urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
