#!/usr/bin/python3
""" Sending a POST request to the passed URL with the email
as parameter and finally displays the body of the response
"""

from sys import argv
import requests

if __name__ == "__main__":
    email = {'email': argv[2]}
    url = requests.post(argv[1], data=email)
    print(url.text)
