#!/usr/bin/python3
"""
Function to return True or False if the object is an instance of the
specified class.

"""


def is_same_class(obj, a_class):
    """ Is same class

    """

    if type(obj) == a_class:
        return True
    else:
        return False
