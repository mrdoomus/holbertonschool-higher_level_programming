#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    matrix_divided - Divides all elements of a matrix
    @matrix: Matrix passed
    @div: Divisor
    Return: New array with divided elements
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    for lst in range(len(matrix)):
        if len(matrix[0]) != len(matrix[lst]):
            raise TypeError('Each row of the matrix must have the same size')
        for pos in range(len(matrix[lst])):
            if type(matrix[lst][pos]) is not int and\
               type(matrix[lst][pos]) is not float:
                raise TypeError('matrix must be a matrix (list of lists)\
                of integers/floats')

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda j: round(j / div, 2), i)))

    return new_matrix
