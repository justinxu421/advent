from intcode_deprecated import IntcodeRunner

def part_1(arr):
    ipt = 1
    ic = IntcodeRunner(arr)
    while ic.done == False:
        ic.run(ipt, ipt)
    print(ic.output)


def part_2(arr):
    ipt = 5
    ic = IntcodeRunner(arr)
    while ic.done == False:
        ic.run(ipt, ipt)
    print(ic.output)

with open('input5.txt') as f:
    arr = list(map(int, f.readline().strip().split(',')))
    part_1(arr[:])
    part_2(arr[:])
