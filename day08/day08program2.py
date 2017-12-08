#!/usr/bin/python
import csv
import operator

registers = dict()
maxIntermediate = 0

def checkRegister(registerName):
    global registers

    if not registerName in registers:
        registers[registerName] = 0

def compareRegister(registerName, op, value):
    global registers

    checkRegister(registerName)

    registerValue = registers[registerName]
    comparisonValue = int(value)

    if (op == "=="):
        return registerValue == comparisonValue

    if (op == "!="):
        return registerValue != comparisonValue
    
    if (op == "<"):
        return registerValue < comparisonValue

    if (op == ">"):
        return registerValue > comparisonValue

    if (op == "<="):
        return registerValue <= comparisonValue

    if (op == ">="):
        return registerValue >= comparisonValue

    print("unrecognised op", op)
    exit        

def processLine(line):
    global registers
    global maxIntermediate

    register = line[0]

    checkRegister(register)

    op = line[1]

    if op == "inc":
        value = int(line[2])
    elif op == "dec":
        value = -int(line[2])
    else:
        print("unrecognised opcode", op)
        exit

    if compareRegister(line[4], line[5], line[6]):
        registers[register] += value

        if (registers[register] > maxIntermediate):
            maxIntermediate = registers[register]

def readFile(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=' ')
        for line in reader:
            processLine(line)

def checkFile(filename):
    global registers
    global maxIntermediate

    registers = dict()
    maxIntermediate = 0

    readFile(filename)

    maxRegisterValue = max(registers, key=lambda key: registers[key])

    print("maxRegisterValue", maxRegisterValue, registers[maxRegisterValue])
    print("maxIntermediate", maxIntermediate)

checkFile("sample.txt")
checkFile("input.txt")
