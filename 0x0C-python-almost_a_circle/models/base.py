#!/usr/bin/python3
"""
    Base class module
"""

import json
import csv
import turtle


class Base:
    """ A base class for classes in this repository
    Atteibutes:
        __nb_objects (int): instantiated Base object count
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for a new Base object
        Args:
            id (int): Base object instance identity
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Serializes dictionaries to JSON
        Args:
            list_dictionaries (list): list of dictionares
            Returns:
                Json format of the list
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Serializes list of objects and save to Classname.json file
        Args:
            list_objs (list): list of subclass of the Base class
        """
        f_name = cls.__name__ + ".json"
        with open(f_name, 'w') as js_file:
            if list_objs is None:
                js_file.write("[]")
            else:
                dict_ls = [obj.to_dictionary() for obj in list_objs]
                js_file.write(cls.to_json_string(dict_ls))

    @staticmethod
    def from_json_string(json_string):
        """ derializes from JSON to py objects
        Args:
            json_string (str): JSON string
        Returns:
            Object of the JSON string
        """
        if json_string == [] or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Instantiate a new class and returns the class
        Args:
            dictionary (dict): dictionary containing insance attribute
        Returns:
            new instance
        """
        if dictionary != {} and dictionary:
            if cls.__name__ == "Square":
                instance = cls(1)
            else:
                instance = cls(1, 1)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """ Reads from a .json file, a list of instances in it
        Returns:
            list - an empty list if file is not found
            list - a list of class instances from the file
        """
        f_name = cls.__name__ + ".json"
        try:
            with open(f_name, 'r') as file:
                obj_list = cls.from_json_string(file.read())
                return [cls.create(**dictn) for dictn in obj_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes list of objects and save to Classname.csv file
        Args:
            list_objs (list): list of subclass of the Base class
        """
        f_name = cls.__name__ + ".csv"
        with open(f_name, 'w') as csv_file:
            if list_objs is None:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                else:
                    fields = ["id", "width", "height", "x", "y"]
                inputs = csv.DictWriter(csv_file, fieldnames=fields)
                for obj in list_objs:
                    inputs.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Returns:
            list: a list of instantiated classes or an empty list
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
