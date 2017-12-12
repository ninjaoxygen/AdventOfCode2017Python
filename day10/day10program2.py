#!/usr/bin/python
import csv
import operator

elements = []
current = 0
skip = 0


def processLine(line, length):
    global elements
    global current
    global skip

    #print("first", elements)

    # process each entry in the swap list
    for i in range(0, len(line)):

        swapCount = line[i]

        for j in range(0, int(swapCount / 2)):
            i1 = (current + j) % length
            i2 = (current + swapCount - j - 1) % length

            #print("swapping ", i1, elements[i1], "with", i2, elements[i2])

            temp = elements[i1]
            elements[i1] = elements[i2]
            elements[i2] = temp 

        #print("after swap", elements)

        current = (current + swapCount + skip) % length
        skip += 1

        #print("current is now", current)


    # get the check by multiplying first two numbers

    print("checksum", elements[0] * elements[1])


def readFile(filename):
    with open(filename) as f:
        return f.readline()

def checkFile(filename, length):

    for i in range(0, length):
        elements.append(i)

    # grab the list from the file
    line = readFile(filename)
    line = line[0:len(line) - 1]
    data = []
    
    #print(line)

    # convert to integers
    for i in range(0, len(line)):
        data.append(ord(line[i]))

    data.append(17)
    data.append(31)
    data.append(73)
    data.append(47)
    data.append(23)
    
    #print(data)

    # 64 iterations of the mixer
    for i in range(0, 64):
        processLine(data, length)

    # calculate dense hash

    dense = []

    current = 0

    for j in range(0, 16):
        # compress one block of 16 values
        xorSum = 0

        for i in range(0, 16):
            xorSum ^= elements[current]
            current += 1

        dense.append(xorSum)

    strHex = ""
    for j in range(0, 16):
        strHex += "%0.2x" % dense[j]

    print(strHex)
    

checkFile("input.txt", 256)
