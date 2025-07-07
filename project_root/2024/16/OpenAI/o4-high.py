import sys
from heapq import heappush, heappop
from collections import defaultdict

def solve(grid):
    n = len(grid)
    si = sj = ei = ej = 0
    for i, row in enumerate(grid):
        j = row.find('S')
        if j != -1:
            si, sj = i, j
        j = row.find('E')
        if j != -1:
            ei, ej = i, j
    dd = [(0,1),(1,0),(0,-1),(-1,0)]
    cost = {}
    deps = defaultdict(list)
    q = [(0,0,si,sj,0,si,sj)]
    while q:
        c, d, i, j, pd, pi, pj = heappop(q)
        key = (d, i, j)
        if key in cost:
            if cost[key] == c:
                deps[key].append((pd, pi, pj))
            continue
        deps[key].append((pd, pi, pj))
        cost[key] = c
        ch = grid[i][j]
        if ch == '#':
            continue
        if ch == 'E':
            end_dir = d
            best = c
            break
        dx, dy = dd[d]
        heappush(q, (c+1, d, i+dx, j+dy, d, i, j))
        nd = (d+1) & 3
        heappush(q, (c+1000, nd, i, j, d, i, j))
        nd = (d+3) & 3
        heappush(q, (c+1000, nd, i, j, d, i, j))
    seen = set()
    seen_pos = set()
    stack = [(end_dir, ei, ej)]
    while stack:
        d, i, j = stack.pop()
        key = (d, i, j)
        if key in seen:
            continue
        seen.add(key)
        seen_pos.add((i, j))
        for pd, pi, pj in deps[key]:
            stack.append((pd, pi, pj))
    return best, len(seen_pos)

if __name__ == '__main__':
    grid = open(sys.argv[1]).read().strip().split('\n')
    p1, p2 = solve(grid)
    print(p1, p2)