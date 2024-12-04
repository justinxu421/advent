from collections import Counter, defaultdict
from copy import deepcopy

import numpy as np

from utils import AbstractDaySubmitter

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
# dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 4

    def parse_file(self, file):
        with open(file) as f:
            a = [list(x) for x in f.read().splitlines()]
            return a

    def check_dir(self, lst, i, j, dir_x, dir_y):
        for idx in range(4):
            new_i, new_j = i + idx * dir_x, j + idx * dir_y
            if new_i < 0 or new_i >= len(lst) or new_j < 0 or new_j >= len(lst[0]):
                return 0
            if lst[new_i][new_j] != "XMAS"[idx]:
                return 0

        return 1

    def check_dirs(self, lst, i, j):
        total = 0
        for dir_x, dir_y in dirs:
            total += self.check_dir(lst, i, j, dir_x, dir_y)

        return total

    def pa(self, lst):
        lst = np.array(lst)
        total = 0
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                if lst[i, j] == "X":
                    total += self.check_dirs(lst, i, j)

        return total

    def check_x(self, lst, i, j):
        m_coords = []
        s_coords = []

        # lst[i][j] == "A", check the 4 corners for M/S
        for dir_x, dir_y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = i + dir_x, j + dir_y
            if new_i < 0 or new_i >= len(lst) or new_j < 0 or new_j >= len(lst[0]):
                return 0  # out of bounds

            letter = lst[new_i][new_j]
            if letter == "M":
                m_coords.append((new_i, new_j))
            elif letter == "S":
                s_coords.append((new_i, new_j))
            else:
                return 0

        if len(m_coords) != 2 or len(s_coords) != 2:
            return 0
        i0, j0 = m_coords[0]
        i1, j1 = m_coords[1]
        """diagonal case
        M.S
        .A.
        S.M
        """
        if i0 != i1 and j0 != j1:
            return 0

        return 1

    def pb(self, lst):
        "MAS in an X shape"
        total = 0
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                if lst[i][j] == "A":
                    total += self.check_x(lst, i, j)

        return total


if __name__ == "__main__":
    DaySubmitter().main()
