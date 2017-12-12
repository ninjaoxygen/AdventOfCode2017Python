#!/usr/bin/python
import csv
import operator

def processLine(line):
    x = 0
    y = 0

    # process each entry in the swap list
    for i in range(0, len(line)):

        value = line[i]

        if value == 'n':
            y += 2
        elif value == 's':
            y -= 2
        elif value == 'ne':
            y += 1
            x += 1
        elif value == 'nw':
            y += 1
            x -= 1
        elif value == 'se':
            y -= 1
            x += 1
        elif value == 'sw':
            y -= 1
            x -= 1

        dist = abs(x) + abs(int((abs(y) - abs(x)) / 2))

    print("final location", x, y)
    print("stepcount", dist)

def readFile(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            return line

def checkFile(filename):
    # grab the list from the file
    line = readFile(filename)
    processLine(line)

processLine(["ne","ne","ne"])
processLine(["ne","ne","sw","sw"])
processLine(["ne","ne","s","s"])
processLine(["se","sw","se","sw","sw"])
checkFile("input.txt")
