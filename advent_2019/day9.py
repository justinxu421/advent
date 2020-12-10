from collections import defaultdict
from intcode_deprecated import IntcodeRunner


with open('input9.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))

ic = IntcodeRunner(arr)
ipt = 2	 
while ic.done == False:
	ic.run(ipt, ipt)
	print('output', ic.output)
