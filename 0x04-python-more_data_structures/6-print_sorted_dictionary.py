#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = list(sorted(a_dictionary.keys()))
    for key in sorted_dict:
        print("{}: {}".format(key, a_dictionary[key]))


'''
MyCode
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary.items())
    new_dic = dict(sorted_dic)
    for key, value in new_dic.items():
        print("{}: {}".format(key, value))
'''
