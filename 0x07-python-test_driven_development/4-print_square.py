#!/usr/bin/python3
''''
This module contains a function that
prints a square with the # character
'''


def print_square(size):
    '''
    print_square function accepts one argument
    which must be an int. The argument determines the sizes of the square
    '''
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    square = '#' * (size)
    for i in range(size):
        print(square)
