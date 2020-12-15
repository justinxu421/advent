from collections import Counter, defaultdict
from utils import print_d

def run(a, num):
    d = {}
    
    last = None
    for i in range(num):
        if i < len(a):
            n = a[i]
            d[n] = i
            last = n
        else:
            # if len(d[last]) > 1:
            if last in d:
                n = i - 1 - d[last]
            else:
                n = 0
            d[last] = i-1
            last = n
        
        i += 1
    
    return n

def p1(a):
    return run(a, 2020)

def p2(a):
    return run(a, 30000000)

### insert how to parse line
def parse_line(line):
    return list(map(int, line.strip().split(',')))

def main():
    with open('input15.txt') as f:
        a = parse_line(f.readline())

        print(a[:10])

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
