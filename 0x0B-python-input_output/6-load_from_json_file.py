#!/usr/bin/python3
"""
    Function to create an Object from a JSON file

"""
import json


def load_from_json_file(filename):
    """
    Creating an object
    """
    with open(filename, "w", encoding="utf-8") as f:
        for lines in f:
            f.write(json.loads(lines))
