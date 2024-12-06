import copy
from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 6

    def parse_file(self, file):
        with open(file) as f:
            a = np.array([list(x) for x in f.read().splitlines()])
            return a

    def in_bounds(self, cur, lst):
        return (
            cur[0] >= 0 and cur[0] < len(lst) and cur[1] >= 0 and cur[1] < len(lst[0])
        )

    def get_cur(self, lst):
        cur = (0, 0)
        for x in range(len(lst)):
            for y in range(len(lst[0])):
                if lst[x][y] == "^":
                    cur = (x, y)
        return cur

    def traverse(self, arr, cur):
        dir = dirs[0]
        
        # steps = 0
        visited = set()
        visited_dirs = set()
        while self.in_bounds(cur, arr):
            # already visited with direction, cause loop
            if (cur, dir) in visited_dirs:
                return False

            visited.add(cur)
            visited_dirs.add((cur, dir))

            new_cur = (cur[0] + dir[0], cur[1] + dir[1])
            # if hit wall rotate 90 until no longer wall and take a step
            while self.in_bounds(new_cur, arr) and arr[new_cur] == "#":
                dir = dirs[(dirs.index(dir) + 1) % 4]
                new_cur = (cur[0] + dir[0], cur[1] + dir[1])
            cur = new_cur
        return visited

    def pa(self, lst):
        cur = self.get_cur(lst)
        return len(self.traverse(lst, cur))

    def pb(self, lst):
        cur = self.get_cur(lst)

        total = 0
        visited = self.traverse(lst, cur)
        # loop through all and add an obstacle
        for x, y in visited - {cur}:
            lst_copy = copy.deepcopy(lst)
            lst_copy[x, y] = "#"
            result = self.traverse(lst_copy, cur)
            if result == False:
                total += 1
        return total


if __name__ == "__main__":
    DaySubmitter().main()
