import numpy as np
from collections import defaultdict

hex_map = {
        'e': [2,0], 
        'se': [1,2], 
        'sw': [-1,2],
        'w': [-2,0], 
        'nw': [-1,-2], 
        'ne': [1, -2]
}

def flip(a):
    tiles = set()
    
    for line in a:
        pos = np.array([0, 0])
        dir_ = ''
        for ch in line:
            dir_ += ch
            # parse and reset direction
            if ch == 'e' or ch == 'w':
                pos += np.array(hex_map[dir_])
                dir_ = ''
        
        pos = tuple(pos)
        if pos in tiles:
            tiles.remove(pos)
        else:
            tiles.add(pos)
    
    return tiles

def p1(a):
    tiles = flip(a)
    return len(tiles)
    return sum(tiles.values())

def get_neighbors(pos):
    neighbors = []
    # loop through neighbors of tile
    for x in hex_map.values():
        n_pos = tuple(pos + np.array(x))
        neighbors.append(n_pos)
    return neighbors

def count_neighbors(tiles, pos):
    return sum(1 for n in get_neighbors(pos) if n in tiles)

def add_neighbors(tiles):
    # append missing adjacent tiles
    #keys = list(tiles.keys())
    whites = []
    for pos in tiles:
        for n in get_neighbors(pos):
            if n not in tiles:
                whites.append(n)
    return whites

def p2(a):
    tiles = flip(a)
    
    for i in range(100):
        new_black, new_white = set(), set()

        if i % 10 == 0:
            print(i, len(tiles))
        
        # loop through these tiles
        whites = add_neighbors(tiles)
        for pos in tiles:
            num = count_neighbors(tiles, pos)
            if num == 0 or num > 2:
                new_white.add(pos)
        for pos in whites:
            num = count_neighbors(tiles, pos)
            if num == 2:
                new_black.add(pos)

        tiles -= new_white
        tiles |= new_black

    return len(tiles)

### insert how to parse line
def parse_line(line):
    return line.strip()

def main():
    with open('input24.txt') as f:
        a = [parse_line(line) for line in f] 

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
