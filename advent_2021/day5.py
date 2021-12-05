from collections import Counter, defaultdict
import numpy as np


def vertical(x1, x2, y1, y2, board):
    if x1 == x2:
        x = x1
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        for y in range(ymin, ymax + 1):
            board[(x, y)] += 1


def horizontal(x1, x2, y1, y2, board):
    if y1 == y2:
        y = y1
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        for x in range(xmin, xmax + 1):
            board[(x, y)] += 1


def p1(a):
    board = defaultdict(int)
    for p1, p2 in a:
        x1, y1 = list(map(int, p1.split(",")))
        x2, y2 = list(map(int, p2.split(",")))
        vertical(x1, x2, y1, y2, board)
        horizontal(x1, x2, y1, y2, board)

    return sum(1 for x in board.values() if x >= 2)


def forward_diagonal(x1, x2, y1, y2, board):
    if (y2 - x2) == (y1 - x1):
        if x1 < x2:
            xmin, ymin = x1, y1
            xmax = x2
        else:
            xmin, ymin = x2, y2
            xmax = x1
        for i in range(xmax - xmin + 1):
            x, y = xmin + i, ymin + i
            board[(x, y)] += 1


def backward_diagonal(x1, x2, y1, y2, board):
    if (y2 + x2) == (y1 + x1):
        if x1 < x2:
            xstart, ystart = x1, y1
            xend = x2
        else:
            xstart, ystart = x2, y2
            xend = x1
        for i in range(xend - xstart + 1):
            x, y = xstart + i, ystart - i
            board[(x, y)] += 1


def p2(a):
    board = defaultdict(int)
    for p1, p2 in a:
        x1, y1 = list(map(int, p1.split(",")))
        x2, y2 = list(map(int, p2.split(",")))
        vertical(x1, x2, y1, y2, board)
        horizontal(x1, x2, y1, y2, board)
        forward_diagonal(x1, x2, y1, y2, board)
        backward_diagonal(x1, x2, y1, y2, board)

    return sum(1 for x in board.values() if x >= 2)


with open("input5.txt") as f:
    a = [x.split(" -> ") for x in f.read().splitlines()]
    print(p1(a))
    print(p2(a))
