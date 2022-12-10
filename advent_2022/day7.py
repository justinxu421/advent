from collections import Counter, defaultdict
import numpy as np

max = 100000


def handle_ls(a, i, dirs, cur):
    while i < len(a) and a[i][0] != "$":
        line = a[i]
        term1, term2 = line.split()
        if term1 == "dir":  # directory / name
            if term2 not in cur:
                cur[term2] = {}
        else:  # size / filename
            cur[term2] = int(term1)
        i += 1
    return i


def get_dirs(a):
    i = 0
    dirs = {}
    # pointers
    cur = dirs
    while i < len(a):
        line = a[i]
        if line[0] == "$":
            command = line[2:]
            if command[:2] == "cd":
                dir = command[3:]
                if dir == "/":  # home
                    cur = dirs
                elif dir == "..":  # up one
                    cur = cur[".."]
                else:  # subdir
                    if dir not in cur:
                        cur[dir] = {}
                    cur[dir][".."] = cur
                    cur = cur[dir]
            elif command[:2] == "ls":
                i = handle_ls(a, i + 1, dirs, cur)
                continue
        i += 1
    return dirs


def parse_dirs(dirs, dir, dir_sizes):
    total = 0
    for key in dirs:
        if key != "..":
            sub = dirs[key]
            if type(sub) == dict:
                total += parse_dirs(sub, dir + "/" + key, dir_sizes)
            else:
                total += sub
    dir_sizes[dir] = total
    return dir_sizes[dir]


def p1(a):
    dirs = get_dirs(a)
    dir_sizes = {}
    parse_dirs(dirs, "/", dir_sizes)

    total = 0
    for v in dir_sizes.values():
        if v <= max:
            total += v
    return total


def p2(a):
    space = 70000000
    unused = 30000000

    dirs = get_dirs(a)
    dir_sizes = {}
    parse_dirs(dirs, "/", dir_sizes)

    sorted_dirs = sorted(dir_sizes.items(), key=lambda x: x[1])

    for dir in sorted_dirs:
        if (dir_sizes["/"] - dir[1]) < (space - unused):
            return dir[1]


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input7.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

