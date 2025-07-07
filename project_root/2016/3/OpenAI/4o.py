import sys
from itertools import chain

def is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

def part1(horizontal):
    return sum(is_triangle(row) for row in horizontal)

def part2(vertical):
    return sum(is_triangle(vertical[i:i+3]) for i in range(0, len(vertical), 3))

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.readlines()

horizontal = [[int(value) for value in row.split()] for row in data]
vertical = list(chain.from_iterable(zip(*horizontal)))

sys.stdout.write(f"{part1(horizontal)} {part2(vertical)}")