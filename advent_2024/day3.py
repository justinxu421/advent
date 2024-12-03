from collections import Counter, defaultdict

import numpy as np
import re

from utils import AbstractDaySubmitter

VALID = "mul(X,Y)"
x_idx = 4
y_idx = 6

class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 3

    def parse_file(self, file):
        with open(file) as f:
            a = f.read().strip()
            return a

    def reset(self):
        self.idx = 0
        self.x = None
        self.y = None

    def pa(self, lst):
        pattern = r"mul\(\d+,\d+\)"
        total = 0 
        matches = re.findall(pattern, lst)
        for match in matches:
            x, y = match.strip('mul(').strip(')').split(',')
            total += int(x) * int(y)

        return total

    def pb(self, lst):
        pattern = r"mul\(\d+,\d+\)"
        pattern_do = r"do()"
        pattern_dont = r"don't()"
        
        d = {}
        for do in re.finditer(pattern_do, lst):
            d[do.start()] = pattern_do
        for dont in re.finditer(pattern_dont, lst):
            d[dont.start()] = pattern_dont
        for match in re.finditer(pattern, lst):
            d[match.start()] = match.group()

        # sort matching regexes in ascending index order
        sorted_d = sorted(d.items())

        total = 0 
        on = True
        for _, val in sorted_d:
            if val == pattern_dont:
                on = False
            elif val == pattern_do:
                on = True
            elif on == True:
                x, y = val.strip('mul(').strip(')').split(',')
                total += int(x) * int(y)

        return total



if __name__ == "__main__":
    DaySubmitter().main()
