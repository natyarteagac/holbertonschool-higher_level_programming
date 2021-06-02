#!/usr/bin/python3
"""
    BaseGeometry class


"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inheritance from Rectangle Class

    """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return "{}".format(self.__size * self.__size)

    def __str__(self):
        str = '[Rectangle] {}/{}'.format(self.__size, self.__size)
        return str
