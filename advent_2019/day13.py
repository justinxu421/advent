from collections import defaultdict
from intcode_deprecated import IntcodeRunner
import numpy as np

inputs = [-1,0,1]

def run_intcode(ic, ipt):
	ic.run(ipt, ipt)
	output = ic.output

	return output

def part_1(arr):
	grid = {}
	ic = IntcodeRunner(arr) 

	ipt = 0
	while ic.done == False:
		a = run_intcode(ic, ipt)
		b = run_intcode(ic, ipt)
		c = run_intcode(ic, ipt)
		grid[a, b] = c

	print(len([k for k,v in grid.items() if v == 2]))
	return grid

def get_input(ballx, padx):
	if ballx > padx:
		return 1
	if ballx == padx:
		return 0
	if ballx < padx:
		return -1

def part_2(arr, grid):
	arr[0] = 2
	ic = IntcodeRunner(arr) 

	ballx = 0
	padx = 0

	ipt = 0 
	while ic.done == False:
		ipt = get_input(ballx, padx)
		a = run_intcode(ic, ipt)
		b = run_intcode(ic, ipt)
		c = run_intcode(ic, ipt)

		if a == -1 and b == 0 and c not in [0,1,2,3,4]:
			score = c
		if c == 3:
			padx = a
		if c == 4:
			ballx = a 

	print(score)


with open('input13.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))
	grid = part_1(arr[:])
	part_2(arr[:], grid)