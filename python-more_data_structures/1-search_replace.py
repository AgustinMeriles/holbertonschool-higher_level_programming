#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for idx, item in enumerate(my_list):
        if item == search:
            new[idx] = replace
    return new
