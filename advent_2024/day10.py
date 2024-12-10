from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 10

    def parse_file(self, file):
        with open(file) as f:
            a = [list(map(int, list(x))) for x in f.read().splitlines()]
            return np.array(a)

    def get_starts(self, rows):
        starts = []
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                if rows[i, j] == 0:
                    starts.append((i, j))
        return starts


    def pa(self, rows):
        starts = self.get_starts(rows)

        score = 0
        for start in starts:
            q = [start]
            visited = set()
            while q:
                x, y = q.pop()
                height = rows[x, y]
                if height == 9:
                    score += 1
                visited.add((x, y))
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < len(rows)
                        and 0 <= ny < len(rows[0])
                        and (nx, ny) not in visited
                        and rows[nx, ny] == height + 1
                    ):
                        q.append((nx, ny))

        return score  

    def pb(self, rows):
        starts = self.get_starts(rows)

        rating_total = 0
        for start in starts:
            rating = 0
            q = [start]
            while q:
                x, y = q.pop()
                height = rows[x, y]
                if height == 9:
                    rating += 1
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < len(rows)
                        and 0 <= ny < len(rows[0])
                        and rows[nx, ny] == height + 1
                    ):
                        q.append((nx, ny))
            print(start, rating)
            rating_total += rating

        return rating_total



if __name__ == "__main__":
    DaySubmitter().main()
