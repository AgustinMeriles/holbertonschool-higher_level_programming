#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print("{}".format('\t'.join(map(str, i))))
