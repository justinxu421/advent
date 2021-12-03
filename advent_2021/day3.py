from collections import Counter, defaultdict


def p1(a):
    gamma, epsilon = "", ""
    for i in range(len(a[0])):
        counts = Counter()
        for x in a:
            counts[x[i]] += 1
        bit = counts.most_common(1)[0][0]
        gamma += bit
        epsilon += str(1 - int(bit))

    return int(gamma, 2) * int(epsilon, 2)


def p2(a):
    oxygen, co2 = a, a
    for i in range(len(a[0])):
        counts = defaultdict(list)
        for x in oxygen:
            counts[x[i]].append(x)
        if len(counts["1"]) >= len(counts["0"]):
            oxygen = counts["1"]
        else:
            oxygen = counts["0"]

    for i in range(len(a[0])):
        counts = defaultdict(list)
        for x in co2:
            counts[x[i]].append(x)
        if len(counts["1"]) < len(counts["0"]):
            co2 = counts["1"]
        else:
            co2 = counts["0"]
        if len(co2) == 1:
            break

    print(oxygen, co2)
    return int(oxygen[0], 2) * int(co2[0], 2)


with open("input3.txt") as f:
    # read array
    a = [x.strip() for x in f]
    print(p1(a))
    print(p2(a))
