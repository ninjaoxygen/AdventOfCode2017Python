f = open("input.txt")
prev = "*"
total = 0
next = f.read(1)
first = next
while next != "\n":
	last = next
	if prev == next:
		total += int(next)
		print(next)
	
	prev = next
	print(next, total)
	next = f.read(1)

if last == first:
	total += int(first)
	
print("total", total)

