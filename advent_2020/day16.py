from collections import Counter, defaultdict

def get_rule_dict(rules):
    rule_dict = {}

    def parse_rule(f):
        low,high = f.split('-')
        return (int(low), int(high))

    for field, rng in rules:
        f1, f2 = rng.split(' or ')
        rule_dict[field] = (parse_rule(f1), parse_rule(f2))

    return rule_dict

def check_key(rule_dict, key, entry):
    f1, f2 = rule_dict[key]
    return f1[0] <= entry <= f1[1] or f2[0] <= entry <= f2[1]

def check(rule_dict, entry):
    for key in rule_dict:
        if check_key(rule_dict, key, entry):
            return True
    return False

def p1(rules, nearby):
    rule_dict = get_rule_dict(rules)

    total = 0
    for ticket in nearby:
        for entry in ticket:
            if not check(rule_dict, entry):
                total += entry
    return total

def check_valid_ticket(ticket, rule_dict):
    for entry in ticket:
        if not check(rule_dict, entry):
            return False
    return True

def get_possible(ticket, rule_dict):
    possible = []
    
    for entry in ticket:
        p = set()
        for key in rule_dict:
            if check_key(rule_dict, key, entry):
                p.add(key)
        possible.append(p)

    return possible

def p2(rules, ticket, nearby):
    rule_dict = get_rule_dict(rules)
    valid_tickets = [ticket for ticket in nearby if check_valid_ticket(ticket, rule_dict)]
    
    possible = get_possible(ticket, rule_dict) 
    for t in valid_tickets:
        new_possible = get_possible(t, rule_dict) 
        possible = [a & b for a,b in zip(possible, new_possible)]
    
    # prune possible by recursively removing the keys with only 1 match
    parsed = set()
    for _ in range(20):
        remove = None
        for i, a in enumerate(possible):
            if len(a) == 1 and i not in parsed:
                remove = a
                parsed.add(i)
                break
        possible = [a-remove if j!=i else a for j,a in enumerate(possible)]
    
    total = 1
    for idx, key in enumerate(possible):
        if 'departure' in list(key)[0]:
            total *= ticket[idx]
    return total

def parse_ticket(line):
    return [int(x) for x in line.strip().split(',')]

def main():
    with open('input16.txt') as f:
        rules, tick, nearby_ticks = f.read().split('\n\n')

        rules = list(map(lambda x: x.split(': '), rules.split('\n')))
        tick = parse_ticket(tick.split(':\n')[1])
        nearby_ticks = [parse_ticket(x) for x in nearby_ticks.split(':\n')[1].strip().split('\n')]
        
        print(f'part one: {p1(rules, nearby_ticks)}')
        print(f'part two: {p2(rules, tick, nearby_ticks)}')

if __name__ == "__main__":
    main()
