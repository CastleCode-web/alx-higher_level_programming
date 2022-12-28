#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [True if value % 2 == 0 else False for value in my_list]

#MyCode---NotWorkingYet
'''#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for value in my_list:
        if (value % 2) == 0:
            return True
        else:
            return False
'''
