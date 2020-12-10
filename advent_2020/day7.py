from collections import defaultdict

KEY = 'shiny gold' 

def p1(a):
	d = defaultdict(set)
	for master, bags in a:
		for count, bag in bags:
			if count != 'no':
				d[bag].add(master)

	total = set()
	stack = [KEY]

	while stack:
		cur = stack.pop()
		for entry in d[cur]:
			if entry not in total:
				stack.append(entry)
				total.add(entry)
	return len(total)

def get_count(d, key):
	# base case
	total = 1
	if d[key][0][0] == 0:
		return total

	for count, bag in d[key]:
		total += count * get_count(d, bag)
	return total


def p2(a):
	d = defaultdict(list)
	for master, bags in a:
		for count, bag in bags:
			if count != 'no':
				d[master].append((int(count), bag))
			else:
				d[master].append((0, bag))

	return get_count(d, KEY) - 1

def parse_str(str):
	return str.split(' bag')[0].strip().split(' ', 1)

### insert how to parse line
def parse_line(line):
	# a contains list of bags
	a, b = line.strip().split(' contain ')
	bags = list(map(parse_str, b.strip().split(', ')))

	return (a.split(' bag')[0], bags)

with open('input7.txt') as f:
	a = [parse_line(line) for line in f]

	for i in range(3):
		print(a[i])

	print(p1(a))
	print(p2(a))

