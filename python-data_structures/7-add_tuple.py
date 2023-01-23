#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lstA = list(tuple_a)
    lstB = list(tuple_b)
    while len(lstA) < 2:
        lstA.append(0)
    while len(lstB) < 2:
        lstB.append(0)
    resA = lstA[0] + lstB[0]
    resB = lstA[1] + lstB[1]
    return (resA, resB)
