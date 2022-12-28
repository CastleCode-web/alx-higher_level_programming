#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_copy = my_list.copy()
    if (idx < 0) or (idx > len(my_list) - 1):
        return new_copy
    else:
        new_copy[idx] = element
        return new_copy



#MyCode
'''#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_copy = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return new_copy
    for i in new_copy:
        if i == new_copy[idx]:
            new_copy[idx] = element
            return new_copy


def new_in_list(my_list, idx, element):
    copied_list = my_list[:]#AnotherWayofGettingaShallowCopy
    if idx < 0:
        return copied_list
    elif idx > len(my_list):
        return copied_list
    for i in range(len(copied_list)):
        if i == idx:
            copied_list[i] = element
            return copied_list'''

