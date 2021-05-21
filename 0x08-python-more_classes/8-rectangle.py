#!/usr/bin/python3
""" class rectangle """


class Rectangle:
    """ Private width and height of the rectangle  """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return ""
        else:
            string = ""
            for j in range(self.__height):
                string += "".join(str(self.print_symbol) * self.__width)
                if j + 1 < self.__height:
                    string += '\n'
        return string

    def __repr__(self):
        string_repr = "Rectangle({}, {})".format(self.__width, self.__height)
        return string_repr

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_1, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area == rect_2.area:
            return rect_1
