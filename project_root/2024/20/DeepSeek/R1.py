import sys
from collections import defaultdict, deque

def compute_path(grid, si, sj, ei, ej):
    N = len(grid)
    dd = [[1,0],[0,1],[-1,0],[0,-1]]
    path = [(si, sj)]
    def in_grid(i, j):
        return 0 <= i < N and 0 <= j < N
    while path[-1] != (ei, ej):
        i, j = path[-1]
        found = False
        for di, dj in dd:
            ii, jj = i + di, j + dj
            if not in_grid(ii, jj):
                continue
            if len(path) > 1 and (ii, jj) == path[-2]:
                continue
            if grid[ii][jj] == "#":
                continue
            path.append((ii, jj))
            found = True
            break
        if not found:
            break
    return path

def part1_optimized(grid, path, times, og):
    N = len(grid)
    dd = [[1,0],[0,1],[-1,0],[0,-1]]
    two_steps = set()
    for di1, dj1 in dd:
        for di2, dj2 in dd:
            two_steps.add((di1+di2, dj1+dj2))
    ans = 0
    def in_grid(i, j):
        return 0 <= i < N and 0 <= j < N
    for t, (i, j) in enumerate(path):
        for (dx, dy) in two_steps:
            ii, jj = i + dx, j + dy
            if not in_grid(ii, jj) or grid[ii][jj] == "#":
                continue
            rem_t = times[(ii, jj)]
            saving = og - (t + 2 + rem_t)
            if saving >= 100:
                ans += 1
    return ans

def part2_optimized(grid, path, times, og):
    N = len(grid)
    max_len = 20
    offsets = []
    for dx in range(-max_len, max_len+1):
        rem = max_len - abs(dx)
        for dy in range(-rem, rem+1):
            offsets.append((dx, dy))
    ans = 0
    def in_grid(i, j):
        return 0 <= i < N and 0 <= j < N
    for t, (i, j) in enumerate(path):
        for (dx, dy) in offsets:
            ii, jj = i + dx, j + dy
            if not in_grid(ii, jj) or grid[ii][jj] == "#":
                continue
            time_used = abs(dx) + abs(dy)
            rem_t = times[(ii, jj)]
            saving = og - (t + time_used + rem_t)
            if saving >= 100:
                ans += 1
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]
    N = len(grid)
    si, sj, ei, ej = -1, -1, -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "S":
                si, sj = i, j
            elif grid[i][j] == "E":
                ei, ej = i, j
    path = compute_path(grid, si, sj, ei, ej)
    og = len(path) - 1
    times = {}
    for t, coord in enumerate(path):
        times[coord] = og - t
    ans1 = part1_optimized(grid, path, times, og)
    ans2 = part2_optimized(grid, path, times, og)
    print(ans1, ans2)