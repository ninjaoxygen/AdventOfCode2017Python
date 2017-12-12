#!/usr/bin/python
import csv

def getProgram(number):
    global programs
    if not number in programs:
        program = dict()
        program['id'] = number
        program['connections'] = dict()
        programs[number] = program
        return program

    return programs[number]

def addConnection(program, connectionToProgram):
    connections = program['connections']
    connections[connectionToProgram] = True

def followPrograms(group):
    global tagList
    checkList = []
    count = 0

    checkList.append(group)
    tagList[0] = True

    while len(checkList) > 0:
        count += 1
        programId = checkList.pop()
        program = getProgram(programId)

        #print("checking program ", program['id'])

        for key in program['connections']:

            if not key in tagList:
                tagList[key] = True
                checkList.append(key)

    print("group", group, "contained", count, "programs")


def readFile(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=' ')
        for line in reader:
            line = list(reversed(line))
            programId = int(line.pop())
            program = getProgram(programId)

            # remove <->
            line.pop()

            for value in line:
                addConnection(program, int(value.replace(',', '')))


def checkFile(filename):
    global programs
    global tagList

    programs = dict()
    tagList= dict()
    readFile(filename)

    groupCount = 0

    for key in programs:
        if not key in tagList:
            groupCount += 1
            followPrograms(key)

    print("groupCount", groupCount)

checkFile("sample.txt")
checkFile("input.txt")
