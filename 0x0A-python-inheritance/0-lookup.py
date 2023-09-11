#!/usr/bin/python3
"""
    Lookup function module
"""


def lookup(obj):
    """ Finds all attributes of an object
    Args:
        obj (object): an instance of any type of object
    Returns:
        list: a lst of attributes of the object instance
    """
    return dir(obj)
