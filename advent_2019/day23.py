from intcode import IntcodeRunner

def part_1(arr):
	computers = []
	qs = []
	for i in range(50):
		ic = IntcodeRunner(arr[:], [i])
		computers.append(ic)
		qs.append([])


	done = set()
	while True:
		for i, c in enumerate(computers):
			if qs[i]:
				while qs[i]:
					x, y = qs[i].pop(0)
					c.add_input(x)
					c.add_input(y)
			else:
				c.add_input(-1)

			c.run()
			
			outputs = c.outputs	
			while outputs:
				address = outputs.pop(0)
				x = outputs.pop(0)
				y = outputs.pop(0)

				if address == 255:
					print(y)
					return
				else:
					qs[address].append((x, y))

def part_2(arr):
	computers = []
	qs = []
	for i in range(50):
		ic = IntcodeRunner(arr[:], [i])
		computers.append(ic)
		qs.append([])


	natSeen = set()
	while True:
		idles = 0 

		for i, c in enumerate(computers):
			if qs[i]:
				while qs[i]:
					x, y = qs[i].pop(0)
					c.add_input(x)
					c.add_input(y)
			else:
				idles += 1
				c.add_input(-1)

			c.run()
			
			outputs = c.outputs	
			while outputs:
				address = outputs.pop(0)
				x = outputs.pop(0)
				y = outputs.pop(0)

				if address == 255:
					natVal = (x,y)

				else:
					qs[address].append((x, y))
					natVal = None

		if idles == 50:
			if natVal in natSeen:
				print(natVal[1])
				return 
			qs[0].append(natVal)
			natSeen.add(natVal)


with open('input23.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))
	part_1(arr)
	part_2(arr)