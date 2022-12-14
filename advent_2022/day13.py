from collections import Counter, defaultdict
import functools
import numpy as np
import ast


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        if left > right:
            return False
        return None
    elif type(left) == list and type(right) == list:
        for i in range(max(len(right), len(left))):
            if i >= len(left):
                return True
            if i >= len(right):
                return False
            item_compare = compare(left[i], right[i])
            if item_compare is None:
                continue
            return item_compare
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(left) == list and type(right) == int:
        return compare(left, [right])


def p1(a):
    total = 0
    for i, lines in enumerate(a):
        left, right = lines.split("\n")
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        comparison = compare(left, right)
        if comparison:
            total += i + 1
    return total


def p2(a):
    d1, d2 = [[2]], [[6]]
    all_ = [d1, d2]
    for lines in a:
        left, right = lines.split("\n")
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        all_ += [left, right]

    left = all_[6]
    right = all_[1]

    def compare_(x, y):
        return -1 if compare(x, y) else 1

    sorted_all = sorted(all_, key=functools.cmp_to_key(compare_))
    sorted_list = list(map(str, sorted_all))
    return (sorted_list.index(str(d1)) + 1) * (sorted_list.index(str(d2)) + 1)


def run(file):
    with open(file) as f:
        a = [x.strip() for x in f.read().split("\n\n")]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input13.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

