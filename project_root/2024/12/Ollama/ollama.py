import sys

def part1(grid):
    n, dirs, seen, plots = len(grid), [[1, 0], [0, 1], [-1, 0], [0, -1]], set(), []
    for i in range(n):
        for j in range(n):
            if (i, j) not in seen:
                stack, current_plot = [(i, j)], []
                while stack:
                    x, y = stack.pop()
                    if (x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != grid[i][j] or (x, y) in seen):
                        continue
                    seen.add((x, y))
                    current_plot.append((x, y))
                    for dx, dy in dirs:
                        stack.append((x + dx, y + dy))
                plots.append([grid[i][j], current_plot])

    def perim(plot):
        ans = 0
        for x, y in plot:
            for dx, dy in dirs:
                if (x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n or grid[x + dx][y + dy] != grid[i][j]):
                    ans += 1
        return ans

    return sum(perim(plot) * len(plot) for _, plot in plots)

def part2(grid):
    n, dirs, seen, plots = len(grid), [[-1, 0], [0, 1], [1, 0], [0, -1]], set(), []
    boundary_corner_patterns = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1]
    ]
    double_corner_patterns = [
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    for i in range(n):
        for j in range(n):
            if (i, j) not in seen:
                stack, current_plot = [(i, j)], []
                while stack:
                    x, y = stack.pop()
                    if (x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != grid[i][j] or (x, y) in seen):
                        continue
                    seen.add((x, y))
                    current_plot.append((x, y))
                    for dx, dy in dirs:
                        stack.append((x + dx, y + dy))
                plots.append([grid[i][j], current_plot])

    def perim(plot):
        plot_set = set(plot)
        x_min, x_max = min(x for x, _ in plot), max(x for x, _ in plot)
        y_min, y_max = min(y for _, y in plot), max(y for _, y in plot)

        ans = 0
        for x in range(x_min - 1, x_max + 2):
            for y in range(y_min - 1, y_max + 2):
                res = [
                    (x, y) in plot_set,
                    (x, y + 1) in plot_set if y + 1 < n else False,
                    (x + 1, y) in plot_set if x + 1 < n else False,
                    (x + 1, y + 1) in plot_set if x + 1 < n and y + 1 < n else False
                ]
                is_corner = int(any(map(lambda p: res == p, boundary_corner_patterns)))
                double_corners = any(map(lambda p: res == p, double_corner_patterns))
                ans += is_corner + (2 * double_corners)

        return ans

    return sum(perim(plot) * len(plot) for _, plot in plots)

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = [list(line.strip()) for line in fin.read().strip().split("\n")]
print(part1(grid), part2(grid))