#!/usr/bin/python3
"""
    Inheritance My list from list class
"""


class MyList(list):
    """ Inheritance of the list class """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
