from collections import Counter, defaultdict
import numpy as np
import ast

def get_tree(x, parent = None):
    tree = Tree(x, parent)
    if type(x) == list and len(x) == 2:
        left_tree = get_tree(x[0], tree)
        right_tree = get_tree(x[1], tree)
        tree.left = left_tree
        tree.right = right_tree
    return tree

class Tree():
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

def overwrite(cur, overwrite):
    cur.data = overwrite
    if cur.parent.left == cur:
        cur.parent.data[0] = overwrite
    elif cur.parent.right == cur:
        cur.parent.data[1] = overwrite

def explode_left(cur, explode_val):
    # bubble up to master parent of branch
    while cur.parent and cur.parent.left == cur:
        cur = cur.parent
    cur = cur.parent

    # if parent exists, go to left branch
    if cur:
        cur = cur.left
        # then find rightmost value
        while cur and cur.left and cur.right:
            cur = cur.right
        overwrite(cur, cur.data + explode_val)

def explode_right(cur, explode_val):
    # bubble up to master parent of branch
    while cur.parent and cur.parent.right == cur:
        cur = cur.parent
    cur = cur.parent

    # if parent exists, then go to right branch
    if cur:
        cur = cur.right
        # then find leftmost value
        while cur and cur.left and cur.right:
            cur = cur.left
        overwrite(cur, cur.data + explode_val)

def check_explode(val, depth):
    if val.left and val.right:
        if depth == 4:
            print('explode', val)
            return True
        else:
            if check_explode(val.left, depth + 1):
                '''
                # explode left, bubble up
                left_val = val.left[0]
                while val.parent.left:
                    pass
                '''
                # explode right, overwrite the list
                val.data[1] = val.left.data[1] + val.right.data
                val.right.data = val.left.data[1] + val.right.data 
                # explode left 
                explode_left(val, val.left.data[0])
                val.data[0] = 0
                val.left = Tree(0, val)
            if check_explode(val.right, depth + 1):
                # explode left, overwrite the list
                val.data[0] = val.right.data[0] + val.left.data
                val.left.data = val.right.data[0] + val.left.data 
                # explode right
                explode_right(val, val.right.data[1])
                val.data[1] = 0
                val.right = Tree(0, val)
                    
    return False

def check_reduce(val):
    if val.left and val.right:
        check_reduce(val.left)
        check_reduce(val.right)
    else:
        # print(val)
        if val.data >= 10:
            val_left = val.data // 2
            val_right = val.data - val_left

            new_tree = get_tree([val_left, val_right], val.parent)
            if val.parent.left == val:
                val.parent.left = new_tree 
                val.parent.data[0] = [val_left, val_right]
            elif val.parent.right == val:
                val.parent.right = new_tree
                val.parent.data[1] = [val_left, val_right]
            overwrite(val, [val_left, val_right])


def reduce(val):
    old_val = ''
    while str(val) != old_val:
        old_val = str(val)
        check_explode(val, 0)
        check_reduce(val)

def p1(a):
    val = a[0]
    reduce(val)

    for x in a[1:]:
        print('before', val)
        val = get_tree([val.data, x.data])
        reduce(val)
    print()
    return val


def p2(a):
    pass


def run(file):
    with open(file) as f:
        a = [
            ast.literal_eval(x)
            for x in f.read().splitlines()
        ]
        a = [get_tree(x) for x in a]

        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    # "input18.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
