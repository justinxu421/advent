from collections import Counter, defaultdict
from utils import print_d

def p1(a):
    pass

def p2(a):
    pass

### insert how to parse line
def parse_line(line):
    return list(line.strip())

def main():
    with open('input14.txt') as f:
        a = [parse_line(line) for line in f] 
        print(a[:10])

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
