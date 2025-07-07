import sys
from collections import defaultdict

def part1(lines):
    adj = defaultdict(set)
    for line in lines:
        a, b = line.split("-")
        adj[a].add(b)
        adj[b].add(a)

    triangles = 0
    for a in adj:
        a_nbrs = adj[a]
        for i in a_nbrs:
            common = a_nbrs.intersection(adj[i])
            for j in common:
                if "t" in (a[0], i[0], j[0]):
                    triangles += 1

    return triangles // 3

def part2(lines):
    adj = defaultdict(set)
    for line in lines:
        a, b = line.split("-")
        adj[a].add(b)
        adj[b].add(a)

    def is_clique(nodes):
        return all(nodes[j] in adj[nodes[i]] for i in range(len(nodes)) for j in range(i + 1, len(nodes)))

    big_clique = []

    for node in adj:
        nbrs = list(adj[node])
        k = len(nbrs)
        for mask in range(1 << k):
            nodes = [node] + [nbrs[i] for i in range(k) if mask & (1 << i)]
            if is_clique(nodes) and len(nodes) > len(big_clique):
                big_clique = nodes

    return ",".join(sorted(big_clique))

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")

    print(part1(lines), part2(lines))