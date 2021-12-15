from collections import Counter, defaultdict
import numpy as np
from functools import cache


def min_path(a):
    import heapq

    visited = set()
    start = [0, [(0, 0)]]
    visited.add((0, 0))

    pq = [start]
    min_ = float("inf")
    dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    while pq:
        total, path = heapq.heappop(pq)
        x, y = path[-1]
        if x == len(a) - 1 and y == len(a[0]) - 1 and total < min_:
            min_ = total

        for i, j in dirs:
            x_, y_ = x + i, y + j
            if (x_, y_) not in visited and 0 <= x_ < len(a) and 0 <= y_ < len(a[0]):
                path_copy = path[:]
                path_copy.append((x_, y_))
                visited.add((x_, y_))
                new_total = total + a[x_, y_]
                heapq.heappush(pq, (new_total, path_copy))

    return min_


def p1(a):
    a = np.array(a)
    return min_path(a)


def p2(a):
    a = np.array(a)
    rows, cols = a.shape
    a_big = np.zeros((rows * 5, cols * 5), dtype=int)
    for i in range(5):
        for j in range(5):
            new_a = a + i + j
            new_a[new_a > 9] -= 9
            a_big[i * rows : (i + 1) * rows, j * cols : (j + 1) * cols] = new_a

    return int(min_path(a_big))


def run(file):
    with open(file) as f:
        a = [list(map(int, list(x))) for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input15.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
