import sys
from collections import deque
from functools import lru_cache

def parse(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[x, y] = c
            if c == '@': start = (x, y)
    return grid, start

def part1(data):
    grid, start = parse(data)
    keys = {c for c in grid.values() if 'a' <= c <= 'z'}
    poi = {start: '@'}
    poi.update({p: c for p, c in grid.items() if c in keys or 'A' <= c <= 'Z'})
    dists = {}
    for p, c in poi.items():
        q = deque([(p, 0, frozenset())])
        seen = {p}
        while q:
            (x, y), d, doors = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                q2 = (x+dx, y+dy)
                if q2 in seen or grid.get(q2) == '#': continue
                seen.add(q2)
                cell = grid[q2]
                doors2 = doors
                if 'A' <= cell <= 'Z': doors2 = doors | {cell.lower()}
                if cell != '.' and cell != '@':
                    dists.setdefault(c, {})[cell] = (d+1, doors2)
                q.append((q2, d+1, doors2))
    allk = frozenset(keys)

    @lru_cache(None)
    def dfs(pos, got):
        if got == allk: return 0
        best = float('inf')
        for k in allk - got:
            if k in dists[pos]:
                dist, doors = dists[pos][k]
                if doors <= got:
                    best = min(best, dist + dfs(k, got | {k}))
        return best

    return dfs('@', frozenset())

def part2(data):
    grid, start = parse(data)
    sx, sy = start
    walls = {(sx+dx, sy+dy) for dx, dy in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]}
    for p in walls: grid[p] = '#'
    starts = [(sx-1, sy-1), (sx+1, sy-1), (sx-1, sy+1), (sx+1, sy+1)]
    keys = {c for c in grid.values() if 'a' <= c <= 'z'}
    poi = {p: str(i) for i, p in enumerate(starts)}
    poi.update({p: c for p, c in grid.items() if c in keys or 'A' <= c <= 'Z'})
    dists = {}
    for p, c in poi.items():
        q = deque([(p, 0, frozenset())])
        seen = {p}
        while q:
            (x, y), d, doors = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                q2 = (x+dx, y+dy)
                if q2 in seen or grid.get(q2) == '#': continue
                seen.add(q2)
                cell = grid[q2]
                doors2 = doors
                if 'A' <= cell <= 'Z': doors2 = doors | {cell.lower()}
                if cell != '.' and cell not in '@1234':
                    dists.setdefault(c, {})[cell] = (d+1, doors2)
                q.append((q2, d+1, doors2))
    allk = frozenset(keys)

    @lru_cache(None)
    def dfs(poss, got):
        if got == allk: return 0
        best = float('inf')
        for k in allk - got:
            for i, p in enumerate(poss):
                if p in dists and k in dists[p]:
                    dist, doors = dists[p][k]
                    if doors <= got:
                        np = list(poss)
                        np[i] = k
                        best = min(best, dist + dfs(tuple(np), got | {k}))
        return best

    return dfs(tuple(str(i) for i in range(4)), frozenset())

if __name__ == '__main__':
    data = open(sys.argv[1]).read().splitlines()
    a = part1(data)
    b = part2(data)
    print(a, b)