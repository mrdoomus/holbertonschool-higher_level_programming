#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""
from requests import post
from sys import argv


if __name__ == '__main__':
    q = ""
    if len(argv) == 2:
        q = argv[1]
        req = post(
            'http://f944a8f69e43.19.hbtn-cod.io:5000/search_user', {'q': q})
        try:
            data = req.json()
            if data:
                print("[{}] {}".format(data.get('id'), data.get('name')))
            else:
                print("No result")
        except TypeError:
            print("Not a valid JSON")
    elif len(argv) == 1:
        req = post(
            'http://f944a8f69e43.19.hbtn-cod.io:5000/search_user', {'q': q})
    else:
        print("No result")
