from collections import Counter, defaultdict
import numpy as np


def p1(a):
    pass


def p2(a):
    pass


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


print('Run test cases')
run("test.txt")
print()
print('Run real cases')
run("input1.txt")
