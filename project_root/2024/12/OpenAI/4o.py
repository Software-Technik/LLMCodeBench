import sys
from collections import deque

def part1(grid):
    n = len(grid)
    dd = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def in_grid(i, j):
        return 0 <= i < n and 0 <= j < n

    seen = set()

    def explore(i, j):
        stack = [(i, j)]
        plot = []
        while stack:
            ci, cj = stack.pop()
            if (ci, cj) in seen or not in_grid(ci, cj) or grid[ci][cj] != grid[i][j]:
                continue
            seen.add((ci, cj))
            plot.append((ci, cj))
            for di, dj in dd:
                stack.append((ci + di, cj + dj))
        return plot

    def count_free(i, j):
        return sum(
            not in_grid(ii, jj) or grid[ii][jj] != grid[i][j]
            for di, dj in dd if (ii := i + di, jj := j + dj)
        )

    def perim(plot):
        return sum(count_free(i, j) for i, j in plot)

    return sum(perim(explore(i, j)) * len(explore(i, j)) for i in range(n) for j in range(n) if (i, j) not in seen)

def part2(grid):
    n = len(grid)
    dd = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def in_grid(i, j):
        return 0 <= i < n and 0 <= j < n

    seen = set()

    def explore(i, j):
        stack = deque([(i, j)])
        plot = set()
        while stack:
            ci, cj = stack.pop()
            if (ci, cj) in seen or not in_grid(ci, cj) or grid[ci][cj] != grid[i][j]:
                continue
            seen.add((ci, cj))
            plot.add((ci, cj))
            for di, dj in dd:
                stack.append((ci + di, cj + dj))
        return plot

    def perim(plot):
        mini, maxi, minj, maxj = n, -1, n, -1
        for i, j in plot:
            mini, maxi = min(mini, i), max(maxi, i)
            minj, maxj = min(minj, j), max(maxj, j)

        ans = 0
        for i in range(mini - 1, maxi):
            for j in range(minj - 1, maxj):
                res = [(i + di, j + dj) in plot for di, dj in ((0, 0), (0, 1), (1, 0), (1, 1))]
                has_corner = res in [
                    (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
                    (1, 1, 1, 0), (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1),
                ]
                has_double_corner = res in [(1, 0, 0, 1), (0, 1, 1, 0)]
                ans += has_corner + has_double_corner * 2

        return ans

    return sum(perim(explore(i, j)) * len(explore(i, j)) for i in range(n) for j in range(n) if (i, j) not in seen)

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))