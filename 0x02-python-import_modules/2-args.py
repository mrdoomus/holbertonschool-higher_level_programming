#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) - 1 == 0:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) - 1 == 1:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

    for i in range(2, len(sys.argv) + 1):
        print("{0:d}: {1}".format(i - 1, sys.argv[i - 1]))
