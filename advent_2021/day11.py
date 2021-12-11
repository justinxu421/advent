from collections import Counter, defaultdict
import numpy as np


def flash_adj(a, i, j):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if (x, y) != (0, 0):
                i_, j_ = i + x, j + y
                if 0 <= i_ < len(a) and 0 <= j_ < len(a[0]):
                    a[i_, j_] += 1


def flash(a, flash_arr):
    flashed = False
    for i in range(len(a)):
        for j in range(len(a[0])):
            if flash_arr[i, j] == 0 and a[i, j] > 9:
                flash_adj(a, i, j)
                flash_arr[i, j] = True
                flashed = True
    return flashed


def run_step(a):
    not_done = True
    # increment
    a += 1
    flash_arr = np.zeros(a.shape, dtype=bool)
    while not_done:
        not_done = flash(a, flash_arr)
        # reset flashed ones
        a[flash_arr.astype(bool)] = 0
    # increment total flashes
    return flash_arr


def p1(a):
    a = np.array(a, dtype=int)
    return sum(run_step(a).sum() for _ in range(100))


def p2(a):
    a = np.array(a, dtype=int)
    step = 1
    while True:
        flash_arr = run_step(a)
        if (flash_arr == 0).sum() == 0:
            return step
        step += 1


def run(file):
    with open(file) as f:
        a = [list(x) for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input11.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
