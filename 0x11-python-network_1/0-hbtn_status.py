#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        req = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
    print("\t- utf8 content: {}".format(req.decode('utf-8')))
