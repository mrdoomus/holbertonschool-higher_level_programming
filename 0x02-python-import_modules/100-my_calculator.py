#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op != "+" and op != "-" and op != "/" and op != "*":
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if op == "+":
                print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
            if op == "-":
                print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
            if op == "*":
                print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
            if op == "/":
                print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
