#!/usr/bin/python

# array of code bytes
code = []

# instruction pointer
ip = 0

# step
step = 0

def readFile(filename):
    with open(filename) as f:
        for line in f:
            code.append(int(line))

def runInstruction():
    global code
    global ip
    global step

    instr = code[ip]
    
    if code[ip] >= 3:
        code[ip] -= 1
    else:
        code[ip] += 1
    
    step += 1
    ip += instr

def runCode():
    global code
    global ip
    global step
    
    print code[0]

    ip = 0
    step = 0
    while (ip >= 0) & (ip < len(code)):
        runInstruction()

code = []
readFile("sample.txt")
runCode()
print "final step was ", step

code = []
readFile("input.txt")
runCode()
print "final step was ", step
