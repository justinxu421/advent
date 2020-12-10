import re
import numpy as np
from queue import PriorityQueue
from collections import defaultdict

def get_indices(arr):
	# get the indexes 
	t_, b_ = 2, len(arr) - 3
	for row in range(t_, b_):
		if ' ' in arr[row, 2:-2]:
			it_ = row-1
			break

	for row in reversed(range(t_, b_)):
		if ' ' in arr[row, 2:-2]:
			ib_ = row+1
			break

	l_, r_ = 2, len(arr[0]) - 3
	for col in range(l_, r_):
		if ' ' in arr[2:-2, col]:
			il_ = col-1
			break
	for col in reversed(range(l_, r_)):
		if ' ' in arr[2:-2, col]:
			ir_ = col+1
			break

	return t_, b_, l_, r_, it_, ib_, il_, ir_

def parse_row(gates, raw_arr, idx, direction, suffix):
	if direction == -1:
		gate_names = [a+b for a,b in zip(raw_arr[idx-2], raw_arr[idx-1])]
	if direction == 1:
		gate_names = [a+b for a,b in zip(raw_arr[idx+1], raw_arr[idx+2])]

	new_gates = {}
	for i, name in enumerate(gate_names):
		if name[0].isalpha() and name[1].isalpha():
			if name != 'AA' and name != 'ZZ':
				name += suffix
			new_gates[name] = (idx,i)
	gates.update(new_gates)

def parse_col(gates, raw_arr, idx, direction, suffix):
	if direction == -1:
		gate_names = [a+b for a,b in zip(raw_arr[:,idx-2], raw_arr[:,idx-1])]
	if direction == 1:
		gate_names = [a+b for a,b in zip(raw_arr[:,idx+1], raw_arr[:,idx+2])]

	new_gates = {}
	for i, name in enumerate(gate_names):
		if name[0].isalpha() and name[1].isalpha():
			if name != 'AA' and name != 'ZZ':
				name += suffix
			new_gates[name] = (i, idx)
	gates.update(new_gates)

def parse_maze(file):
	with open(file) as f:
		stripped_arr = [] 
		raw_arr = []
		for row, line in enumerate(f):
			line = line.rstrip('\n')
			new_line = re.sub(r'[A-Z]', ' ', line)

			raw_arr.append(list(line))
			stripped_arr.append(list(new_line))


		arr = np.stack(stripped_arr) 
		raw_arr = np.stack(raw_arr)
		t_, b_, l_, r_, it_, ib_, il_, ir_ = get_indices(arr)

		gates = {}
		parse_row(gates, raw_arr, t_, -1, '_o')
		parse_row(gates, raw_arr, b_, 1, '_o')
		parse_col(gates, raw_arr, l_, -1, '_o')
		parse_col(gates, raw_arr, r_, 1, '_o')
		parse_row(gates, raw_arr, it_, 1, '_i')
		parse_row(gates, raw_arr, ib_, -1, '_i')
		parse_col(gates, raw_arr, il_, 1, '_i')
		parse_col(gates, raw_arr, ir_, -1, '_i')

		inv_gates = {}
		for k,v in gates.items():
			inv_gates[v] = k

		# make sure the coordinates of the gates are all '.'
		assert [(g,c) for g,c in gates.items() if arr[c] != '.'] == []
		return arr, gates, inv_gates

def check_bounds(arr, point):
	return point[0] >= 0 and point[0] < len(arr) \
		and point[1] >= 0 and point[1] < len(arr[0])

def get_valid_moves(arr, point):
	moves = [(point[0]-1, point[1]), (point[0]+1, point[1]), \
		(point[0], point[1]-1), (point[0], point[1]+1)]
	return [x for x in moves if check_bounds(arr,x) and arr[x] == '.']

def bfs(arr, gate, start, inv_gates):
	q = [(start,0)]
	visited = set()

	dists = {}
	while q:
		curr, dist = q.pop(0)
		visited.add(curr)

		if curr != start and curr in inv_gates:
			gate = inv_gates[curr]
			dists[gate] = dist

		for n in get_valid_moves(arr, curr):
			if n not in visited:
				q.append((n, dist+1))		 

	return dists

# get the gate to gate distances
def get_dists(arr, gates, inv_gates):
	g2g_dists = {}
	for gate in gates:
		g2g_dists[gate] = bfs(arr, gate, gates[gate], inv_gates)
	return g2g_dists

# get the warps with levels
def get_recursive_warps(g1, l, levels): 
	dists = {} 
	# link inner to outer
	if g1[-2] == '_':
		if g1[-2:] == '_o':
			g2 = g1[:-2]+'_i'
			nl = l-1
		elif g1[-2:] == '_i':
			g2 = g1[:-2]+'_o'
			nl = l+1
		# if only 1 level, then everything is 0
		if levels == 1:
			nl = 0
		if nl >= 0 and nl < levels:
			dists[(g2, nl)] = 1
	return dists

# get the gate to gate distances with levels
def get_dists_levels(g2g_dists, levels):
	g2g_dists_levels = {}
	for l in range(levels):
		for g1 in g2g_dists:
			# create warping states
			dists = get_recursive_warps(g1 ,l, levels)

			for g2 in g2g_dists[g1]:
				# parse base levels
				if l == 0:
					dists[(g2,l)] = g2g_dists[g1][g2]
				elif g1[-2] == '_' and g2[-2] == '_' :
					dists[(g2,l)] = g2g_dists[g1][g2]

			g2g_dists_levels[(g1, l)] = dists

	return g2g_dists_levels

arr, gates, inv_gates = parse_maze('input20.txt')
g2g_dists = get_dists(arr, gates, inv_gates)

def get_min_dist(levels):
	g2g_dists_levels = get_dists_levels(g2g_dists, levels)
	seen = {}
	pq = PriorityQueue()
	pq.put((0,'AA',0))

	visited = set()
	while not pq.empty():
		total, curr, level  = pq.get()
		visited.add((curr, level))
		if curr == 'ZZ' and level == 0:
			return total
		for (n,new_level), d in g2g_dists_levels[(curr, level)].items():
			if (n,new_level) not in visited:
				pq.put((total+d, n, new_level))
# no levels
def part_1():
	print('part 1: {}'.format(get_min_dist(1)))

# set arbitrary number of levels
def part_2():
	print('part 2: {}'.format(get_min_dist(40)))

part_1()
part_2()