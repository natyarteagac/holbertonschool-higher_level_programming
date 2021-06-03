#!/usr/bin/python3
"""
    Int class

"""


class MyInt(int):
    """ Return inverted operator

    """

    def __eq__(self, x: object):
        return super().__eq__(not x)

    def __ne__(self, x: object):
        return super().__ne__(not x)
