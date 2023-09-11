#!/usr/bin/python3
"""
    Module of function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ A function that checks for instance of an object
    Args:
        obj (object): An object of any class
        a_class (object) : a class in Python
    Returns:
        bool: True of obj is an instance of a_class else False
    """
    return isinstance(obj, a_class)
