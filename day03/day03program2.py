#!/usr/bin/python

# now I wish I had done the first one the naive way
# this time we will build a matrix and step around it
# totalling the values

# there probably is a mathematical way to calculate the adjacency
# but I am quicker to program it this way!

import math

with open("input.txt") as fp:
    value = int(fp.readline())

def getSideLength(value):
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

    return sideLength

# this is WAY too high, but at least "enough"
side = getSideLength(value) + 3
print "side = ", side

offset = int(side / 2)

# create a matrix to store values
values = [[0 for x in range(side)] for y in range(side)]

values[offset][offset] = 1

posx = offset + 1
posy = offset + 1

direction = 0
sideLength = 2
sideCount = 0

def advance():
    global direction, posx, posy, sideLength, sideCount
    if direction == 0:
        posy = posy - 1
    elif direction == 1:
        posx = posx - 1
    elif direction == 2:
        posy = posy + 1
    elif direction == 3:
        posx = posx + 1

    calc()

    sideCount = sideCount + 1

    if sideCount == sideLength:
        sideCount = 0
        direction = (direction + 1) % 4
        if direction == 0:
            sideLength += 2
            posx += 1
            posy += 1

def calc():
    global total, values, posx, posy

    values[posx][posy] = \
        values[posx - 1][posy - 1] + \
        values[posx - 1][posy] + \
        values[posx - 1][posy + 1] + \
        values[posx][posy - 1] + \
        values[posx][posy + 1] + \
        values[posx + 1][posy - 1] + \
        values[posx + 1][posy] + \
        values[posx + 1][posy + 1]

for x in range(1, value):
    advance()
    possible = values[posx][posy]

    if possible > value:
        print possible
        break; 
