#!/usr/bin/python3
"""
    save_to_json_file function module
"""
import json


def save_to_json_file(my_obj, filename):
    """ A funtion that covnerts an object to JSON string and write it to given
    file
    Args:
        my_obj (object): to covert to JSON string
        filename (file): file to write string to
    Returns:
        None
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
