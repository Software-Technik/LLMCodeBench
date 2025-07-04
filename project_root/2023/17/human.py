from queue import PriorityQueue
import sys
import numpy as np

def navigate(grid, minval, maxval):
    q = PriorityQueue()
    max_y, max_x = (v - 1 for v in grid.shape)
    goal = max_y, max_x
    q.put((0, (0, 0, 0)))
    q.put((0, (0, 0, 1)))
    seen = set()

    while q:
        cost, (y, x, direction) = q.get()
        if (y, x) == goal:
            break
        if (y, x, direction) in seen:
            continue
        seen.add((y, x, direction))
        original_cost = cost
        for s in [-1, 1]:
            cost = original_cost
            new_y, new_x = y, x
            for i in range(1, maxval + 1):
                if direction == 1:
                    new_x = x + i * s
                else:
                    new_y = y + i * s
                if new_x < 0 or new_y < 0 or new_x > max_x or new_y > max_y:
                    break
                cost += grid[new_y, new_x]
                if ((new_y, new_x, 1 - direction)) in seen:
                    continue
                if i >= minval:
                    q.put((cost, (new_y, new_x, 1 - direction)))
    return cost



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