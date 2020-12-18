from collections import Counter, defaultdict
from utils import print_d

def evaluate(eq):
    string = []
    while eq:
        cur = eq.pop(0)

        if cur == ')':
            return str(eval(''.join(string)))

        if cur == '(':
            string.append(evaluate(eq))
        else:
            string.append(cur)

        if len(string) == 3:
            string = [str(eval(''.join(string)))]
    
    return str(eval(''.join(string)))

def p1(a):
    total = 0
    for eq in a:
        total += int(evaluate(eq))
    return total

def evaluate_2(eq):
    print(''.join(eq))

    string = []
    while eq:
        cur = eq.pop(0)
        print(f'string: {string}, cur: {cur}')

        if cur == ')':
            return str(eval(''.join(string)))

        if cur == '(':
            string.append(evaluate_2(eq))
        else:
            string.append(cur)

        if len(string) >= 3 and string[-2] == '+':
            exp = string[-3:]
            for _ in range(3):
                string.pop()
            string.append(str(eval(''.join(exp))))
            '''
            if string[1] == '+':
                string = [str(eval(''.join(string)))]
            '''
    
    return str(eval(''.join(string)))

def p2(a):
    total = 0
    for eq in a:
        total += int(evaluate_2(eq))
    return total

### insert how to parse line
def parse_line(line):
    return list(line.strip().replace(' ', ''))

def main():
    with open('input18.txt') as f:
        a = [parse_line(line) for line in f] 
        #print(f'part one: {p1(a[:])}')
        print(f'part two: {p2(a[:])}')

if __name__ == "__main__":
    main()
