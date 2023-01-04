#!/usr/bin/python3
"""
This module contains a function that multiplies
2 matrices by using the module NumPy
It takes as arguments 2 matrices 'm_a' and 'm_b'
And returns a matrix
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices
    by using the module NumPyIt takes as arguments
    2 matrices 'm_a' and 'm_b'And returns a matirx
    """
    return np.dot(m_a, m_b)
