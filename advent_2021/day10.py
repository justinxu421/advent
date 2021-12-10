from collections import Counter, defaultdict
import numpy as np

bracket_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
inverse_map = {v: k for (k, v) in bracket_map.items()}

def parse_brackets(x):
    stack = []
    for b in x:
        if b in bracket_map:
            stack.append(b)
        else:
            # complete
            if not stack:
                return False, stack
            # corrupted
            if stack[-1] != inverse_map[b]:
                return True, b
            # continue
            else:
                stack.pop()
    return False, stack

def p1(a):
    corrupted = []
    for x in a:
        corrupt, b = parse_brackets(x)
        if corrupt:
            corrupted.append(b)
            
    return sum(scores[char] for char in corrupted)


scores_2 = {")": 1, "]": 2, "}": 3, ">": 4}




def p2(a):
    scores = []
    for x in a:
        score = 0
        corrupt, stack = parse_brackets(x)
        if not corrupt:
            for i in stack[::-1]:
                score = score * 5 + scores_2[bracket_map[i]]
            scores.append(score)

    print(len(scores))
    return sorted(scores)[len(scores) // 2]


def run(file):
    with open(file) as f:
        a = [list(x) for x in f.read().splitlines()]
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
