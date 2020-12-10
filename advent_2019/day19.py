from intcode import IntcodeRunner
import numpy as np
import matplotlib.pyplot as plt

with open('input19.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))

def run_intcode(arr, i, j):
	ic = IntcodeRunner(arr[:])
	ic.set_inputs((i,j))
	ic.run()
	return ic.outputs[-1]

def get_square(start, arr, grid, w, plot=False):
	w = 100
	img = np.zeros((w,w))
	for i in range(w):
		for j in range(w):
			point = (start[0]+i, start[1]+j)
			if point not in grid:
				o = run_intcode(arr, point[0], point[1])
				grid[point] = o
			img[i,j] = grid[point]

	# get the total sum
	if plot:
		plt.imshow(img)
		plt.savefig('image19.png')
	return sum(sum(img))

def part_1(arr):
	print(get_square((0,0), arr, {}, 50, True))

def check_square(start, arr, grid):
	for i in range(start[0] + 100):
		for j in range(start[1] + 100):
			if (i,j) not in grid:
				o = run_intcode(arr, i, j)
				grid[i,j] = o
			if grid[i,j] != 1:
				return False
	return True


def part_2(arr):
	grid = {}
	x,y = 600,800

	while True:
		n1 = get_square((x+1,y), arr, grid, 100)
		n2 = get_square((x, y+1), arr, grid, 100)
		if n1 > n2:
			x += 1
			n = n1
		else:
			y += 1
			n = n2

		print(x,y,n)

		if n == 100*100:
			print('answer')
			return (x,y) 

part_1(arr)
print(part_2(arr))