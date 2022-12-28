#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maxi = my_list[0]
        for value in my_list:
            if value > maxi:
                maxi = value
        return maxi


#MyCode
'''#!/usr/bin/python3
def max_integer(my_list=[]):
    largest_number = None

    if len(my_list) == 0:
        return None
    else:
        for value in my_list:
            if (largest_number == None) or (largest_number < value):
                largest_number = value
        return largest_number
'''
