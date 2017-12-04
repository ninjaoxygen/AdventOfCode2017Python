#!/usr/bin/python

import csv
import sys

def checkLine(line):
    print("checking line")
    for value in line:
        for divisor in line:
            if (value != divisor) & (value % divisor == 0):
                print(value, divisor)
                return value / divisor

    return 0

with open("input.txt") as tsv:
    checksum = 0
    for lineAsStrings in csv.reader(tsv, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
        line = []

        for valueString in lineAsStrings:
            line.append(int(valueString))

        checksum += checkLine(line)

print("checksum", checksum)
