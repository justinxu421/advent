from collections import Counter, defaultdict
import numpy as np

ROTATIONS = [
    "0,1,2",
    "0,-1,-2",
    "0,-2,1",
    "0,2,-1",
    "-0,2,1",
    "-0,-2,-1",
    "-0,-1,2",
    "-0,1,-2",
    "1,2,0",
    "1,-2,-0",
    "1,-0,2",
    "1,0,-2",
    "-1,0,2",
    "-1,-0,-2",
    "-1,2,-0",
    "-1,-2,0",
    "2,0,1",
    "2,-0,-1",
    "2,-1,0",
    "2,1,-0",
    "-2,1,0",
    "-2,-1,-0",
    "-2,0,-1",
    "-2,-0,1",
]


def rotate(v, rotation):
    a, b, c = rotation.split(",")
    tup = (
        v[abs(int(a))] * (-1 if a[0] == "-" else 1),
        v[abs(int(b))] * (-1 if b[0] == "-" else 1),
        v[abs(int(c))] * (-1 if c[0] == "-" else 1),
    )
    return tup


def get_diffs(beacons):
    arr = np.array(beacons)

    for x, y, z in beacons:
        pass


def check(beacons_i, all_beacons, scanners):
    for rotation in ROTATIONS:
        beacons = np.array([rotate(coords, rotation) for coords in beacons_i])
        for i in range(len(beacons)):
            for j in range(len(all_beacons)):
                offset = beacons[i] - list(all_beacons)[j]
                set_i = {tuple(coords) for coords in beacons - offset}
                intersect = set_i & all_beacons
                if len(intersect) >= 12:
                    # print(intersect)
                    print(len(intersect))
                    all_beacons |= set_i
                    return True, offset
    return False, None


def get_beacons_and_scanners(a):
    all_beacons = set()
    scanners = {0: (0, 0, 0)}

    # initialize the first
    beacons_0 = np.array([list(map(int, beacon.split(","))) for beacon in a[0][1:]])
    set_0 = {tuple(coords) for coords in beacons_0}
    all_beacons |= set_0

    remaining = a[1:]
    while remaining:
    # if remaining:
        scanner = remaining.pop(0)
        beacons_i = np.array(
            [list(map(int, beacon.split(","))) for beacon in scanner[1:]]
        )
        res, offset = check(beacons_i, all_beacons, scanners)
        if res == False:
            remaining.append(scanner)
        else:
            scanners[scanner[0]] = offset
            print(scanner[0], len(all_beacons))

    return all_beacons, scanners

def p1(all_beacons):
    return len(all_beacons)


def p2(all_scanners):
    max_dist, max_tuple = 0, None
    for scanner_1 in all_scanners.values():
        for scanner_2 in all_scanners.values():
            dist = np.abs(np.array(scanner_1) - np.array(scanner_2)).sum()
            if dist > max_dist:
                max_dist = dist
                max_tuple = (scanner_1, scanner_2)

    print(max_tuple)
    return max_dist


def run(file):
    with open(file) as f:
        a = [x.split("\n") for x in f.read().split("\n\n")]
        all_beacons, all_scanners = get_beacons_and_scanners(a)
        print(f"Part 1: {p1(all_beacons)}")
        print(f"Part 2: {p2(all_scanners)}")


test_files = [
    "test.txt",
    "input19.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
