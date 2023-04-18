#!/usr/bin/python3
""" This module contains a function that returns an
    object represented by JSON string
"""
import json


def from_json_string(my_str):
    """ Takes an argument and returns the object
        represented by JSON string
    """
    return json.loads(my_str)
