#!/usr/bin/python
import csv

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

def balanceProgram(programName):
    global programs


    program = programs[programName]

    # start with this program's weight
    program["totalWeight"] = program["weight"]

    # add on all the children, with a recursive call :-/
    children = program["children"]

    for child in children:
        balanceProgram(child)
        program["totalWeight"] += programs[child]["totalWeight"]

    # if len(children) > 0:
    #     print "balanced", programName
    #     for child in children:
    #         print "  ", child, programs[child]["totalWeight"]

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
            rootProgram = programName
            print(programName, "is the root program" )

    # work out the total weights on each program
    balanceProgram(rootProgram)

    # follow down the tree to the odd program
    print("following chain of odd programs to leaf...")
    followOddProgram(rootProgram)

def followOddProgram(programName):
    program = programs[programName]

    counts = dict()

    for child in program["children"]:
        childProgram = programs[child]

        if not childProgram["totalWeight"] in counts:
            counts[childProgram["totalWeight"]] = []

        counts[childProgram["totalWeight"]].append(child)

    if len(counts) > 2: # given the problem stated, this should never happen
        print(child, "broken here!")
        exit
    elif len(counts) == 2: # two weights, the odd one out should have a single item, the other one should have at least two items
        oddWeight = 0
        oddChild = ""
        normalWeight = 0

        for weight in counts:
            #print child, "checking weight", weight
            weightCount = len(counts[weight])
            #print child, "has ", weightCount, "of", weight
            if weightCount == 1:
                #print "...and this is the odd child!", counts[weight][0]
                oddWeight = weight
                oddChild = counts[weight][0]
            else:
                #print "...and this is the normal weight", counts[weight][0]
                normalWeight = weight

        if len(oddChild) > 0:
            print(oddChild, "is", oddWeight,"but should be",normalWeight)
            delta = oddWeight - normalWeight
            print("delta = ", delta)
            print("original weight", programs[oddChild]["weight"], ", correct weight", programs[oddChild]["weight"] - delta)

            followOddProgram(oddChild)

checkFile("sample.txt")
checkFile("input.txt")
