def check_valid(x):
	low, high, char, pas = x

	total = 0
	for c in pas:
		if c == char:
			total += 1
	if total >= low and total <= high:
		return True
	return False

def check_valid_2(x):
	low, high, char, pas = x

	a = pas[(low-1)] == char 
	b = pas[(high-1)] == char
	return a ^ b

def p1(a):
	return sum(check_valid(x) for x in a)

def p2(a):
	return sum(check_valid_2(x) for x in a)

def parse_line(line):
	a, b, pas = line.split(' ')
	low, high = a.split('-')

	low, high = int(low), int(high)
	char = b[0]

	return (low, high, char, pas.strip())

with open('input2.txt') as f:
	a = []
	for line in f:
		a.append(parse_line(line))
	print(a[:5])

	print(p1(a))
	print(p2(a))
