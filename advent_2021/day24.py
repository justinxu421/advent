from collections import Counter, defaultdict
import numpy as np


def handle(instr, a, b, vars_):
    if b in ["w", "x", "y", "z"]:
        b = vars_[b]
    else:
        b = int(b)

    if instr == "add":
        vars_[a] = vars_[a] + b
    elif instr == "mul":
        vars_[a] = vars_[a] * b
    elif instr == "div":
        vars_[a] = vars_[a] // b
    elif instr == "mod":
        vars_[a] = vars_[a] % b
    elif instr == "eql":
        vars_[a] = 1 if vars_[a] == b else 0


def process(a, input, verbose=False):
    vars_ = defaultdict(int)

    for x in a:
        instr = x[0]
        if instr == "inp":
            if verbose:
                print(vars_)
            vars_["w"] = input.pop(0)
        else:
            handle(instr, x[1], x[2], vars_)

    return vars_


def find_reduction(instructions, start, i, j, zeros):
    cur_score = process(instructions, start[:])["z"]

    reductions = []
    for x in range(1, 10):
        for y in range(1, 10):
            start_copy = start[:]
            start_copy[i] = x
            start_copy[j] = y

            score = process(instructions, start_copy[:])["z"]
            if score == 0:
                zeros.add(tuple(start_copy))
            if score < (cur_score // 10):
                reductions.append(start_copy)

    return reductions


def p1(instructions):
    seen = set()
    zeros = set()
    start = [9 for _ in range(14)]
    seen.add(tuple(start))

    q = [start]
    while q:
        # print(len(q))
        start = q.pop()
        current = process(instructions, start[:])["z"]

        if current == 0:
            print(current, start)

        # select 2 random indices 10 times
        for _ in range(10):
            i, j = np.random.choice(14, 2)

            reductions = find_reduction(instructions, start, i, j, zeros)
            for reduction in reductions:
                if tuple(reduction) not in seen:
                    q.append(reduction)
                    seen.add(tuple(reduction))

    largest = sorted(list(set([tuple(x) for x in zeros])))[-1]
    return "".join([str(x) for x in largest])


def p2(instructions):
    seen = set()
    zeros = set()
    start = [1 for _ in range(14)]
    seen.add(tuple(start))

    q = [start]
    while q:
        # print(len(q))
        start = q.pop()
        current = process(instructions, start[:])["z"]

        if current == 0:
            print(current, start)

        # select 2 random indices 10 times
        for _ in range(10):
            i, j = np.random.choice(14, 2)

            reductions = find_reduction(instructions, start, i, j, zeros)
            for reduction in reductions:
                if tuple(reduction) not in seen:
                    q.append(reduction)
                    seen.add(tuple(reduction))

    smallest = sorted(list(set([tuple(x) for x in zeros])))[0]
    return "".join([str(x) for x in smallest])


def run(file):
    with open(file) as f:
        a = [x.split() for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "input24.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
