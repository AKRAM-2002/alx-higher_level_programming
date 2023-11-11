#!/usr/bin/python3

class Rectangle(Base):
    """Rectangle Class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get the width of the object.

        Returns:
        - int: The width value.
        """
        return self.__width

    @property
    def height(self):
        """
        Get the height of the object.

        Returns:
        - int: The height value.
        """
        return self.__height

    @property
    def x(self):
        """
        Get the x-coordinate of the object.

        Returns:
        - int: The x-coordinate value.
        """
        return self.__x

    @property
    def y(self):
        """
        Get the y-coordinate of the object.

        Returns:
        - int: The y-coordinate value.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Set the width of the object.

        Parameters:
        - value (int): The new width value.
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height of the object.

        Parameters:
        - value (int): The new height value.
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the object.

        Parameters:
        - value (int): The new x-coordinate value.
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the object.

        Parameters:
        - value (int): The new y-coordinate value.
        """
        self.__y = value
