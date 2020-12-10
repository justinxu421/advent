from intcode import IntcodeRunner
import numpy as np

with open('input21.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))
	ic = IntcodeRunner(arr)

T = J = False

def parse_input(ipt):
	return [ord(c) for c in ipt]

def display_output(ic):
	for x in ic.outputs:
		try:
			print(chr(x), end='')
		except:
			print(x)

ipts = [
'OR D J',
'OR A T',
'AND B T',
'AND C T',
'AND D T',
'NOT T T',
'AND T J',
'NOT T T',
'OR E T',
'OR H T',
'AND T J',
'RUN\n'
]

program = parse_input('\n'.join(ipts))

ic.set_inputs(program)

ic.run()
display_output(ic)
