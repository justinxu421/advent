from collections import Counter, defaultdict
import numpy as np
import heapq


def get_adj(a, i, j):
    adj = []
    for (x, y) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        i_, j_ = i + x, j + y
        if 0 <= i_ < len(a) and 0 <= j_ < len(a[0]):
            adj.append((i_, j_))
    return adj


def check_adj(a, i, j):
    return all(a[i_, j_] > a[i, j] for i_, j_ in get_adj(a, i, j))


def get_low_points(a):
    low_points = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if check_adj(a, i, j):
                low_points.append((i, j))
    return low_points


def p1(a):
    low_points = get_low_points(a)
    return sum(a[i, j] + 1 for i, j in low_points)


def p2(a):
    low_points = get_low_points(a)

    # run dijkstra's
    basin_sums = []
    for point in sorted(low_points, key=lambda x: a[x[0], x[1]], reverse=True):
        basin = {point}
        q = [point]

        while q:
            pi, pj = heapq.heappop(q)
            for i_, j_ in get_adj(a, pi, pj):
                if (
                    (i_, j_) not in basin
                    and a[i_, j_] != 9
                    and a[i_, j_] - a[pi, pj] >= 0
                ):
                    heapq.heappush(q, (i_, j_))
                    basin.add((i_, j_))

        basin_sums.append(len(basin))
    return np.prod(sorted(basin_sums, reverse=True)[:3])


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        a = np.array([list(map(int, list(x))) for x in a])
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input9.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
