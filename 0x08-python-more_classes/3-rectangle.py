#!/usr/bin/python3
""" class rectangle """


class Rectangle:
    """ Private width and height of the rectangle  """
    pass

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):

        return self.__height * self.__width

    def perimeter(self):
        if self.__width and self.__height == 0:
            return 0
        else:
            return self.__width + self.__height + self.width + self.__height

    def __str__(self):
        if self.__width and self.__height == 0:
            return
        else:
            string = ""
            for j in range(self.__height):
                string += "".join("#" * self.__width)
                if j + 1 < self.__height:
                    string += '\n'
        return string
