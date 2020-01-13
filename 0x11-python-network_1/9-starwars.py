#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search=' + argv[1]
    req = get(url)
    data = req.json()
    print("Number of results: {}".format(data['count']))
    for key in data['results']:
        print(key['name'])
