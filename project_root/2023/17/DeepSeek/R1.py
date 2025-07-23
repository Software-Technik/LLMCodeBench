import heapq
import sys
import numpy as np

def navigate(grid, minval, maxval):
    rows, cols = grid.shape
    goal = (rows - 1, cols - 1)
    dist = np.full((rows, cols, 2), np.inf)
    heap = []
    dist[0, 0, 0] = 0
    dist[0, 0, 1] = 0
    heapq.heappush(heap, (0, 0, 0, 0))
    heapq.heappush(heap, (0, 0, 0, 1))
    
    while heap:
        cost, y, x, d = heapq.heappop(heap)
        if (y, x) == goal:
            return cost
        if cost > dist[y, x, d]:
            continue
        nd = 1 - d
        for s in (-1, 1):
            ny, nx = y, x
            ncost = cost
            for step in range(1, maxval + 1):
                if nd == 1:
                    nx = x + s * step
                else:
                    ny = y + s * step
                if ny < 0 or ny >= rows or nx < 0 or nx >= cols:
                    break
                ncost += grid[ny, nx]
                if step < minval:
                    continue
                if ncost < dist[ny, nx, nd]:
                    dist[ny, nx, nd] = ncost
                    heapq.heappush(heap, (ncost, ny, nx, nd))
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