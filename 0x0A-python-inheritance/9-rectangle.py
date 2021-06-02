#!/usr/bin/python3
"""
    BaseGeometry class


"""


class BaseGeometry:
    """ BaseGeometry class

    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format())
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))


class Rectangle(BaseGeometry):
    """ Rectangle inheritance from BaseGeometry

    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        print("{}".format(self.__height * self.__width))

    def __str__(self):
        str = '[Rectangle] {} / {}.format(self.__width, "self.__height)'
        return str
