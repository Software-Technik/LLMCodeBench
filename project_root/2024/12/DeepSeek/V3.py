import sys

def part1(grid):
    n = len(grid)
    dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seen = set()
    plots = []

    for i in range(n):
        for j in range(n):
            if (i, j) in seen:
                continue
            stack = [(i, j)]
            current_plot = []
            color = grid[i][j]
            while stack:
                ci, cj = stack.pop()
                if (ci, cj) in seen:
                    continue
                if not (0 <= ci < n and 0 <= cj < n):
                    continue
                if grid[ci][cj] != color:
                    continue
                seen.add((ci, cj))
                current_plot.append((ci, cj))
                for di, dj in dd:
                    stack.append((ci + di, cj + dj))
            plots.append((color, current_plot))

    perimeter = 0
    for color, plot in plots:
        plot_set = set(plot)
        p = 0
        for i, j in plot:
            for di, dj in dd:
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < n) or grid[ni][nj] != color:
                    p += 1
        perimeter += p * len(plot)
    return perimeter

def part2(grid):
    n = len(grid)
    dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set()
    plots = []

    for i in range(n):
        for j in range(n):
            if (i, j) in seen:
                continue
            stack = [(i, j)]
            current_plot = []
            color = grid[i][j]
            while stack:
                ci, cj = stack.pop()
                if (ci, cj) in seen:
                    continue
                if not (0 <= ci < n and 0 <= cj < n):
                    continue
                if grid[ci][cj] != color:
                    continue
                seen.add((ci, cj))
                current_plot.append((ci, cj))
                for di, dj in dd:
                    stack.append((ci + di, cj + dj))
            plots.append((color, current_plot))

    perimeter = 0
    corner_cases = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1]
    ]
    double_corner_cases = [[1, 0, 0, 1], [0, 1, 1, 0]]

    for color, plot in plots:
        plot_set = set(plot)
        p = 0
        min_i = min(i for i, j in plot)
        max_i = max(i for i, j in plot)
        min_j = min(j for i, j in plot)
        max_j = max(j for i, j in plot)
        for i in range(min_i - 1, max_i + 1):
            for j in range(min_j - 1, max_j + 1):
                coords = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
                res = [1 if (x, y) in plot_set else 0 for x, y in coords]
                if res in corner_cases:
                    p += 1
                elif res in double_corner_cases:
                    p += 2
        perimeter += p * len(plot)
    return perimeter

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))