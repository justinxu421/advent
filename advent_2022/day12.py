from collections import Counter, defaultdict
import numpy as np

def bfs(start, end, arr):
    arr[start[0]][start[1]] = chr(ord('a'))
    arr[end[0]][end[1]] = chr(ord('z'))
    # do bfs
    q = [(start[0], start[1], 0, None)]
    visited = set()
    while len(q) > 0:
        curr = q.pop(0)
        x, y, depth, prev = curr
        if x >= 0 and x < len(arr) and y >= 0 and y < len(arr[0]) and (x, y) not in visited:
            curr_val = ord(arr[x][y])
            if prev is None or curr_val - prev <= 1:
                # print(x, y, depth, chr(prev) if prev else "None", chr(curr_val))
                if (x,y) == end:
                    # print(arr[20][136], arr[20][137], arr[20][138])
                    return depth

                visited.add((x, y))
                q += [(x - 1, y, depth + 1, curr_val), (x + 1, y, depth + 1, curr_val), (x, y - 1, depth + 1, curr_val), (x, y + 1, depth + 1, curr_val)]
    return 999999

def p1(a):
    arr = [list(line) for line in a]
    
    start, end = None, None
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'S':
                start = (i,j)
            elif arr[i][j] == 'E':
                end = (i,j)
                
    arr[start[0]][start[1]] = chr(ord('a'))
    arr[end[0]][end[1]] = chr(ord('z'))
    return bfs(start, end, arr)


def p2(a):
    arr = [list(line) for line in a]
    
    starts = []
    start, end = None, None
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'a' or arr[i][j] == 'S':
                starts.append((i,j))
            if arr[i][j] == 'S':
                start = (i,j)
            elif arr[i][j] == 'E':
                end = (i,j)
                
    arr[start[0]][start[1]] = chr(ord('a'))
    arr[end[0]][end[1]] = chr(ord('z'))
    
    min_ = 99999
    for start in starts:
        min_ = min(min_, bfs(start, end, arr))
    return min_


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input12.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

