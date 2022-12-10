from collections import Counter, defaultdict
import numpy as np


def new_max(a, i, j, max, visible):
    tree = int(a[i][j])
    if tree > max:
        visible.add((i, j))
        max = tree
    return max


def p1(a):
    visible = set()

    rows, cols = len(a), len(a[0])
    for i in range(rows):
        max = -1
        for j in range(cols):
            max = new_max(a, i, j, max, visible)

    for i in range(rows):
        max = -1
        for j in range(cols)[::-1]:
            max = new_max(a, i, j, max, visible)

    for j in range(cols):
        max = -1
        for i in range(rows):
            max = new_max(a, i, j, max, visible)

    for j in range(cols):
        max = -1
        for i in range(rows)[::-1]:
            max = new_max(a, i, j, max, visible)

    return len(visible)


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def p2(a):
    max_score = 0
    rows, cols = len(a), len(a[0])
    for i in range(rows):
        for j in range(cols):
            tree = int(a[i][j])

            vision_score = 1
            for x, y in dirs:
                vision = 0
                i_, j_ = i + x, j + y
                while i_ >= 0 and i_ < rows and j_ >= 0 and j_ < cols:
                    vision += 1
                    new_tree = int(a[i_][j_])
                    if new_tree >= tree:
                        break
                    i_ += x
                    j_ += y
                vision_score *= vision
            max_score = max(vision_score, max_score)
    return max_score


def run(file):
    with open(file) as f:
        a = [list(x) for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input8.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

