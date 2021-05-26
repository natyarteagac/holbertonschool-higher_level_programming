#!/usr/bin/python3
"""

    Function to print a square

"""


def print_square(size):
    """
    Printing the square
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
            raise TypeError('size must be an integer')
    for index in range(size):
        for index2 in range(size):
            print("#", end='')
        print()
