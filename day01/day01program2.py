#!/usr/bin/python

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

sequence = []
total = 0

# read the file in	
f = open("input.txt")
next = f.read(1)
while is_number(next):
    sequence.append(next)
    next = f.read(1)

# vars for the loop
length = len(sequence)
halfLength = int(len(sequence) / 2)

print("length", length)
print("halfLength", halfLength)

for x in range(0, len(sequence)):
    if sequence[x] == sequence[(x + halfLength) % length]:
        total += int(sequence[x])
	
print("total", total)
