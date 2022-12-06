from collections import Counter, defaultdict
import numpy as np


def get_item(x):
    half = len(x) // 2
    first, second = x[:half], x[half:]
    intersect = set(first) & set(second)
    item = intersect.pop()
    return item


def get_score(item):
    lower = ord(item) - ord("a") + 1
    upper = ord(item) - ord("A") + 1
    if lower > 0 and lower <= 26:
        return lower
    else:
        return upper + 26


def p1(a):
    total = 0
    for x in a:
        item = get_item(x)
        total += get_score(item)
    return total


def p2(a):
    total = 0
    while a:
        lines = a[:3]
        intersect = set(lines[0]) & set(lines[1]) & set(lines[2])
        item = intersect.pop()
        total += get_score(item)
        a = a[3:]

    return total


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input3.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

