#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list




#MyCode
'''#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    for i in my_list:
        if i == my_list[idx]:
            my_list[idx] = element
            return my_list'''

'''def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
            return my_list'''

