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
