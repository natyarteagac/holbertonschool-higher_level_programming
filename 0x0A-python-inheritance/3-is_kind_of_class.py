#!/usr/bin/python3
"""
Function to return True or False if the object is an instance of a class
of a class that inherited from.

"""


def is_kind_of_class(obj, a_class):
    """ Using method isintance to verify the object

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
