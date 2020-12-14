from collections import Counter, defaultdict
from utils import print_d

def mask_num(mask, bin_num):
    idx = 0
    for idx in range(len(bin_num)):
        if mask[idx] != 'X':
            bin_num[idx] = mask[idx]
    return int(''.join(bin_num), 2)

def p1(a):
    d = {}
    mask = None
    for ins, num in a:
        if ins == 'mask':
            mask = list(num)
        else:
            address = int(ins[4:-1])
            bin_num = list(str(bin(int(num)))[2:].zfill(36))
            d[address] = mask_num(mask, bin_num)

    return sum(d.values())

def mask_num_2(mask, bin_num):
    idx = 0
    for idx in range(len(bin_num)):
        if mask[idx] == '1':
            bin_num[idx] = '1'
        if mask[idx] == 'X':
            bin_num[idx] = 'X'
    return bin_num

import itertools
def decode(mem_str):
    all_addresses = []

    all_i = []
    for i, x in enumerate(mem_str):
        if x == 'X':
            all_i.append(i)

    for combo in itertools.product(['0','1'], repeat = len(all_i)):
        mem_str_copy = mem_str[:]
        for j, b in enumerate(list(combo)):
            mem_str_copy[all_i[j]] = b
        all_addresses.append(int(''.join(mem_str_copy), 2))

    return all_addresses


def p2(a):
    d = {}
    mask = None
    for ins, num in a:
        if ins == 'mask':
            mask = list(num)
        else:
            address = int(ins[4:-1])
            bin_num = list(str(bin(int(address)))[2:].zfill(36))
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
