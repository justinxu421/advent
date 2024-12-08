from collections import Counter, defaultdict
import itertools

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 8

    def parse_file(self, file):
        with open(file) as f:
            a = [list(x) for x in f.read().splitlines()]
            return a

    def inbounds(self, i, j, rows):
        return 0 <= i < len(rows) and 0 <= j < len(rows[0])

    def get_antinodes(self, rows, pair):
        antinodes = set()

        coord_1, coord_2 = pair
        i_1, j_1 = coord_1
        i_2, j_2 = coord_2
        diff_i = i_2 - i_1
        diff_j = j_2 - j_1

        antinode_1 = (i_1 - diff_i, j_1 - diff_j)
        antinode_2 = (i_2 + diff_i, j_2 + diff_j)
        if self.inbounds(*antinode_1, rows):
            antinodes.add(antinode_1)
        if self.inbounds(*antinode_2, rows):
            antinodes.add(antinode_2)
        return antinodes

    def get_nodes(self, rows):
        nodes = defaultdict(list)
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                if rows[i][j] != ".":
                    nodes[rows[i][j]].append((i, j))
        return nodes


    def pa(self, rows):
        all_antinodes = set()

        nodes = self.get_nodes(rows)
        for node, coords in nodes.items():
            for pair in itertools.combinations(coords, 2):
                antinodes = self.get_antinodes(rows, pair)
                all_antinodes |= antinodes

        return len(all_antinodes)

    def get_antinodes_2(self, rows, pair):
        antinodes = set()

        coord_1, coord_2 = pair
        antinodes.add(coord_1)
        antinodes.add(coord_2)
        i_1, j_1 = coord_1
        i_2, j_2 = coord_2
        diff_i = i_2 - i_1
        diff_j = j_2 - j_1

        antinode_1 = (i_1 - diff_i, j_1 - diff_j)
        antinode_2 = (i_2 + diff_i, j_2 + diff_j)
        while self.inbounds(*antinode_1, rows):
            antinodes.add(antinode_1)
            antinode_1 = (antinode_1[0] - diff_i, antinode_1[1] - diff_j)
        while self.inbounds(*antinode_2, rows):
            antinodes.add(antinode_2)
            antinode_2 = (antinode_2[0] + diff_i, antinode_2[1] + diff_j)
        return antinodes

    def pb(self, rows):
        all_antinodes = set()
        nodes = self.get_nodes(rows)
        for node, coords in nodes.items():
            for pair in itertools.combinations(coords, 2):
                antinodes = self.get_antinodes_2(rows, pair)
                all_antinodes |= antinodes
        return len(all_antinodes)


if __name__ == "__main__":
    DaySubmitter().main()
