import sys
from collections import defaultdict, deque

NDIRS = {'>': 1, '^': -1j, '<': -1, 'v': 1j}

def parse(text):
    lines = text.strip().splitlines()
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x+1j*y] = c
    start = 1
    maxx = max(p.real for p in grid)
    maxy = max(p.imag for p in grid)
    end = (maxx-1) + 1j*(maxy-1)
    return grid, start, end

def find_adjacent(start, grid, terminals, ndirs_enabled):
    adj = []
    q = deque([(start,0,{start})])
    while q:
        p,l,seen = q.popleft()
        if p in terminals and p!=start:
            adj.append((p,l))
            continue
        x,y = p.real, p.imag
        neigh = (p-1j, p-1, p+1, p+1j)
        cnt = 0
        valid = []
        for n in neigh:
            if n in grid and n not in seen and grid[n]!='#':
                valid.append(n); cnt+=1
        if cnt>1 and p!=start:
            adj.append((p,l)); continue
        for n in valid:
            c = grid[n]
            if ndirs_enabled and c in NDIRS:
                nxt = n+NDIRS[c]
                if nxt!=p:
                    q.append((nxt, l+2, seen|{n,nxt}))
            else:
                q.append((n, l+1, seen|{n}))
    return adj

def build_graph(grid, start, end, ndirs_enabled):
    graph = defaultdict(list)
    seen = set()
    q = [start]
    while q:
        p = q.pop()
        if p in seen: continue
        seen.add(p)
        for n,l in find_adjacent(p, grid, {start,end}, ndirs_enabled):
            graph[p].append((n,l))
            if n not in seen: q.append(n)
    return graph

def longest_path(graph, start, end):
    best=0
    q=[(start,0,{start})]
    while q:
        p,l,seen = q.pop()
        if p==end:
            if l>best: best=l
        else:
            for n,nl in graph[p]:
                if n not in seen:
                    q.append((n, l+nl, seen|{n}))
    return best

def part1(text):
    g,s,e = parse(text)
    return longest_path(build_graph(g,s,e,True),s,e)

def part2(text):
    g,s,e = parse(text)
    return longest_path(build_graph(g,s,e,False),s,e)

if __name__=="__main__":
    fn=sys.argv[1]
    t=open(fn).read()
    print(part1(t), part2(t))