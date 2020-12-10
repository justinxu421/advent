from copy import deepcopy
from utils import print_grid_levels

def get_adj1(grid,x):
	i,j,l = x
	adj = []
	adj.append((i-1,j,l))
	adj.append((i,j-1,l))
	adj.append((i+1,j,l))
	adj.append((i,j+1,l))
	return adj


def get_bugs(grid,adj):
	bugs = 0
	for a in adj:
		if a in grid and grid[a] == '#':
			bugs += 1
	return bugs


def update(grid,x,adj):
	bugs = get_bugs(grid, adj)
	# dead bug
	if grid[x] == '#':
		if bugs != 1:
			return '.'
		else:
			return '#'
	# infested
	if grid[x] == '.':
		if bugs in [1,2]:
			return '#'
		else:
			return '.'


def iter(grid):
	new_grid = {} 
	for x in grid:
		adj = get_adj1(grid,x)
		new = update(grid,x,adj) 
		new_grid[x] = new

	return new_grid 


def calc_biodiversity(grid):
	total = 0
	count = 0
	for i in range(5):
		for j in range(5):
			if grid[i,j,0] == '#':
				total += 2**count
			count += 1
	return total


def part_1(grid):
	g = grid

	scores = set()
	while True:
		bd = calc_biodiversity(g)
		if bd in scores:
			print(bd)
			break
		scores.add(bd)

		g = iter(g)


def get_adj2(x):
	i,j,l = x
	adj = []
	# top
	if (i-1,j) == (2,2):
		for x in range(5):
			adj.append((4,x,l+1))
	else:
		# top edge
		if i == 0:
			adj.append((1,2,l-1))
		else:
			adj.append((i-1,j,l))

	# down 
	if (i+1,j) == (2,2):
		for x in range(5):
			adj.append((0,x,l+1))
	else:
		# bottom edge
		if i == 4:
			adj.append((3,2,l-1))
		else:
			adj.append((i+1,j,l))

	# left
	if (i,j-1) == (2,2):
		for x in range(5):
			adj.append((x,4,l+1))
	else:
		# left edge
		if j == 0:
			adj.append((2,1,l-1))
		else:
			adj.append((i,j-1,l))

	# right
	if (i,j+1) == (2,2):
		for x in range(5):
			adj.append((x,0,l+1))
	else:
		# right edge
		if j == 4:
			adj.append((2,3,l-1))
		else:
			adj.append((i,j+1,l))

	return adj

def iter2(grid):
	new_grid = {}
	for x in grid:
		adj = get_adj2(x)
		new = update(grid,x,adj)
		new_grid[x] = new	
	return new_grid

def init_level(g, l):
	for i in range(5):
		for j in range(5):
			if (i,j) != (2,2):
				g[i,j,l] = '.' 

def part_2(grid):
	grid.pop((2,2,0))
	g = grid

	for r in range(200):
		levels = [x[2] for x in g]
		min_l, max_l = min(levels), max(levels)
		init_level(g, min_l-1)
		init_level(g, max_l+1)

		g = iter2(g)
		# print(r, sum([1 for k,v in g.items() if v == '#']))

	print(sum([1 for k,v in g.items() if v == '#']))

grid = {}
with open('input24.txt') as f:
	for i, line in enumerate(f):
		for j, x in enumerate(line.strip()):
			grid[i,j,0] = x

part_1(grid)
part_2(grid)