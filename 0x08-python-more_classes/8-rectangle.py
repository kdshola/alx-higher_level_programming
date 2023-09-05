#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Model of a rectangle
    Attributes:
        number_of_instances (int): number of existing object instance
        print_symbol (str): used to repersent an object instance
        can be changed to any type
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes rectangle width and height
        Args:
            width (int): length if a rectangle
            height (int): height of a rectangle
        Returns:
            None
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """getter of private variable width
        Returns:
        int: width of an instance of the class rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of private variable width
        Args:
            value (int): height of an instance of the class rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter of private variable height
        Returns:
            int: height of an instance of the class rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of private variable height
        Args:
            value (int): height of an instance of the class rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of an instance of the class rectangle
        Returns:
            int: area of an instance of the class rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of an instance of the class rectangle
        Returns:
            int: perimeter of an instance of the class rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Defines the informal representation of the of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            string = ""
            string += "\n".join(str(self.print_symbol) * self.__width
                                for num in range(self.__height))
            return string

    def __repr__(self):
        """Defines the formal representation of the of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message upon deletion of a Rectangle instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determines the bigger of two rectangles based on their areas
        Args:
            rect_1 (Rectangle): An instance of the class Rectangle
            rect_2 (Rectangle): An instance of the class Rectangle
        Returns:
            Rectangle: Bigger rectangle instance of the two given instances
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        greater = rect_1.area() >= rect_2.area()
        if greater:
            return rect_1
        else:
            return rect_2
