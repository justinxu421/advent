from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 7

    def parse_file(self, file):
        with open(file) as f:
            a = [x.split(": ") for x in f.read().splitlines()]
            return a

    def evaluate_2(self, total, nums):
        if len(nums) == 0:
            return False

        if len(nums) == 1:
            return total == nums[0]

        a, b = nums[0], nums[1]
        case_1 = [a + b] + nums[2:]
        case_2 = [a * b] + nums[2:]

        return self.evaluate_2(total, case_1) or self.evaluate_2(total, case_2)

    def pa(self, rows):
        total = 0
        for row in rows:
            total_row, nums = row
            total_row = int(total_row)
            nums = list(map(int, nums.split()))
            if self.evaluate_2(total_row, nums):
                total += total_row

        return total

    def evaluate_2(self, total, nums):
        if len(nums) == 0:
            return False

        if len(nums) == 1:
            return total == nums[0]

        a, b = nums[0], nums[1]
        case_1 = [a + b] + nums[2:]
        case_2 = [a * b] + nums[2:]
        case_3 = [int(str(a) + str(b))] + nums[2:]

        return self.evaluate_2(total, case_1) or self.evaluate_2(total, case_2) or self.evaluate_2(total, case_3)

    def pb(self, rows):
        total = 0
        for row in rows:
            total_row, nums = row
            total_row = int(total_row)
            nums = list(map(int, nums.split()))
            if self.evaluate_2(total_row, nums):
                total += total_row

        return total
        pass


if __name__ == "__main__":
    DaySubmitter().main()
