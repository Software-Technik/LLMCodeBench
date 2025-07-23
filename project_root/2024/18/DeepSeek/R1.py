import sys
from collections import deque

def part1(lines):
    coords = set(tuple(map(int, line.split(','))) for line in lines[:1024])
    dd = [(1,0), (0,1), (-1,0), (0,-1)]
    N = 70
    q = deque([(0,0)])
    dist = {}
    dist[(0,0)] = 0
    while q:
        i, j = q.popleft()
        if (i, j) == (N, N):
            return dist[(i, j)]
        for di, dj in dd:
            ii, jj = i + di, j + dj
            if 0 <= ii <= N and 0 <= jj <= N and (ii, jj) not in coords and (ii, jj) not in dist:
                dist[(ii, jj)] = dist[(i, j)] + 1
                q.append((ii, jj))

def part2(lines):
    coords = [tuple(map(int, line.split(','))) for line in lines]
    dd = [(1,0), (0,1), (-1,0), (0,-1)]
    N = 70
    def doable(idx):
        blocked_set = set(coords[:idx])
        q = deque([(0,0)])
        visited = set([(0,0)])
        while q:
            i, j = q.popleft()
            if (i, j) == (N, N):
                return True
            for di, dj in dd:
                ii, jj = i + di, j + dj
                if 0 <= ii <= N and 0 <= jj <= N and (ii, jj) not in blocked_set and (ii, jj) not in visited:
                    visited.add((ii, jj))
                    q.append((ii, jj))
        return False
    lo = 0
    hi = len(coords) - 1
    while hi > lo:
        mid = (lo + hi) // 2
        if doable(mid):
            lo = mid + 1
        else:
            hi = mid
    return ",".join(map(str, coords[lo - 1]))

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))