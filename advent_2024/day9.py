from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 9

    def parse_file(self, file):
        with open(file) as f:
            a = list(map(int, f.read().strip()))
            return a

    def init_arr(self, map):
        arr = []
        id = 0
        is_free = False
        id_mapping = []
        free_space_mapping = []

        for entry in map:
            if is_free:
                free_space_mapping.append((len(arr), entry))
                arr += ['.'] * entry
            else:
                id_mapping.append((len(arr), entry))
                arr += [id] * entry
                id += 1
            is_free = not is_free

        return arr, id_mapping, free_space_mapping

    def move_blocks(self, arr):
        begin, end = 0, len(arr) - 1
        while begin < end:
            if arr[begin] == '.':
                arr[begin], arr[end] = arr[end], arr[begin]
                begin += 1
                end -= 1
                while arr[end] == '.':
                    end -= 1
            else:
                begin += 1

    def get_checksum(self, arr):
        total = 0
        for index, entry in enumerate(arr):
            if entry != '.':
                total += index * entry
        return total


    def pa(self, map):
        arr, _, _ = self.init_arr(map)
        self.move_blocks(arr)
        return self.get_checksum(arr)

    def move_blocks_2(self, arr, id_mapping, free_space_mapping):
        for index, block_size in reversed(id_mapping):
            free_index = 0
            # loop through free spaces where index is left of the current file ID index 
            while free_index < len(free_space_mapping) and free_space_mapping[free_index][0] < index:
                # if free space is sufficient, then swap, update free space mapping and move on to next file ID 
                if free_space_mapping[free_index][1] >= block_size:
                    start = free_space_mapping[free_index][0]
                    end = start + block_size 
                    arr[start:end], arr[index:index + block_size] = arr[index:index + block_size], arr[start:end]
                    free_space_mapping[free_index] = (end, free_space_mapping[free_index][1] - block_size)
                    break
                free_index += 1

    def pb(self, map):
        arr, id_mapping, free_space_mapping = self.init_arr(map)
        self.move_blocks_2(arr, id_mapping, free_space_mapping)
        return self.get_checksum(arr)


if __name__ == "__main__":
    DaySubmitter().main()
