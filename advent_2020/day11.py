from collections import Counter, defaultdict
import copy

def count_neighbors(a, x, y):
    total = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                x_, y_ = x+i, y+j
                if 0 <= x_ < len(a) and 0 <= y_ < len(a[0]) and a[x_][y_] == '#':
                    total += 1
    return total

def count(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '#':
                count += 1
    return count

def p1(a):
    prev = None
   
    while prev != a:
        new_a = copy.deepcopy(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                n = count_neighbors(a, i, j)
                if a[i][j] == 'L' and n == 0:
                    new_a[i][j] = '#'
                elif a[i][j] == '#' and n >= 4:
                    new_a[i][j] = 'L'

        prev = a
        a = new_a
    
    return count(new_a), count(a)

def count_neighbors_2(a, x, y):
    total = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                x_, y_ = x+i, y+j
                # skip floor
                while 0 <= x_ < len(a) and 0 <= y_ < len(a[0]) and a[x_][y_] == '.':
                    x_, y_ = x_+i, y_+j
                if 0 <= x_ < len(a) and 0 <= y_ < len(a[0]) and a[x_][y_] == '#':
                    total += 1
    return total

def p2(a):
    prev = None
   
    while prev != a:
        new_a = copy.deepcopy(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                n = count_neighbors_2(a, i, j)
                if a[i][j] == 'L' and n == 0:
                    new_a[i][j] = '#'
                elif a[i][j] == '#' and n >= 5:
                    new_a[i][j] = 'L'

        prev = a
        a = new_a
    
    return count(new_a), count(a)

### insert how to parse line
def parse_line(line):
    return list(line.strip())

with open('input11.txt') as f:
    a = [parse_line(line) for line in f] 

    print(f'part one: {p1(a)}')
    print(f'part two: {p2(a)}')

