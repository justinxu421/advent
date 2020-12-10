import numpy as np
import math

def get_rel_coord(x0, y0, x, y):
	return (x-x0, y-y0)	

def get_relative_asteroids(arr, x0, y0):
	rel_coords = []
	for y in range(len(arr)):
		for x in range(len(arr[0])):
			if (x,y) != (x0,y0) and arr[y,x] == '#':
				rel_coords.append(get_rel_coord(x0, y0, x, y))
	return rel_coords

def get_unique_asteroids(rel_coords):
	# maps from relative coordinate to gcd
	unique_ = {}
	for x_, y_ in rel_coords:
		gcd = math.gcd(x_, y_)
		pair = (x_//gcd, y_//gcd)
		if pair not in unique_:
			unique_[pair] = gcd
		unique_[pair] = min(unique_[pair], gcd)
	return unique_

# get num asteroids detected at position
def num_asteroids(arr, x0, y0):
	rel_coords = get_relative_asteroids(arr, x0, y0)
	unique_ = get_unique_asteroids(rel_coords)
	return len(unique_)

def part_1(arr):
	ast_map = {}
	for y in range(len(arr)):
		for x in range(len(arr[0])):
			if arr[y,x] == '#':
				ast_map[(x,y)] = num_asteroids(arr, x, y)

	max_ = max(ast_map.items(), key=lambda x: x[1])
	print('part 1: coordinate {} with {} asteroids in sight'.format(max_[0], max_[1]))
	return max_

def get_angle(x_, y_):
	# get angle from relative rel_coords
	angle = math.atan2(x_, -y_)
	# make it positive
	if angle < 0:
		angle += 2*np.pi

	return angle

def vaporize(arr, x0, y0, count):
	rel_coords = get_relative_asteroids(arr, x0, y0)
	unique_ = get_unique_asteroids(rel_coords)

	coord_angle = []
	for (x_,y_),gcd in unique_.items():
		angle = get_angle(x_, y_)

		true_coord = (x0+x_*gcd, y0+y_*gcd)
		coord_angle.append((true_coord, angle))

	# start vaporizing 
	for coord, angle in sorted(coord_angle, key=lambda x: x[1]):
		arr[(coord[1], coord[0])] = '.'
		count += 1
		if count == 200:
			print('part 2: final coord {} is asteroid number {}'.format(coord, count))

	return count


def part_2(arr, x0, y0):
	count = 0
	while count <= 200:
		count = vaporize(arr, x0, y0, count)


with open('input10.txt') as f:
	arr = []
	for line in f:
		arr.append(list(line.strip()))
	arr = np.array(arr)

	(x0,y0), num_asteroids = part_1(arr)
	part_2(arr, x0, y0)



