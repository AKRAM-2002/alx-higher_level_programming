#!/usr/bin/python3

"""
This module contains a class that defines a Rectangle.
"""

class Rectangle:
    """
    Class that defines a rectangle.
    """

    number_of_instances = 0


    def __init__(self, width=0, height=0):
        """
        Initializes the instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances +=1

    @property
    def width(self):
        """
        Returns the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Defines the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Defines the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle, which is the product of its width and height.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle. If either the width or height is zero, the perimeter is 0.
            Otherwise, it is calculated as 2 times the sum of the width and height.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
    

    def __str__(self):

        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle using '#' symbols.
            If either the width or height is zero, an empty string is returned.
            Each row of the rectangle is represented on a new line.
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]
    
    def __repr__(self):
        """ Method that returns the string represantion of the instance

        Returns:
            string represenation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)
            
    def __del__(self):
        """
          Method that prints a message when the instance is gone

        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -=1
