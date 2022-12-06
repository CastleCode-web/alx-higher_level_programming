#!/usr/bin/python3
def no_c(my_string):
    strg = ""
    for letter in my_string:
        if letter != "c" and letter != "C":
            strg += letter
    return strg
