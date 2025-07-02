import sys
import math, itertools

def part1(data):
    return sum(sum(a := [*map(int, i.split("x"))]) ** 2 - sum(i * i for i in a) + min([math.prod(i) for i in itertools.combinations(a, 2)]) for i in data)

def part2(data):
    return sum(2 * sum((a := sorted(map(int, i.split("x"))))[:2]) + math.prod(a) for i in data)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")