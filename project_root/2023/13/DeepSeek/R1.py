import sys
from collections import defaultdict

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
    adj = []
    for n0 in n4(start):
        if n0 not in grid or grid[n0]=='#':
            continue
        prev = start
        current = n0
        length = 1
        seen = {start, n0}
        while True:
            if current in terminals and current != start:
                adj.append((current, length))
                break
                
            neighbors = [n for n in n4(current) if n in grid and grid[n]!='#' and n != prev]
            if not neighbors:
                break
                
            if ndirs_enabled and grid[current] in NDIRS:
                next_pos = current + NDIRS[grid[current]]
                if next_pos == prev or next_pos not in grid or grid[next_pos]=='#':
                    break
                neighbors = [next_pos]
                
            if len(neighbors) > 1:
                adj.append((current, length))
                break
                
            nxt = neighbors[0]
            if nxt in seen:
                break
            seen.add(nxt)
            prev = current
            current = nxt
            length += 1
            
            nbs = [n for n in n4(current) if n in grid and grid[n]!='#'] 
            if len(nbs) > 2:
                adj.append((current, length))
                break
    return adj

def build_graph(grid, start, end, ndirs_enabled):
    graph, seen, q = defaultdict(list), set(), [start]
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
    visited = set([start])
    stack = [(start, 0, 0)]
    max_length = 0
    while stack:
        node, length, idx = stack[-1]
        if node == end:
            if length > max_length:
                max_length = length
            visited.remove(node)
            stack.pop()
            continue
        neighbors = graph[node]
        if idx < len(neighbors):
            n, nl = neighbors[idx]
            stack[-1] = (node, length, idx+1)
            if n not in visited:
                visited.add(n)
                stack.append((n, length+nl, 0))
        else:
            visited.remove(node)
            stack.pop()
    return max_length

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