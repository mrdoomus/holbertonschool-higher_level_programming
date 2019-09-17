#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    else:
        end = 0
        for i in matrix:
            for j in i:
                if end == 2:
                    print("{:d}".format(j), end="")
                    end = 0
                else:
                    print("{:d} ".format(j), end="")
                    end += 1
            print("")
