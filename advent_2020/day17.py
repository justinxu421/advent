from collections import Counter, defaultdict
from utils import print_d

def print_cube(cube, depth, w_l, w_h, h_l, h_h):
    for x in range(-depth, depth + 1):
        print(x)
        for y in range(w_l, w_h):
            r = ''
            for z in range(h_l, h_h):
                r += cube.get((x, y, z), '.')
            print(r)
        print()

def check_neighbors(cube, x, y, z):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (i,j,k) == (0,0,0):
                    continue
                x_, y_, z_ = x+i, y+j, z+k
                if cube.get((x_,y_,z_)) == '#':
                    total += 1
    return total

def p1(a):
    cube = {}
    
    w, h = len(a), len(a[0])

    for i in range(w):
        for j in range(h):
            cube[(0,i,j)] = a[i][j]

    depth = 1
    w_l, w_h = -1, w+1
    h_l, h_h = -1, h+1

    for i in range(6):
        new_cube = {}
        for x in range(-depth, depth + 1):
            for y in range(w_l, w_h):
                for z in range(h_l, h_h):
                    n = check_neighbors(cube, x, y, z)
                    if cube.get((x, y, z)) == '#':
                        if n in [2,3]:
                            new_cube[x,y,z] = '#'
                        else:
                            new_cube[x,y,z] = '.'
                    else:
                        if n == 3:
                            new_cube[x,y,z] = '#'
                        else:
                            new_cube[x,y,z] = '.'
        cube = new_cube
        # increment
        depth += 1
        w_l, w_h = w_l-1, w_h + 1
        h_l, h_h = h_l-1, h_h+1

    return sum(1 for v in cube.values() if v == '#')

def check_neighbors_4d(cube, w, x, y, z):
    total = 0
    for l in range(-1, 2):
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (l,i,j,k) == (0,0,0,0):
                        continue
                    w_, x_, y_, z_ = w+l, x+i, y+j, z+k
                    if cube.get((w_,x_,y_,z_)) == '#':
                        total += 1
    return total

def p2(a):
    cube = {}
    
    w, h = len(a), len(a[0])

    for i in range(w):
        for j in range(h):
            cube[(0,0,i,j)] = a[i][j]

    d1, d2 = 1, 1
    w_l, w_h = -1, w+1
    h_l, h_h = -1, h+1

    for i in range(6):
        new_cube = {}
        for w in range(-d1, d1+1):
            for x in range(-d2, d2+1):
                for y in range(w_l, w_h):
                    for z in range(h_l, h_h):
                        n = check_neighbors_4d(cube, w ,x, y, z)
                        if cube.get((w, x, y, z)) == '#':
                            if n in [2,3]:
                                new_cube[w,x,y,z] = '#'
                            else:
                                new_cube[w,x,y,z] = '.'
                        else:
                            if n == 3:
                                new_cube[w,x,y,z] = '#'
                            else:
                                new_cube[w,x,y,z] = '.'
        cube = new_cube
        # increment
        d1, d2 = d1+1, d2+1
        w_l, w_h = w_l-1, w_h + 1
        h_l, h_h = h_l-1, h_h+1

    return sum(1 for v in cube.values() if v == '#')

### insert how to parse line
def parse_line(line):
    return list(line.strip())

def main():
    with open('input17.txt') as f:
    #with open('test.txt') as f:
        a = [parse_line(line) for line in f]
        print(a[:10])

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
