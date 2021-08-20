#!/usr/bin/python3
""" Displaying Error codes with testing from intranet"""
from sys import argv
import requests

if __name__ == "__main__":
    url = requests.get(argv[1])
    if url.status_code <= 400:
        print(url.text)
    else:
        print("Error code: {}".format(url.status_code))
