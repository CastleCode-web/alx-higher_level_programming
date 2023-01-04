#!/usr/bin/python3
'''
This module contains a function that computes the sum of two integers.
Both arguments a and b, if floats
are casted to int and return value must always be an integer
'''


def add_integer(a, b=98):
    '''
    add_integer is a function that returns the sum of two integers
    '''
    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    elif not type(a) is int:  # a type must be an exact integer
        raise TypeError("a must be an integer")
    elif not type(b) is int:  # b type must be an excat integer
        raise TypeError("b must be an integer")
    return a+b
