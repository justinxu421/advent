from collections import Counter, defaultdict
import numpy as np


def p1(a):
    line = a[0]
    for i in range(len(line) - 3):
        if len(set(line[i : i + 4])) == 4:
            return i + 4


def p2(a):
    line = a[0]
    for i in range(len(line) - 13):
        if len(set(line[i : i + 14])) == 14:
            return i + 14


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input6.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

