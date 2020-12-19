def match(message, pattern, rules):
    # return True if all character depleted
    if len(message) == 0 and len(pattern) == 0:
        return True
    # if either is empty, then False
    if len(pattern) == 0 or len(message) == 0:
        return False
    # if pattern becomes too long from looping, then impossible case
    if len(pattern) > len(message):
        return False

    x = pattern[-1]
    # alpha character
    if type(rules[x]) == str:
        # exit if character doesn't match
        if rules[x] != message[-1]:
            return False
        return match(message[:-1], pattern[:-1], rules)
    # replace nesting
    elif len(rules[x]) == 1:
        pattern = pattern[:-1] + rules[x][0]
        return match(message, pattern, rules)
    elif len(rules[x]) == 2:
        pattern_0 = pattern[:-1] + rules[x][0]
        pattern_1 = pattern[:-1] + rules[x][1]
        return match(message, pattern_0, rules) or match(message, pattern_1, rules)

def get_rules(a):
    rules = {}
    for key, line in a:
        if '"' in line:
            rules[key] = line[1:-1]
        elif '|' in line:
            r1, r2 = line.split(' | ')
            rules[key] = (r1.split(), r2.split())
        else:
            rules[key] = [line.split()]
    return rules

def p1(a, text):
    rules = get_rules(a) 
    return sum(match(message, ['0'], rules) for message in text)

def get_rules_2(a):
    rules = {}
    for key, line in a:
        if '"' in line:
            rules[key] = line[1:-1]
        elif '|' in line:
            r1, r2 = line.split(' | ')
            rules[key] = (r1.split(), r2.split())
        else:
            rules[key] = [line.split()]
    
    # replace rules to insert looping
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    return rules

def p2(a, text):
    rules = get_rules_2(a) 
    return sum(match(message, ['0'], rules) for message in text)

### insert how to parse line
def parse_line(line):
    return line.strip().split(': ')

def main():
    with open('input19.txt') as f:
    #with open('test.txt') as f:
        rules, text = f.read().split('\n\n')
        a = [parse_line(line) for line in rules.strip().split('\n')] 
        text = text.strip().split('\n')

        print(f'part one: {p1(a,text)}')
        print(f'part two: {p2(a, text)}')

if __name__ == "__main__":
    main()
