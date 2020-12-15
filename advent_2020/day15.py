from collections import Counter, defaultdict
from utils import print_d

def p1(a):
    d = defaultdict(list)
    
    last = None
    for i in range(2020):
        if i < len(a):
            n = a[i]
            d[n].append(i)
            last = n
        else:
            if last in d and len(d[last]) > 1:
                n = d[last][-1] - d[last][-2]
            else:
                n = 0
            d[n].append(i)
            last = n
        
        i += 1
    
    return n

def p2(a):
    d = defaultdict(list)
    
    last = None
    for i in range(30000000):
        if i < len(a):
            n = a[i]
            d[n].append(i)
            last = n
        else:
            if last in d and len(d[last]) > 1:
                n = d[last][-1] - d[last][-2]
            else:
                n = 0
            d[n].append(i)
            last = n
        
        i += 1
    
    return n

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
