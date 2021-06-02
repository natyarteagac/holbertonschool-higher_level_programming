#!/usr/bin/python3
"""
    Function that writes an object to a
    text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writing an object to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(my_obj))
        return json.dumps(my_obj)
