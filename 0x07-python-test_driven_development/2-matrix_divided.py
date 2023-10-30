#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a specified number.

    Args:
        matrix (list of lists): A matrix consisting of integer or float elements.
        div (int or float): The number to divide the matrix by.

    Returns:
        list of lists: A new matrix with elements resulting from the division.

    Raises:
        TypeError: If matrix is not a list of lists, or if the elements within the lists are not integers or floats.
        TypeError: If div is not an integer or float.
        ValueError: If the lists within the matrix do not have the same size.
        ZeroDivisionError: If div is zero.
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero") 

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    len_e = 0
    for rows in matrix:
        if not rows or not isinstance(rows, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len_e != 0 and len(rows) != len_e:
            raise TypeError("Each row of the matrix must have the same size")
        for elm in rows:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        len_e = len(rows)

     return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
