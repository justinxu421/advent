from collections import Counter, defaultdict
from utils import print_d
import numpy as np


# rotate 90 degrees clockwise
def rotate(arr, num):
    l = [list(a) for a in arr.split('\n')]
    for _ in range(num):
        l = list(zip(*l[::-1]))
    return '\n'.join([''.join(a) for a in l])

# flip
def flip(arr):
    l = [list(a) for a in arr.split('\n')]
    l = [x[::-1] for x in l]
    return '\n'.join([''.join(a) for a in l])

# generate a string array from the raw string
def get_arr_from_str(arr):
    return [list(a) for a in arr.split('\n')]

# get the strings for the 4 edges
def get_edges(arr_str):
    arr = arr_str.split('\n')
    left = ''.join([x[0] for x in arr])
    right = ''.join([x[-1] for x in arr])
    top, bot  = arr[0], arr[-1]
    return left, top, right, bot

# get dict {tile_num: [left, top, right, bot]}
def get_edge_dict(a):
    d = {}
    for tile, arr in a:
        tile_num = int(tile.split()[1])
        arr_str = '\n'.join(arr)
        #left, top, right, bot = get_edges(arr_str)
        #d[tile_num] = (left, top, right, bot, arr_str)
        d[tile_num] = arr_str
    return d

# find the corners (tiles that match only 2 of its edges)
def find_corners(d):
    matches = defaultdict(list)
    match_nums = {}

    for tile_num in d:
        count = 0
        for i, edge in enumerate(get_edges(d[tile_num])):
            for t2 in d:
                # skip self
                if t2 == tile_num:
                    continue
                for j, edge2 in enumerate(get_edges(d[t2])):
                    if edge2 == edge:
                        matches[tile_num].append((t2, i, j, 1))
                        count += 1
                    elif edge2[::-1] == edge:
                        matches[tile_num].append((t2, i, j, 2))
                        count += 1
        match_nums[tile_num] = count

    corners = [num for num, count in match_nums.items() if count == 2]
    return corners, [matches[corner] for corner in corners] 

# try all rotations and flips
def orient(start, arr, idx1, idx2):
    for j in range(4):
        new_arr = rotate(arr, j)
        if get_edges(start)[idx1] == get_edges(new_arr)[idx2]:
            return new_arr

        new_arr = flip(new_arr)
        if get_edges(start)[idx1] == get_edges(new_arr)[idx2]:
            return new_arr

# find matches by trying all orientations
def find_match(start, d, tile_num, idx1, idx2):
    edges = get_edges(start)
    for t2 in d:
        if t2 == tile_num:
            continue
        for j, edge2 in enumerate(get_edges(d[t2])):
            if edge2 == edges[idx1] or edge2[::-1] == edges[idx1]:
                return orient(start, d[t2], idx1, idx2), t2

# generate array and save it as a numpy file
def save_array(corners, d):
    tile_num = corners[0]
    parsed = set()
    parsed.add(tile_num)
    
    # rotrate 90 degrees 3 times clockwise in order to align corner to top left
    # check which edges match to see how to rotate
    start = rotate(d[tile_num], 3)
    all_tiles = np.empty((120, 120), dtype = object)
    all_tiles[:10,:10] = get_arr_from_str(start)
    prev_row, prev_tile = start, tile_num
    
    # loop through the 12 by 12 array to generate the map
    for i in range(12):
        # get match for next row, must match top
        if i != 0:
            start, tile_num = find_match(prev_row, d, prev_tile, 3, 1)
            prev_row, prev_tile = start, tile_num
            all_tiles[10*i:10*i+10, :10] = get_arr_from_str(start)
        # get match to the right
        for j in range(1, 12):
            start, tile_num = find_match(start, d, tile_num, 2, 0)
            all_tiles[10*i:10*i+10, 10*j:10*j+10] = get_arr_from_str(start)
    np.save('text_20.npy', all_tiles.astype('str'))

def p1(a):
    d = get_edge_dict(a)
    corners, matches = find_corners(d)
    print(corners, matches)
    
    # save the array in the orientation for part 2
    save_array(corners, d)

    # multiply corner indices together
    total = 1
    for corner in corners:
        total *= corner
    return total

# remove the borders by taking 8x8 square of each tile
def remove_borders(all_tiles):
    remove = [10*i for i in range(12)] + [10*i+9 for i in range(12)]
    all_tiles = np.delete(all_tiles, remove, 0)
    all_tiles = np.delete(all_tiles, remove, 1)
    return all_tiles

# pattern for monster
pattern = '''                  #
#    ##    ##    ###
 #  #  #  #  #  #'''

# check if monster at this offset
def check_monster(new_tiles, x, y, pattern_idx):
    for i,j in pattern_idx:
        x_, y_ = x+i, y+j
        if new_tiles[x_, y_] != '#':
            return False
    return True

# loop all offsets for monsters
def search_monster(new_tiles, pattern_idx):
    monsters = []
    for x in range(new_tiles.shape[0] - 3):
        for y in range(new_tiles.shape[1] - 19):
            if check_monster(new_tiles, x, y, pattern_idx):
                monsters.append((x, y))
    return monsters

def p2(a):
    all_tiles = np.load('text_20.npy')
    new_tiles = remove_borders(all_tiles)
   
    # indices that the monster is at
    pattern_idx = []
    for i, line in enumerate(pattern.split('\n')):
        print(line)
        for j in range(len(line)):
            if line[j] == '#':
                pattern_idx.append((i,j))

    # try all orientations and search for monsters
    # break early if we found it
    for i in range(4):
        tiles = np.rot90(new_tiles, i)
        monsters = search_monster(tiles, pattern_idx)
        if len(monsters) != 0: break
        monsters = search_monster(np.flip(tiles, 0), pattern_idx)
        if len(monsters) != 0: break
        monsters = search_monster(np.flip(tiles, 1), pattern_idx)
        if len(monsters) != 0: break
    
    # return number of remaining '#' characters
    return sum(sum(tiles == '#')) - len(monsters) * len(pattern_idx)

### insert how to parse line
def parse_line(line):
    a, b = line.strip().split(':\n')
    return a.strip(), b.split('\n')

def main():
    with open('input20.txt') as f:
        lines = f.read().split('\n\n')
        a = [parse_line(line) for line in lines] 

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
