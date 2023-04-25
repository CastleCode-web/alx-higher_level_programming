#!/usr/bin/python3
""" This module contains a square class that inherits
    from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ creates a square class that inherits from rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for the size attribute of square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ returns the string representation of square class """
        a = type(self).__name__
        b = self.id
        c = self.width
        e = self.x
        f = self.y
        return f"[{a}] ({b}) {e}/{f} - {c}"

    @property
    def size(self):
        """ returns the width and height of square """
        return self.width

    @size.setter
    def size(self, value):
        """ updates the width and height with value """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns attribute to args or kwargs """
        if args:
            for arg in range(len(args)):
                try:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[1]
                    self.x = args[2]
                    self.y = args[3]
                except IndexError:
                    pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ returns the dictionary representation of square """
        some_dict = {}
        some_dict["id"] = self.id
        some_dict["size"] = self.size
        some_dict["x"] = self.x
        some_dict["y"] = self.y
        return some_dict
