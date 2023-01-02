#!/usr/bin/python3
'''
This module contains a function that divides all elements
of a matrix. Each element must be an absolute int or float
and the divisor must be a number but not 0
'''
def matrix_divided(matrix, div):
    '''
    matrix_divided is a function that divides all element of a matrix and 
    returns a new list without altering the old
    '''
    checkfor_matrix = all(isinstance(element, list) for element in matrix)
    if checkfor_matrix is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_list = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            inner_list = []
            for col in row:
                if not isinstance(col, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    inner_list.append(round(col/div, 2))
        result_list.append(inner_list)
    return result_list
