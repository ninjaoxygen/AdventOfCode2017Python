#!/usr/bin/python
import csv
import math

# array of code bytes
blocks = []

previousStates = []

# step
step = 0

def readFile(filename):
    global blocks
    
    blocks = []

    with open(filename) as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            for value in line:
                blocks.append(int(value))

def show():
    global blocks
    print(blocks)

def findHighest():
    global blocks
    
    maxIndex = 0
    maxValue = -1

    for i in range(0, len(blocks)):
        if (blocks[i] > maxValue):
            maxIndex = i
            maxValue = blocks[maxIndex]

    return maxIndex

def rebalance():
    global blocks

    previousStates.append(list(blocks))

    i = findHighest()

    # take the value to be redistributed
    v = blocks[i]
    blocks[i] = 0

    #print("max", "index", i, "value", v)

    # amount to divide over
    n = len(blocks)

    for j in range(0, len(blocks)):
        # amount to redistribute into this block
        amount = int(math.ceil(v / float(n)))

        # remaining blocks to divide over
        n -= 1

        # remaining value to redistribute
        v -= amount

        # which block to change
        which = (j + i + 1) % len(blocks)

        #print("adding", amount, " to ", which)

        blocks[which] += amount

def checkLoop():
    for i in range(0, len(previousStates)):
        if blocks == previousStates[i]:
            print("loop found at ", i, "after", len(previousStates) - i, "cycles")
            return True

    return False

def checkFile(filename):
    global previousStates
    previousStates = []
    readFile(filename)
    finished = False

    while finished == False:
        #show()
        rebalance()
        finished = checkLoop()

checkFile("sample.txt")
checkFile("input.txt")
