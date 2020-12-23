from collections import Counter, defaultdict
from utils import print_d

def play(a, b, recursive = False):
    combos = set()

    while True:
        deck = (tuple(a), tuple(b))
    
        # exit cases for winner
        if len(a) == 0:
            return 'b', a, b
        elif len(b) == 0:
            return 'a', a, b
        elif deck in combos:
            return 'a', a, b

        # add to set to prevent infinite loop
        combos.add(deck)

        c1, c2 = a.pop(0), b.pop(0)

        # handle recursive case if flag is on to get winner
        if recursive and c1 <= len(a) and c2 <= len(b):
            winner, _, _ = play(a[:c1], b[:c2])
        else:
            winner = 'a' if c1 > c2 else 'b'

        if winner == 'a':
            a.append(c1)
            a.append(c2)
        else:
            b.append(c2)
            b.append(c1)

# reverse list and get total sum
def get_total(a, b):
    total = 0
    for i, x in enumerate(a[::-1]):
        total += x * (i+1)

    for i, x in enumerate(b[::-1]):
        total += x * (i+1)

    return total

def p1(a, b):
    winner, a, b = play(a[:], b[:])
    return get_total(a, b)

def p2(a, b):
    winner, a, b = play(a[:], b[:], True)
    return get_total(a, b)

def main():
    with open('input22.txt') as f:
        a, b = f.read().strip().split('\n\n')
        a = [int(x) for x in a.strip().split('\n')[1:]]
        b = [int(x) for x in b.strip().split('\n')[1:]]

        print(f'part one: {p1(a, b)}')
        print(f'part two: {p2(a, b)}')

if __name__ == "__main__":
    main()
