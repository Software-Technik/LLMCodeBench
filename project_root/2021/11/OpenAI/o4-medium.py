import sys

def step(grid):
    n, m = len(grid), len(grid[0])
    flashed = [[False]*m for _ in range(n)]
    stack = []
    for i in range(n):
        for j in range(m):
            grid[i][j] += 1
            if grid[i][j] > 9:
                stack.append((i, j))
    flashes = 0
    while stack:
        i, j = stack.pop()
        if flashed[i][j]:
            continue
        flashed[i][j] = True
        flashes += 1
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and not flashed[ni][nj]:
                    grid[ni][nj] += 1
                    if grid[ni][nj] > 9:
                        stack.append((ni, nj))
    for i in range(n):
        for j in range(m):
            if flashed[i][j]:
                grid[i][j] = 0
    return flashes

def part1(grid):
    total = 0
    for _ in range(100):
        total += step(grid)
    return total

def part2(grid):
    n, m = len(grid), len(grid[0])
    target = n * m
    step_count = 0
    while True:
        step_count += 1
        if step(grid) == target:
            return step_count

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]
grid0 = [list(map(int, line)) for line in data]
import copy
g1 = copy.deepcopy(grid0)
g2 = copy.deepcopy(grid0)
res1 = part1(g1)
res2 = part2(g2)
sys.stdout.write(f"{res1} {res2}")