import sys
from collections import defaultdict
from itertools import product


def part1(lines):
    adj = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        adj[a].append(b)
        adj[b].append(a)

    triangles = set()
    for a in dict(adj):
        for i in adj[a]:
            for j in adj[a]:
                if j in adj[i]:
                    triangles.add(tuple(sorted([a, i, j])))

    ans = 0
    for a, b, c in triangles:
        if "t" in [a[0], b[0], c[0]]:
            ans += 1

    return ans


def part2(lines):

    adj = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        adj[a].append(b)
        adj[b].append(a)

    def is_clique(nodes):
        n = len(nodes)
        for i in range(n):
            for j in range(i + 1, n):
                if not nodes[i] in adj[nodes[j]]:
                    return False
        return True

    big_clique = []

    for node in adj:
        nbrs = adj[node]
        for mask in product((False, True), repeat=len(nbrs)):
            nodes = [node]
            for i, x in enumerate(mask):
                if x:
                    nodes.append(nbrs[i])

            if is_clique(nodes):
                if len(nodes) > len(big_clique):
                    big_clique = nodes

    return ",".join(sorted(big_clique))


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")

    print(part1(lines), part2(lines))
