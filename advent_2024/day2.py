from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 2

    def parse_file(self, file):
        lst = []
        with open(file) as f:
            for x in f.read().splitlines():
                row = x.split()
                row = list(map(int, row))
                lst.append(row)

        return lst

    def is_safe(self, row):
        diffs = Counter()

        prev = row[0]
        diff = row[1] - row[0] 
        sign = 1 if diff > 0 else -1  # positive or negative diffs
        for idx in range(1, len(row)):
            num = row[idx]
            diff = sign * (num - prev)
            if diff in [1, 2, 3]:
                diffs[diff] += 1
            else:
                return False
            prev = num
        return True


    def pa(self, lst):
        total = 0
        for row in lst:
            total += self.is_safe(row)

        return total

    def is_safe_b(self, row):
        if self.is_safe(row):
            return 1

        # remove one element from list
        for idx in range(len(row)):
            new_row = row[:idx] + row[idx+1:]
            if self.is_safe(new_row):
                return 1

        return 0

    def pb(self, lst):
        total = 0
        for row in lst:
            total += self.is_safe_b(row)

        return total


if __name__ == "__main__":
    DaySubmitter().main()
