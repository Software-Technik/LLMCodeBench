import sys
from heapq import heappush, heappop
from collections import defaultdict

def part1(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            c = grid[i][j]
            if c == "S": start = (i, j)
            elif c == "E": end = (i, j)
    dd = ((0,1),(1,0),(0,-1),(-1,0))
    q = [(0,0,start[0],start[1])]
    seen = set()
    while q:
        cost,d,i,j = heappop(q)
        key = (d,i,j)
        if key in seen: continue
        seen.add(key)
        if grid[i][j]=="#": continue
        if (i,j)==end: return cost
        di,dj = dd[d]
        ni,nj = i+di,j+dj
        if 0<=ni<n and 0<=nj<n:
            heappush(q,(cost+1,d,ni,nj))
        heappush(q,(cost+1000,(d+1)&3,i,j))
        heappush(q,(cost+1000,(d-1)&3,i,j))

def part2(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            c = grid[i][j]
            if c == "S": start = (i, j)
            elif c == "E": end = (i, j)
    dd = ((0,1),(1,0),(0,-1),(-1,0))
    q = [(0,0,start[0],start[1],0,start[0],start[1])]
    cost = {}
    deps = defaultdict(list)
    while q:
        c,d,i,j,pd,pi,pj = heappop(q)
        key = (d,i,j)
        if key in cost:
            if cost[key]==c: deps[key].append((pd,pi,pj))
            continue
        cost[key]=c
        deps[key].append((pd,pi,pj))
        if grid[i][j]=="#": continue
        if (i,j)==end:
            end_dir = d
            break
        di,dj = dd[d]
        ni,nj = i+di,j+dj
        if 0<=ni<n and 0<=nj<n:
            heappush(q,(c+1,d,ni,nj,d,i,j))
        heappush(q,(c+1000,(d+1)&3,i,j,d,i,j))
        heappush(q,(c+1000,(d-1)&3,i,j,d,i,j))
    stack = [(end_dir,end[0],end[1])]
    seen = set()
    seen_pos = set()
    while stack:
        d,i,j = stack.pop()
        key = (d,i,j)
        if key in seen: continue
        seen.add(key)
        seen_pos.add((i,j))
        for pd,pi,pj in deps[key]:
            stack.append((pd,pi,pj))
    return len(seen_pos)

with open(sys.argv[1]) as f:
    grid = f.read().splitlines()
print(part1(grid), part2(grid))