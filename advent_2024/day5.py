from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 5

    def parse_file(self, file):
        with open(file) as f:
            a, b = f.read().split("\n\n")
            all_rules = [list(map(int, x.split("|"))) for x in a.splitlines()]
            pages_list  = [list(map(int, x.split(","))) for x in b.splitlines()]
            return all_rules, pages_list

    def parse_rules(self, all_rules):
        # mapping from before page to set of after pages
        rules = defaultdict(set)

        for before, after in all_rules:
            rules[before].add(after)
        return rules

    def topo_sort(self, valid_rules):
        before_keys = set(before for before, _ in valid_rules)
        after_keys = set(after for _, after in valid_rules)
        start = list(before_keys - after_keys)[0]
        rules = self.parse_rules(valid_rules)

        order = []
        visited = set()
        def topo_helper(node):
            for neighbor in rules[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    topo_helper(neighbor)
            order.append( node)

        topo_helper(start)
        return order[::-1]

    def get_valid_order(self, all_rules, pages):
        valid_rules = []
        for before, after in all_rules:
            pages_set = set(pages)
            if before in pages_set and after in pages_set:
                valid_rules.append([before, after])

        return self.topo_sort(valid_rules)

    def pa(self, lst):
        all_rules, pages_list = lst

        total = 0    
        for pages in pages_list:
            order = self.get_valid_order(all_rules, pages)
            if order == pages:
                total += pages[len(pages) // 2]

        return total

    def reorder(self, pages: list, order: list):
        indices = []
        for page in pages:
            indices.append(order.index(page))
        indices.sort()

        middle_index = indices[len(indices) // 2]
        return order[middle_index]

    def pb(self, lst):
        all_rules, pages_list = lst

        total = 0
        for pages in pages_list:
            order = self.get_valid_order(all_rules, pages)
            if order == pages:
                continue
            new_middle = self.reorder(pages, order)
            total += new_middle

        return total


if __name__ == "__main__":
    DaySubmitter().main()
