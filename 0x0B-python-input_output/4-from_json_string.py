#!/usr/bin/python3
"""
    from_json_string function module
"""


def from_json_string(my_str):
    """ A funtion that coverts JSON string to object
    Args:
        my_str (object): JSON string to convert
    Returns:
        str: a python object corresponding to the JSON string
    """
    import json
    return json.loads(my_str)
