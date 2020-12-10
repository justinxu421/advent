from collections import defaultdict
import itertools

from intcode_deprecated import IntcodeRunner

# init intcode runners	
def init_intcode_runners(arr, num_intcodes):
	ic_runners = []
	for i in range(num_intcodes):
		arr_copy = arr[:]
		ic_runners.append(IntcodeRunner(arr_copy))
	return ic_runners

def part_1(arr):
	seq = [0,1,2,3,4]
	permutes = itertools.permutations(seq) 
	outputs = []

	for inputs in permutes:
		ic_runners = init_intcode_runners(arr, 5)

		# set the initial input to 0 and then loop through
		ipt2 = 0
		for i in range(5):
			# first input is mode
			ipt1 = inputs[i]
			ic_runners[i].run(ipt1, ipt2)
			ipt2 = ic_runners[i].output
		# get the final output
		outputs.append(ipt2)

	print(max(outputs))

def part_2(arr):
	seq = [5,6,7,8,9]
	permutes = itertools.permutations(seq) 
	outputs = []

	for inputs in permutes:
		ic_runners = init_intcode_runners(arr, 5)

		ipt2 = 0
		while not any([ic.done for ic in ic_runners]):
			for i in range(5):
				ipt1 = inputs[i]
				ic_runners[i].run(ipt1, ipt2)
				ipt2 = ic_runners[i].output
		outputs.append(ipt2)
	print(max(outputs))


with open('input7.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))
	# arr = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
	part_1(arr)
	part_2(arr)


