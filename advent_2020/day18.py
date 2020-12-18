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
    a = int(string[0])
   
    i = 1
    while i < len(string):
        b = int(string[i+1])
        if string[i] == '*':
            a *= b
        elif string[i] == '+':
            a += b
        i += 2
    return a

def p1(a):
    total = 0
    for eq in a:
        total += evaluate(eq, 0, naive)[0]
    return total

# + takes precendence over *
def precedence(string):
    a = int(string[0])

    i = 1
    while i < len(string):
        b = int(string[i+1])
        if string[i] == '*':
            return a * precedence(string[i+1:]) 
        elif string[i] == '+':
            a += b
        i += 2
    return a

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
