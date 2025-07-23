import sys
from collections import defaultdict

def is_within_bounds(i, j, n):
    return 0 <= i < n and 0 <= j < n

def find_positions(grid, n):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "S":
                si, sj = i, j
            elif grid[i][j] == "E":
                ei, ej = i, j
    return si, sj, ei, ej

def construct_path(grid, n, si, sj, ei, ej):
    path = [(si, sj)]
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while path[-1] != (ei, ej):
        i, j = path[-1]
        for di, dj in directions:
            n_i, n_j = i + di, j + dj
            if not is_within_bounds(n_i, n_j, n) or grid[n_i][n_j] == "#" or len(path) > 1 and (n_i, n_j) == path[-2]:
                continue
            path.append((n_i, n_j))
            break
    return path

def calculate_times(og, path):
    times = {coord: og - t for t, coord in enumerate(path)}
    return times

def part1(grid):
    n = len(grid)
    si, sj, ei, ej = find_positions(grid, n)
    path = construct_path(grid, n, si, sj, ei, ej)
    og = len(path) - 1
    times = calculate_times(og, path)

    direction_vectors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    saved = {}
    for t, coord in enumerate(path):
        i, j = coord
        for di1, dj1 in direction_vectors:
            for di2, dj2 in direction_vectors:
                ii, jj = i + di1 + di2, j + dj1 + dj2
                if not is_within_bounds(ii, jj, n) or grid[ii][jj] == "#":
                    continue
                rem_t = times[(ii, jj)]
                key = (i, j, ii, jj)
                val = og - (t + rem_t + 2)
                saved[key] = val
    counts = defaultdict(int)
    for v in saved.values():
        if v >= 0:
            counts[v] += 1
        if v >= 100:
            return counts[100]

def part2(grid):
    n = len(grid)
    si, sj, ei, ej = find_positions(grid, n)
    path = construct_path(grid, n, si, sj, ei, ej)
    og = len(path) - 1
    times = calculate_times(og, path)

    max_len = 20
    counts = defaultdict(int)
    saved = {}
    directions = [[-n, 0], [n, 0], [0, -n], [0, n], [-max_len+2, 0], [0, max_len+1]]
    for s in range(4):
        for di1, dj1 in [(i, j) for i in directions[s] for j in directions[s]]:
            for t, coord in enumerate(path):
                i, j = coord
                ii, jj = i + di1, j + dj1
                time_used = abs(ii - i) + abs(jj - j)
                if not is_within_bounds(ii, jj, n) or grid[ii][jj] == "#" or time_used > max_len:
                    continue

                rem_t = times[(ii, jj)]
                key = (i, j, ii, jj)
                val = og - (t + rem_t + abs(di1) + abs(dj1))
                saved[key] = val
    for v in saved.values():
        if v >= 0:
            counts[v] += 1
        if v >= 100:
            return counts[100]

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]
print(part1(grid), part2(grid))