from collections import Counter, defaultdict
import numpy as np


def make_rock(a):
    rock = np.full((1000, 1000), ".")

    highest = 0
    for line in a:
        cur = None
        for step in line:
            x, y = list(map(int, step.split(",")))
            highest = max(y, highest)
            if cur is not None:
                x0, y0 = cur
                if x0 == x:
                    for i in range(min(y0, y), max(y0, y) + 1):
                        rock[x0, i] = "#"
                        pass
                if y0 == y:
                    for i in range(min(x0, x), max(x0, x) + 1):
                        rock[i, y0] = "#"
            cur = (x, y)
    return rock, highest


def p1(a):
    start = (500, 0)
    rock, _ = make_rock(a)

    flag = True
    units = 0
    while flag:
        i, j = start
        try:
            while True:
                # down
                if rock[i, j + 1] == ".":
                    j += 1
                # down left
                elif rock[i - 1, j + 1] == ".":
                    i -= 1
                    j += 1
                # down right
                elif rock[i + 1, j + 1] == ".":
                    i += 1
                    j += 1
                else:
                    rock[i, j] = "o"
                    units += 1
                    break
        except:
            flag = False

    return units


def p2(a):
    start = (500, 0)
    rock, highest = make_rock(a)
    floor = highest + 2

    flag = True
    units = 0
    while flag:
        i, j = start
        while True:
            # down
            if j == floor - 1:
                rock[i, j] = "o"
                units += 1
                break
            elif rock[i, j + 1] == ".":
                j += 1
            # down left
            elif rock[i - 1, j + 1] == ".":
                i -= 1
                j += 1
            # down right
            elif rock[i + 1, j + 1] == ".":
                i += 1
                j += 1
            else:
                if (i, j) == (500, 0):
                    return units
                rock[i, j] = "o"
                units += 1
                break

    return units


def run(file):
    with open(file) as f:
        a = [x.split(" -> ") for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input14.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

