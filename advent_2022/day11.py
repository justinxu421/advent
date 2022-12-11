from collections import Counter, defaultdict
import numpy as np
import math


def parse_items(line):
    item_string = line[1]
    return list(map(int, item_string.split("Starting items: ")[1].split(",")))


def parse_rules(line):
    operation, test, true_, false_ = line[2], line[3], line[4], line[5]
    operation = operation.split("Operation: new = ")[1]
    test = int(test.split("Test: divisible by ")[1])
    true_ = int(true_.split("If true: throw to monkey ")[1])
    false_ = int(false_.split("If false: throw to monkey ")[1])

    return operation, test, true_, false_


def run_round(a, d, item_counts):
    for i, line in enumerate(a):
        items = d[i]

        operation, test, true_, false_ = parse_rules(line)
        for item in items:
            item_counts[i] += 1
            op_str = operation.replace("old", str(item))
            worry = eval(op_str) // 3
            if worry % test == 0:
                d[true_].append(worry)
            else:
                d[false_].append(worry)
        d[i] = []


def p1(a):
    ## get starting items
    d = {}
    for i, line in enumerate(a):
        d[i] = parse_items(line)

    item_counts = Counter()
    for _ in range(20):
        run_round(a, d, item_counts)
    first, second = item_counts.most_common(2)
    return first[1] * second[1]


def run_round_2(a, d, rules, item_counts, lcm):
    for i in range(len(a)):
        items = d[i]
        operation, test, true_, false_ = rules[i]

        for item in items:
            item_counts[i] += 1
            op_str = operation.replace("old", str(item))
            worry = eval(op_str) % lcm
            if worry % test == 0:
                d[true_].append(worry)
            else:
                d[false_].append(worry)
        d[i] = []


def p2(a):
    ## get starting items
    d = {}
    for i, line in enumerate(a):
        d[i] = parse_items(line)

    divisors = []
    rules = {}
    for i, line in enumerate(a):
        operation, test, true_, false_ = parse_rules(line)
        rules[i] = (operation, test, true_, false_)
        divisors.append(test)

    lcm = math.lcm(*divisors)

    item_counts = Counter()
    for _ in range(10000):
        run_round_2(a, d, rules, item_counts, lcm)
    first, second = item_counts.most_common(2)
    return first[1] * second[1]


def run(file):
    with open(file) as f:
        a = [x.split("\n") for x in f.read().split("\n\n")]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input11.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

