#!/usr/bin/python3

def safe_print_list_integer(my_list=[], x=0):
    reg = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (reg)
