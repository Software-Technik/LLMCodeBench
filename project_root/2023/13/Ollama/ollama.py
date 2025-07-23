import sys
from collections import defaultdict

NDIRS = {'>': 1, '^': -1j, '<': -1, 'v': 1j}

def n4(p):
    dxdy = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    return [p + x + y * 1j for x, y in dxdy]

parse = lambda text: (
    {x + y * 1j: c for y, line in enumerate(text.strip().splitlines()) for x, c in enumerate(line)},
    next(x + min(y, y * 1j) for y, l in enumerate(next(t.split() for t in text.strip().splitlines())) for x, c in enumerate(l)),
    max(p.real for p in p) - 1 + 1j * (max(complex(p).imag for p in p))
)

def find_adjacent(start, grid, terminals, ndirs_enabled):
    adj = []
    q = [(start, 0, {start})]
    while q:
        p, length, seen = q.pop(0)
        if p in terminals and (p != start):
            adj.append((p, length))
            continue
        neighbors = [n for n in n4(p) if n in grid and n not in seen and grid[n] != '#']
        if len(neighbors) > 1:
            adj.append((p, length))
            continue
        next_positions = []
        for neighbor in neighbors:
            gn = grid[neighbor]
            if ndirs_enabled and gn in NDIRS and neighbor + NDIRS[gn] != p:
                next_neighbors = [neighbor + NDIRS[gn], neighbor + 2 * NDIRS[gn]]
                next_positions += [(pos, length - len([f for f in n4(neighbor) if f == start])) for pos in next_neighbors]
            elif gn == '.' or not ndirs_enabled:
                next_positions.append((neighbor, length))
        q.extend(next_positions)
    return adj

def build_graph(grid, start, end, ndirs_enabled):
    graph = defaultdict(list)
    seen = set([start])
    stack = [start]
    while stack:
        p = stack.pop()
        if p not in seen:
            stack.append(p)
            continue
        for n, length in find_adjacent(p, grid, [start, end], ndirs_enabled):
            graph[p].append((n, length))
            if n not in seen:
                stack.append(n)
    return graph

def longest_path(graph, start, end):
    longest = 0
    q = [(start, 0, {start})]
    while q:
        p, l, seen = q.pop()
        if p == end:
            longest = max(longest, l)
            continue
        for n, length in graph[p]:
            if n not in seen:
                q.append((n, l + length, seen | {n}))
    return longest

def part1(text):
    grid, start, ends = parse(text)
    graph = build_graph(grid, start, ends, ndirs_enabled=True)
    return sum(length for _, _, length in find_adjacent(start, grid, ends, True))

def part2(text):
    grid, start, end = parse(text)
    graph = build_graph(grid, 0+0j, max(max(complex(c).real + y * 1j for c in r)) -1j + 4* 1j + grid[-end].imag, ndirs_enabled=False)
    return sum(length for _, position in find_adjacent(start, graph, end or [-ends[-1], end[-1]])

if __name__ == "__main__":
    input_file = str(sys.argv[1])
    with open(input_file) as f:
        text = f.read()
    print(part1(text), part2(text))