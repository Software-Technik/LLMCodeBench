import sys
from heapq import heappush, heappop

def part1(lines):
    coords = set(map(tuple, map(lambda x: map(int, x.split(",")), lines[:1024])))
    dd = ((1, 0), (0, 1), (-1, 0), (0, -1))
    N = 70

    def h(i, j):
        return abs(N - i) + abs(N - j)

    def in_grid(i, j):
        return 0 <= i < N and 0 <= j < N and (i, j) not in coords

    q = [(h(0, 0), 0, 0)]
    cost = {}
    while q:
        c, i, j = heappop(q)
        if (i, j) in cost:
            continue
        cost[(i, j)] = c - h(i, j)

        if (i, j) == (N, N):
            return cost[(i, j)]

        for di, dj in dd:
            ii, jj = i + di, j + dj
            if in_grid(ii, jj):
                heappush(q, (cost[(i, j)] + 1 + h(ii, jj), ii, jj))

def part2(lines):
    coords = list(map(tuple, map(lambda x: map(int, x.split(",")), lines)))
    dd = ((1, 0), (0, 1), (-1, 0), (0, -1))
    N = 70

    def h(i, j):
        return abs(N - i) + abs(N - j)

    def doable(idx):
        blocked = coords[:idx]
        q = [(h(0, 0), 0, 0)]
        cost = {}
        while q:
            c, i, j = heappop(q)
            if (i, j) in cost:
                continue
            cost[(i, j)] = c - h(i, j)

            if (i, j) == (N, N):
                return True

            for di, dj in dd:
                ii, jj = i + di, j + dj
                if 0 <= ii < N and 0 <= jj < N and (ii, jj) not in blocked:
                    heappush(q, (cost[(i, j)] + 1 + h(ii, jj), ii, jj))

        return False

    lo = 0
    hi = len(coords) - 1
    while hi > lo:
        mid = (lo + hi + 1) // 2
        if doable(mid):
            lo = mid
        else:
            hi = mid - 1

    return ",".join(map(str, coords[lo]))

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = [line.strip() for line in fin.readlines()]
    print(part1(lines), part2(lines))