import sys
from heapq import heappush, heappop
from collections import defaultdict

def part1(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q = [(0, 0, start[0], start[1])]
    seen = set()
    while q:
        cost, d, i, j = heappop(q)
        if (d, i, j) in seen:
            continue
        seen.add((d, i, j))

        if grid[i][j] == "#":
            continue

        if grid[i][j] == "E":
            return cost

        ii = i + dd[d][0]
        jj = j + dd[d][1]
        if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] != '#':
            nbr = (cost + 1, d, ii, jj)
            if nbr[1:] not in seen:
                heappush(q, nbr)

        left_d = (d + 3) % 4
        nbr_left = (cost + 1000, left_d, i, j)
        if nbr_left[1:] not in seen:
            heappush(q, nbr_left)

        right_d = (d + 1) % 4
        nbr_right = (cost + 1000, right_d, i, j)
        if nbr_right[1:] not in seen:
            heappush(q, nbr_right)

    return -1

def part2(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q = [(0, 0, start[0], start[1], 0, start[0], start[1])]
    cost = {}
    deps = defaultdict(list)
    end_dir = -1
    while q:
        top = heappop(q)
        c, d, i, j, pd, pi, pj = top
        if (d, i, j) in cost:
            if cost[(d, i, j)] == c:
                deps[(d, i, j)].append((pd, pi, pj))
            continue

        deps[(d, i, j)].append((pd, pi, pj))
        cost[(d, i, j)] = c

        if grid[i][j] == "#":
            continue

        if grid[i][j] == "E":
            end_dir = d
            break

        ii = i + dd[d][0]
        jj = j + dd[d][1]
        if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] != '#':
            nbr = (c + 1, d, ii, jj, d, i, j)
            heappush(q, nbr)

        left_d = (d + 3) % 4
        nbr_left = (c + 1000, left_d, i, j, d, i, j)
        heappush(q, nbr_left)

        right_d = (d + 1) % 4
        nbr_right = (c + 1000, right_d, i, j, d, i, j)
        heappush(q, nbr_right)

    stack = [(end_dir, end[0], end[1])]
    seen = set()
    seen_pos = set()
    while stack:
        top = stack.pop()
        if top in seen:
            continue
        seen.add(top)
        seen_pos.add(top[1:])
        for nbr in deps[top]:
            stack.append(nbr)

    return len(seen_pos)

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))