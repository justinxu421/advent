from collections import Counter, defaultdict
from utils import print_d

def parse_rule(f):
    low,high = f.split('-')
    return (int(low), int(high))

def check(all_rules, entry):
    for low, high in all_rules:
        if entry >= low and entry <=  high:
            return True
    return False

def get_rules(rules):
    rule_dict = {}
    all_rules = []
    for field, rng in rules:
        f1, f2 = rng.split(' or ')
        all_rules.append(parse_rule(f1))
        all_rules.append(parse_rule(f2))
        rule_dict[field] = (parse_rule(f1), parse_rule(f2))
    return all_rules, rule_dict

def p1(rules, tickets, nearby):
    all_rules, rule_dict = get_rules(rules)
    total = 0
    for i, ticket in enumerate(nearby):
        for entry in ticket:
            if not check(all_rules, int(entry)):
                total += int(entry)
    return total

def check_valid_ticket(ticket, all_rules):
    for entry in ticket:
        if not check(all_rules, int(entry)):
            return False
    return True

def get_valid_tickets(rules, nearby):
    all_rules, rule_dict = get_rules(rules)
    return [ticket for ticket in nearby if check_valid_ticket(ticket, all_rules)]

def check_f(f1, entry):
    low, high = f1
    return  entry >= low and entry <= high

def get_possible(entry, rule_dict, keys):
    p = set()
    for key in keys:
        f1, f2 = rule_dict[key]
        if check_f(f1, entry) or check_f(f2, entry):
            p.add(key)
    return p

def p2(rules, ticket, nearby):
    all_rules, rule_dict = get_rules(rules)
    valid_tickets = get_valid_tickets(rules, nearby)
    
    keys = list(rule_dict.keys())

    possible = [get_possible(int(entry), rule_dict, keys) for entry in ticket]
    for t in valid_tickets:
        print([len(a) for a in possible])
        new_possible = [get_possible(int(entry), rule_dict, keys) for entry in t]
        possible = [a & b for a,b in zip(possible, new_possible)]
    
    skip = set()
    for _ in range(20):
        remove = None
        for i, a in enumerate(possible):
            if len(a) == 1 and list(a)[0] not in skip:
                remove = a
                skip.add(list(a)[0])
                break
        possible = [a-remove if j!=i else a for j,a in enumerate(possible)]

    print([len(a) for a in possible])
    for i,a in enumerate(possible):
        print(i, a)

    total = 1
    for idx in [3, 6, 13, 14, 15, 18]:
        total *= int(ticket[idx])
        print(ticket[idx])
    return total

### insert how to parse line
def parse_line(line):
    return list(line.strip())

def main():
    with open('input16.txt') as f:
        rules, tickets, nearby = f.read().split('\n\n')

        rules = list(map(lambda x: x.split(': '), rules.split('\n')))
        tickets = tickets.split(':\n')[1].split(',')
        nearby = list(map(lambda x: x.split(','), nearby.split(':\n')[1].strip().split('\n')))
        
        print(f'part one: {p1(rules, tickets, nearby)}')
        print(f'part two: {p2(rules, tickets, nearby)}')

if __name__ == "__main__":
    main()
