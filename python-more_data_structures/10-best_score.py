#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    student = ""
    if a_dictionary == None:
        return None
    else:
        for i in a_dictionary:
            if a_dictionary[i] > best:
                best = a_dictionary[i]
                student = i
        return student
