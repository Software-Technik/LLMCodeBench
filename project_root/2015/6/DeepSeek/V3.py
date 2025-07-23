import sys
import re
from collections import defaultdict

def part1(data):
    grid = defaultdict(int)
    op_map = {"turn on": 1, "turn off": 0, "toggle": -1}
    for inst in data:
        op, coord1, coord2 = re.findall(r"(.*)\s(\d+\,\d+)\sthrough\s(\d+\,\d+)", inst)[0]
        x1, y1 = map(int, coord1.split(","))
        x2, y2 = map(int, coord2.split(","))
        action = op_map[op]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == -1:
                    grid[(x, y)] ^= 1
                else:
                    grid[(x, y)] = action
    return sum(grid.values())

def part2(data):
    grid = defaultdict(int)
    op_map = {"turn on": 1, "turn off": -1, "toggle": 2}
    for inst in data:
        op, coord1, coord2 = re.findall(r"(.*)\s(\d+\,\d+)\sthrough\s(\d+\,\d+)", inst)[0]
        x1, y1 = map(int, coord1.split(","))
        x2, y2 = map(int, coord2.split(","))
        delta = op_map[op]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[(x, y)] += delta
                if grid[(x, y)] < 0:
                    grid[(x, y)] = 0
    return sum(grid.values())

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")