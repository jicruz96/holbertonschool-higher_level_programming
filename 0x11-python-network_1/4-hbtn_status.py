#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """


import requests

if __name__ == "__main__":

    url = 'https://intranet.hbtn.io/status'
    content = requests.get(url).text
    print("Body response:")
    print("\ttype: {}".format(type(content)))
    print("\tcontent: {}".format(content))
