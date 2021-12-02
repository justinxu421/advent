def p1(a):
    h, d = 0, 0
    for d_, x in a:
        x = int(x)
        if d_ == "forward":
            h += x
        elif d_ == "down":
            d += x
        elif d_ == "up":
            d -= x

    return h * d


def p2(a):
    h, d, aim = 0, 0, 0
    for d_, x in a:
        x = int(x)
        if d_ == "forward":
            h += x
            d += aim * x
        elif d_ == "down":
            aim += x
        elif d_ == "up":
            aim -= x

    return h * d


with open("input2.txt") as f:
    # read array
    a = [x.strip().split() for x in f]
    print(p1(a))
    print(p2(a))
