#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
from requests import get
from sys import argv


if __name__ == '__main__':
    page = get(argv[1])
    print(page.headers['X-Request-Id'])
