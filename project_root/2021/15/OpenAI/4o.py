import sys
import numpy as np
import heapq

def dijkstra(grid, start, end):
    w, h = len(grid), len(grid[0])
    visited = set()
    min_heap = [(0, start)]
    while min_heap:
        cost, (x, y) = heapq.heappop(min_heap)
        if (x, y) == end:
            return cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                heapq.heappush(min_heap, (cost + grid[nx][ny], (nx, ny)))

def part1(data):
    grid = [[int(x) for x in line] for line in data.splitlines()]
    return dijkstra(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))

def part2(data):
    grid = np.array([[int(x) for x in line] for line in data.splitlines()])
    row = np.hstack([(grid + i - 1) % 9 + 1 for i in range(5)])
    grid = np.vstack([(row + i - 1) % 9 + 1 for i in range(5)])
    return dijkstra(grid, (0, 0), (grid.shape[0] - 1, grid.shape[1] - 1))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")