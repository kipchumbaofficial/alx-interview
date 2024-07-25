#!/usr/bin/python3
"""Pascals Triangle Algorithm
Generates a Pascal's triangle with n rows
"""


def pascal_triangle(n):
    '''Function to generate Pascals triangle
    only when n > 0 else return an empty list
    '''

    if n > 0:
        retval = [[1]]
        for rows in range(1, n):
            row = [1]
            for idx in range(1, rows):
                row.append(retval[rows - 1][idx - 1] + retval[rows - 1][idx])
            row.append(1)
            retval.append(row)
        return retval
    return []
