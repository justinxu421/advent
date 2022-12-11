from collections import Counter, defaultdict
import numpy as np


def check_counter(counter, X, signal):
    if counter % 40 == 20:
        signal.append(counter * X)


def p1(a):
    X = 1

    counter = 0
    signal = []
    for line in a:
        if line[:4] == "noop":
            counter += 1
            check_counter(counter, X, signal)
        elif line[:4] == "addx":
            num = int(line[5:])
            counter += 1
            check_counter(counter, X, signal)

            counter += 1
            check_counter(counter, X, signal)
            X += num

    return sum(signal)


def check_counter_and_draw(counter, X, array):
    position = (counter - 1) % 40
    if position >= (X - 1) and position <= (X + 1):
        array[counter - 1] = "#"
    else:
        array[counter - 1] = "."


def p2(a):
    X = 1
    array = ["." for _ in range(240)]

    counter = 0
    for line in a:
        if line[:4] == "noop":
            counter += 1
            check_counter_and_draw(counter, X, array)
        elif line[:4] == "addx":
            num = int(line[5:])
            counter += 1
            check_counter_and_draw(counter, X, array)
            counter += 1
            check_counter_and_draw(counter, X, array)
            X += num

    for i in range(6):
        print("".join(array[i * 40 : (i + 1) * 40]))


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input10.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
