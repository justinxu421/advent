import numpy as np
import cmath
from collections import defaultdict

map_ = {'e': 0, 'ne': 60, 'nw': 120, 'w': 180, 'sw': 240, 'se': 300}
round_ = 2

hex_map = {
        'e': [2,0], 
        'se': [1,2], 
        'sw': [-1,2],
        'w': [-2,0], 
        'nw': [-1,-2], 
        'ne': [1, -2]
}

def flip_(a):
    tiles = defaultdict(int)
    
    for line in a:
        pos = np.array([0, 0])
        dir_ = ''
        for ch in line:
            #print(pos)
            dir_ += ch
            # parse and reset direction
            if ch == 'e' or ch == 'w':
                pos += np.array(hex_map[dir_])
                dir_ = ''
        
        pos = tuple(pos)
        tiles[pos] = 1 - tiles[pos]
    
    print(tiles)
    return tiles

memo = {}
def process(line):
    if line not in memo:
        pos = 0
        dir_ = ''
        for ch in line:
            #print(pos)
            dir_ += ch
            # reset direction
            if ch == 'e' or ch == 'w':
                angle = map_[dir_] / 180 * np.pi
                pos += complex(np.cos(angle), np.sin(angle))
                dir_ = ''
        pos = round(pos.real, round_) + round(pos.imag, round_) * 1j
        memo[line] = pos
    return memo[line]

def flip(a):
    tiles = {}
    
    for line in a:
        pos = process(line) 
        tiles[pos] = 1 - tiles.get(pos, (0,0))[0], line

    return tiles

def p1(a):
    tiles = flip_(a)
    return sum(x for x in tiles.values())
    #return sum(x[0] for x in tiles.values())

def get_neighbors(line):
    neighbors = []
    # loop through neighbors of tile
    for dir_ in map_:
        n_line = line + dir_
        pos = process(n_line)
        neighbors.append((pos, n_line))
    return neighbors

def count_neighbors(tiles, line):
    count = 0
    for n, n_line in get_neighbors(line):
        if tiles.get(n, (0,0))[0] == 1:
            count += 1
    return count

def p2(a):
    tiles = flip(a)
    
    for i in range(100):
        new_tiles = {}
        print(i, sum(x[0] for x in tiles.values()))
        
        # append missing tiles
        check = list(tiles.values())
        for color, line in check:
            for n, n_line in get_neighbors(line):
                if n not in tiles:
                    tiles[n] = (0, n_line)
        
        check = list(tiles.values())
        for color, line in check:
            tile = process(line)
            num = count_neighbors(tiles, line)
            if color == 1:
                if num == 0 or num > 2:
                    new_tiles[tile] = 0, line
                else:
                    new_tiles[tile] = 1, line
            if color == 0:
                if num == 2:
                    new_tiles[tile] = 1, line
                else:
                    new_tiles[tile] = 0, line

        tiles = new_tiles

    return sum(x[0] for x in tiles.values())

### insert how to parse line
def parse_line(line):
    return line.strip()

def main():
    #with open('input24.txt') as f:
    with open('test.txt') as f:
        a = [parse_line(line) for line in f] 

        print(f'part one: {p1(a)}')
        #print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
