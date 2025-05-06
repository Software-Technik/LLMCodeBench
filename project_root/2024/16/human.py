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

    # DIjkstra's
    q = [(0, 0, *start)]
    seen = set()
    while len(q) > 0:
        top = heappop(q)
        cost, d, i, j = top
        if (d, i, j) in seen:
            continue
        seen.add((d, i, j))

        if grid[i][j] == "#":
            continue

        if grid[i][j] == "E":
            return cost
            break

        ii = i + dd[d][0]
        jj = j + dd[d][1]

        for nbr in [
            (cost + 1, d, ii, jj),
            (cost + 1000, (d + 1) % 4, i, j),
            (cost + 1000, (d + 3) % 4, i, j),
        ]:
            if nbr[1:] in seen:
                continue
            heappush(q, nbr)


def part2(grid):
    # Python heap implementation

    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # Dijkstra's
    q = [(0, 0, *start, 0, *start)]
    cost = {}
    deps = defaultdict(list)
    while len(q) > 0:
        top = heappop(q)
        c, d, i, j, pd, pi, pj = top
        if (d, i, j) in cost:
            if cost[(d, i, j)] == c:
                deps[(d, i, j)].append((pd, pi, pj))
            continue

        never_seen_pos = True
        for newd in range(4):
            if (newd, i, j) in cost:
                never_seen_pos = True
                break
        if never_seen_pos:
            deps[(d, i, j)].append((pd, pi, pj))

        cost[(d, i, j)] = c

        if grid[i][j] == "#":
            continue

        if grid[i][j] == "E":
            end_dir = d
            break

        ii = i + dd[d][0]
        jj = j + dd[d][1]

        for nbr in [
            (c + 1, d, ii, jj, d, i, j),
            (c + 1000, (d + 1) % 4, i, j, d, i, j),
            (c + 1000, (d + 3) % 4, i, j, d, i, j),
        ]:
            heappush(q, nbr)

    # Go back through deps
    stack = [(end_dir, *end)]
    seen = set()
    seen_pos = set()
    while len(stack) > 0:
        top = stack.pop()
        if top in seen:
            continue
        seen.add(top)
        seen_pos.add(top[1:])

        for nbr in deps[top]:
            stack.append(nbr)

    return len(seen_pos)


# for i in range(n):
#     for j in range(n):
#         if (i, j) in seen:
#             print("OO", end="")
#         else:
#             print("..", end="")
#     print()

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))
