import sys
import numpy as np
import heapq

def navigate(grid, minval, maxval):
    max_y, max_x = grid.shape[0] - 1, grid.shape[1] - 1
    goal = (max_y, max_x)
    heap = []
    heapq.heappush(heap, (0, 0, 0, 0))
    heapq.heappush(heap, (0, 0, 0, 1))
    seen = set()

    while heap:
        cost, y, x, direction = heapq.heappop(heap)
        if (y, x) == goal:
            return cost
        if (y, x, direction) in seen:
            continue
        seen.add((y, x, direction))
        for s in (-1, 1):
            new_cost = cost
            for i in range(1, maxval + 1):
                new_y = y + (i * s if direction == 0 else 0)
                new_x = x + (i * s if direction == 1 else 0)
                if new_x < 0 or new_y < 0 or new_x > max_x or new_y > max_y:
                    break
                new_cost += grid[new_y, new_x]
                if i >= minval and (new_y, new_x, 1 - direction) not in seen:
                    heapq.heappush(heap, (new_cost, new_y, new_x, 1 - direction))
    return -1

def part1(data):
    grid = np.array([[int(char) for char in line.strip()] for line in data])
    return navigate(grid, minval=1, maxval=3)

def part2(data):
    grid = np.array([[int(char) for char in line.strip()] for line in data])
    return navigate(grid, minval=4, maxval=10)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]
sys.stdout.write(f"{part1(data)} {part2(data)}")