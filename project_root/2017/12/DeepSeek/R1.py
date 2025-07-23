import sys
from collections import defaultdict

def build_graph(data):
    graph = defaultdict(list)
    for line in data:
        if not line.strip():
            continue
        node, neighbors = line.split(" <-> ")
        node = int(node)
        neighbors_list = list(map(int, neighbors.split(", ")))
        graph[node] = neighbors_list
    return graph

def dfs(start, graph, visited):
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current])

def part1(graph):
    visited = set()
    dfs(0, graph, visited)
    return len(visited)

def part2(graph):
    visited = set()
    groups = 0
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited)
            groups += 1
    return groups

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

graph = build_graph(data)
sys.stdout.write(f"{part1(graph)}\n{part2(graph)}\n")