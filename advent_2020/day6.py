def count_unique(entry):
	return len(set(''.join(entry)))

def p1(a):
	return sum(count_unique(entry) for entry in a)

def count_unanimous(entry):
	all_q = None
	for x in entry:
		if all_q is None:
			all_q = set(x)
		else:
			all_q &= set(x)
	return len(all_q)


def p2(a):
	return sum(count_unanimous(entry) for entry in a)

### insert how to parse line
def parse_line(line):
	binary = line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R','1')
	return int(''.join(binary), 2)

with open('input6.txt') as f:
	a = [line.split() for line in f.read().split('\n\n')]
	# print(a)

	print(p1(a))
	print(p2(a))

