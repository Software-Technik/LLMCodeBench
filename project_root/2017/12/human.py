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
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current])

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

# Chargement des données
input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

# Affichage des résultats
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")