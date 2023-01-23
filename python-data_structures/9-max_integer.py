#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    maxI = min(my_list)
    if length == 0:
        return None
    else:
        for i in my_list:
            if i > maxI:
                maxI = i
        return maxI
