import sys
from collections import defaultdict
from itertools import combinations


def part1(grid):
    n = len(grid)

    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    def get_antinodes(a, b):
        ax, ay = a
        bx, by = b

        cx, cy = ax - (bx - ax), ay - (by - ay)
        dx, dy = bx + (bx - ax), by + (by - ay)

        if in_bounds(cx, cy):
            yield (cx, cy)
        if in_bounds(dx, dy):
            yield (dx, dy)

    all_locs = defaultdict(list)
    antinodes = set()

    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i, j))

    for locs in all_locs.values():
        for a, b in combinations(locs, r=2):
            antinodes.update(get_antinodes(a, b))

    return len(antinodes)


def part2(grid):
    n = len(grid)

    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    def get_antinodes(a, b):
        ax, ay = a
        bx, by = b
        dx, dy = bx - ax, by - ay

        i = 0
        while True:
            cx, cy = ax - dx * i, ay - dy * i
            if in_bounds(cx, cy):
                yield (cx, cy)
            else:
                break
            i += 1

        i = 0
        while True:
            cx, cy = bx + dx * i, by + dy * i
            if in_bounds(cx, cy):
                yield (cx, cy)
            else:
                break
            i += 1

    all_locs = defaultdict(list)
    antinodes = set()

    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i, j))

    for locs in all_locs.values():
        for a, b in combinations(locs, r=2):
            antinodes.update(get_antinodes(a, b))

    return len(antinodes)


if __name__ == "__main__":
    input_path = sys.argv[1]
    with open(input_path) as fin:
        grid = fin.read().strip().split("\n")
        print(part1(grid), part2(grid))