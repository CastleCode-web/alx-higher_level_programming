#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for value in range((len(my_list) - 1), -1, -1):
            print("{:d}".format(my_list[value]))



#MyCode
'''#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list:
        print('{}'.format(my_list[-i]))

#AnotherWay
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) + 1):
        if i == 0:
            continue
        else:
            print("{}".format(my_list[-i]))'''

