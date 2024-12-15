from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 12

    def parse_file(self, file):
        with open(file) as f:
            a = [list(x) for x in f.read().splitlines()]
            return np.array(a)

    def get_coords(self, rows, key, i, j):
        coords = set()
        coords.add((i, j))

        q = [(i, j)]
        while q:
            x, y = q.pop()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(rows)
                    and 0 <= ny < len(rows[0])
                    and (nx, ny) not in coords
                    and rows[nx, ny] == key
                ):
                    q.append((nx, ny))
                    coords.add((nx, ny))
        return coords

    def get_regions(self, rows):
        mapping = defaultdict(set)
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                mapping[rows[i, j]].add((i, j))

        regions = {}
        for key in mapping:
            index = 0
            while mapping[key]:
                i, j = list(mapping[key])[0]
                coords = self.get_coords(rows, key, i, j)
                regions[(key, index)] = coords
                mapping[key] -= coords
                index += 1

        return regions

    def get_area(self, region):
        return len(region)

    def get_perimeter(self, region):
        adjacent = 0
        for i, j in region:
            for dx, dy in dirs:
                if (i + dx, j + dy) in region:
                    adjacent += 1
        return 4 * len(region) - adjacent

    def pa(self, rows):
        regions = self.get_regions(rows)

        price = 0
        for key, coords in regions.items():
            area = self.get_area(coords)
            perimeter = self.get_perimeter(coords)
            print(key, area, perimeter)
            price += area * perimeter
        return price

    def get_sides(self, region):
        corners = 0
        for i, j in region:
            NW, W, SW, N, S, NE, E, SE = [
                (i + x, j + y) in region
                for x in range(-1, 2)
                for y in range(-1, 2)
                if x != 0 or y != 0
            ]
            corners += sum(
                [
                    N and W and not NW,
                    N and E and not NE,
                    S and W and not SW,
                    S and E and not SE,
                    not (N or W),
                    not (N or E),
                    not (S or W),
                    not (S or E),
                ]
            )
        return corners

    def pb(self, rows):
        regions = self.get_regions(rows)

        price = 0
        for key, coords in regions.items():
            area = self.get_area(coords)
            sides = self.get_sides(coords)
            print(key, area, sides)
            price += area * sides
        return price


if __name__ == "__main__":
    DaySubmitter().main()
