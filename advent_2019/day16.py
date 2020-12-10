import numpy as np

base = [0,1,0,-1]

def get_ones(num):
	return abs(num) % 10

def conv(input, idx):
	pattern = np.roll(np.repeat(base, idx), -1)
	m = len(input) // len(pattern) + 1
	pat = np.tile(pattern, m)[:len(input)]
	return get_ones(sum(input * pat))

def part_1():
	with open('input16.txt') as f:
		ipt = list(map(int, list(f.readline().strip())))

	for i in range(100):
		# length of output
		output = []
		for idx in range(1, len(ipt)+1):
			num = conv(ipt, idx)
			output.append(num)
		ipt = output

	print(''.join(map(str, ipt[:8])))

def part_2():
	with open('input16.txt') as f:
		input_str = f.readline().strip()
		offset = int(input_str[:7])
		base_input = list(map(int,input_str))
		ipt = np.tile(base_input, 10000)[offset:]

	copies = 10000
	for i in range(100):
		ipt = np.cumsum(ipt[::-1]) % 10
		ipt = ipt[::-1]

	print(''.join(map(str, ipt[:8])))

part_1()
part_2()