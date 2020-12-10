def p1(a):
	return max(a)

def p2(a):
	a.sort()
	prev = a[0]-1
	for x in sorted(a):
		if x != prev+1:
			return prev, x
		prev = x

### insert how to parse line
def parse_line(line):
	binary = line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R','1')
	return int(''.join(binary), 2)

with open('input5.txt') as f:
	a = f.readlines()
	a = list(map(parse_line, a))

	print(p1(a))
	print(p2(a))

