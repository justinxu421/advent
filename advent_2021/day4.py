from collections import Counter, defaultdict
import numpy as np

def find_bingo(board, marked):
    for i in range(5):
        if marked[i].sum() == 5:
            return True
        elif marked[:, i].sum() == 5:
            return True
    return False

def mark(board, marked, num):
    for i in range(5):
        for j in range(5):
            if board[i, j] == num:
                marked[i, j] = 1

def get_score(board, marked, num):
    sum = 0
    for i in range(5):
        for j in range(5):
            if marked[i,j] == 0:
                sum += board[i,j]
    print(sum, num)
    return sum * num

def process(a):
    nums = a[0].split(',')
    nums = list(map(int, nums))
    boards = {}
    for i, x in enumerate(a[1:]):
        board = [y.split() for y in x.split('\n')]
        boards[i] = np.array(board).astype(int), np.zeros((5,5))
    return nums, boards

def p1(a):
    nums, boards = process(a)
    for num in nums:
        for board, marked in boards.values():
            mark(board, marked, num)
            if find_bingo(board, marked):
                return get_score(board, marked, num) 


def p2(a):
    nums, boards = process(a)
    not_solved = set(range(len(boards))) 

    for num in nums:
        for idx, (board, marked) in enumerate(boards.values()):
            mark(board, marked, num)
            if find_bingo(board, marked):
                not_solved.discard(idx)
                if len(not_solved) == 0:
                    return get_score(board, marked, num)

with open("input4.txt") as f:
    # read array
    a = [x.strip() for x in f.read().split('\n\n')]
    print(p1(a))
    print(p2(a))
