#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = len(sys.argv) - 1
    if a == 0:
        print("{} arguments.".format(a))
    elif a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))
    for index, arg in enumerate(sys.argv):
        b = sys.argv[0]
        if arg == b:
            continue
        print("{:d}: {:s}".format(index, arg))
