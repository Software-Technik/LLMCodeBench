import sys
from collections import defaultdict

def part1(grid):
    N = len(grid)
    in_grid = lambda i, j: 0 <= i < N and 0 <= j < N
    si = sj = ei = ej = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "S":
                si, sj = i, j
            elif grid[i][j] == "E":
                ei, ej = i, j

    dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    path = [(si, sj)]
    while path[-1] != (ei, ej):
        i, j = path[-1]
        for di, dj in dd:
            ii, jj = i + di, j + dj
            if not in_grid(ii, jj):
                continue
            if len(path) > 1 and (ii, jj) == path[-2]:
                continue
            if grid[ii][jj] == "#":
                continue
            path.append((ii, jj))
            break

    og = len(path) - 1
    times = {coord: og - t for t, coord in enumerate(path)}
    counts = defaultdict(int)
    ans = 0

    for t, (i, j) in enumerate(path):
        for di1, dj1 in dd:
            ii1, jj1 = i + di1, j + dj1
            if not in_grid(ii1, jj1) or grid[ii1][jj1] == "#":
                continue
            for di2, dj2 in dd:
                ii, jj = ii1 + di2, jj1 + dj2
                if not in_grid(ii, jj) or grid[ii][jj] == "#":
                    continue
                rem_t = times.get((ii, jj), 0)
                v = og - (t + rem_t + 2)
                if v >= 0:
                    counts[v] += 1
                if v >= 100:
                    ans += 1
    return ans

def part2(grid):
    N = len(grid)
    in_grid = lambda i, j: 0 <= i < N and 0 <= j < N
    si = sj = ei = ej = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "S":
                si, sj = i, j
            elif grid[i][j] == "E":
                ei, ej = i, j

    dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    path = [(si, sj)]
    while path[-1] != (ei, ej):
        i, j = path[-1]
        for di, dj in dd:
            ii, jj = i + di, j + dj
            if not in_grid(ii, jj):
                continue
            if len(path) > 1 and (ii, jj) == path[-2]:
                continue
            if grid[ii][jj] == "#":
                continue
            path.append((ii, jj))
            break

    og = len(path) - 1
    times = {coord: og - t for t, coord in enumerate(path)}
    counts = defaultdict(int)
    ans = 0
    max_len = 20

    for t, (i, j) in enumerate(path):
        for di in range(-max_len, max_len + 1):
            for dj in range(-max_len, max_len + 1):
                time_used = abs(di) + abs(dj)
                if time_used > max_len:
                    continue
                ii, jj = i + di, j + dj
                if not in_grid(ii, jj) or grid[ii][jj] == "#":
                    continue
                rem_t = times.get((ii, jj), 0)
                v = og - (t + rem_t + time_used)
                if v >= 0:
                    counts[v] += 1
                if v >= 100:
                    ans += 1
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]
    print(part1(grid), part2(grid))