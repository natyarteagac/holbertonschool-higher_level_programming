#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for numberoflists in range(len(matrix)):
        for index in range(len(matrix[numberoflists])):
            print("{:d}".format(matrix[numberoflists][index]), end='')
            if index + 1 < len(matrix[numberoflists]):
                print(end=' ')
        print()
