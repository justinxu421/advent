from collections import Counter, defaultdict
import numpy as np


def p1(a):
    min_x, min_y, min_z = -50, -50, -50
    cubes = np.zeros((101, 101, 101))

    for x in a:
        direction, res = x
        ranges = [list(map(int, y[2:].split(".."))) for y in res.split(",")]
        x_, y_, z_ = ranges

        lx, rx = x_
        ly, ry = y_
        lz, rz = z_

        if direction == "on":
            write = 1
        elif direction == "off":
            write = 0

        cubes[
            lx - min_x : rx + 1 - min_x,
            ly - min_y : ry + 1 - min_y,
            lz - min_z : rz + 1 - min_z,
        ] = write

    return cubes.astype(int).sum()


def get_intersection(range_1, range_2):
    (x1, y1, z1) = range_1
    (x2, y2, z2) = range_2

    def intersect_segments(a, b):
        if b[0] > a[1] or a[0] > b[1]:
            return False
        else:
            return (max(a[0], b[0]), min(a[1], b[1]))

    x_int = intersect_segments(x1, x2)
    y_int = intersect_segments(y1, y2)
    z_int = intersect_segments(z1, z2)
    if x_int and y_int and z_int:
        return (x_int, y_int, z_int)


def get_vol(range_):
    x, y, z = range_
    return (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)


def p2(a):
    all_ranges = []
    for x in a:
        direction, res = x
        ranges = tuple([tuple(map(int, y[2:].split(".."))) for y in res.split(",")])
        all_ranges.append((direction, ranges))

    # find intersection with existing
    # have key be 1 if include, 0 if exclude
    range_tuples = []
    for direction, ranges in all_ranges:
        new_keys = []
        for range_exist, v in range_tuples:
            int_ = get_intersection(range_exist, ranges)
            if int_:
                # 1 to -1, -1 to 1
                new_keys.append((int_, -v))
        range_tuples += new_keys

        # if on just add it in the include
        if direction == "on":
            range_tuples.append((ranges, 1))

    return sum(get_vol(range_) * v for range_, v in range_tuples)


def run(file):
    with open(file) as f:
        a = [x.split() for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test2.txt",
    "test.txt",
    "input22.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
