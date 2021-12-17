from collections import Counter, defaultdict
import numpy as np


def parse_packets(type_, packets):
    if type_ == 0:
        return sum(packets)
    elif type_ == 1:
        return np.prod(packets)
    elif type_ == 2:
        return min(packets)
    elif type_ == 3:
        return max(packets)
    elif type_ == 5:
        assert len(packets) == 2 
        return int(packets[0] > packets[1])
    elif type_ == 6:
        assert len(packets) == 2 
        return int(packets[0] < packets[1])
    elif type_ == 7:
        assert len(packets) == 2 
        return int(packets[0] == packets[1])


def convert_hex(a):
    bin_str = bin(int(a, 16))[2:].zfill(len(a) * 4)
    return bin_str


def handle_literal(bin_str, i):
    total_str = ""
    while i < len(bin_str):
        first = bin_str[i]
        i += 1
        total_str += bin_str[i : i + 4]
        i += 4
        # last iteration
        if first == "0":
            break

    literal_eval = int(total_str, 2)
    return i, literal_eval


def handle_length_type_0(bin_str, versions, i):
    # read next 15 bits and sum to length
    L = int(bin_str[i : i + 15], 2)
    i += 15

    old_i = i
    packets = []
    while i - old_i < L:
        i, packet = decode(bin_str, versions, i)
        packets.append(packet)
    return i, packets


def handle_length_type_1(bin_str, versions, i):
    # read next 11 bits and run that many cycles
    num = int(bin_str[i : i + 11], 2)
    i += 11

    packets = []
    for _ in range(num):
        i, packet = decode(bin_str, versions, i)
        packets.append(packet)
    return i, packets


def decode(bin_str, versions, i):
    V = bin_str[i : i + 3]
    i += 3
    T = bin_str[i : i + 3]
    i += 3

    version = int(V, 2)
    versions.append(version)

    type_ = int(T, 2)
    if type_ == 4:
        return handle_literal(bin_str, i)
    else:
        I = bin_str[i]
        i += 1
        if I == "0":
            i, packets = handle_length_type_0(bin_str, versions, i)
        elif I == "1":
            i, packets = handle_length_type_1(bin_str, versions, i)
        return i, parse_packets(type_, packets)

    return i, None


def p1(a):
    bin_str = convert_hex(a)
    versions = []
    decode(bin_str, versions, 0)
    return sum(versions)


def p2(a):
    bin_str = convert_hex(a)
    return decode(bin_str, [], 0)[1]


def run(file):
    with open(file) as f:
        a = f.read().strip()
        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input16.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
