#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status with requests"""
from requests import get


if __name__ == '__main__':
    page = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(page.text)))
    print("\t- content: {}".format(page.content.decode('utf-8')))
