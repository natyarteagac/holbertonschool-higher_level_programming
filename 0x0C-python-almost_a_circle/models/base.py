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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        new_list = []
        for index in range(len(list_objs)):
            new_list.append(cls.to_dictionary(list_objs[index]))
        with open(cls.__name__ + ".json", "w+", encoding="utf=8") as f:
            f.write(Base.to_json_string(new_list))
