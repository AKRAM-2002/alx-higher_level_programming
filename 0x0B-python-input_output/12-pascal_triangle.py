#!/usr/bin/python3
"""Pascal triangle """

def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the matrix with the first row
    matrix = [[1]]

    # Generate subsequent rows
    for _ in range(1, n):
        # Get the previous row
        prev_row = matrix[-1]
        # Initialize the new row with the first element as 1
        new_row = [1]
        # Calculate the values for the next row
        for i in range(1, len(prev_row)):
            new_value = prev_row[i - 1] + prev_row[i]
            new_row.append(new_value)


        # Set the last element of the row to 1
        new_row.append(1)

        # Append the new row to the matrix
        matrix.append(new_row)

    return matrix
