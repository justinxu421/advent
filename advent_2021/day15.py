from collections import Counter, defaultdict
import numpy as np
from functools import cache

def min_path(a):
    import heapq
    visited = set()
    start = [0, [(0,0)]]
    visited.add((0,0))

    pq = [start]
    min_ = float('inf')
    dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    while pq:
        total, path = heapq.heappop(pq)
        x, y = path[-1]
        if x == len(a)-1 and y == len(a[0])-1 and total < min_:
            min_ = total
        
        for i, j in dirs: 
            x_, y_ = x+i, y+j
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
    a_big = np.zeros((a.shape[0]*5, a.shape[1]*5))
    for i in range(5):
        for j in range(5):
            for x in range(a.shape[0]):
                for y in range(a.shape[1]):
                    val = a[x,y] + i + j
                    if val >= 10:
                        val -= 9
                    big_x, big_y = a.shape[0] * i + x, a.shape[1] * j + y
                    a_big[big_x, big_y] = val
                            
    return min_path(a_big)

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