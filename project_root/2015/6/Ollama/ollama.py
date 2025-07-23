import re
from itertools import cycle
from collections import defaultdict

def part1(data):
    grid = defaultdict(int)
    ops = ["turn on", "turn off", "toggle"]
    for inst in data:
        op, (x1, y1), (x2, y2) = re.match(r"(.*?)\s(\d+),\s*(\d+) through\s(\d+),\s*(\d+)", inst).groups()
        val = cycle([1, 0, -1]).next(lambda x: ops.index(op))

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[(x, y)] += val
    return sum(grid.values())

def part2(data):
    grid = defaultdict(int)
    for inst in data:
        op, (x1, y1), (x2, y2) = re.match(r"(.*?)\s(\d+),\s*(\d+) through\s(\d+),\s*(\d+)", inst).groups()
        delta = lambda x: cycle([1, -1]).next("off" in op)

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[(x, y)] += delta(op)
    return sum(grid.values())

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")