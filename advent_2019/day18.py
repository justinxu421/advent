import numpy as np
import sys
import queue as Q 

with open('input18.txt') as f:
	arr = []	
	for line in f:
		arr.append(list(line.strip()))

	arr = np.stack(arr)
	print(arr.shape)

coord_dict = {}
keys = []
for i in range(len(arr)):
	for j in range(len(arr[0])):
		x = arr[i,j] 
		if x == '@':
			coord_dict[x] = (i,j)
		if x <= 'z' and x >= 'a':
			coord_dict[x] = (i,j)
			keys.append(x)
		if x <= 'Z' and x >= 'A':
			coord_dict[x] = (i,j)

def check_bounds(arr, point):
	return point[0] >= 0 and point[0] < len(arr) \
		and point[1] >= 0 and point[1] < len(arr[0])

def get_valid_moves(arr, point):
	moves = [(point[0]-1, point[1]), (point[0]+1, point[1]), \
		(point[0], point[1]-1), (point[0], point[1]+1)]
	return [x for x in moves if check_bounds(arr,x) and arr[x] != '#']

def bfs(arr, start):
	doors = []
	q = [(start,0,doors)]

	visited = set()

	min_dists = {}
	while q:
		curr, dist, doors = q.pop(0)
		door_copy = doors[:]

		visited.add(curr)

		if curr != start and arr[curr].isalpha():
			if arr[curr].islower():
				min_dists[arr[curr]] = (dist, doors)
			if arr[curr].isupper():
				door_copy.append(arr[curr])

		for n in get_valid_moves(arr, curr):
			if n not in visited:
				q.append((n, dist+1, door_copy))		 
	return min_dists


def get_key_to_key_dists():
	k2k_dists = {}
	for key1 in keys + ['@']:
		k2k_dists[key1] = bfs(arr, coord_dict[key1])
	return k2k_dists

def get_reachable_keys(start, k2k_dists, curr_keys):
	dists = []
	curr_doors = [k.upper() for k in list(curr_keys)]
	remaining_keys = set(keys) - set(curr_keys)

	for key, (dist, doors) in k2k_dists[start].items():
		if key in remaining_keys and len(set(doors) - set(curr_doors)) == 0:
			dists.append((key,dist))
	return dists

def minwalk(arr, start, curr_keys, seen):
	ck_str = ''.join(sorted(curr_keys))
	if (start, ck_str) in seen:
		return seen[(start, ck_str)]

	dists = get_reachable_keys(start, k2k_dists, curr_keys)
	if len(curr_keys) - len(keys) == 0:
		# done!
		ans = 0
	else:
		totals = []
		for k, dist in dists:
			totals.append(dist + minwalk(arr, k, curr_keys + k, seen))
		ans = min(totals)

	seen[(start, ck_str)] = ans
	return ans

k2k_dists = get_key_to_key_dists()
def part_1(arr):
	seen = {}
	print(minwalk(arr, '@', '', seen))


part_1(arr)
