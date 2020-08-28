#!/usr/bin/python3
""" Task 0 """

from urllib import request

if __name__ == "__main__":

    url = 'https://intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        print("Body response:")
        for item in response:
            print("\t- type: {}".format(type(item)))
            print("\t- content: {}".format(item))
            print("\t- utf8 content: {}".format(item.decode("utf-8")))
