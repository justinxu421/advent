from collections import Counter, defaultdict
import numpy as np
import copy


def step(a):
    new_a = copy.deepcopy(a)

    shift_right = np.roll(a, -1, axis=1)
    match = (a == ">") & (shift_right == ".")
    new_a[match] = "."
    new_a[np.roll(match, 1, axis=1)] = ">"
    a = new_a
    # print(a)

    new_a = copy.deepcopy(a)
    shift_down = np.roll(a, -1, axis=0)
    match = (a == "v") & (shift_down == ".")
    new_a[match] = "."
    new_a[np.roll(match, 1, axis=0)] = "v"
    # print(new_a)

    return new_a


def p1(a):
    old_a = None

    i = 0
    while (old_a != a).any():
        # print(i, a)
        old_a = a
        a = step(a)
        i += 1

    return i


def p2(a):
    pass


def run(file):
    with open(file) as f:
        a = [list(x) for x in f.read().splitlines()]
        a = np.array(a)
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input25.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
