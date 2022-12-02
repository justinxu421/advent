def p1(a):
    points = 0
    for x in a:
        elf, me = x.split()
        p1 = ord(elf) - ord("A") + 1
        p2 = ord(me) - ord("X") + 1
        points += p2

        if (p2 - p1) % 3 == 1:
            points += 6
        if p2 == p1:
            points += 3

    return points


def p2(a):
    points = 0
    for x in a:
        elf, state = x.split()

        # 0/1/2
        p1 = ord(elf) - ord("A")

        if state == "X":
            p2 = (p1 - 1) % 3
        if state == "Y":
            p2 = p1
            points += 3
        if state == "Z":
            p2 = (p1 + 1) % 3
            points += 6

        points += p2 + 1
    return points


def run(file):
    with open(file) as f:
        a = [x for x in f.read().splitlines()]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input2.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()

