import sys
from collections import defaultdict
from itertools import combinations


def part1(grid):
    n = len(grid)
    in_bounds = lambda x, y: 0 <= x < n and 0 <= y < n
    antinodes = set()
    all_locs = defaultdict(list)

    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i, j))

    for freq in all_locs:
        locs = all_locs[freq]
        for a, b in combinations(locs, 2):
            ax, ay = a
            bx, by = b
            dx, dy = bx - ax, by - ay
            cx, cy = ax - dx, ay - dy
            if in_bounds(cx, cy):
                antinodes.add((cx, cy))
            dx, dy = bx - ax, by - ay
            dx, dy = bx + dx, by + dy
            if in_bounds(dx, dy):
                antinodes.add((dx, dy))

    return len(antinodes)


def part2(grid):
    n = len(grid)
    in_bounds = lambda x, y: 0 <= x < n and 0 <= y < n
    antinodes = set()
    all_locs = defaultdict(list)

    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i, j))

    for freq in all_locs:
        locs = all_locs[freq]
        for a, b in combinations(locs, 2):
            ax, ay = a
            bx, by = b
            dx, dy = bx - ax, by - ay
            i = 1
            while True:
                cx, cy = ax - dx * i, ay - dy * i
                if in_bounds(cx, cy):
                    antinodes.add((cx, cy))
                else:
                    break
                i += 1
            i = 1
            while True:
                cx, cy = bx + dx * i, by + dy * i
                if in_bounds(cx, cy):
                    antinodes.add((cx, cy))
                else:
                    break
                i += 1

    return len(antinodes)


input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))