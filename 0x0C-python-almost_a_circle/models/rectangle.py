#!/usr/bin/python3
"""
    Creating Rectangle Class inheritance from Base


"""
from models.base import Base


class Rectangle(Base):
    """
    Definition of the Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Defining all the atributes of the clase
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """
        Getter for area
        """
        return self.__height * self.__width

    def display(self):
        """
        Setter
        """
        print("\n" * self.__y, end="")
        for j in range(self.__height):
            print(" " * self.__x, end="")
            for x in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returning a string
        """
        string = "[Rectangle]({}) {}/{} - {}/{}"
        return string.format(self.id, self.__x, self.__y,
                             self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updating kwgars in dictionary
        """
        for index in range(len(args)):
            if index == 0:
                self.id = args[index]
            if index == 1:
                self.__width = args[index]
            if index == 2:
                self.__height = args[index]
            if index == 3:
                self.__x = args[index]
            if index == 4:
                self.__y = args[index]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returning new dictionary
        """
        new_dictionary = {}
        new_dictionary['id'] = self.id
        new_dictionary['width'] = self.width
        new_dictionary['height'] = self.height
        new_dictionary['x'] = self.x
        new_dictionary['y'] = self.y
        return new_dictionary
