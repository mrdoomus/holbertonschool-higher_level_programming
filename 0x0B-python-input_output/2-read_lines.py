#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    Opens and prints certain amount of lines
    :param filename: Name of the file
    :param nb_lines: Number of lines in the text
    """
    with open(filename, 'r', encoding='utf-8') as f:
        tot_lines = sum(1 for line in open(filename))

        if nb_lines <= 0 or nb_lines > tot_lines:
            nb_lines = tot_lines

        for line in range(nb_lines):
            if nb_lines < tot_lines:
                print(f.readline(), end='')
            elif nb_lines >= tot_lines:
                if line == nb_lines - 1:
                    print(f.readline())
                else:
                    print(f.readline(), end='')
