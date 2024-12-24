import argparse
import os
import shutil
import subprocess
from datetime import datetime

def create_day_file(day):
    # Read the template file
    with open('template.py', 'r') as template_file:
        template_content = template_file.read()

    # Replace the day number
    updated_content = template_content.replace(
        'raise NotImplementedError()',
        f'return {day}'
    )

    # Write the new day file
    with open(f'day{day}.py', 'w') as day_file:
        day_file.write(updated_content)

    print(f"Created day{day}.py for Advent of Code, Day {day}.")

def download_input(day):
    try:
        result = subprocess.run(['aocd', str(day)], 
                                capture_output=True, text=True, check=True)
        with open(f'input{day}.txt', 'w') as input_file:
            input_file.write(result.stdout)
        print(f"Downloaded input for Day {day} and saved as input{day}.txt")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading input: {e}")
        print(f"AOCD output: {e.output}")

def main():
    parser = argparse.ArgumentParser(description="Create a new day's file for Advent of Code")
    parser.add_argument('day', type=int, help='Day number')
    args = parser.parse_args()

    create_day_file(args.day)
    download_input(args.day)

if __name__ == "__main__":
    main()
