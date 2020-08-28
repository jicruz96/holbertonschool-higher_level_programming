#!/usr/bin/python3
""" Task 1 """

from urllib import request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
