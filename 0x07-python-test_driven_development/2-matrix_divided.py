#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    matrix_divided - Divides all elements of a matrix
    @matrix: Matrix passed
    @div: Divisor
    Return: New array with divided elements
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    if (matrix == [[]] or matrix == []) or len(matrix) == 0:
        raise TypeError(msg)

    if type(matrix) is list and type(matrix[0]) is not list:
        raise TypeError(msg)

    for lst in range(len(matrix)):
        if len(matrix[0]) != len(matrix[lst]):
            raise TypeError('Each row of the matrix must have the same size')
        if type(matrix) is not list or type(matrix[lst]) is not list:
            raise TypeError(msg)
        if matrix[lst] == [] or len(matrix[lst]) == 0:
            raise TypeError(msg)

        for pos in range(len(matrix[lst])):
            if type(matrix[lst][pos]) is not int and\
               type(matrix[lst][pos]) is not float:
                raise TypeError(msg)

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda j: round(j / div, 2), i)))

    return new_matrix
