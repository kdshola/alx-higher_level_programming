#!/usr/bin/python3
"""
    Module containing add_attribute function
"""



def add_attribute(obj, attribute, value):
    """A function that adds attribute to an object
    Args:
        obj (object): An object of any class
        attribute (obj): Attrinute of abject obj
        value: value to give attribute
    Retuns:
        None
    Raises:
        TypeError: if object has no such attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
