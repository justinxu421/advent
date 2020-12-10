from collections import defaultdict

def run_cmd(cmd, num, i, total):
    if cmd == 'acc':
        return i+1, total + num
    elif cmd == 'nop':
        return i+1, total
    elif cmd == 'jmp':
        return i+num, total

def run_loop(a):
    i = 0
    instructions = set()

    total = 0
    while i not in instructions:
        instructions.add(i)
        cmd, num = a[i]
        i, total = run_cmd(cmd, num, i, total) 
        if i == len(a):
            return True, total 
    return False, total

def p1(a):
    return run_loop(a)

def p2(a):
    entries = []
    for i, (cmd, num) in enumerate(a):
        if cmd in ['nop', 'jmp']:
            entries.append((i, cmd, num))
    
    replace = {'nop':'jmp', 'jmp':'nop'}
    for idx, cmd, num in entries:
        a_copy = a[:]
        a_copy[idx] = (replace[cmd], num)

        res = run_loop(a_copy)
        if res[0]:
            return res

### insert how to parse line
def parse_line(line):
    a, b = line.strip().split(' ')
    sign = b[0]
    if sign == '+':
        return a, int(b[1:])
    else:
        return a, -int(b[1:])
    print(a[:5])

with open('input8.txt') as f:
    # a = [line.split() for line in f.read().split('\n\n')]
    a = [parse_line(line) for line in f]

    print(f'part one: {p1(a)}')
    print(f'part two: {p2(a)}')

