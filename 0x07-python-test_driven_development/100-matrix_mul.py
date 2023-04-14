#!/usr/bin/python3
"""
This module contains 2 functions
1]. 'matrix_mul(m_a, m_b):'
and
2]. 'get_size(matrix):'
The complete information of the functions
(prototype, declaration & definition)
can be found in the function's documentation
"""


from functools import reduce


def matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices.
    It takes as parameters,
    m_a => which is a list of lists,
    m_b => which is a list of lists,
    and if not these parameters, raises an error.
    Then multiplies the 2 lists of lists, and returns
    a list of lists corresponding to the resulting size
    """
    def get_size(matrix):
        """
        This function gets the size of a matrix.
        It takes as a parameter,
        matrix => which is a list of lists,
        then returns the size of the matrix
        (rows and columns respectively) in a tuple
        """
        return (len(matrix), len(matrix[0]))

    mess_1_a = "m_a should contain only integers or floats"
    mess_1_b = "m_b should contain only integers or floats"
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif all(isinstance(a, list) for a in m_a) is not True:
        raise TypeError("m_a must be a list of lists")
    elif all(len(a) != 0 for a in m_a) is not True:
        raise ValueError("m_a can't be empty")
    elif all(isinstance(v, (int, float)) for a in m_a for v in a) is not True:
        raise TypeError("m_a should contain only integers or floats")
    elif all(len(a) == len(m_a[0]) for a in m_a) is not True:
        raise TypeError("each row of m_a must be of the same size")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    elif all(isinstance(b, list) for b in m_b) is not True:
        raise TypeError("m_b must be a list of lists")
    elif all(len(b) != 0 for b in m_b) is not True:
        raise ValueError("m_b can't be empty")
    elif all(isinstance(v, (int, float)) for b in m_b for v in b) is not True:
        raise TypeError("m_b should contain only integers or floats")
    elif all(len(b) == len(m_b[0]) for b in m_b) is not True:
        raise TypeError("each row of m_b must be of the same size")
    elif get_size(m_a)[-1] != get_size(m_b)[0]:
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        m_bb = [[inn[num] for inn in m_b] for num in range(len(m_b[0]))]
        collate = []
        for a in m_a:
            level = []
            for b in m_bb:
                level.append((a, b))
            collate.append(level)
        result = []
        for items in collate:
            inner = []
            for item in items:
                pairs = [[new[k] for new in item] for k in range(len(item[0]))]
                sp = sum([reduce(lambda x, y: x * y, pair) for pair in pairs])
                inner.append(sp)
            result.append(inner)
    return result

"""
	Another method

	#!/usr/bin/python3
	#multiplies two matrices

def matrix_mul(m_a, m_b):
    #multiplies two matrices with certain conditions
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(m_a, list) for elem in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_a[0]) < len(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(m_b, list) for elem in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if len(m_b[0]) < len(m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    #creates a transpose of m_b
    new_list = []
    for i in range(len(m_b)):
        some_list = []
        for j in range(len(m_b[i])):
            x = m_b[j][i]
            some_list.append(x)
        new_list.append(some_list)
    m_b = new_list
    #multiplies the row of m_a by that of the transposed m_b
    matrix_mult = []
    for i in range(len(m_a)):
        some_list = []
        for j in range(len(m_b)):
            d = 0
            for k in range(len(m_b[i])):
                if not isinstance(m_a[i][k], int):
                    raise TypeError("m_a should contain only integers or floats")
                elif not isinstance(m_b[j][k], int):
                    raise TypeError("m_b should contain only integers or floats")
                x = m_a[i][k] * m_b[j][k]
                d += x
            some_list.append(d)
        matrix_mult.append(some_list)
    return matrix_mult
"""

