#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    max_actual = my_list[0]
    for numero in my_list[1:]:
        if numero > max_actual:
            max_actual = numero
    return max_actual
