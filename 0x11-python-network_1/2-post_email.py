#!/usr/bin/python3
""" Sending a POST request to the passed URL with the email
as parameter and displaying the body of the response"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]})
    data = data.encode('utf-8')
    url = argv[1]
    with request.urlopen(url, data) as response:
        print("Your email is: {}".format(argv[2]))
