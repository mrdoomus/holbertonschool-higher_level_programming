#!/usr/bin/python3
"""list 10 commits from rails repo"""
from requests import get
from sys import argv


if __name__ == '__main__':
    full_url = 'https://api.github.com/repos/' + \
        argv[2] + '/' + argv[1] + '/' + 'commits'
    url = get(full_url)
    data = url.json()
    for key in data[:10]:
        print("{}: {}".format(key.get('sha'),
                              key.get('commit').get('author').get('name')))
