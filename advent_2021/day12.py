from collections import Counter, defaultdict
import numpy as np


def p1(a):
    edges = defaultdict(list)
    for x, y in a:
        edges[x].append(y)
        edges[y].append(x)
    
    q = [['start']]
    
    all_paths = []
    while q:
        path = q.pop(0)
        cur = path[-1]
        if cur == 'end':
            all_paths.append(path)
        else:
            visited = [node for node in path if node.islower()]
            for node in edges[cur]:
                if node not in visited:
                    path_copy = path[:]
                    path_copy.append(node)
                    q.append(path_copy)
    
    return len(all_paths)



def p2(a):
    edges = defaultdict(list)
    for x, y in a:
        edges[x].append(y)
        edges[y].append(x)
    
    q = [['start']]
    
    all_paths = []
    while q:
        path = q.pop(0)
        cur = path[-1]
        if cur == 'end':
            all_paths.append(path)
        else:
            visited = Counter(node for node in path if node.islower())
            for node in edges[cur]:
                if node == 'start':
                    continue
                if node not in visited or (visited.most_common()[0][1] < 2):
                    path_copy = path[:]
                    path_copy.append(node)
                    q.append(path_copy)
    
    return len(all_paths)


def run(file):
    with open(file) as f:
        a = [x.split('-') for x in f.read().splitlines()]
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