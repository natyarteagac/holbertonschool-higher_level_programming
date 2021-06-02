#!/usr/bin/python3
"""
    Function to read a file

"""


def read_file(filename=""):
    """
    Reading the given file
    """
    with open(filename, "r", encoding="utf-8") as f:
        for lines in f:
            print(lines, end="")
