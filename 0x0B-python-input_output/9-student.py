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

    def to_json(self):
        """ method that returns the dictionary representation of a student """
        return self.__dict__
