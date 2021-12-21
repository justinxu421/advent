from collections import Counter, defaultdict
import numpy as np
from functools import cache


def p1(a):
    total_1, total_2 = 0, 0
    start_1, start_2 = a

    c = 0
    player = 1
    while max(total_1, total_2) < 1000:
        sum_ = (3 * c + 6) % 100
        c += 3
        if player == 1:
            start_1 = (start_1 + sum_ - 1) % 10 + 1
            total_1 += start_1
            player = 2
        else:
            start_2 = (start_2 + sum_ - 1) % 10 + 1
            total_2 += start_2
            player = 1

    print(total_1, total_2, c)
    return min(total_1, total_2) * c


@cache
def wins(total_1, total_2, start_1, start_2, player):
    if total_1 >= 21:
        return (1, 0)
    if total_2 >= 21:
        return (0, 1)

    total = (0, 0)
    for r1 in range(1, 4):
        for r2 in range(1, 4):
            for r3 in range(1, 4):
                sum_ = r1 + r2 + r3
                if player == 1:
                    score = (start_1 + sum_ - 1) % 10 + 1
                    new_total = wins(total_1 + score, total_2, score, start_2, 2)
                elif player == 2:
                    score = (start_2 + sum_ - 1) % 10 + 1
                    new_total = wins(total_1, total_2 + score, start_1, score, 1)
                total = (total[0] + new_total[0], total[1] + new_total[1])

    return total


def p2(a):
    start_1, start_2 = a
    total_wins = wins(0, 0, start_1, start_2, 1)

    w1, w2 = total_wins
    return max(w1, w2)


def run(a):
    print(f"Part 1: {p1(a)}")
    print(f"Part 2: {p2(a)}")


test_files = [[4, 8], [8, 1]]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
