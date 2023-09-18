#!/usr/bin/python3
"""
    A module containing class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square model"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a square
        Args:
            size (int): width and height of the square
            x (int): x coordinate of the square
            y (int): x coordinate of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter of square size """
        return self.height

    @size.setter
    def size(self, value):
        """ Setter for square size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns the informal representation of a square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    def to_dictionary(self):
        """ Returns the dictionary representation of a square """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }

    def update(self, *args, **kwargs):
        """ Updates instance attributes
        Args:
            args (ints): new attributed to update in order of id, size, x and y
            kwargs (dict): new attributes in key value pairs
        """
        if len(args) != 0 and args:
            iteration = 0
            for arg in args:
                if iteration == 0:
                    if arg:
                        self.id = arg
                    else:
                        self.__init__(self.size, self.x, self.y)
                elif iteration == 1:
                    self.size = arg
                elif iteration == 2:
                    self.x = arg
                elif iteration == 3:
                    self.y = arg
                iteration += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
