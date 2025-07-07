import sys
import math
from collections import defaultdict

def manhattan_distance(n):
    if n == 1:
        return 0
    layer = math.ceil((math.sqrt(n) - 1) / 2)
    side_len = 2 * layer
    max_val = (2 * layer + 1) ** 2
    steps_back = (max_val - n) % side_len
    return layer + abs(steps_back - layer)

def spiral_sum(threshold):
    grid = defaultdict(int, {(0, 0): 1})
    x = y = 0
    dx, dy = 1, 0
    steps = 1
    while True:
        for _ in range(2):
            for _ in range(steps):
                x += dx
                y += dy
                val = sum(grid[(x + i, y + j)]
                          for i in [-1, 0, 1]
                          for j in [-1, 0, 1])
                if val > threshold:
                    return val
                grid[(x, y)] = val
            dx, dy = -dy, dx
        steps += 1

def part1(data):
    return manhattan_distance(int(data[0]))

def part2(data):
    return spiral_sum(int(data[0]))

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")