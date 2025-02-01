from typing import Union
import numpy as np
from utils import AbstractDaySubmitter

"""
Advent of Code 2024 Day 13: Button Pressing Game

Each puzzle input describes a game with:
- Button A that moves (ax,ay) per press, costs 3 coins
- Button B that moves (bx,by) per press, costs 1 coin
- Target prize at coordinates (px,py)

Part 1: Find minimum cost to reach prize
Part 2: Same but prize coordinates are increased by 10^13
"""

COST_A = 3  # Cost per press of button A
COST_B = 1  # Cost per press of button B
REWARD_CHANGE = 10**13  # Amount prize moves in part 2
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

    def solve_game(self, row):
        """
        Solve for minimum cost to reach prize coordinates.
        Uses linear algebra to find exact solution rather than brute force.
        
        Returns cost of optimal solution, or 0 if no solution exists.
        """
        ax, ay, bx, by, px, py = row
        
        # System of equations:
        # ax*a + bx*b = px
        # ay*a + by*b = py
        # Where a,b are number of button presses
        
        det = ax*by - ay*bx
        if det == 0:  # No unique solution
            return 0
            
        # Solve using Cramer's rule
        a = (px*by - py*bx) / det
        b = (ax*py - ay*px) / det
        
        if a >= 0 and b >= 0 and a.is_integer() and b.is_integer():
            return int(a) * COST_A + int(b) * COST_B
        return 0

    def pa(self, rows):
        total = 0
        for row in rows:
            total += self.solve_game(row)
        return total

    def solve_game_b(self, row):
        """Same as solve_game but with shifted prize coordinates"""
        ax, ay, bx, by, px, py = row
        return self.solve_game([ax, ay, bx, by, 
                              px + REWARD_CHANGE, 
                              py + REWARD_CHANGE])

    def pb(self, rows):
        total = 0
        for row in rows:
            total += self.solve_game_b(row)
        return total


if __name__ == "__main__":
    DaySubmitter().main()
