#!/usr/bin/python3
"""

    Function to divide all the elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    matrix divided by the int div sended previously
    """
    Errstr = "matrix must be a matrix (list of lists) of integers/floats"
    new_list = []
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if matrix[[]] == 0:
        raise TypeError(Errstr)

    for listleng in range(len(matrix)):
        new_list.append([])

    len_row = len(matrix[0])
    for index in range(len(matrix)):
        count = 0
        for number in matrix[index]:
            if type(number) != int and type(number) != float:
                raise TypeError(Errstr)
            new_list[index].append(round((number / div), 2))
            count += 1
        if len_row != count:
            raise TypeError('Each row of the matrix must have the same size')

    return new_list
