from collections import Counter, defaultdict
import numpy as np

def get_adj(a, i, j):
    adj = []
    for (x, y) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        i_, j_ = i + x, j + y
        if ( 
            0 <= i_ < len(a) 
            and 0 <= j_ < len(a[0]) 
        ):
            adj.append((i_, j_))
    return adj
    
def check_adj(a, i, j):  # sourcery skip: merge-nested-ifs
    return all(a[i_, j_] > a[i, j] for i_, j_ in get_adj(a, i, j))
                

def p1(a):
    low_points = []

    for i in range(len(a)):
        for j in range(len(a[0])):
            if check_adj(a, i, j):
                low_points.append(a[i, j] + 1)
    return sum(low_points) 


def p2(a):
    low_points = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if check_adj(a, i, j):
                low_points.append((i, j))

    # run dijkstra's
    import heapq
    basin_points = {}
    mask = np.ones(a.shape, dtype=bool)

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i,j] == 9:
                mask[i,j] = 0

    for idx, point in enumerate(sorted(low_points, key = lambda x: -a[x[0], x[1]])):
        basin = {point}
        q = [point] 

        while q:
            pi, pj = heapq.heappop(q)
            for i_, j_ in get_adj(a, pi, pj): 
                if (i_, j_) not in basin and a[i_, j_] != 9 and a[i_, j_] - a[pi, pj] >= 0:
                    heapq.heappush(q, (i_, j_))
                    basin.add((i_, j_))

            for i, j in basin:
                mask[i, j] = False
        basin_points[idx] = basin

    # print(sorted(basin_sums.values(), key = lambda x: len(x), reverse = True))
    basin_sums = list(map(lambda x: len(x), basin_points.values()))
    total = sum(basin_sums) + (a==9).sum()

    return np.prod(sorted(basin_sums, reverse = True)[:3])



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