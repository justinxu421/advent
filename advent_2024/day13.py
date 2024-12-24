from collections import Counter, defaultdict

import numpy as np

from typing import Union
from utils import AbstractDaySubmitter

COST_A = 3
COST_B = 1
REWARD_CHANGE = 10000000000000
class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        return 13
    
    def parse_line(self, line):
        a, b, prize = line.split('\n')
        ax, ay = a.strip("Button A: ").split(', ')
        ax, ay = int(ax.strip('X+')), int(ay.strip('Y+'))

        bx, by = b.strip("Button B: ").split(', ')
        bx, by = int(bx.strip('X+')), int(by.strip('Y+'))

        px, py = prize.strip("Prize: ").split(', ')
        px, py = int(px.strip('X=')), int(py.strip('Y='))

        return [ax, ay, bx, by, px, py]

    def parse_file(self, file: str) -> Union[list[list[str]], list[int], np.ndarray]:
        with open(file) as f:
            content = f.read().strip()
        
        sections = [self.parse_line(line) for line in content.split("\n\n")]
        return sections
 # Try parsing as space-separated values
    def solve_game(self, row):
        ax, ay, bx, by, px, py = row
        for b_press in range(100):
            bx_cost = b_press * bx
            by_cost = b_press * by

            a_presses_x = (px - bx_cost) / ax
            a_presses_y = (py - by_cost) / ay
            if a_presses_x.is_integer() and a_presses_x == a_presses_y:
                return b_press * COST_B + int(a_presses_x) * COST_A
        # tried all press amounst and didn't get an answer
        return 0

    def pa(self, rows):
        total = 0
        for row in rows:
            total += self.solve_game(row)
        return total

    def solve_game_b(self, row):
        ax, ay, bx, by, px, py = row
        px += REWARD_CHANGE 
        py += REWARD_CHANGE 
        for b_press in range(REWARD_CHANGE):
            bx_cost = b_press * bx
            by_cost = b_press * by

            a_presses_x = (px - bx_cost) / ax
            a_presses_y = (py - by_cost) / ay
            if a_presses_x < 0 or a_presses_y < 0:
                break
            if a_presses_x.is_integer() and a_presses_x == a_presses_y:
                return b_press * COST_B + int(a_presses_x) * COST_A
        # tried all press amounst and didn't get an answer
        return 0

    def pb(self, rows):
        total = 0
        for row in rows:
            total += self.solve_game_b(row)
        return total


if __name__ == "__main__":
    DaySubmitter().main()
