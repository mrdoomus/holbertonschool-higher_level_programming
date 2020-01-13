#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""
from requests import post
from sys import argv


if __name__ == '__main__':
    if len(argv) == 2:
        req = post('http://0.0.0.0:5000/search_user', {'q': argv[1]})
        try:
            data = req.json()
            if data:
                print("[{}] {}".format(data.get('id'), data.get('name')))
            else:
                print("No result")
        except TypeError:
            print("Not a valid JSON")
    else:
        print("No result")
