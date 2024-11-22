#!/usr/bin/python3
"""Rotate 2D Matrix 90 Degrees Clockwise
"""


def rotate_2d_matrix(matrix):
    """ Function for rotating 2D Matrix 90 degrees clockwise
    """

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
