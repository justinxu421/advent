import numpy as np
import pandas as pd


def p1(a):
    diffs = np.array(a[1:]) - np.array(a[:-1])
    return (diffs > 0).sum()


def p2(a):
    b = pd.Series(a).rolling(3).sum().dropna()
    diffs = np.array(b[1:]) - np.array(b[:-1])
    return (diffs > 0).sum()


with open("input1.txt") as f:
    # read array
    a = [int(x.strip()) for x in f]
    print(p1(a))
    print(p2(a))
