def get_trees(a, r, d):
	x, y = 0, 0

	trees = 0
	while x < len(a):
		b = y % len(a[0])
		if a[x][b] == '#':
			trees += 1
		x += d
		y += r

	return trees

def p1(a):
	return get_trees(a, 3, 1)

def p2(a):
	pairs = [(1,1), (3,1), (5,1), (7,1), (1,2)]
	total = 1
	for x, y in pairs:
		total *= get_trees(a, x, y)

	return total


### insert how to parse line
def parse_line(line):
	return list(line.strip())

with open('input3.txt') as f:
	a = []
	for line in f:
		a.append(parse_line(line))

	print(p1(a))
	print(p2(a))
