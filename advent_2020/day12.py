from collections import Counter, defaultdict
from utils import print_d

dir_map = {'N': 0, 'E': 1, 'S': 2, 'W':3}
#dir_map_inv = {0:'N', 1:'E', 2:'S', 3:'W'}

def move_dir(i, j, d, num):
    m_ = [(1,0), (0,1), (-1,0), (0,-1)]
    return i + num * m_[d][0], j + num * m_[d][1]

def parse_dir(d_, num, i, j, d):
    if d_ in ['N', 'E', 'S', 'W']:
        i_, j_ = move_dir(i, j, dir_map[d_], num)
        return i_, j_, d
    elif d_ == 'R':
        steps = num // 90
        new_dir = (d + steps) % 4
        return i, j, new_dir
    elif d_ == 'L':
        steps = (360 - num) // 90
        new_dir = (d + steps) % 4
        return i, j, new_dir
    elif d_ == 'F':
        i_, j_ = move_dir(i, j, d, num)
        return i_, j_, d

def p1(a):
    d = 1 # East
    i,j = 0,0
    for d_, num in a:
        i,j, d = parse_dir(d_, num, i, j, d)
    return abs(i) + abs(j)

def rotate_way(w1, w2, steps):
    if steps == 0:
        return w1, w2
    elif steps == 1:
        return -w2, w1
    elif steps == 2:
        return -w1, -w2
    elif steps == 3:
        return w2, -w1

def parse_dir_2(d_, num, i, j, w1, w2):
    if d_ in ['N', 'E', 'S', 'W']:
        w1_, w2_ = move_dir(w1, w2, dir_map[d_], num)
        return i, j, w1_, w2_
    elif d_ == 'R':
        steps = num // 90
        new_w1, new_w2 = rotate_way(w1, w2, steps)
        return i, j, new_w1, new_w2
    elif d_ == 'L':
        steps = (360 - num) // 90
        new_w1, new_w2 = rotate_way(w1, w2, steps)
        return i, j, new_w1, new_w2
    elif d_ == 'F':
        return i + w1 * num, j + w2 * num, w1, w2

def p2(a):
    w1, w2 = 1, 10

    d = 'E'
    i,j = 0,0
    for d_, num in a:
        i,j, w1,w2  = parse_dir_2(d_, num, i, j, w1, w2)
    return abs(i) + abs(j)

### insert how to parse line
def parse_line(line):
    return line[0], int(line.strip()[1:])

def main():
    with open('input12.txt') as f:
        a = [parse_line(line) for line in f] 
        print(a[:10])

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
