from collections import Counter, defaultdict
import numpy as np
from utils import print_grid, convert


def enhance(a, canvas, pad):
    canvas = np.pad(canvas, (3, 3), constant_values=pad)
    new_canvas = np.full(canvas.shape, ".", dtype="str")

    for i in range(1, len(canvas) - 1):
        for j in range(1, len(canvas[0]) - 1):
            pixels = (
                (canvas[i - 1 : i + 2, j - 1 : j + 2].flatten() == "#")
                .astype(int)
                .astype("str")
            )
            num = int("".join(pixels), 2)
            new_canvas[i, j] = a[num]
    return new_canvas[1:-1, 1:-1]

def get_next_pad(a, pad):
    if pad == ".":
        return a[0]
    else:
        return a[-1]

    
def p1(a, b):
    canvas = b

    pad = "."
    for _ in range(2):
        canvas = enhance(a, canvas, pad)
        pad = get_next_pad(a, pad)

    return (canvas == "#").sum()


def p2(a, b):
    canvas = b

    pad = "."
    for idx in range(50):
        if idx % 10 == 0:
            print(idx)
        canvas = enhance(a, canvas, pad)
        pad = get_next_pad(a, pad)

    return (canvas == "#").sum()


def run(file):
    with open(file) as f:
        a, b = [x for x in f.read().split("\n\n")]
        a = a.strip()
        b = np.array([list(x) for x in b.strip().split("\n")])
        print(f"Part 1: {p1(a, b)}")
        print(f"Part 2: {p2(a, b)}")


test_files = [
    "test.txt",
    "input20.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
