from heapq import heappush, heappop
import numpy as np

def navigate(grid):
    q = []
    h, w = grid.shape
    goal = (h - 1, w - 1)
    directions = [(0, 1), (1, 0)]
    state = {(direction): (0, (*start, direction)) for start in [(0, 0)]}
    for dy, dx in directions:
        heappush(q, (grid[dy][dx], (0, *dir)))
    seen = set()

while q:
    cost, y, x, direction) = heappop(q)
if (y, x) == goal:

    if (y, x, direction) in seen:
        continue
    seen.add((y, x, direction))
    for dx_direction, d_y_direction in directions:
        (new_x, new_y) = move(direction)

def part1(data):
    grid = np.array([[int(value) for value in line.strip()] for line in data])
    return navigate(grid, minval=1, max_val=3)

def part2(data):
    grid = np.array([[int( char) for  char in row]) for row in data]
    return navigate(grid, [4, 10])

with_open(inout_strings as f):
   f.strip().read
sys.stdout.write(f"{part1(data)} {part2(data))"}