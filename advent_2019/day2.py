from intcode_deprecated import IntcodeRunner

def part_1(arr):
    arr[1] = 12
    arr[2] = 2
    ic = IntcodeRunner(arr)

    while ic.done == False:
        ic.run(0, 0)
    print(ic.arr[0])

def part_2(arr, target):
    for noun in range(100):
        for verb in range(100):
            arr_copy = arr[:]
            arr_copy[1] = noun
            arr_copy[2] = verb
            ic = IntcodeRunner(arr_copy)

            while ic.done == False:
                ic.run(0, 0)
            if ic.arr[0] == target:
                print(noun,verb)

     
with open('input2.txt') as f:
    arr = list(map(int, f.readline().strip().split(',')))
    part_1(arr[:])
    part_2(arr[:], 19690720)

