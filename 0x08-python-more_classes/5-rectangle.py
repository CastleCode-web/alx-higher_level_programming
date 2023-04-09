#!/usr/bin/python3
""" contains class with del method """


class Rectangle(object):
    """ creates a class that has del method """
    def __init__(self, width=0, height=0):
        """ Instantiates the width and height attributes """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ gets the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width attribute """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height attribute """
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculate the perimeter of the rectangle """
        perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """ prints the rectangle with # """
        a = '#' * self.__width
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range((self.__height - 1)):
            print(a)
        return a

    def __repr__(self):
        """ returns the string representation of rectangle """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ deletes an instance/object """
        print("Bye rectangle...")
