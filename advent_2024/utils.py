from abc import ABC ,abstractmethod
import argparse
from aocd import submit

class AbstractDaySubmitter(ABC):
    def __init__(self) -> None:
        super().__init__()

    @property
    def file_name(self):
        return f"input{self.day()}.txt"

    @abstractmethod
    def day(self) -> int:
        """Day we are solving"""
        pass

    @abstractmethod
    def parse_file(self, file) -> list:
        """Implementation of some way to parse input file {file}"""
        pass

    @abstractmethod
    def pa(self, lst) -> int:
        """Implementation of part a"""
        pass

    @abstractmethod
    def pb(self, lst) -> int:
        """Implementation of part b"""
        pass

    def run(self, file):
        print(f"Run cases for {file}")
        a = self.parse_file(file)
        print(f"Part 1: {self.pa(a)}")
        print(f"Part 2: {self.pb(a)}")


    def submit_part_a(self):
        print(f"Submitting part a answer with {self.file_name}")
        a = self.parse_file(self.file_name)
        answer = self.pa(a)
        print(answer)
        submit(answer, part="a", day=self.day(), year=2024)


    def submit_part_b(self):
        print(f"Submitting part b answer with {self.file_name}")
        a = self.parse_file(self.file_name)
        answer = self.pb(a)
        print(answer)
        submit(answer, part="b", day=self.day(), year=2024)

    def main(self):
        """
        Main function to handle running the program on various input texts
        as well as submittins answers with command line arguments -sa and -sb
        """

        parser = argparse.ArgumentParser(prog="myprogram")
        parser.add_argument(
            "-a", "--submita", action="store_true", default=False, help="Submit part a"
        )
        parser.add_argument(
            "-b", "--submitb", action="store_true", default=False, help="Submit part b"
        )
        parser.add_argument(
            "-t", "--runtest", action="store_true", default=False, help="Only run on test.txt"
        )
        args = parser.parse_args()

        if args.submita:
            self.submit_part_a()

        elif args.submitb:
            self.submit_part_b()
        elif args.runtest:
            self.run("test.txt")
        else:
            test_files = [
                "test.txt",
                self.file_name,
            ]
            for file in test_files:
                self.run(file)


