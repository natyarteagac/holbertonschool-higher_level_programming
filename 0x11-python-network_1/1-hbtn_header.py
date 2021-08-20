#!/usr/bin/python3
""" Displaying the value of X-Request-Id variable"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        html = response.read()
    # Ussing .get() method taking header's attribute returning the id's value
    for elements in response.__dict__:
        value = response.headers.get('X-Request-Id')
    print(value)
