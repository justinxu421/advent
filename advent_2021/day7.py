from collections import Counter, defaultdict
import numpy as np

def move1(num, x):
    return abs(num-x)

def move2(num, x):
    b = abs(num-x)
    return b * (b+1) // 2

# align all of a to [x] * len(a)
def align(a, x, move):
    total = 0
    for num in a:
        total += move(num, x)
    return total

def p1(a):
    return min(align(a, x, move1) for x in range(max(a)))

def p2(a):
    pass
    return min(align(a, x, move2) for x in range(max(a)))


def run(file):
    with open(file) as f:
        a = list(map(int, f.read().strip().split(',')))        
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


print('Run test cases')
run("test.txt")
print()
print('Run real cases')
run("input7.txt")
