#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """


import requests

if __name__ == "__main__":

    url = 'https://intranet.hbtn.io/status'
    content = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
