from intcode import IntcodeRunner
import sys

def display_output(ic):
	for x in ic.outputs:
		try:
			print(chr(x), end='')
		except:
			print(x)

with open('input25.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))

def parse_input(ipt):
	return [ord(c) for c in ipt]


ipts = [
'north',
'take wreath',
'east',
'east',
'east',
'take weather machine',
'west',
'west',
'west',
'south',
'south',
'west',
'take prime number',
'west',
'take astrolabe',
'east',
'east',
'south',
'take candy cane',
'north',
'north',
'east',
'take food ration',
'south',
'east',
'south',
'take hypercube',
'east',
'take space law space brochure',
'north',
]
ic = IntcodeRunner(arr)
program = parse_input('\n'.join(ipts)+'\n')
ic.set_inputs(program)
ic.run()

items = ['candy cane', 'wreath', 'hypercube', 'food ration', 
'weather machine', 'space law space brochure', 'prime number', 'astrolabe']

from itertools import combinations
for i in range(9):
	for p in combinations(items, i):
		ic.outputs = []
		for item in p:
			i1 = 'drop ' + item + '\n' 
			ic.add_inputs(parse_input(i1))

		ic.add_inputs(parse_input('west\n'))
		ic.add_inputs(parse_input('inv\n'))
		ic.run()
		display_output(ic)

		for item in p:
			i3 = 'take ' + item + '\n' 
			ic.add_inputs(parse_input(i3))


# display_output(ic)

# while not ic.done:
# 	ic.run()
# 	display_output(ic)
# 	ic.outputs = []
# 	data = sys.stdin.readline()
# 	program = parse_input(data)
# 	ic.add_inputs(program)

