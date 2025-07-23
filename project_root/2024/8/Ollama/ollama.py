import sys
from collections import defaultdict
from itertools import combinations


def part1(grid):
    def get_antinodes(grid, pairs):
        antinodes = set()
        for (x1, y1), (x2, y2) in pairs:
            dx, dy = x2 - x1, y2 - y1
            x, y = x1 + dx, y1 + dy
            if 0 <= x < n and 0 <= y < n: antinodes.add((x, y))
            x, y = x1 - dx, y1 - dy
            if 0 <= x < n and 0 <= y < n: antinodes.add((x, y))
        return len(antinodes)
    n = len(grid)
    locs = defaultdict(list)
    for i in range(n):
        row = grid[i]
        for j in range(n):
            locs[row[j]].append((i, j))
    pairs = list(combinations(x, 2) for x in locs.values())
    return get_antinodes(grid, (pair for pairs in pairs for pair in pairs))


def part2(grid):
    def get_antinodes(grid, pairs):
        antinodes = set()
        for (x1, y1), (x2, y2) in pairs:
            dx, dy = x2 - x1, y2 - y1
            i = 0
            while True:
                i += 1
                x, y = x1 + dx * i, y1 + dy * i
                if not (0 <= x < n and 0 <= y < n): break
                antinodes.add((x, y))
            i = 0
            while True:
                i += 1
                x, y = x1 - dx * i, y1 - dy * i
                if not (0 <= x < n and 0 <= y < n): break
                antinodes.add((x, y))
        return len(antinodes)
    n = len(grid)
    locs = defaultdict(list)
    for i in range(n):
        row = grid[i]
        for j in range(n):
            locs[row[j]].append((i, j))
    pairs = list(combinations(x, 2) for x in locs.values())
    return get_antinodes(grid, (pair for pairs in pairs for pair in pairs))


input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))