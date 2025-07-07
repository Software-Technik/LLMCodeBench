import sys
from collections import defaultdict, deque

NDIRS = {'>': 1, '^': -1j, '<': -1, 'v': 1j}
n4 = lambda p: [p - 1j, p - 1, p + 1, p + 1j]

def parse(text):
    grid = {
        x + 1j * y: c
        for y, line in enumerate(text.strip().splitlines())
        for x, c in enumerate(line.strip())
    }
    start = 1
    end = max(p.real for p in grid) - 1 + 1j * max(p.imag for p in grid)
    return grid, start, end

def find_adjacent(start, grid, terminals, ndirs_enabled):
    adj, q = [], deque([(start, 0, {start})])
    while q:
        p, l, seen = q.popleft()
        if p in terminals and p != start:
            adj.append((p, l))
            continue

        neighbors = [n for n in n4(p) if n in grid and n not in seen and grid[n] != '#']
        if len(neighbors) > 1 and p != start:
            adj.append((p, l))
            continue

        for n in neighbors:
            if ndirs_enabled and grid[n] in NDIRS and n + NDIRS[grid[n]] != p:
                next_pos = n + NDIRS[grid[n]]
                q.append((next_pos, l + 2, seen | {n, next_pos}))
            elif grid[n] == '.' or not ndirs_enabled:
                q.append((n, l + 1, seen | {n}))
    return adj

def build_graph(grid, start, end, ndirs_enabled):
    graph, seen, q = defaultdict(list), set(), deque([start])
    while q:
        p = q.pop()
        if p in seen:
            continue
        seen.add(p)
        for n, l in find_adjacent(p, grid, [start, end], ndirs_enabled):
            graph[p].append((n, l))
            if n not in seen:
                q.append(n)
    return graph

def longest_path(graph, start, end):
    longest, q = 0, deque([(start, 0, {start})])
    while q:
        p, l, seen = q.pop()
        if p == end:
            longest = max(longest, l)
            continue
        for n, nl in graph[p]:
            if n not in seen:
                q.append((n, l + nl, seen | {n}))
    return longest

def part1(text):
    grid, start, end = parse(text)
    graph = build_graph(grid, start, end, ndirs_enabled=True)
    return longest_path(graph, start, end)

def part2(text):
    grid, start, end = parse(text)
    graph = build_graph(grid, start, end, ndirs_enabled=False)
    return longest_path(graph, start, end)

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")