#!/usr/bin/python3
"""
    Function to create a class

"""


class Student:
    """
    creation of the class student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        iterator = 0
        new_dictionary = {}
        if type(attrs) == list:
            for iterator in attrs:
                if iterator in self.__dict__:
                    new_dictionary[iterator] = self.__dict__[iterator]
            return new_dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.first_name = json
        self.last_name = json
        self.age = json
