#!/usr/bin/python3


def pascal_triangle(n):
    """
    Calculates the pascal Triagnle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pc_list = [[1], [1, 1]]
    pensee = []

    for row in range(2, n):
        pensee = [1]
        for column in range(1, row):
            number = pc_list[row - 1][column - 1] + pc_list[row - 1][column]
            pensee.append(number)
        pensee.append(1)
        pc_list.append(pensee)
    return pc_list
