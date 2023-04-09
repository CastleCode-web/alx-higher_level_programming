#!/usr/bin/python3
""" this module contains class method """


class Rectangle(object):
    """ contains a class method """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ increaments number_of_instances everytime
            a new instance is created
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    def __del__(self):
        """ decreaments number_of_instances everytime
            an instance is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    def __repr__(self):
        """ returns the string representation of rectangle """
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        """ prints the rectangle with # character """
        a = str(self.print_symbol) * self.__width
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range((self.__height - 1)):
            print(a)
        return a

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of the rectangle """
        perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            return 0
        return perimeter

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            a = rect_1.area()
            b = rect_2.area()
            if a == b:
                return rect_1
            elif a > b:
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance
            with "width == height == size
        """
        return cls(size, size)
