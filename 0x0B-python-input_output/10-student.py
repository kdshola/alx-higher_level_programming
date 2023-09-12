#!/usr/bin/python3
"""
    module containing class Student
"""


class Student:
    """ A class that represents a student """
    def __init__(self, first_name, last_name, age):
        """ Initializes student instance with attributes
        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): students age
        Returns: None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ method that returns the dictionary representation of a student """
        if type(attrs) == list:
            for item in self.__dict__:
                if type(item) is not str:
                    return self.__dict__
            name_dict = {}
            for i in range(len(attrs)):
                for key in self.__dict__:
                    if attrs[i] == key:
                        name_dict[key] = self.__dict__[key]
            return name_dict
        return self.__dict__
