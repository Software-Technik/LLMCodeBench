import sys
from collections import defaultdict

def part1(grid):

    N = len(grid)

    def in_grid(i, j):
        return 0 <= i < N and 0 <= j < N

    si = sj = ei = ej = None

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
            if in_grid(ii, jj) and len(path) <= 1 or (ii, jj) != path[-2]:
                if grid[ii][jj] != "#":
                    path.append((ii, jj))
                    break

    og = len(path) - 1

    times = {coord: og - t for t, coord in enumerate(path)}

    saved = {}
    for t, coord in enumerate(path):
        i, j = coord
        for di1, dj1 in dd:
            for di2, dj2 in dd:
                ii, jj = i + di1 + di2, j + dj1 + dj2
                if in_grid(ii, jj) and grid[ii][jj] != "#":
                    rem_t = times.get((ii, jj), 0)
                    saved[(i, j, ii, jj)] = og - (t + rem_t + 2)

    ans = sum(1 for v in saved.values() if v >= 100)
    return ans

def part2(grid):
    N = len(grid)

    def in_grid(i, j):
        return 0 <= i < N and 0 <= j < N

    si = sj = ei = ej = None

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
            if in_grid(ii, jj) and len(path) <= 1 or (ii, jj) != path[-2]:
                if grid[ii][jj] != "#":
                    path.append((ii, jj))
                    break

    og = len(path) - 1

    times = {coord: og - t for t, coord in enumerate(path)}

    max_len = 20
    saved = {}
    for t, coord in enumerate(path):
        i, j = coord
        for ii in range(max(i - max_len, 0), min(i + max_len + 1, N)):
            for jj in range(max(j - max_len, 0), min(j + max_len + 1, N)):
                time_used = abs(ii - i) + abs(jj - j)
                if in_grid(ii, jj) and time_used <= max_len and grid[ii][jj] != "#":
                    rem_t = times.get((ii, jj), 0)
                    saved[(i, j, ii, jj)] = og - (t + rem_t + time_used)

    ans = sum(1 for v in saved.values() if v >= 100)
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]
    print(part1(grid), part2(grid))