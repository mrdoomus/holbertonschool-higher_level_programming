#!/usr/bin/python3
"""Swapi request, handles pagination"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search=' + argv[1]
    req = get(url)
    data = req.json()
    print("Number of results: {}".format(data['count']))
    for key in data['results']:
        print(key['name'])

    while data.get("next"):
        url = data.get("next")
        response = get(url)
        data = response.json()
        for key in data['results']:
            print(key.get("name"))
