#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first integer.
        b (int): The second integer. Defaults to 98.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return int(a + b)

