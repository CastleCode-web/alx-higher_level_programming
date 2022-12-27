'''#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    output_list = []
    count = 0
    while count < list_length:
        try:
            result = my_list_1[count] / my_list_2[count]
        except(TypeError):
            print("wrong type")
            result = 0
        except(ZeroDivisionError):
            print("division by 0")
            result = 0
        except(IndexError):
            print("out of range")
            result = 0
        finally:
            output_list.append(result)
        count += 1
    return output_list'''
#MyCode
#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
        '''for index in range(list_length):
        The for is outside try block because I want to loop through the value one by one'''
            a = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            a = 0
            print('division by zero')
        except TypeError:
            a = 0
            print('wrong type')
        except IndexError:
            a = 0
            print('out of range')
        finally:
            new_list.append(a)
    return new_list

