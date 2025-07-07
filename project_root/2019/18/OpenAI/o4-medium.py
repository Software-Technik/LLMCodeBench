import sys
from collections import deque
from heapq import heappush, heappop

def build(data, part2=False):
    grid = {}
    keys = {}
    doors = {}
    starts = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[x, y] = c
            if c == '@':
                starts.append((x, y))
            elif c.islower():
                keys[c] = (x, y)
            elif c.isupper():
                doors[c] = (x, y)
    if part2:
        x, y = starts[0]
        for dx, dy in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
            grid[x+dx, y+dy] = '#'
        starts = [(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]
    return grid, starts, keys, doors

def build_graph(grid, starts, keys, doors):
    pts = list(starts) + [keys[k] for k in sorted(keys)]
    K = len(keys)
    S = len(starts)
    key_list = sorted(keys)
    key_index = {k:i for i,k in enumerate(key_list)}
    N = len(pts)
    graph = [ [] for _ in range(N) ]
    for i, (sx, sy) in enumerate(pts):
        dq = deque()
        dq.append((sx, sy, 0, 0))
        dist = {(sx, sy):(0,0)}
        while dq:
            x, y, d, m = dq.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                c = grid.get((nx,ny),'#')
                if c=='#': continue
                dm = m
                if c.isupper(): dm |= 1<<key_index[c.lower()]
                nd = d+1
                prev = dist.get((nx,ny))
                if prev is None or nd<prev[0] or (nd==prev[0] and dm<prev[1]):
                    dist[nx,ny] = (nd, dm)
                    dq.append((nx,ny,nd,dm))
        for k, (kx, ky) in enumerate([keys[k] for k in key_list]):
            if (kx, ky) in dist:
                d, m = dist[kx, ky]
                graph[i].append((S+k, d, m))
    return graph, S, K

def solve_part(grid, starts, keys, doors, part2=False):
    graph, S, K = build_graph(grid, starts, keys, doors)
    N = len(graph)
    ALL = (1<<K)-1
    if not part2:
        hq = [(0,0,0)]
        seen = {}
        while hq:
            d, u, m = heappop(hq)
            if m==ALL: return d
            if seen.get((u,m),1e18)<=d: continue
            seen[u,m]=d
            for v, w, req in graph[u]:
                bit = v-S
                if m>>bit&1: continue
                if req & ~m: continue
                nm = m|(1<<bit)
                heappush(hq,(d+w, v, nm))
    else:
        hq = [(0,tuple(range(S)),0)]
        seen = {}
        while hq:
            d, us, m = heappop(hq)
            if m==ALL: return d
            if seen.get((us,m),1e18)<=d: continue
            seen[us,m]=d
            for i,u in enumerate(us):
                for v, w, req in graph[u]:
                    bit = v-S
                    if m>>bit&1: continue
                    if req & ~m: continue
                    nm = m|(1<<bit)
                    tus = list(us)
                    tus[i]=v
                    tus = tuple(tus)
                    heappush(hq,(d+w, tus, nm))

data = sys.stdin.read().splitlines()
grid1, starts1, keys1, doors1 = build(data, part2=False)
ans1 = solve_part(grid1, starts1, keys1, doors1, part2=False)
grid2, starts2, keys2, doors2 = build(data, part2=True)
ans2 = solve_part(grid2, starts2, keys2, doors2, part2=True)
print(ans1, ans2)