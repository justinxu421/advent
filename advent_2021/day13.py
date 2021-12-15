from collections import Counter, defaultdict
import numpy as np
from utils import *

def process_flip(paper, fold):
    new_points = set()
    f = fold.split('fold along ')[1].split('=')
    dir_, num = f
    num = int(num)

    if dir_ == 'y':
        for x, y in paper:
            if y > num:
                y = num - (y - num)
            new_points.add((x,y))
    elif dir_ == 'x':
        for x, y in paper:
            if x > num:
                x = num - (x - num)
            new_points.add((x,y))
    return new_points

def p1(a, b):
    paper = set()
    for x,y in a:
        paper.add((x,y))
    
    fold = b[0]
    paper = process_flip(paper, fold)
    return len(paper)
    

def p2(a, b):
    paper = set()
    for x,y in a:
        paper.add((x,y))
    
    for fold in b:
        paper = process_flip(paper, fold)

    print_grid(paper, transpose = False)


def run(file):
    with open(file) as f:
        x, y = f.read().split('\n\n')
        a = [list(map(int, (x_.split(',')))) for x_ in x.split('\n')]
        b = y.strip().split('\n')
        print(f"Part 1: {p1(a, b)}")
        print(f"Part 2: {p2(a, b)}")


test_files = [
    "test.txt",
    "input13.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()