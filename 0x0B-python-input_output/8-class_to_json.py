#!/usr/bin/python3
"""
    class_to_json function module
"""


def class_to_json(obj):
    """  returns the dictionary description for JSON serialization of an object
    """
    return obj.__dict__
