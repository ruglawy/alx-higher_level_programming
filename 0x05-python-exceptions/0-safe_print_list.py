#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            counter += 1
    except Exception as e:
        pass
    finally:
        print()
        return counter
