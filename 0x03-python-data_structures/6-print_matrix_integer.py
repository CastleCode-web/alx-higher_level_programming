#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for value in range(len(element)):
            if value == (len(element) - 1):
                print("{:d}".format(element[value]), end="")
            else:
                print("{:d} ".format(element[value]), end="")
        print("")



#MyCode
'''#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end="")
        print()
'''
