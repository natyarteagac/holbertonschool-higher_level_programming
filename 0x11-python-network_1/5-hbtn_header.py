#!/usr/bin/python3
""" Response header value """
import requests
from sys import argv

if __name__ == "__main__":
    url = requests.get(argv[1])
    print(url.headers.get('X-Request-Id'))
