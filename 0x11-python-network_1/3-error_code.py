#!/usr/bin/python3
"""Displays the body of the response"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as exception:
        print("Error code: {}".format(exception.__dict__.get('code')))
