#!/usr/bin/python

import csv
import sys

def checkLine(line):
    print("checking line")
    for value in line:
        print value

with open("input.txt") as tsv:
    count = 0
    for line in csv.reader(tsv, delimiter=" "):

        lineSet = set(line)

        print len(line), len(lineSet), len(line) == len(lineSet)

        if len(line) == len(lineSet):
            count += 1

print "count", count
