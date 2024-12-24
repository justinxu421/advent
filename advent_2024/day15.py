from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 15

    def parse_file(self, file):
        with open(file) as f:
            a = [x.split() for x in f.read().splitlines()]
            return a

    def pa(self, rows):
        pass

    def pb(self, rows):
        pass


if __name__ == "__main__":
    DaySubmitter().main()
