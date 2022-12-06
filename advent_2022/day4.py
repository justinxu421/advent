from collections import Counter, defaultdict
import numpy as np


def p1(a):
    total = 0
    for line in a:
        pair1, pair2 = line.split(",")
        low1, high1 = pair1.split("-")
        low2, high2 = pair2.split("-")
        range1 = set(range(int(low1), int(high1) + 1))
        range2 = set(range(int(low2), int(high2) + 1))
        if len(range1 & range2) == min(len(range1), len(range2)):
            total += 1
    return total


def p2(a):
    total = 0
    for line in a:
        pair1, pair2 = line.split(",")
        low1, high1 = pair1.split("-")
        low2, high2 = pair2.split("-")
        range1 = set(range(int(low1), int(high1) + 1))
        range2 = set(range(int(low2), int(high2) + 1))
        if len(range1 & range2) > 0:
            total += 1
    return total


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input4.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

