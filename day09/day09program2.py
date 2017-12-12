#!/usr/bin/python
import csv
import operator

def score(line):

    score = 0
    depth = 0
    garbage = False # 1 = in 
    ignore = False
    garbageCount = 0

    for pos in range(0, len(line)):
        if ignore:
            ignore = False
        elif garbage:
            if line[pos] == '!':
                ignore = True
            elif line[pos] == '>':
                garbage = False
            else:
                garbageCount += 1
        else:
            if line[pos] == '{':
                depth = depth + 1
            elif line[pos] == '}':
                score += depth
                depth -= 1
            elif line[pos] == '<':
                garbage = True

    print('Depth', depth)
    print('Score', score)
    print('Garbage Count', garbageCount)
    return score

def readFile(filename):
    with open(filename) as f:
            print(score(f.readline()))

if (score("{}") != 1): print("case 1 is broken")
if (score("{{{}}}") != 6): print("case 2 is broken")
if (score("{{},{}}") != 5): print("case 3 is broken")
if (score("{{{},{},{{}}}}") != 16): print("case 4 is broken")
if (score("{<a>,<a>,<a>,<a>}") != 1): print("case 5 is broken")
if (score("{{<ab>},{<ab>},{<ab>},{<ab>}}") != 9): print("case 6 is broken")
if (score("{{<!!>},{<!!>},{<!!>},{<!!>}}") != 9): print("case 7 is broken")
if (score("{{<a!>},{<a!>},{<a!>},{<ab>}}") != 3): print("case 8 is broken")

readFile("input.txt")
