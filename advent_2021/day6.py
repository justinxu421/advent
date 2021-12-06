from collections import Counter, defaultdict
from functools import cache
import numpy as np

def p1(a):
    timers = np.array(a)
    for i in range(80):
        timers -= 1
        zeros = timers == -1
        if zeros.sum() > 0:
            timers[zeros] = 6
            timers = np.concatenate((timers, np.array([8] * zeros.sum())))
    return len(timers)

@cache
def recurse(left):
    orig = left
    if orig < 0:
        return 0
    else:
        total = 1 + recurse(left - 9)
        while left >= 7:
            left -= 7
            total += 1 + recurse(left - 9)
        return total

def p2(a):
    total = 0
    for num in a:
        x = recurse(256 - num - 1)
        total += 1 + x
    return total

def p2b(a):
    fish_counts = Counter(a)
    for _ in range(256):
        new_counts = Counter()
        for timer, count in fish_counts.items():
            if timer == 0:
                new_counts[6] += count
                new_counts[8] += count
            else:
                new_counts[timer - 1] += count
        fish_counts = new_counts
    return sum(fish_counts.values())

def p2c(a):
    fish_counts = np.zeros(9)
    for num in a:
        fish_counts[num] += 1

    for _ in range(256):
        zeros = fish_counts[0]
        fish_counts = np.append(fish_counts[1:], 0)
        fish_counts[6] += zeros
        fish_counts[8] += zeros
    return int(fish_counts.sum())

def run(file):
    with open(file) as f:
        a = list(map(int, f.read().strip().split(',')))
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")
        print(f"Part 2 better: {p2b(a)}")
        print(f"Part 2 cetter: {p2c(a)}")


print('Run test cases')
run("test.txt")
print('Run real cases')
run("input6.txt")
