#!/usr/bin/python3
"""


    Creating the Square Class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Inheritance from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Defining the atributes of the class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.width = value
                self.height = value

    def __str__(self):
        """
        Returning atributes
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updating kwargs in dictionary
        """
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for index in range(len(args)):
                if index == 0:
                    self.id = args[index]
                if index == 1:
                    self.size = args[index]
                if index == 2:
                    self.x = args[index]
                if index == 3:
                    self.y = args[index]

    def to_dictionary(self):
        """
        Creating new dictionary
        """
        new_dictionary = {}
        new_dictionary['id'] = self.id
        new_dictionary['size'] = self.size
        new_dictionary['x'] = self.x
        new_dictionary['y'] = self.y
        return new_dictionary
