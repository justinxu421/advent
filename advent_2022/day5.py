from collections import Counter, defaultdict
import numpy as np


def parse_crates(crates):
    stacks = {}
    rows = []
    n = 4
    for line in crates.split("\n")[:-1]:
        parsed = [line[i + 1 : i + n - 2] for i in range(0, len(line), n)]
        rows.append(parsed)

    for col in range(len(rows[0])):
        stacks[col + 1] = []
        for row in rows[::-1]:
            if row[col] != " ":
                stacks[col + 1].append(row[col])
    return stacks


def p1(crates, steps):
    stacks = parse_crates(crates)
    for step in steps.split("\n"):
        try:
            arr = step.split(" ")
            num, stack1, stack2 = arr[1], arr[3], arr[5]
            for _ in range(int(num)):
                top = stacks[int(stack1)].pop()
                stacks[int(stack2)].append(top)
        except:
            pass
    return "".join([stack[-1] for stack in stacks.values()])


def p2(crates, steps):
    stacks = parse_crates(crates)
    for step in steps.split("\n"):
        try:
            arr = step.split(" ")
            num, s1, s2 = arr[1], arr[3], arr[5]

            stack1 = stacks[int(s1)]
            stack2 = stacks[int(s2)]

            to_move = stack1[-int(num) :]
            stacks[int(s1)] = stack1[: -int(num)]
            stack2 += to_move
        except:
            pass
    return "".join([stack[-1] for stack in stacks.values()])


def run(file):
    with open(file) as f:
        crates, steps = f.read().split("\n\n")
        print(f"Part 1: {p1(crates, steps)}")
        print(f"Part 2: {p2(crates, steps)}")


test_files = [
    "test.txt",
    "input5.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

