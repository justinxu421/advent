from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 5

    def parse_file(self, file):
        with open(file) as f:
            a, b = f.read().split("\n\n")
            a = [list(map(int, x.split("|"))) for x in a.splitlines()]
            b = [list(map(int, x.split(","))) for x in b.splitlines()]
            return a, b

    def check_pages(self, pages, rules, reverse_rules):
        seen = set()
        # go in reverse order
        for page in pages:
            seen.add(page)
            if page in reverse_rules:
                befores = rules[page]
                # violation of rule
                if len(seen & befores) > 0:
                    return 0

        seen = set()
        for page in reversed(pages):
            seen.add(page)
            if page in rules:
                afters = reverse_rules[page]
                # violation of rule
                if len(seen & afters) > 0:
                    return 0
        return pages[len(pages) // 2]

    def parse_rules(self, a):
        # mapping from before page to set of after pages
        rules = defaultdict(set)
        reverse_rules = defaultdict(set)

        for before, after in a:
            rules[before].add(after)
            reverse_rules[after].add(before)
        return rules, reverse_rules

    def pa(self, lst):
        a, b = lst
        rules, reverse_rules = self.parse_rules(a)

        total = 0
        for pages in b:
            middle = self.check_pages(pages, rules, reverse_rules)
            total += middle

        return total

    def reorder(self, pages: list, order: list):
        indices = []
        for page in pages:
            indices.append(order.index(page))
        indices.sort()

        middle_index = indices[len(indices) // 2]
        return order[middle_index]
    
    def topo_sort(self, rules, reverse_rules):
        start = list(set(rules.keys()) - set(reverse_rules.keys()))[0]
        # topo sort rules
        order = []
        stack = []
        visited = set()
        q = [start]
        while q:
            node = q.pop()
            if node not in visited:
                visited.add(node)
                q.extend(rules[node])
                while stack and node not in rules[stack[-1]]: # new stuff here!
                    order.append(stack.pop())
                stack.append(node)
        return stack + order[::-1]

    def get_valid_rules(self, a, pages):
        valid_rules = []
        for before, after in a:
            pages_set = set(pages)
            if before in pages_set and after in pages_set:
                valid_rules.append([before, after])

        rules, reverse_rules = self.parse_rules(valid_rules)
        return self.topo_sort(rules, reverse_rules)

    def pb(self, lst):
        a, b = lst
        rules, reverse_rules = self.parse_rules(a)

        total = 0
        for pages in b:
            middle = self.check_pages(pages, rules, reverse_rules)
            if middle == 0:
                order = self.get_valid_rules(a, pages)
                new_middle = self.reorder(pages, order)
                total += new_middle

        return total


if __name__ == "__main__":
    DaySubmitter().main()
