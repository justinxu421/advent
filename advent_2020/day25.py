from collections import Counter, defaultdict
from utils import print_d

div = 20201227

memo = {}
def transform(subject, loop, end = None):
    start = 1
    for i in range(loop):
        if end and start == end:
            return i, end
        start = start * subject % div
    return i, start

def p1(a):
    print(f'array is {a}\n')
    card, x  = transform(7, 100000000, a[0])
    print(f'card is {card}, {x}')
    door, y  = transform(7, 100000000, a[1])
    print(f'door is {door}, {y}\n')

    _, a1 = transform(a[0], door)
    print(f'a1 is {a1}')
    _, a2 = transform(a[1], card)
    print(f'a2 is {a2}')

    return a1, a2

### insert how to parse line
def parse_line(line):
    return int(line.strip())

def main():
    with open('input25.txt') as f:
        a = [parse_line(line) for line in f] 
        print(f'part one: {p1(a)}')

if __name__ == "__main__":
    main()
