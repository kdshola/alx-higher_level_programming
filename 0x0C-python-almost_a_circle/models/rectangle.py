#!/usr/bin/python3
"""
    module containing class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ A subclass of the Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiates a Rectangle object
        Args:
            width (int): Rectangle width
            height (int): Rectangle heigth
            x (int): Instance x coordinate
            y (int): Instance y coordinate
            id (int): Instance identity+
        Raises:
            TypeError: If x or y is not an integer
            TyoeError: if width of heigth is not an integer
            ValueError: if width or heigth is <= 0
            ValueError: If x or y is < 0
        Returns:
            None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """ Getter fot thr private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height attribute
            Args:
                value (int): height of instance
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """ Getter fot thr private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width attribute
            Args:
                value (int): width of instance
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """ Getter for the private instance attribute x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x cordinate attribute
            Args:
                value (int): height of instance
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for the private instance attribute y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y coordinate attribute
            Args:
                value (int): y coordinate of instance
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates instance area
        Returns:
            int: area of a particlar Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """ Prints rectangle instance to stdout """
        [print("") for i in range(self.y)]
        for num in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            print("#" * self.width, end="")
            print()

    def __str__(self):
        """ Returns informal representation of a Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Updates instance attributes
        Args:
            args (ints): new attributed to update in order of id, width, heigth
            x and y
            kwargs (dict): new attributes in key value pairs
        """
        if len(args) != 0 and args:
            iteration = 0
            for arg in args:
                if iteration == 0:
                    if arg:
                        self.id = arg
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                elif iteration == 1:
                    self.width = arg
                elif iteration == 2:
                    self.height = arg
                elif iteration == 3:
                    self.x = arg
                elif iteration == 4:
                    self.y = arg
                iteration += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "height":
                    self.height = value
                elif key == "width":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }
