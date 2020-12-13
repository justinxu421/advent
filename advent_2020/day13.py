from collections import Counter, defaultdict
from utils import print_d

def p1(x, a):
    buses = []
    for bus in a:
        if bus != 'x':
            buses.append(int(bus))

    min_ = 999999999999999999999
    min_bus = None
    for bus in buses:
        new = ((int(x)+1) // bus + 1) * bus
        
        if new < min_:
            min_ = new
            min_bus = bus
    
    print(min_, x, min_bus)
    return (min_ - x) * min_bus

def check_valid(buses, x):
    for i, bus in buses:
        if x % bus != i:
            return False
    return True

def p2(a):
    buses = []
    for i, bus in enumerate(a):
        if bus != 'x':
            buses.append((-i % int(bus), int(bus)))
    
    prod = 1
    for i, bus in buses:
        prod *= bus
    
    buses.sort(key = lambda x: x[1])
    print(prod)
    print(buses)
    
    increment = 1

    r1, m1 = buses[-1]
    r1 = r1 % m1
    while len(buses) >= 2:
        r2, m2 = buses[-2]
        print(r1, m1, r2, m2)
        
        while r1 % m2 != r2:
            r1 += m1
        m1 = m1*m2
        buses.pop()

    print(check_valid(buses, r1))
    print(check_valid(buses, 1068781))
    return r1

### insert how to parse line
def parse_line(line):
    return list(line.strip())
    #return line[0], int(line.strip()[1:])

def main():
    with open('input13.txt') as f:
        x = int(f.readline())
        a = f.readline().strip().split(',')
        #a = [parse_line(line) for line in f] 
        print(x, a[:10])

        print(f'part one: {p1(x, a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
