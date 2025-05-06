import sys


def part1(grid):

    n = len(grid)

    dd = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def in_grid(i, j):
        return (0 <= i < n) and (0 <= j < n)

    seen = set()
    plots = []

    for i in range(n):
        for j in range(n):
            if (i, j) in seen:
                continue

            stack = [(i, j)]
            plots.append([grid[i][j], []])

            print(f"looking at i={i}, j={j}, grid[i][j]={grid[i][j]}")

            while len(stack) > 0:
                ci, cj = stack.pop()
                if (ci, cj) in seen:
                    continue
                if not in_grid(ci, cj):
                    continue
                if grid[ci][cj] != grid[i][j]:
                    continue
                seen.add((ci, cj))

                plots[-1][1].append((ci, cj))
                for di, dj in dd:
                    ii, jj = ci + di, cj + dj
                    stack.append((ii, jj))

    def count_free(i, j):
        ans = 0
        for di, dj in dd:
            ii, jj = i + di, j + dj
            if not in_grid(ii, jj):
                ans += 1
            elif grid[ii][jj] != grid[i][j]:
                ans += 1
        return ans

    def perim(plot):
        ans = 0
        for i, j in plot:
            ans += count_free(i, j)
        return ans

    ans = 0
    for c, plot in plots:
        print(c, plot, perim(plot))
        ans += perim(plot) * len(plot)

    return ans


def part2(grid):

    n = len(grid)

    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def in_grid(i, j):
        return (0 <= i < n) and (0 <= j < n)

    seen = set()
    plots = []

    for i in range(n):
        for j in range(n):
            if (i, j) in seen:
                continue

            stack = [(i, j)]
            plots.append([grid[i][j], []])

            while len(stack) > 0:
                ci, cj = stack.pop()
                if (ci, cj) in seen:
                    continue
                if not in_grid(ci, cj):
                    continue
                if grid[ci][cj] != grid[i][j]:
                    continue
                seen.add((ci, cj))

                plots[-1][1].append((ci, cj))
                for di, dj in dd:
                    ii, jj = ci + di, cj + dj
                    stack.append((ii, jj))

    def perim(plot):
        # Iterate through all 2x2 subplots
        plot = set(plot)

        def test(coords):
            res = []
            for i, j in coords:
                res.append((i, j) in plot)
            return list(map(int, res))

        mini, maxi = 0, n
        minj, maxj = 0, n
        for i, j in plot:
            mini, maxi = min(mini, i), max(maxi, i)
            minj, maxj = min(minj, j), max(maxj, j)

        ans = 0
        for i in range(mini - 1, maxi):
            for j in range(minj - 1, maxj):
                res = test([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
                has_corner = res in [
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                    [1, 1, 1, 0],
                    [1, 1, 0, 1],
                    [1, 0, 1, 1],
                    [0, 1, 1, 1],
                ]
                has_double_corner = res in [[1, 0, 0, 1], [0, 1, 1, 0]]
                ans += has_corner + has_double_corner * 2

        return ans

    ans = 0
    for c, plot in plots:
        ans += perim(plot) * len(plot)

    return ans

input_path = sys.argv[1]

with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))
