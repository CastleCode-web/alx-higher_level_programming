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
