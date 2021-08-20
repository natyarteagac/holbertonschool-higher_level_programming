#!/usr/bin/python3
"""Fetching https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        # Printing the type of the response
        print("\t - type: {}".format(type(html)))
        # Printing the content.
        print("\t - content: {}".format(html))
        # Printing decode format
        print("\t - utf8 content: {}".format(html.decode('utf-8')))
