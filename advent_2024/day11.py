import math
from collections import Counter, defaultdict
from functools import cache

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 11

    def parse_file(self, file):
        with open(file) as f:
            a = list(map(int, f.read().strip().split()))
            return a

    def process_num(self, num):
        if num == 0:
            return [1]

        num_str = str(num)
        if len(num_str) % 2 == 0:
            half_digits = len(num_str) // 2
            first = int(num_str[:half_digits])
            second = int(num_str[half_digits:])
            return [first, second]
        else:
            return [2024 * num]

    def blink(self, nums):
        new_nums = []

        for num in nums:
            new_nums.extend(self.process_num(num))
        return new_nums

    @cache
    def get_num_digits(self, num, iters_remain):
        if iters_remain == 0:
            return 1
        total = 0
        nums = self.process_num(num)
        for _num in nums:
            total += self.get_num_digits(_num, iters_remain - 1)
        return total

    def pa(self, rows):
        total = 0
        for num in rows:
            total += self.get_num_digits(num, 25)
        return total

    def pb(self, rows):
        total = 0
        for num in rows:
            total += self.get_num_digits(num, 75)
        return total

if __name__ == "__main__":
    DaySubmitter().main()
