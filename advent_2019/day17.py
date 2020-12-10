from intcode import IntcodeRunner
import numpy as np
import sys
import utils

N,E,S,W = 0,1,2,3

def parse_outputs(outputs):
	arr = []
	line = []
	for output in outputs:
		if output != 10:
			line.append(chr(output))
		if output == 10:
			arr.append(line)
			line = []
	return arr	

def check_adjacent(point, arr):
	adjacents = [(point[0]-1, point[1]), (point[0], point[1]-1), 
				(point[0]+1, point[1]), (point[0], point[1]+1)]

	for adjacent in adjacents:
		if arr[adjacent] != '#':
			return False
	return True

def get_intersects(arr):
	scafs = []
	for i in range(1,len(arr)-1):
		for j in range(1,len(arr[0])-1):
			if arr[i,j] == '#':
				scafs.append((i,j))
	intersects = [scaf for scaf in scafs if check_adjacent(scaf, arr)]
	return intersects

def get_alignment(intersects, arr):
	max_x, max_y = len(arr), len(arr[0])

	total = 0
	for (x,y) in intersects:
		total += x*y
	return total

def part_1():
	with open('input17.txt') as f:
		arr = list(map(int, f.readline().strip().split(',')))
		ic = IntcodeRunner(arr)

		ic.run()
		outputs = ic.outputs[:-2]

		str_arr = ''.join(chr(x) for x in ic.outputs)
		print(str_arr)

		arr = parse_outputs(outputs)
		arr = np.stack(arr)

		intersects = get_intersects(arr) 
		print(get_alignment(intersects, arr))

def part_2():
	with open('input17.txt') as f:
		arr = list(map(int, f.readline().strip().split(',')))
		arr[0] = 2
		ic2 = IntcodeRunner(arr)

		mov_func = [ord(c) for c in 'A,A,B,C,B,C,B,A,C,A\n']
		mov_a = [ord(c) for c in 'R,8,L,12,R,8\n']
		mov_b = [ord(c) for c in 'L,10,L,10,R,8\n']
		mov_c = [ord(c) for c in 'L,12,L,12,L,10,R,10\n']

		inputs = []
		inputs.extend(mov_func)
		inputs.extend(mov_a)
		inputs.extend(mov_b)
		inputs.extend(mov_c)
		inputs.extend([ord('n'), ord('\n')])
		ic2.set_inputs(inputs)

		ic2.run()
		print(ic2.outputs[-1])

part_1()
part_2()