#!/sr/bin/python3
"""
    to_json_string function module
"""


def to_json_string(my_obj):
    """ A funtion that coverts an object to JSON string
    Args:
        my_obj (object): object to convert
    Returns:
        str: JSON format of an object
    """
    import json
    return json.dumps(my_obj)
