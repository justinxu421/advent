from collections import Counter, defaultdict
from utils import print_d

def p1(x, a):
    buses = [int(bus) for bus in a if bus != 'x']

    def min_div( bus):
        return bus, ((int(x)+1) // bus + 1) * bus
        
    div_list = list(map(min_div, buses))
    div_list.sort(key = lambda x: x[0])
    
    min_bus, min_  = div_list[0]
    return (min_ - x) * min_bus

# ensure our solution is valid
def check_valid(buses, x):
    for i, bus in buses:
        if x % bus != i:
            return False
    return True

def p2(a):
    # get the remainders and divisors and sort
    buses = [(-i % int(bus), int(bus)) for i, bus in enumerate(a) if bus != 'x']
    buses.sort(key = lambda x: x[1])
    
    r1, m1 = buses[-1]
    while len(buses) >= 2:
        r2, m2 = buses[-2]
        
        while r1 % m2 != r2:
            r1 += m1
        m1 = m1*m2
        buses.pop()

    print(check_valid(buses, r1))
    return r1

def main():
    with open('input13.txt') as f:
        x = int(f.readline())
        a = f.readline().strip().split(',')

        print(x, a[:10])

        print(f'part one: {p1(x, a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
