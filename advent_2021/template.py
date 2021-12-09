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


test_files = [
    "test.txt",
    "input1.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()