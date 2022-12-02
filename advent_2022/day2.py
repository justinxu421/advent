from collections import Counter, defaultdict
import numpy as np

win_map = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
draw = {"A": "X", "B": "Y", "C": "Z"}

point_map = {"X": 1, "Y": 2, "Z": 3}


def p1(a):
    points = 0
    for x in a:
        elf, me = x.split()
        points += point_map[me]
        if win_map[elf] == me:
            points += 6
        elif draw[elf] == me:
            points += 3
    return points


def p2(a):
    points = 0
    for x in a:
        elf, s_ = x.split()

        # 0/1/2
        p1 = ord(elf) - ord("A")
        # -1/0/1
        state = ord(s_) - ord("X") - 1

        # lose
        if state == -1:
            p2 = (p1 - 1) % 3
        if state == 0:
            p2 = p1
        if state == 1:
            p2 = (p1 + 1) % 3
        me = chr(p2 + ord("X"))

        points += point_map[me]
        if state == 1:
            points += 6
        elif state == 0:
            points += 3
    return points

    pass


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input2.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

