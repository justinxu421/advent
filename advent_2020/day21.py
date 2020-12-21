from collections import Counter, defaultdict
from utils import print_d

# intersect ingredients to get possible ingredients with allergens
def get_allergen_dict(a):
    d = {}
    for ingredients, allergens in a:
        for a_ in allergens:
            if a_ not in d:
                d[a_] = ingredients
            else:
                d[a_] = ingredients & d[a_]
    return d

def p1(a):
    a.sort(key = lambda x: len(x[1])) 
    d = get_allergen_dict(a)

    total = 0
    # loop through and remove ingredients in allergen list
    for ingredients, allergens in a:
        possible = set(ingredients)
        for key in d:
            possible -= d[key]
        total += len(possible)
    
    return total

# find the first key with length ingredient list
def find_key(d, parsed):
    for key in d:
        if key not in parsed and len(d[key]) == 1:
            parsed[key] = d[key]
            return key
    return False

def p2(a):
    a.sort(key = lambda x: len(x[1])) 
    d = get_allergen_dict(a)
    
    parsed = {}
    for _ in range(10):
        key = find_key(d, parsed)

        if not key:
            break

        # remove deterministic ingredient for each allergen and loop 
        for k2 in d:
            if k2 != key:
                d[k2] -= parsed[key]
    
    return ','.join([str(x[1])[1:-1] for x in sorted(list(parsed.items()), key = lambda x: x[0])])


### insert how to parse line
def parse_line(line):
    ingredients, allergens = line.strip().split('(contains ')
    return set(ingredients.split()), set(allergens[:-1].split(', '))

def main():
    with open('input21.txt') as f:
    #with open('test.txt') as f:
        a = [parse_line(line) for line in f] 

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
