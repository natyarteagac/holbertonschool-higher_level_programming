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
        """
        Defining all the atributes of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returning a dictionary of the list of give atributes
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Creating a dictionary of dictionaries
        """
        if list_objs is None:
            list_objs = []
        new_list = []
        for index in range(len(list_objs)):
            new_list.append(cls.to_dictionary(list_objs[index]))
        with open(cls.__name__ + ".json", "w+", encoding="utf=8") as f:
            f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returning a dictionary
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creating dummy instance """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Loading a file """
        filename = cls.__name__ + ".json"
        if not filename:
            return []
        else:
            with open(filename, "r", encoding="utf-8") as f:
                new_list_two = []
                new_list_two = cls.from_json_string(f.read())
                new_list_three = []
                for index in range(len(new_list_two)):
                    new_list_three.append(cls.create(**new_list_two[index]))
                return new_list_three
