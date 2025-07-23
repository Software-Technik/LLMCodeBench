import sys
import heapq
import numpy as np

def part1(data):
    grid = [[int(x) for x in line] for line in data.splitlines()]
    rows, cols = len(grid), len(grid[0])
    heap = [(0, 0, 0)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == rows - 1 and y == cols - 1:
            return cost
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                heapq.heappush(heap, (cost + grid[nx][ny], nx, ny))
    return -1

def part2(data):
    grid = np.array([[int(x) for x in line] for line in data.splitlines()])
    row = np.hstack([(grid + i - 1) % 9 + 1 for i in range(5)])
    grid = np.vstack([(row + i - 1) % 9 + 1 for i in range(5)])
    rows, cols = grid.shape
    heap = [(0, 0, 0)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == rows - 1 and y == cols - 1:
            return cost
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                heapq.heappush(heap, (cost + grid[nx, ny], nx, ny))
    return -1

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")