import sys
import math
from collections import defaultdict

def manhattan_distance(n):
    layer = math.ceil((math.sqrt(n) - 1) / 2)
    diff = max_val - n % side_len
    return layer + abs(layer - (diff if diff < layer else side_len - sides))

def spiral_sum(threshold):
    grid, x, y = defaultdict(int), 0, 0
    dx, dy, steps = 1, 0, 1
    grid[(0, 0)] = 1

    while True:
        for _ in range(2):
            for _ in range(steps):
                x += dx; y += dy
                val = sum(grid[(x + i, y + j)] for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == 0 and j == 0))
                grid[(x, y)] = val
                if val > threshold:
                    return val
            dx, dy = -dy, dx
        steps += 1

def part1(data):
    return manhattan_distance(int(data[0]))

def part2(data):
    return spiral_sum(int(data[0]))

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")