def get_cals(a):
    all_cals = []
    for x in a:
        cals = sum(list(map(int, x.split())))
        all_cals.append(cals)
    return all_cals


def p1(a):
    all_cals = get_cals(a)
    return max(all_cals)


def p2(a):
    all_cals = get_cals(a)
    top_3 = sorted(all_cals)[-3:]
    return sum(top_3)


def run(file):
    with open(file) as f:
        a = [x for x in f.read().split("\n\n")]
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "input1.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
