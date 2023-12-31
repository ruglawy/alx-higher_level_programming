#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                new_list[i] = result
            except TypeError as t:
                print("wrong type")
            except ZeroDivisionError as z:
                print("division by 0")
            except IndexError as ind:
                print("out of range")
    except Exception as e:
        print("out of range")
    finally:
        return new_list
