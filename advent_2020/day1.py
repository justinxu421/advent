def p1(a):
	s = set()
	for x in a:
		if (2020 - x) in s:
			print(x, 2020-x)
			return x* (2020-x) 
		else:
			s.add(x)

def p2(a):
	for i in range(len(a)-2):
		for j in range(i+1, len(a)-1):
			for k in range(j+1, len(a)):
				total =  a[i] + a[j] + a[k]
				if total == 2020:
					print(a[i], a[j], a[k])
					return a[i]*a[j]*a[k]

def p2_b(e):
	e.sort()
	for i in range(len(e) - 2):
		k = len(e) - 1
		j = i + 1

		while j < k:
			total = e[i] + e[j] + e[k]
			if total == 2020:
				print(e[i], e[j], e[k])
				return e[i] * e[j] * e[k]
			elif total < 2020:
				j += 1
			elif total > 2020:
				k -= 1

with open('input1.txt') as f:
	# read array 
	a = [int(x.strip()) for x in f]
	print(p1(a))
	print(p2_b(a))