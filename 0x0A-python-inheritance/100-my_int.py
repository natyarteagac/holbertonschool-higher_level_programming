#!/usr/bin/python3
"""
    Int class

"""


class MyInt(int):
    """ Return inverted operator

    """

    def __bool__(self):
        return False
