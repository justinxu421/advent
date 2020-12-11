from collections import Counter, defaultdict
from utils import print_d

# generate DIRS
DIRS = [(i,j) for i in range(-1, 2) for j in range(-1,2) if (i,j) != (0,0)]

def count(d):
    return sum(1 for x in d.values() if x == '#')

def count_neighbors(d, x, y):
    return sum(1 for i,j in DIRS if d.get((x+i,y+j), 0) == '#')

def next_iter(d, count_neighbors, m_):
    new_d = {}

    for (x,y), v in d.items():
        n = count_neighbors(d, x, y)
        if v == 'L' and n == 0:
            new_d[(x,y)] = '#'
        elif v == '#' and n >= m_:
            new_d[(x,y)] = 'L'
        else:
            new_d[(x,y)] = v

    return new_d

def p1(d):
    while True:
        new_d = next_iter(d, count_neighbors, 4)

        if new_d == d:
            break
        d = new_d
    
    return count(new_d)

def count_neighbors_2(d, x, y):
    total = 0
    for i,j in DIRS:
        x_, y_ = x+i, y+j

        # skip floors
        while d.get((x_,y_), 0) == '.':
            x_ += i
            y_ += j

        if d.get((x_,y_), 0) == '#':
            total += 1

    return total

def p2(d):
    while True:
        new_d = next_iter(d, count_neighbors_2, 5)

        if new_d == d:
            break
        d = new_d
    
    return count(new_d)

def gen_dict(a):
    d = {}
    for i in range(len(a)):
        for j in range(len(a[0])):
            d[i,j] = a[i][j]
    return d

### insert how to parse line
def parse_line(line):
    return list(line.strip())

def main():
    with open('input11.txt') as f:
        a = [parse_line(line) for line in f] 
        a = gen_dict(a)
        print_d(a)

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
