import sys
from collections import defaultdict

def build_graph(data):
    graph = defaultdict(list)
    for node, neighbors in (line.split(" <-> ") for line in data if line.strip()):
        graph[int(node)] = list(map(int, neighbors.split(", ")))
    return graph

def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

def part1(data):
    graph = build_graph(data)
    visited = set()
    dfs(graph, 0, visited)
    return len(visited)

def part2(data):
    graph = build_graph(data)
    visited = set()
    groups = sum(dfs(graph, node, visited) or 1 for node in graph if node not in visited)
    return groups

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")