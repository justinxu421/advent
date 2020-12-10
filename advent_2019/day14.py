from collections import defaultdict
import networkx as nx

def parse_unit(str):
	u, c = str.split(' ')
	return int(u), c

def parse_line(line, reactions, dag):
	reactants, prod = line.split(' => ')
	reactant_list = reactants.split(', ')

	unit, chemical = parse_unit(prod)
	reactions[chemical] = (unit, list(map(parse_unit, reactant_list)))

	for reactant in reactant_list:
		dag.add_edge(chemical, parse_unit(reactant)[1])


def decompose_chemical(chemical, amount, reactions, prods):
	unit, reactants = reactions[chemical]
	multiple = (amount-1) // unit + 1
	for u_, r_ in reactants:
		prods[r_] += u_*multiple


def process_prods(prods, topo_order):
	# leftover = defaultdict(int)
	num_ore = 0
	while prods:
		for chemical in topo_order:
			if chemical in prods:
				amount = prods[chemical]
				del prods[chemical]
				break

		if chemical == 'ORE':
			num_ore += amount
		else:
			decompose_chemical(chemical, amount, reactions, prods)
	return num_ore

def part_1(reactions, topo_order):
	prods = defaultdict(int)
	prods['FUEL'] = 1

	num_ore = process_prods(prods, topo_order)

	print('part 1: {}'.format(num_ore))
	return num_ore

def part_2(reactions, topo_order, part_1_ore):
	max_ore = 1000000000000
	guess = max_ore // part_1_ore 
	min_guess = guess
	max_guess = 2*guess -1

	while (max_guess - min_guess) > 1:
		mid = (max_guess + min_guess) // 2

		prods = defaultdict(int)
		prods['FUEL'] = mid 
		num_ore = process_prods(prods, topo_order)

		print(mid, num_ore)
		if num_ore > max_ore:
			max_guess = mid
		else:
			min_guess = mid	

	# probably right, but check the diagnostics to make sure
	print('part 2: {}'.format(min_guess))


with open('input14.txt') as f:
	reactions = {}
	dag = nx.DiGraph()

	for line in f:
		parse_line(line.strip(), reactions, dag)	

	# order to parse chemicals
	topo_order = list(nx.topological_sort(dag))

	part_1_ore = part_1(reactions, topo_order)
	part_2(reactions, topo_order, part_1_ore)
