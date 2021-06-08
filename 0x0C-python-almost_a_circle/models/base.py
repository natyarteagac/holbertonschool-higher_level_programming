#!/usr/bin/python3
"""
    Creating the Base Class


"""
import json


class Base:
    """
    Creating the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with open(Base.json, "w", encoding="utf=8") as f:
            if list_objs is None:
                f.write("[]")
            else:
