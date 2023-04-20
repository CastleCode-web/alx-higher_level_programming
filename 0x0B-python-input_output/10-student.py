#!/usr/bin/python3
""" Module contains a class, a constructor and methods """


class Student(object):
    """ creates a class named Student """
    def __init__(self, first_name, last_name, age):
        """ construct the first_name, last_name and age attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of student instance """
        if attrs == None:
            return self.__dict__
        else:
            attr_dict = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    attr_dict[item] = self.__dict__[item]
            return attr_dict
