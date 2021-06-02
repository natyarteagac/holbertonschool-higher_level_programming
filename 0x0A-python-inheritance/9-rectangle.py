#!/usr/bin/python3
"""
    BaseGeometry class


"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inheritance from BaseGeometry

    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return "{}".format(self.__height * self.__width)

    def __str__(self):
        str = '[Rectangle] {}/{}'.format(self.__width, self.__height)
        return str
