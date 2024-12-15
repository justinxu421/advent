from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 12

    def parse_file(self, file):
        with open(file) as f:
            a = [list(x) for x in f.read().splitlines()]
            return np.array(a)

    def get_regions(self, rows):
        pass

    def pa(self, rows):
        self.get_regions(rows)
        mapping = defaultdict(list)
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                mapping[rows[i, j]].append((i, j))
        print(mapping)

        pass

    def pb(self, rows):
        pass


if __name__ == "__main__":
    DaySubmitter().main()
