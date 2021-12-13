from collections import Counter, defaultdict
import numpy as np

def process_flip(paper, fold):
    new_points = {}
    f = fold.split('fold along ')[1].split('=')
    dir_, num = f
    num = int(num)

    if dir_ == 'y':
        for x, y in paper:
            if y > num:
                y_ = num - (y - num)
                new_points[(x,y_)] = '#'
            else:
                new_points[(x,y)] = '#'
    elif dir_ == 'x':
        for x, y in paper:
            if x > num:
                x_ = num - (x - num)
                new_points[(x_,y)] = '#'
            else:
                new_points[(x,y)] = '#'
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

    paper_grid = {(y,x): '#' for (x,y) in paper}
    def print_grid(grid):
        rows = [x[0] for x in grid]
        cols = [x[1] for x in grid]
        min_col, max_col = min(cols), max(cols)
        min_row, max_row = min(rows), max(rows)

        for row in range(min(rows), max(rows)+1):
            r_str = [' ']*(max_col-min_col+1)
            for point in grid:
                if point[0] == row:
                    r_str[point[1] - min_col] = str(grid[point])
            print(''.join(r_str))
    
    print_grid(paper_grid)


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