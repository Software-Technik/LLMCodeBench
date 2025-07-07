import sys
import numpy as np
from heapq import heappop, heappush


def navigate(grid, minval, maxval):
    q = []
    max_y, max_x = (v - 1 for v in grid.shape)
    goal = (max_y, max_x)
    heappush(q, (0, 0, 0, 0))
    seen = set()

    while q:
        cost, y, x, direction = heappop(q)
        if (y, x) == goal:
            return cost
        if (y, x, direction) in seen:
            continue
        seen.add((y, x, direction))
        for s in [-1, 1]:
            new_y, new_x = y, x
            for i in range(1, maxval + 1):
                if direction == 1:
                    new_x = x + i * s
                else:
                    new_y = y + i * s
                if new_x < 0 or new_y < 0 or new_x > max_x or new_y > max_y:
                    break
                new_cost = cost + grid[new_y, new_x]
                if ((new_y, new_x, 1 - direction)) in seen:
                    continue
                if i >= minval:
                    heappush(q, (new_cost, new_y, new_x, 1 - direction))


def part1(data):
    grid = np.array([[int(char) for char in line] for line in data])
    return navigate(grid, minval=1, maxval=3)


def part2(data):
    grid = np.array([[int(char) for char in line] for line in data])
    return navigate(grid, minval=4, maxval=10)


input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f if line.strip()]
sys.stdout.write(f"{part1(data)} {part2(data)}")