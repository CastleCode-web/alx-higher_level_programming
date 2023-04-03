#!/usr/bin/python3
'''
This module contains a afunction that
prints string characters to stdout
'''


def say_my_name(first_name, last_name=""):
    '''
    say_my_name is a function that prints the first and
    last names of users in string format
    '''
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
