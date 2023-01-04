#!/usr/bin/python3
'''
This module contains a function that
prints new lines after . ? and : characters
'''


def text_indentation(text):
    '''
    text_indentation is a function that accepts
    one argument of string type. It loops through the string
    and prints 2 new lines after every . ? and : characters
    '''
    if not type(text) is str:
        raise TypeError("text must be a string")
    var = ''
    for i in text:
        var += i
        if i == '.' or i == '?' or i == ':':
            print(var.strip())
            print()
            var = ''
