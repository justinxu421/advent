from collections import Counter, defaultdict
from utils import print_d

def simplify(string):
    return str(eval(''.join(string)))

def evaluate(eq, i, f):
    string = []
    while i < len(eq):
        cur = eq[i]
        i += 1
        
        # exit out of recursion
        if cur == ')':
            return simplify(string), i
            
        # recursively evaluate
        if cur == '(':
            res, i = evaluate(eq, i, f)
            string.append(res)
        else:
            string.append(cur)
        
        # simplify if length of string is 3
        string = f(string)
    
    return simplify(string), i

def naive(string):
    if len(string) == 3:
        string = [simplify(string)]
    return string

def p1(a):
    total = 0
    for eq in a:
        total += int(evaluate(eq, 0, naive)[0])
    return total

# + takes precendence over *
def precedence(string):
    # simplify only if last 3 are '+'
    if len(string) >= 3 and string[-2] == '+':
        exp = string[-3:]
        string = string[:-3]
        string.append(simplify(exp))
    return string

def p2(a):
    total = 0
    for eq in a:
        total += int(evaluate(eq, 0, precedence)[0])
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
