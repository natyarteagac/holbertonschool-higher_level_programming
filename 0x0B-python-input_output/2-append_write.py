#!/usr/bin/python3
"""
    Function to append a string into the text

"""


def append_write(filename="", text=""):
    """
    Writing the text
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
