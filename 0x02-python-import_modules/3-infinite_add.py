#!/usr/bin/python3
import sys
if __name__ == '__main__':
    total = 0
    for i in range(2, len(sys.argv) + 1):
        total += int(sys.argv[i - 1])
    print(total)
