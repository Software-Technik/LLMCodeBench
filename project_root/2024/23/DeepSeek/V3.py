import sys
from collections import defaultdict
from itertools import combinations, product


def part1(lines):
    adj = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        adj[a].append(b)
        adj[b].append(a)

    triangles = set()
    for a in adj:
        neighbors = adj[a]
        for i, j in combinations(neighbors, 2):
            if j in adj[i]:
                triangles.add(frozenset({a, i, j}))

    ans = 0
    for triangle in triangles:
        if any(node.startswith('t') for node in triangle):
            ans += 1
    return ans


def part2(lines):
    adj = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        adj[a].append(b)
        adj[b].append(a)

    def is_clique(nodes):
        return all(b in adj[a] for a, b in combinations(nodes, 2))

    max_clique = []
    nodes = list(adj.keys())
    for node in nodes:
        neighbors = adj[node]
        for size in range(len(neighbors), 0, -1):
            for selected in combinations(neighbors, size):
                current_clique = [node] + list(selected)
                if is_clique(current_clique):
                    if len(current_clique) > len(max_clique):
                        max_clique = current_clique
                    break
            if len(max_clique) > size + 1:
                break

    return ",".join(sorted(max_clique))


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))