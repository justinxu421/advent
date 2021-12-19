from collections import Counter, defaultdict
import numpy as np
import ast


def get_tree(x, parent=None):
    if type(x) == list and len(x) == 2:
        # don't store data None
        tree = Tree(None, parent)
        left_tree = get_tree(x[0], tree)
        right_tree = get_tree(x[1], tree)
        tree.left = left_tree
        tree.right = right_tree
    else:
        tree = Tree(x, parent)
    return tree


class Tree:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        if self.data is not None:
            return str(self.data)
        else:
            left_str = str(self.left)
            right_str = str(self.right)
            return f"[{left_str}, {right_str}]"


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
        cur.data += explode_val


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
        cur.data += explode_val


def check_explode(val, depth):
    if val.left and val.right:
        if depth == 4:
            return "explode"
        elif check_explode(val.left, depth + 1) == True:
            return True
        elif check_explode(val.left, depth + 1) == "explode":
            right = val.right
            while right.data is None:
                right = right.left
            right.data += val.left.right.data

            explode_left(val, val.left.left.data)
            val.left = Tree(0, val)
            return True
        elif check_explode(val.right, depth + 1) == True:
            return True
        elif check_explode(val.right, depth + 1) == "explode":
            left = val.left
            while left.data is None:
                left = left.right
            left.data += val.right.left.data

            explode_right(val, val.right.right.data)
            val.right = Tree(0, val)
            return True

    return False


def check_reduce(val):
    if val.left and val.right:
        r1 = check_reduce(val.left)
        if r1:
            return True
        r2 = check_reduce(val.right)
        if r2:
            return True
    else:
        if val.data >= 10:
            val_left = val.data // 2
            val_right = val.data - val_left
            new_tree = get_tree([val_left, val_right], val.parent)
            if val.parent.left == val:
                val.parent.left = new_tree
            elif val.parent.right == val:
                val.parent.right = new_tree
            return True

    return False


def reduce(val):
    old_val = str(val)

    check_explode(val, 0)
    if old_val != str(val):
        reduce(val)

    check_reduce(val)
    if old_val != str(val):
        reduce(val)


def get_magnitude(val):
    if val.data is not None:
        return val.data
    return 3 * get_magnitude(val.left) + 2 * get_magnitude(val.right)


def p1(a):
    val = get_tree(a[0])
    reduce(val)

    for x in a[1:]:
        val = get_tree([ast.literal_eval(str(val)), x])
        reduce(val)

    print(val)
    return get_magnitude(val)


def p2(a):
    largest = 0
    for x in range(len(a)):
        for y in range(len((a))):
            if x != y:
                val = get_tree([a[x], a[y]])
                reduce(val)
                largest = max(largest, get_magnitude(val))

    return largest


def run(file):
    with open(file) as f:
        a = [ast.literal_eval(x) for x in f.read().splitlines()]

        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input18.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
