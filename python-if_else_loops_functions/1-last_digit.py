#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = f"Last digit of {number} is"
if number < 0:
    number = number * -1
last = number % 10
if last > 5:
    string = f"{string} {last} and is greater than 5"
    print(string)
elif last < 6 and last != 0:
    string = f"{string} {last} and is less than 6 and not 0"
    print(string)
elif last == 0:
    string = f"{string} {last} and is 0"
    print(string)
