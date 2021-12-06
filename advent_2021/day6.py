from collections import Counter, defaultdict
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

def recurse(left, cache):
    orig = left
    if orig < 0:
        return 0
    elif orig in cache:
        return cache[orig]
    else:
        total = 1 + recurse(left - 9, cache)
        while left >= 7:
            left -= 7
            total += 1 + recurse(left - 9, cache)
        cache[orig] = total
        return cache[orig]

def p2(a):
    total = 0
    cache = {}
    for num in a:
        x = recurse(256 - num - 1, cache)
        total += 1 + x
    return total

def run(file):
    with open(file) as f:
        a = list(map(int, f.read().strip().split(',')))
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


print('Run test cases')
run("test.txt")
print('Run real cases')
run("input6.txt")
