import sys
from collections import defaultdict

def build_graph(data):
    graph = defaultdict(list)
    for line in data:
        if not line.strip():
            continue
        node, neighbors = line.split(" <-> ")
        graph[int(node)] = list(map(int, neighbors.split(", ")))
    return graph

def dfs(start, graph, visited):
    stack = [start]
    visited.add(start)
    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

def part1(data):
    graph = build_graph(data)
    visited = set()
    dfs(0, graph, visited)
    return len(visited)

def part2(data):
    graph = build_graph(data)
    visited = set()
    groups = 0
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited)
            groups += 1
    return groups

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")