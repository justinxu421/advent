from parse import *

####### part 1
with open('input22.txt') as f:
	rules = f.read().strip().split('\n')

def new_stack(arr):
	return list(reversed(arr))

def cut(arr, n):
	if n > 0:
		return arr[n:] + arr[:n]
	else:
		return cut(arr, len(arr)+n)

def increment(arr, n):
	length = len(arr)
	a = [None for _ in range(len(arr))]

	for i in range(length):
		idx = (i * n) % length
		a[idx] = arr[i]

	return a

def parse_line(line, arr):
	if line == 'deal into new stack':
		return new_stack(arr)
	elif 'deal with increment ' in line:
		n = int(parse("deal with increment {}", line)[0])
		return increment(arr, n)
	elif 'cut ' in line:
		n = int(parse("cut {}", line)[0])
		return cut(arr, n)

def part_1(rules):
	arr = [i for i in range(10007)]
	for line in rules:
		arr = parse_line(line, arr)

	for idx, x in enumerate(arr):
		if x == 2019:
			print(idx)

###### part 2
def rev_new_stack(a, b, L):
	return (-a, L-1-b)

def rev_cut(n, a, b, L):
	return (a, b+n % L)

def rev_increment(n, a, b, L):
	# get the mod inverse (assume that L is prime)
	n_ = pow(n,L-2,L)
	return  n_*a%L, n_*b % L

def parse_reverse(line, a, b, L):
	if line == 'deal into new stack':
		return rev_new_stack(a, b, L)
	elif 'deal with increment ' in line:
		n = int(parse("deal with increment {}", line)[0])
		return rev_increment(n, a, b, L) 
	elif 'cut ' in line:
		n = int(parse("cut {}", line)[0])
		return rev_cut(n, a, b, L)

def shuffle(L, rules):
	a,b = 1,0
	for line in reversed(rules):
		a, b = parse_reverse(line, a, b, L)
	return a,b

# find f^N(x)
# f(x) = ax+b | g(x) = cx+d
# f^2(x) =  f o f (x) = a(ax+b)+b = aax + (ab+b)
# f o g(x) = a(cx+d)+b = acx + (ad+b)
def shuffle_N(N, L, a, b):
	if N == 0:
		return 1,0
	if N%2 == 0:
		return shuffle_N(N//2, L, a*a % L, (a*b+b) % L)
	else:
		c,d = shuffle_N(N-1,L,a,b)
		return a*c % L, (a*d+b) % L


def shuffle_alot(N, L, rules, pos):
	a,b = shuffle(L, rules)
	a_,b_ = shuffle_N(N, L, a, b)
	return (pos*a_ + b_) % L

def part_2(rules):
	NUM_CARDS = 119315717514047
	ITERS = 101741582076661
	print(shuffle_alot(ITERS, NUM_CARDS, rules, 2020))

part_1(rules)
part_2(rules)

# testing
# print(shuffle_alot(20, 101, rules, 20))

# arr = [i for i in range(101)]
# for _ in range(10):
# 	for line in rules:
# 		arr = parse_line(line, arr)
# print(arr[20])