from collections import Counter, defaultdict
from utils import print_d

# intersect ingredients to get possible ingredients with allergens
def get_allergen_dict(a):
    d = {}
    for ingredients, allergens in a:
        for a_ in allergens:
            if a_ not in d:
                d[a_] = ingredients.copy()
            else:
                d[a_] = ingredients & d[a_]
    return d

def p1(a):
    a.sort(key = lambda x: len(x[1])) 
    d = get_allergen_dict(a)
    
    # loop through and or together to get removable ingredients
    remove = set()
    for v in d.values():
        remove |= v
    
    ingredients, allergens = zip(*a)
    return sum(len(ing - remove) for ing in ingredients)

# find the first key with length ingredient list
def find_key(d, parsed):
    for key in d:
        if key not in parsed and len(d[key]) == 1:
            parsed[key] = d[key]
            return key
    return None

def p2(a):
    a.sort(key = lambda x: len(x[1])) 
    d = get_allergen_dict(a)
    
    parsed = {}
    for _ in range(10):
        key = find_key(d, parsed)
        
        if not key:
            break
        
        # remove from ingredients and reconstruct allergen dict
        for ingredients, allergens in a:
            ingredients -= parsed[key]
            allergens -= set([key])
        d = get_allergen_dict(a)

        '''
        # remove deterministic ingredient for each allergen and loop 
        for k2 in d:
            if k2 != key:
                d[k2] -= parsed[key]
        '''

    return ','.join([str(x[1])[2:-2] for x in sorted(list(parsed.items()), key = lambda x: x[0])])


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
