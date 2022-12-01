import numpy as np


def p1(a):
    max = -1
    for x in a:
        cals = sum(list(map(int, x.split())))
        if cals > max:
            max = cals
    return max


def p2(a):
    all_cals = []
    for x in a:
        cals = sum(list(map(int, x.split())))
        all_cals.append(cals)

    top_3 = sorted(all_cals)[-3:]
    return sum(top_3)


def run(file):
    with open(file) as f:
        a = [x for x in f.read().split("\n\n")]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "input1.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
