def move_tail(T, H):
    t1, t2 = T
    h1, h2 = H

    if t1 == h1:
        diff = h2 - t2
        if abs(diff) < 2:
            return T
        if diff == 2:
            T = (t1, t2 + 1)
        if diff == -2:
            T = (t1, t2 - 1)
    if t2 == h2:
        diff = h1 - t1
        if abs(diff) < 2:
            return T
        if diff == 2:
            return (t1 + 1, t2)
        if diff == -2:
            return (t1 - 1, t2)

    x_diff = h1 - t1
    y_diff = h2 - t2
    if x_diff == 2 and y_diff > 0:
        return (t1 + 1, t2 + 1)
    if x_diff == 2 and y_diff < 0:
        return (t1 + 1, t2 - 1)
    if x_diff == -2 and y_diff > 0:
        return (t1 - 1, t2 + 1)
    if x_diff == -2 and y_diff < 0:
        return (t1 - 1, t2 - 1)

    if y_diff == 2 and x_diff > 0:
        return (t1 + 1, t2 + 1)
    if y_diff == 2 and x_diff < 0:
        return (t1 - 1, t2 + 1)
    if y_diff == -2 and x_diff > 0:
        return (t1 + 1, t2 - 1)
    if y_diff == -2 and x_diff < 0:
        return (t1 - 1, t2 - 1)
    return T


dir_dict = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}


def p1(a):
    spots = set()
    T, H = (0, 0), (0, 0)
    spots.add(T)
    for line in a:
        dir, dist = line.split()
        x, y = dir_dict[dir]
        for _ in range(int(dist)):
            H = (H[0] + x, H[1] + y)
            T = move_tail(T, H)
            spots.add(T)

    return len(spots)


def p2(a):
    spots = set()
    positions = {}
    for i in range(10):
        positions[i] = (0, 0)

    spots.add(positions[9])
    for line in a:
        dir, dist = line.split()
        x, y = dir_dict[dir]
        for _ in range(int(dist)):
            H = positions[0]
            positions[0] = (H[0] + x, H[1] + y)
            for i in range(1, 10):
                positions[i] = move_tail(positions[i], positions[i - 1])
            spots.add(positions[9])
    return len(spots)


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input9.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

