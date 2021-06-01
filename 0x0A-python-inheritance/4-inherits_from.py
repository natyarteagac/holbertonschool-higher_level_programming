#!/usr/bin/python3
"""
Function to return True or False if the object is an instance of
a class that inherited
"""


def inherits_from(obj, a_class):
    if issubclass(a_class):
        return True
    else:
        return False
