#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    result = 0
    for idx, item in enumerate(my_list):
        if item in new:
            continue
        else:
            new.append(my_list[idx])
    for i in range(len(new)):
        result += new[i]
    return result
