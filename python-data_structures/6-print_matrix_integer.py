#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        cont = 0
        for i in row:
            cont += 1
            if len(row) != cont:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()
