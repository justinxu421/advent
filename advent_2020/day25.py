from collections import Counter, defaultdict
from utils import print_d

div = 20201227

memo = {}
def transform(subject, loop):
    if loop == 0:
        memo[subject, loop] = 1
    elif (subject, loop) not in memo:
        memo[subject, loop] = subject * memo[subject, loop-1] % div
    return memo[subject, loop]

def p1(a):
    memo = {}
    for i in range(100000000):
        key = transform(7, i)
        if key == a[0]:
            card = i
            print(card, key)
        if key == a[1]:
            door = i
            print(door, key)
            break
    
    print(card, door)

    for i in range(door+1):
        a1 = transform(a[0], i)
    print(i, a1)
    for i in range(card+1):
        a2 = transform(a[1], i)
    print(i, a2)

    return a1, a2

### insert how to parse line
def parse_line(line):
    return int(line.strip())

def main():
    with open('input25.txt') as f:
        a = [parse_line(line) for line in f] 

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
