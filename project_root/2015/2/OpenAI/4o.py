import sys
from itertools import combinations
from functools import reduce

def part1(data):
    total = 0
    for dim in data:
        a, b, c = map(int, dim.split("x"))
        side1, side2, side3 = a * b, b * c, c * a
        min_side = min(side1, side2, side3)
        total += 2 * (side1 + side2 + side3) + min_side
    return total

def part2(data):
    total = 0
    for dim in data:
        a, b, c = sorted(map(int, dim.split("x")))
        total += 2 * (a + b) + a * b * c
    return total

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")