from collections import Counter, defaultdict

import numpy as np
from utils import AbstractDaySubmitter

class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 1

    def pa(self, a):
        pass


    def pb(self, a):
        pass


    def parse_file(self, file):
        with open(file) as f:
            a = [x.split() for x in f.read().splitlines()]
            return a

if __name__ == "__main__":
     DaySubmitter().main()
