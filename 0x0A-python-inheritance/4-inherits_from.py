#!/usr/bin/python3
"""
    Module of function inherits_from
"""


def inherits_from(obj, a_class):
    """ A function that checks for inheritance from a_class
    Args:
        obj (object): An object of any class
        a_class (object) : a class in Python
    Returns:
        bool: True of obj is subclass of a_class else False
    """
    return a_class != type(obj) and issubclass(type(obj), a_class)
