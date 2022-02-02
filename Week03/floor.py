#Write a program (floor.py), that takes in a float and outputs an int rounded down, you will need the math module math.floor()

import math

numberToFloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberToFloor)
print('{} floored is {}'.format(numberToFloor, flooredNumber))