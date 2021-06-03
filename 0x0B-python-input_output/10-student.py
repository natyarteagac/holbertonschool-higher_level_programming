#!/usr/bin/python3
"""
    Function to create a class

"""


from typing import NewType


class Student:
    """
    creation of the class student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dic = {}
        iterator = 0
        for iterator in range(attrs):
            iterator += 1
            if attrs == self.__dict__:
                return new_dic[iterator]
