#!/usr/bin/python3
"""
    Function to write a file

"""


def write_file(filename="", text=""):
    """
    Writing the text
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
