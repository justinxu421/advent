from collections import Counter, defaultdict
import numpy as np

digit_map = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def p1(a):
    total = 0
    for _, y in a:
        for d in y.split():
            if len(d) in [2, 4, 3, 7]:
                total += 1
    return total


def solve(x):
    _609 = []
    _235 = []
    for digit in x.split():
        digit = set(digit)
        if len(digit) == 3:
            acf = digit
        elif len(digit) == 2:
            cf = digit
        elif len(digit) == 4:
            bcdf = digit
        elif len(digit) == 7:
            abcdefg = digit
        elif len(digit) == 6:
            _609.append(digit)
        elif len(digit) == 5:
            _235.append(digit)

    abdfg = set.intersection(*_609)
    adg = set.intersection(*_235)

    # 7 - 4
    a = acf - cf
    
    # 8 - 4 - intersection(_609)
    e = abcdefg - bcdf - abdfg
    g = abcdefg - bcdf - a - e

    # now we know d
    d = adg - a - g
    # now we can find b
    b = abcdefg - adg - acf - e

    # remaining 2 for cf
    f = abdfg - adg - b
    c = cf - f

    # make sure we have solved
    assert(len(a) == 1)
    assert(len(b) == 1)
    assert(len(c) == 1)
    assert(len(d) == 1)
    assert(len(e) == 1)
    assert(len(f) == 1)
    assert(len(g) == 1)

    return {
        a.pop(): "a",
        b.pop(): "b",
        c.pop(): "c",
        d.pop(): "d",
        e.pop(): "e",
        f.pop(): "f",
        g.pop(): "g",
    }

def get_output(mapping, y):
    output = 0
    for output_str in y.split():
        # decrypt and sort and make a string so that we can figure out the output
        decrypted = "".join(sorted([mapping[dig] for dig in output_str.strip()]))
        output = output * 10 + digit_map[decrypted]
    return output

def p2(a):
    total = 0
    for x, y in a:
        mapping = solve(x)
        total += get_output(mapping, y)

    return total


def run(file):
    with open(file) as f:
        a = [x.split(" | ") for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input8.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
