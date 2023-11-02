#!/usr/bin/python3
""" creates class Square 
    Args: size --> int
          position --> tuple
"""

class Square:
    """ Square class"""
    def __init__(self, size=0, position=(0, 0)):
        
        self.size = size
        self.position = position

    @property
    def size(self):
        """ size attribute getter"""
        return self.__size

    @size.setter
    def size(self, value):

        """ size attribute setter """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value



    @property
    def position(self):
        """ position attribute getter """
        return self.__position
    

    @position.setter
    def position(self, value):
        """ position attribute setter """


        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
        

    def area(self):
        """ Returns area of square --> int"""
        return self.__size * self.__size
    
    def my_print(self):
        """ prints a square"""
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

    def __str__(self):
        """ prints a square"""
        square = ''
        if self.size == 0:
            print(square)
       
        return square
    
    def __eq__(self, other):
        """ checks equality between two squares"""
        if isinstance(self, Square) and isinstance(self, Square):
            return (self.area == other.area) 
        
        
    def __lt__(self, other):
        """ checks less than between two squares"""
        if isinstance(self, Square) and isinstance(other, Square):
            return (self.area() < other.area())
        

    def __le__(self, other):
        """ checks less than equal to between two squares"""
        if isinstance(self, Square) and isinstance(other, Square):
            return (self.area() <= other.area())
        
    def __gt__(self, other):
        """ checks greater than between two squares"""
        if isinstance(self, Square) and isinstance(other, Square):
            return (self.area() > other.area())
        
    def __ge__(self, other):
        """ checks greater than equal between two squares"""
        if isinstance(self, Square) and isinstance(other, Square):
            return (self.area() >= other.area())
