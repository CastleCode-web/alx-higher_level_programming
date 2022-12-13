#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = len(sys.argv) - 1
    sum_arg = 0
    if a == 0:
        sum_arg += a
    elif a >= 1:
        for index, arg in enumerate(sys.argv):
            b = sys.argv[0]
            if arg == b:
                continue
            sum_arg += int(arg)
    print(sum_arg)
