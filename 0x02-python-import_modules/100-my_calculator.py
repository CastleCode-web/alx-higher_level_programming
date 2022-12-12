#!/usr/bin/python3
"""
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arg_length = len(sys.argv) - 1
    if arg_length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        operator = ['+', '-', '*', '/']
        b = int(sys.argv[3])

        if sys.argv[2] == operator[0]:
            print("{:d} {} {:d} = {:d}".format(a, operator[0], b, add(a, b)))
        elif sys.argv[2] == operator[1]:
            print("{:d} {} {:d} = {:d}".format(a, operator[1], b, sub(a, b)))
        elif sys.argv[2] == operator[2]:
            print("{:d} {} {:d} = {:d}".format(a, operator[2], b, mul(a, b)))
        elif sys.argv[2] == operator[3]:
            print("{:d} {} {:d} = {:d}".format(a, operator[3], b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
"""

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        a = int(argv[1])
        b = int(argv[3])
        op = ['+', '-', '*', '/']

        if argv[2] == op[0]:
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

        elif argv[2] == op[1]:
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

        elif argv[2] == op[2]:
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

        elif argv[2] == op[3]:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

        elif argv[2] not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)            
