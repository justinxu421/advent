from collections import Counter, defaultdict
import numpy as np

def get_y(vt, t):
    return (vt + (vt - t)) / 2 * t


def p1(a):
    x, y = a.split(',')
    y_min, y_max = map(int, y[3:].split('..'))
    return int((abs(y_min) - 1) * abs(y_min) / 2)


def check(xv, yv, x_min, x_max, y_min, y_max):
    x, y = 0, 0
    while x <= x_max + 1 and y >= y_min + 1:
        x += xv
        y += yv
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True 

        if xv > 0: xv -= 1
        elif xv < 0: xv += 1
        yv -= 1

    return False

    
def p2(a):
    x, y = a.split(',')
    x_min, x_max = map(int, x[2:].split('..'))
    y_min, y_max = map(int, y[3:].split('..'))


    x_ = int(np.sqrt(2 * x_min))
    y_ = int((abs(y_min) - 1) * abs(y_min) / 2)
    total = 0
    for xv in range(x_, x_max + 1):
        for yv in range(y_min, y_):
            if check(xv, yv, x_min, x_max, y_min, y_max):
                total += 1
    return total 

def run(file):
    with open(file) as f:
        a = f.read().split('target area: ')[1]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input17.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()