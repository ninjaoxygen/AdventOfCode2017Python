#!/usr/bin/python

# first, let's understand the maths of the grid

# 37  36  35  34  33  32  31
# 38  17  16  15  14  13  30
# 39  18   5   4   3  12  29
# 40  19   6   1!  2  11  28
# 41  20   7   8   9! 10  27
# 42  21  22  23  24  25! 26
# 43  44  45  46  47  48  49!

# the squares with an ! are 1^2, 3^2, 5^2, 7^2 at (0,0), (1,1), (2,2), (3,3) etc
# so a sqrt can tell us which "shell" a number is in by comparing to odd sqrts

import math

with open("input.txt") as fp:
    value = int(fp.readline())

def check(value):
    # take the square root to determine the shell
    sqrt = math.ceil(math.sqrt(value))

    # work out the base root of our shell
    square = int((sqrt) / 2 - 1) * 2 + 1

    # base number of our shell
    base = square * square

    # base number of the next shell out
    nextBase = (square + 2) * (square + 2)

    # number of cells in our shell
    deltaBase = nextBase - base

    # number of cells on a side of our shell
    sideLength = deltaBase / 4

    # our shell number - which is also how many steps out from the centre cell we need to take
    shell = sideLength / 2

    # how many cells around our shell we are
    valueBaseOffset = value - base

    # on each side, how many steps from the midpoint of the side we are
    sideOffset = abs((valueBaseOffset - 1) % sideLength + 1 - shell)

    #print "value = ", value, "base = ", base, "nextBase = ", nextBase, "deltaBase = ", deltaBase, "sideLength = ", sideLength, "shell = ", shell, "valueBaseOffset = ", valueBaseOffset, "sideOffset = ", sideOffset

    # shell steps "out" towards our side, then sideOffset steps "across" along the side
    return shell + sideOffset

print check(12), 3
print check(23), 2
print check(1024), 31
print check(value), "??"
