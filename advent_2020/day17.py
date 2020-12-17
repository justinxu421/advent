def print_cube(cube, depth, w, h):
    for x in range(-depth, depth + 1):
        print(x)
        for y in range(-depth, w + depth + 1):
            r = ''
            for z in range(-b, h + depth + 1):
                r += cube.get((x, y, z), '.')
            print(r)
        print()

def check_neighbors(cube, coord):
    x,y,z = coord
    coords = [(a,b,c) for a in range(-1, 2) for b in range(-1, 2) for c in range(-1, 2) if (a,b,c) != (0,0,0)]
    return sum(1 for a,b,c in coords if cube.get((x+a,y+b,z+c)) == '#')

def get_next(cube, coord, cn):
    n = cn(cube, coord)
    if cube.get(coord) == '#':
        if n in [2,3]:
            return '#'
        else:
            return '.'
    else:
        if n == 3:
            return '#'
        else:
            return '.'

def p1(a):
    cube = {}
    
    w_, h_ = len(a), len(a[0])
    for i in range(w_):
        for j in range(h_):
            cube[(0,i,j)] = a[i][j]

    for depth in range(1,7):
        new_cube = {}
        for x in range(-depth, depth + 1):
            for y in range(-depth, w_ + depth):
                for z in range(-depth, h_ + depth):
                    new_cube[x,y,z] = get_next(cube, (x,y,z), check_neighbors)
        cube = new_cube

    return sum(1 for v in cube.values() if v == '#')

def check_neighbors_4d(cube, coord):
    w,x,y,z = coord
    coords = [(a,b,c,d) for a in range(-1, 2) for b in range(-1, 2) for c in range(-1, 2) for d in range(-1, 2) if (a,b,c,d) != (0,0,0,0)]
    return sum(1 for a,b,c,d in coords if cube.get((w+a,x+b,y+c,z+d)) == '#')

def p2(arr):
    cube = {}
    
    w_, h_ = len(arr), len(arr[0])
    for i in range(w_):
        for j in range(h_):
            cube[(0,0,i,j)] = arr[i][j]

    for d in range(1, 7):
        new_cube = {}
        for w in range(-d, d+1):
            for x in range(-d, d+1):
                for y in range(-d, w_+d):
                    for z in range(-d, h_+d):
                        new_cube[w,x,y,z] = get_next(cube, (w,x,y,z), check_neighbors_4d)
        cube = new_cube

    return sum(1 for v in cube.values() if v == '#')

### insert how to parse line
def parse_line(line):
    return list(line.strip())

def main():
    with open('input17.txt') as f:
        arr = [parse_line(line) for line in f]

        print(f'part one: {p1(arr)}')
        print(f'part two: {p2(arr)}')

if __name__ == "__main__":
    main()
