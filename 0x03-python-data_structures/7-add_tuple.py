#!/usr/bin/python3
"""
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= len(tuple_b):
        max_len = len(tuple_a)
    else:
        max_len = len(tuple_b)
    sum_list = []
    for value in range(max_len):
        if value < len(tuple_a):
            first = tuple_a[value]
        else:
            first = 0
        if value < len(tuple_b):
            second = tuple_b[value]
        else:
            second = 0
        sum_list.append(first + second)
    return tuple(sum_list)
"""


def add_tuple(tuple_a=(), tuple_b=()):

    a = len(tuple_a)
    b = len(tuple_b)

    sums = ((tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0),
            (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if b > 1 else 0))

    return sums
