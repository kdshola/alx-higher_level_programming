#!/sr/bin/python3
"""
    load_from_json_file function module
"""
import json


def load_from_json_file(filename):
    """ A funtion that converts an JSON string to an object from a file
    Args:
        filename (file): file to write string to
    Returns:
        object: object from the JSON string
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
