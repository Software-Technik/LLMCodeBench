import sys
from collections import deque

NDIRS = {'>': 1, '^': -1j, '<': -1, 'v': 1j}

def parse(text):
    grid = {}
    lines = text.strip().splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            grid[x + 1j*y] = c
    start = 1
    max_x = max(p.real for p in grid)
    max_y = max(p.imag for p in grid)
    end = (max_x - 1) + 1j*max_y
    return grid, start, end

def find_adjacent(p0, grid, terminals, ndirs_enabled):
    adj = []
    dq = deque([(p0, 0, {p0})])
    while dq:
        p, l, seen = dq.popleft()
        if p in terminals and p != p0:
            adj.append((p, l))
            continue
        nbs = []
        for d in (1, -1, 1j, -1j):
            np = p + d
            if np in grid and grid[np] != '#' and np not in seen:
                nbs.append(np)
        if len(nbs) > 1 and p != p0:
            adj.append((p, l))
            continue
        for np in nbs:
            c = grid[np]
            if ndirs_enabled and c in NDIRS and np + NDIRS[c] != p:
                np2 = np + NDIRS[c]
                dq.append((np2, l+2, seen | {np, np2}))
            elif c == '.' or not ndirs_enabled:
                dq.append((np, l+1, seen | {np}))
    return adj

def build_graph(grid, start, end, ndirs_enabled):
    graph = {}
    seen = set()
    stack = [start]
    terminals = (start, end)
    while stack:
        p = stack.pop()
        if p in seen:
            continue
        seen.add(p)
        nbrs = find_adjacent(p, grid, terminals, ndirs_enabled)
        graph[p] = nbrs
        for q, _ in nbrs:
            if q not in seen:
                stack.append(q)
    return graph

def longest_path(graph, start, end):
    nodes = list(graph.keys())
    if end not in graph:
        nodes.append(end)
    idx = {p: i for i, p in enumerate(nodes)}
    adj = [[] for _ in nodes]
    for p, nbrs in graph.items():
        u = idx[p]
        for q, l in nbrs:
            adj[u].append((idx[q], l))
    s, t = idx[start], idx[end]
    max_len = 0
    def dfs(u, mask, cur):
        nonlocal max_len
        if u == t:
            if cur > max_len:
                max_len = cur
            return
        for v, l in adj[u]:
            bit = 1 << v
            if not (mask & bit):
                dfs(v, mask | bit, cur + l)
    dfs(s, 1 << s, 0)
    return max_len

def part1(text):
    grid, start, end = parse(text)
    return longest_path(build_graph(grid, start, end, True), start, end)

def part2(text):
    grid, start, end = parse(text)
    return longest_path(build_graph(grid, start, end, False), start, end)

if __name__ == "__main__":
    text = open(sys.argv[1]).read()
    r1 = part1(text)
    r2 = part2(text)
    sys.stdout.write(f"{r1} {r2}")