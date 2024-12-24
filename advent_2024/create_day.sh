#!/bin/bash

# Check if a day number was provided
if [ $# -eq 0 ]; then
    echo "Please provide a day number."
    exit 1
fi

DAY=$1
YEAR=2024  # Change this if needed

# Clone template.py and replace the day number
cp template.py day${DAY}.py
sed -i.bak "s/raise NotImplementedError()/return ${DAY}/" day${DAY}.py
rm day${DAY}.py.bak  # Remove the backup file created by sed

# Create input file using aocd
aocd ${DAY} > input${DAY}.txt

echo "Created day${DAY}.py and input${DAY}.txt for Advent of Code ${YEAR}, Day ${DAY}."
