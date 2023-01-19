#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
addR = add(a, b)
subR = sub(a, b)
mulR = mul(a, b)
divR = div(a, b)
print("{} + {} = {}".format(a, b, addR))
print("{} - {} = {}".format(a, b, subR))
print("{} * {} = {}".format(a, b, mulR))
print("{} / {} = {}".format(a, b, divR))
