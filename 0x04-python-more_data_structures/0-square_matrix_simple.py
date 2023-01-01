#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, row)) for row in matrix])

#MyCode
'''def square_matrix_simple(matrix=[]):
    new_list = []
   # inner_list = []
    for row in matrix:
        inner_list = []
        for col in range(len(row)):
            inner_list.append(row[col] ** 2)
        new_list.append(inner_list)
    return new_list
'''
