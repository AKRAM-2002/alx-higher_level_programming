#!/usr/bin/python3
def print_square(size):
    """
    A function to print a square with the character #

    Args:
        size: length of square must be integer
    Returns:
        None
    
    Raises:
        TyperError: size is not integer
        ValueError: If size is less than 0 

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
