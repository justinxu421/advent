from collections import Counter

def p1(a):
    all_  = [0] + sorted(a) + [max(a) + 3]
    diffs = []

    for i in range(1, len(all_)):
        diffs.append(all_[i] - all_[i-1])
    diffs = Counter(diffs)

    return diffs[1] * diffs[3]

def find_all_paths(all_, idx, d):
    if idx in d:
        return d[idx]
    
    if idx == len(all_)-1:
        return 1

    valids = []
    for i in range(1, 4):
        if idx+i < len(all_) and 1 <= all_[idx+i] - all_[idx] <= 3:
            valids.append(idx+i)
    
    if not valids:
        return 0
    
    total = 0
    for new_idx in valids:
        total += find_all_paths(all_, new_idx, d)
    d[idx] = total

    return total

def p2(a):
    all_  = sorted(a)
    all_.insert(0, 0)

    return find_all_paths(all_, 0, {})

### insert how to parse line
def parse_line(line):
    return int(line.strip())

with open('input10.txt') as f:
    a = [parse_line(line) for line in f] 
    print(a[:10])

    print(f'part one: {p1(a)}')
    print(f'part two: {p2(a)}')

