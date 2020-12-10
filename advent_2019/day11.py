from intcode_deprecated import IntcodeRunner
import matplotlib.pyplot as plt
import numpy as np

directions = {0: 'N', 1:'E', 2:'S', 3:'W'}

def move(state, direction):
	if direction == 0:
		return (state[0]-1, state[1])
	if direction == 1: 
		return (state[0], state[1]+1)
	if direction == 2:
		return (state[0]+1, state[1])
	if direction == 3:
		return (state[0], state[1]-1)

# black or '.' is 0, white or '.#' is 1
def update_grid(grid, state, direction, output1, output2):
	# color current state
	grid[state] = output1
	# turn left 90
	if output2 == 0: 
		direction = (direction - 1) % 4
	# turn right 90
	if output2 == 1: 
		direction = (direction + 1) % 4
	new_state = move(state, direction)
	return new_state, direction


def run_intcode(ic, ipt):
	ic.run(ipt, ipt)
	output1 = ic.output
	ic.run(ipt, ipt)
	output2 = ic.output

	return ic, output1, output2

def part_1(arr):
	grid = {}
	colored_states = set()
	state = (0,0)
	direction = 0
	ic = IntcodeRunner(arr) 

	while ic.done == False:
		if state not in grid:
			grid[state] = 0
		ic, output1, output2 = run_intcode(ic, grid[state])
		colored_states.add(state)
		state, direction = update_grid(grid, state, direction, output1, output2)

	print(len(colored_states))

def part_2(arr):
	grid = np.ones((10,45))
	state = (0,0)
	direction = 0
	ic = IntcodeRunner(arr) 

	while ic.done == False:
		ic, output1, output2 = run_intcode(ic, grid[state])
		state, direction = update_grid(grid, state, direction, output1, output2)

	plt.imshow(grid)
	plt.savefig('grid.png')


with open('input11.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))
	part_1(arr[:])
	part_2(arr[:])
