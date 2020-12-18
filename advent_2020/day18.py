from collections import Counter, defaultdict
from utils import print_d

def evaluate(eq, i, f):
    string = []
    while i < len(eq):
        cur = eq[i]
        i += 1
        
        # exit out of recursion
        if cur == ')':
            return f(string), i
            
        # recursively evaluate
        if cur == '(':
            res, i = evaluate(eq, i, f)
            string.append(res)
        else:
            string.append(cur)
    
    return f(string), i

def naive(string):
    if len(string) == 1:
        return int(string[0])

    if string[-2] == '*':
        return naive(string[:-2]) * int(string[-1])
    elif string[-2] == '+':
        return naive(string[:-2]) + int(string[-1])

def p1(a):
    total = 0
    for eq in a:
        total += evaluate(eq, 0, naive)[0]
    return total

# + takes precendence over *
def precedence(string):
    if len(string) == 1:
        return int(string[0])

    if string[-2] == '*':
        return precedence(string[:-2]) * int(string[-1])
    elif string[-2] == '+':
        string = string[:-3] + [int(string[-3]) + int(string[-1])]
        return precedence(string)

def p2(a):
    total = 0
    for eq in a:
        total += evaluate(eq, 0, precedence)[0]
    return total

### insert how to parse line
def parse_line(line):
    return list(line.strip().replace(' ', ''))

def main():
    with open('input18.txt') as f:
        a = [parse_line(line) for line in f] 
        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
