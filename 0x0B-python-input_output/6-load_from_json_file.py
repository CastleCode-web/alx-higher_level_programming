#!/usr/bin/python3
""" This module contains a function that creates
    an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ creates an object from a JSON file """
    with open(filename, mode="r", encoding="utf-8") as MyFile:
        return json.load(MyFile)
