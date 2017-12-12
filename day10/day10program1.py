#!/usr/bin/python
import csv
import operator

def processLine(line, length):
    elements = []

    for i in range(0, length):
        elements.append(i)

    print("first", elements)

    current = 0
    skip = 0

    # process each entry in the swap list
    for i in range(0, len(line)):

        swapCount = line[i]

        for j in range(0, int(swapCount / 2)):
            i1 = (current + j) % length
            i2 = (current + swapCount - j - 1) % length

            print("swapping ", i1, elements[i1], "with", i2, elements[i2])

            temp = elements[i1]
            elements[i1] = elements[i2]
            elements[i2] = temp 

        print("after swap", elements)

        current = (current + swapCount + skip) % length
        skip += 1

        print("current is now", current)


    # get the check by multiplying first two numbers

    print("checksum", elements[0] * elements[1])


def readFile(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            return line

def checkFile(filename, length):
    # grab the list from the file
    line = readFile(filename)
    
    print(line)

    # convert to integers
    for i in range(0, len(line)):
        line[i] = int(line[i])

    print(line)

    processLine(line, length)

checkFile("sample.txt", 5)
checkFile("input.txt", 256)
