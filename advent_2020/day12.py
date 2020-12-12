from collections import Counter, defaultdict
from utils import print_d

# generate DIRS
DIRS = [(i,j) for i in range(-1, 2) for j in range(-1,2) if (i,j) != (0,0)]
dir_map = {'N': 0, 'E': 1, 'S': 2, 'W':3}
dir_map_inv = {0:'N', 1:'E', 2:'S', 3:'W'}

def parse_dir(d_, num, i, j, d):
    if d_ == 'N':
        return i+num, j, d
    elif d_ == 'S':
        return i-num, j, d
    elif d_ == 'E':
        return i, j+num, d
    elif d_ == 'W':
        return i, j-num, d
    elif d_ == 'R':
        steps = num // 90
        new_dir = (dir_map[d] + steps) % 4
        return i, j, dir_map_inv[new_dir]
    elif d_ == 'L':
        steps = (360 - num) // 90
        new_dir = (dir_map[d] + steps) % 4
        return i, j, dir_map_inv[new_dir]
    elif d_ == 'F':
        return parse_dir(d, num, i, j, d)

def p1(a):
    d = 'E'
    i,j = 0,0
    for d_, num in a:
        i,j, d = parse_dir(d_, num, i, j, d)
    print(i,j)
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
    if d_ == 'N':
        return i, j, w1+num, w2
    elif d_ == 'S':
        return i, j, w1-num, w2
    elif d_ == 'E':
        return i, j, w1, w2+num
    elif d_ == 'W':
        return i, j, w1, w2-num
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
