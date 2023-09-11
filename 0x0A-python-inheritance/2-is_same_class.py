#!/usr/bin/python3
"""
    Module of function is_same_class
"""


def is_same_class(obj, a_class):
    """ A function that checks for instance of an object
    Args:
        obj (object): An object of any class
        a_class (object) : a class in Python
    Returns:
        bool: True of obj of class a_class exactly else False
    """
    return a_class == type(obj)
