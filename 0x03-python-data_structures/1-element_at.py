#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0) or (idx > len(my_list) - 1):
        return None
    else:
        return my_list[idx]



#MyCode
'''#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    for i in my_list:
        if i == my_list[idx]:
            return i'''

'''def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]'''

