from collections import Counter, defaultdict
from utils import print_d

# very clean way of getting a 36 bit string, not obscure or hacky at all
def get_bin_str(num):
    return list(str(bin(int(num)))[2:].zfill(36))

def get_int_from_bin(bin_num):
    return int(''.join(bin_num), 2)

def get_address(in_):
    return in_[4:-1]

def mask_num(mask, bin_num):
    idx = 0
    for idx in range(len(bin_num)):
        if mask[idx] != 'X':
            bin_num[idx] = mask[idx]
    return get_int_from_bin(bin_num)

def p1(a):
    d = {}
    mask = None
    for in_, num in a:
        if in_ == 'mask':
            mask = list(num)
        else:
            address = get_address(in_)
            d[address] = mask_num(mask, get_bin_str(num))

    return sum(d.values())

def mask_num_2(mask, bin_num):
    idx = 0
    for idx in range(len(bin_num)):
        if mask[idx] != '0':
            bin_num[idx] = mask[idx]
    return bin_num

import itertools
def decode(mem_str):
    all_addresses = []

    all_i = [i for i,x in enumerate(mem_str) if x == 'X']
    for combo in itertools.product(['0','1'], repeat = len(all_i)):
        mem_str_copy = mem_str[:]
        for j, b in enumerate(list(combo)):
            mem_str_copy[all_i[j]] = b
        all_addresses.append(int(''.join(mem_str_copy), 2))

    return all_addresses

def p2(a):
    d = {}
    mask = None
    for in_, num in a:
        if in_ == 'mask':
            mask = list(num)
        else:
            bin_num = get_bin_str(get_address(in_))
            mem_str = mask_num_2(mask, bin_num)
            addresses = decode(mem_str)

            for add in addresses:
                d[add] = int(num)

    return sum(d.values())

### insert how to parse line
def parse_line(line):
    return line.strip().split(' = ')

def main():
    with open('input14.txt') as f:
        a = [parse_line(line) for line in f] 
        print(a[:10])

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
