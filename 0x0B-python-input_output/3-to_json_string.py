#!/usr/bin/python3
"""
    Function to return the JSON representation
    of an object

"""
import json


def to_json_string(my_obj):
    """
    Returning my_obj into a string
    """
    return json.dumps(my_obj)
