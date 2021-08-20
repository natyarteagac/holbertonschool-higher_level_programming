#!/usr/bin/python3
""" Sending a POST request to the passed URL with the email
as parameter and displaying the body of the response"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    # Encode the data object into a string
    email = argv[2]
    data = parse.urlencode({'email': email})
    # Set the encoding schema
    data = data.encode('utf-8')
    url = argv[1]
    # Make the POST request to the source
    with request.urlopen(url, data) as response:
        html = response.read()
        html = html.decode('utf-8')
        print(html)
