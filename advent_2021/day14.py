from collections import Counter, defaultdict
import numpy as np

def step(a, rules):
    i = 0
    while i < len(a) - 1:
        sub_str = a[i: i+2]
        if sub_str in rules:
            a = a[:i+1] + rules[sub_str] + a[i+1:]
            i += 1
        i += 1
    return a

def get_rules(b):
    rules = {}
    for x in b:
        pair, insert = x.split(' -> ')
        rules[pair] = insert
    return rules
     
def p1(a, b):
    rules = get_rules(b) 
    for itr in range(10):
        a = step(a, rules)
                
    counts = Counter(list(a))      
    counts = counts.most_common()
    
    return counts[0][1] - counts[-1][1]

import copy
def step_2(a_tuples, rules):
    a_tuples_copy = copy.deepcopy(a_tuples)
    for pair, val in a_tuples.items():
        if pair in rules:
            pair_1 = pair[0] + rules[pair]
            pair_2 = rules[pair] + pair[1]

            a_tuples_copy[pair] -= val
            a_tuples_copy[pair_1] += val
            a_tuples_copy[pair_2] += val

    return a_tuples_copy

def get_counts(a_tuples, a):
    counts = Counter()
    for pair, v in a_tuples.items():
        counts[pair[0]] += v
        counts[pair[1]] += v
    counts[a[0]] += 1
    counts[a[-1]] += 1

    return Counter({k: v//2 for k,v in counts.items()})
    
def p2(a, b):
    rules = get_rules(b)

    a_tuples = Counter()
    for i in range(len(a)-1):
        sub_str = a[i:i+2]
        a_tuples[sub_str] += 1
        
    for _ in range(40):
        # print(a_tuples)
        counts = get_counts(a_tuples, a)
        # print(counts) 
        # print()

        a_tuples = step_2(a_tuples, rules)
                
    counts = get_counts(a_tuples, a)
    print(counts) 

    counts = counts.most_common()
    print(counts)
    return counts[0][1] - counts[-1][1]


def run(file):
    with open(file) as f:
        a, b = f.read().split('\n\n')
        b = [y for y in b.split('\n')]
        print(f"Part 1: {p1(a, b)}")
        print(f"Part 2: {p2(a, b)}")


test_files = [
    "test.txt",
    "input14.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()