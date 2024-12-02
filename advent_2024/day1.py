from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 1

    def pa(self, lst):
        left = [int(x[0]) for x in lst]
        right = [int(x[1]) for x in lst]
        left.sort()
        right.sort()

        total = 0
        for num1, num2 in zip(left, right):
            diff = abs(num1 - num2)
            total += diff
        return total

    def pb(self, lst):
        left = [int(x[0]) for x in lst]
        right = [int(x[1]) for x in lst]
        right_counter = Counter(right)

        total = 0
        for num in left:
            total += num * right_counter[num]
        return total

    def parse_file(self, file):
        with open(file) as f:
            a = [x.split() for x in f.read().splitlines()]
            return a


if __name__ == "__main__":
    DaySubmitter().main()
