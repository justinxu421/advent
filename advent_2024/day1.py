from collections import Counter, defaultdict
import numpy as np


def p1(a):
    left = [int(x[0]) for x in a]
    right = [int(x[1]) for x in a]
    left.sort()
    right.sort()

    total = 0
    for num1, num2 in zip(left, right):
        diff = abs(num1 - num2)
        total += diff
    return total



def p2(a):
    left = [int(x[0]) for x in a]
    right = [int(x[1]) for x in a]
    right_counter = Counter(right)

    total = 0
    for num in left:
        total += num * right_counter[num]
    return total





def run(file):
    with open(file) as f:
        a = [x.split() for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input1.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
