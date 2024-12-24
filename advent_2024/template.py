from collections import Counter, defaultdict

import numpy as np

from utils import AbstractDaySubmitter


class DaySubmitter(AbstractDaySubmitter):
    def day(self):
        raise NotImplementedError()

    def parse_file(self, file: str) -> list[list[str]] | list[int] | np.ndarray:
        with open(file) as f:
            content = f.read().strip()
 # Try parsing as space-separated values
        if ' ' in content:
            return [line.split() for line in content.splitlines()]
        
        # Try parsing as comma-separated values
        elif ',' in content:
            return [line.split(',') for line in content.splitlines()]
        
        # Try parsing as a single column of integers
        elif content.replace('\n', '').isdigit():
            return [int(line) for line in content.splitlines()]
        
        # Try parsing as a 2D grid
        elif all(len(line) == len(content.splitlines()[0]) for line in content.splitlines()):
            return np.array([list(line) for line in content.splitlines()])
        
        # Default: return as list of strings
        else:
            return content.splitlines()

    def pa(self, rows):
        pass

    def pb(self, rows):
        pass


if __name__ == "__main__":
    DaySubmitter().main()
