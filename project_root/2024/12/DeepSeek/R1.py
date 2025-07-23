import sys

def part1(grid):
    n = len(grid)
    dd = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    def in_grid(i, j):
        return 0 <= i < n and 0 <= j < n

    seen = set()
    ans = 0

    for i in range(n):
        for j in range(n):
            if (i, j) in seen:
                continue
            stack = [(i, j)]
            area = 0
            perim_sum = 0
            base_char = grid[i][j]
            while stack:
                ci, cj = stack.pop()
                if (ci, cj) in seen:
                    continue
                if not in_grid(ci, cj) or grid[ci][cj] != base_char:
                    continue
                seen.add((ci, cj))
                area += 1
                free_count = 0
                for di, dj in dd:
                    ni, nj = ci + di, cj + dj
                    if not in_grid(ni, nj) or grid[ni][nj] != base_char:
                        free_count += 1
                perim_sum += free_count
                for di, dj in dd:
                    ni, nj = ci + di, cj + dj
                    stack.append((ni, nj))
            ans += perim_sum * area
    return ans

def part2(grid):
    n = len(grid)
    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    def in_grid(i, j):
        return 0 <= i < n and 0 <= j < n

    seen = set()
    ans = 0

    for i in range(n):
        for j in range(n):
            if (i, j) in seen:
                continue
            stack = [(i, j)]
            plot_list = []
            min_i, max_i = i, i
            min_j, max_j = j, j
            base_char = grid[i][j]
            while stack:
                ci, cj = stack.pop()
                if (ci, cj) in seen:
                    continue
                if not in_grid(ci, cj) or grid[ci][cj] != base_char:
                    continue
                seen.add((ci, cj))
                plot_list.append((ci, cj))
                min_i = min(min_i, ci)
                max_i = max(max_i, ci)
                min_j = min(min_j, cj)
                max_j = max(max_j, cj)
                for di, dj in dd:
                    ni, nj = ci + di, cj + dj
                    stack.append((ni, nj))
            plot_set = set(plot_list)
            area = len(plot_list)
            p = 0
            for i2 in range(min_i - 1, max_i + 1):
                for j2 in range(min_j - 1, max_j + 1):
                    corners = [(i2, j2), (i2, j2+1), (i2+1, j2), (i2+1, j2+1)]
                    res = [1 if (x, y) in plot_set else 0 for x, y in corners]
                    if res in [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1], [1,1,1,0], [1,1,0,1], [1,0,1,1], [0,1,1,1]]:
                        p += 1
                    elif res in [[1,0,0,1], [0,1,1,0]]:
                        p += 2
            ans += p * area
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))