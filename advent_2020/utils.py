from collections import defaultdict, Counter

# print an array
def print_arr(a):
    for x in a:
        print(''.join(x))

# print an array in dictionary form
def print_d(d):
    xs = [x for x,y in d]
    ys = [y for x,y in d]
    
    for x in range(min(xs), max(xs)+1):
        row = []
        for y in range(min(ys), max(ys)+1):
            row.append(d[x,y])
        print(''.join(row))
    print()




