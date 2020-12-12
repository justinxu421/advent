DIRS = 'NESWRLF'
moves = [1, 1j, -1, -1j]

def parse_dir(d_num, num, start, d):
    if d_num < 4:
        return start + moves[d_num]*num, d
    elif d_num == 4:
        return start, (d + num // 90) % 4
    elif d_num == 5:
        return start, (d + 4 -  num // 90) % 4
    else:
        return start + moves[d]*num, d

def p1(a):
    d = 1 # East
    start = 0
    for d_, num in a:
        start, d = parse_dir(DIRS.find(d_), num, start, d)
    return abs(start.real) + abs(start.imag)

def parse_dir_2(d_num, num, start, way):
    if d_num < 4:
        return start, way + moves[d_num]*num
    elif d_num == 4:
        return start, way * 1j**(num//90)
    elif d_num == 5:
        return start, way * 1j**(4 - num//90)
    else:
        return start + num*way, way

def p2(a):
    start = 0
    way = 1 + 10j

    for d_, num in a:
        start, way  = parse_dir_2(DIRS.find(d_), num, start, way)
    return abs(start.real) + abs(start.imag)

### insert how to parse line
def parse_line(line):
    return line[0], int(line.strip()[1:])

def main():
    with open('input12.txt') as f:
        a = [parse_line(line) for line in f] 
        print(a[:10])

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
