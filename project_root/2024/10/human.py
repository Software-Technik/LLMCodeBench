import sys
from functools import lru_cache


def part1(grid):

    n = len(grid)

    dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def in_grid(i, j):
        return (0 <= i < n) and (0 <= j < n)

    def score(i, j):
        # Do DFS
        if grid[i][j] != "0":
            return 0

        ans = 0

        stack = [(i, j)]
        visited = set()
        while len(stack) > 0:
            curi, curj = stack.pop()
            cur = int(grid[curi][curj])

            if cur == 9:
                ans += 1
                continue

            for di, dj in dd:
                ii, jj = curi + di, curj + dj

                if not in_grid(ii, jj):
                    continue

                nbr = int(grid[ii][jj])
                if nbr != cur + 1:
                    continue
                stack.append((ii, jj))

        return ans

    ans = 0
    for i in range(n):
        for j in range(n):
            ans += score(i, j)

    return ans


def part2(grid):

    n = len(grid)

    dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def in_grid(i, j):
        return (0 <= i < n) and (0 <= j < n)

    @lru_cache(None)
    def rating(i, j):
        if grid[i][j] == "9":
            return 1

        ans = 0
        for di, dj in dd:
            ii, jj = i + di, j + dj
            if not in_grid(ii, jj):
                continue

            if int(grid[ii][jj]) == int(grid[i][j]) + 1:
                ans += rating(ii, jj)

        return ans

    ans = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "0":
                ans += rating(i, j)

    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))
