import numpy as np
import pandas as pd
from functools import reduce


def p1(a):
    diffs = map(lambda x: x[0] - x[1], zip(a[1:], a[:-1]))
    return sum([x > 0 for x in diffs])


def rolling3(a):
    tuples = zip(a[:-2], a[1:-1], a[2:])
    return map(lambda x: x[0] + x[1] + x[2], tuples)


def p2(a):
    diffs = map(lambda x: x[0] - x[1], zip(rolling3(a[1:]), rolling3(a[:-1])))
    return sum([x > 0 for x in diffs])


with open("input1.txt") as f:
    # read array
    a = [int(x.strip()) for x in f]
    print(p1(a))
    print(p2(a))
