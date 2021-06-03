#!/usr/bin/python3
"""
    Function to create an Object from a JSON file

"""
import json


def load_from_json_file(filename):
    """
    Creating an object
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f)
