from collections import defaultdict

# check if 2 nums in valid sum to total
def check_valid(total, valid):
    all = set()
    for x in valid:
        if (total - x) in all:
            return True
        all.add(x)
    return False

def p1(a):
    for i in range(26, len(a)):
        valid = a[i-25:i]
        if not check_valid(a[i], valid):
            return a[i], i

def p2(a):
    target, idx = p1(a)
    
    total = a[0] + a[1]
    start, end  = 0, 1
    while end < idx:
        if total == target:
            window = a[start:end+1]
            return min(window) + max(window)

        while total < target:
            end += 1
            total += a[end]

        while total > target:
            total -= a[start]
            start += 1

    '''
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            arr = a[i:j+1]
            if sum(arr) == num:
                print(arr)
                return min(arr) + max(arr)
    '''


### insert how to parse line
def parse_line(line):
    return int(line.strip())

with open('input9.txt') as f:
    a = [parse_line(line) for line in f]

    print(f'part one: {p1(a)}')
    print(f'part two: {p2(a)}')

