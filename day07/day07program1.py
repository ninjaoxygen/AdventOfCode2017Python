#!/usr/bin/python
import csv
import math

def readFile(filename):
    global programs
    
    with open(filename) as f:
        reader = csv.reader(f, delimiter=' ')
        for line in reader:
            program = dict()
            programName = line[0]
            programWeight = line[1]

            # remove anything up to and including '->'
            del line[0:3]

            # strip the brackets from programWeight and convert to an int
            programWeight = int(programWeight[1:len(programWeight) - 1])

            # make a list of the children
            programChildren = []

            for value in line:
                value = value.replace(",", "")
                programChildren.append(value)

            program["name"] = programName
            program["weight"] = programWeight
            program["children"] = programChildren

            programs[programName] = program
 

def checkFile(filename):
    global programs
    programs = dict()
    readFile(filename)

    for programName in programs:
        program = programs[programName]

        for child in program["children"]:
            childProgram = programs[child]
            childProgram["parent"] = programName

    for programName in programs:
        program = programs[programName]
        if not "parent" in program:
            print(programName, "is the root program")
    
checkFile("sample.txt")
checkFile("input.txt")
