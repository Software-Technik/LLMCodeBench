import sys
from itertools import chain

def is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

def part1(data):
    return sum(is_triangle(row) for row in data)

def part2(data):
    vertical = list(chain.from_iterable(zip(*data)))
    return sum(is_triangle(vertical[i:i+3]) for i in range(0, len(vertical), 3))

with open(sys.argv[1], 'r') as infile:
    data = [[int(value) for value in row.split()] for row in infile]

sys.stdout.write(f"{part1(data)} {part2(data)}")