#!/usr/bin/python

import csv
import sys

with open("input.txt") as tsv:
    checksum = 0
    for line in csv.reader(tsv, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
        lineLargest = 0
        lineSmallest = sys.maxint
        for valueString in line:
            value = int(valueString)

            if value < lineSmallest:
                lineSmallest = value

            if value > lineLargest:
                lineLargest = value

        difference = lineLargest - lineSmallest

        checksum += difference

        print("largest", lineLargest, "smallest", lineSmallest, "difference", difference, "checksum", checksum)

print("checksum", checksum)
