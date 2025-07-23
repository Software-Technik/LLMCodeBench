import sys
from collections import defaultdict
from itertools import product

def part1(lines):
    adj = defaultdict(list)
    triangles = set()

    for line in lines:
        a, b = line.split("-")
        if "t" == a[0]:
            nodes = {a}
            for i in adj[a]:
                for j in adj[a]:
                    if j != i and j in adj[i] and "t" in (j[0],):
                        triangles.add(tuple(sorted([a, i, j])))
        adj[a].append(b)
        adj[b].append(a)

    return len(triangles)

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
        nbr_count = len(nbrs)
        mask = None

        # To avoid redundant checks, start with the longest possible clique
        if 1 <= nbr_count < 25:
            mask_gen = list(product((False, True), repeat=nbr_count))

        else: mask_gen = [[True]]

    for cliq_mask in mask_gen:
        nodes = [node]
        for i, x in enumerate(cliq_mask):
            if x:
                nodes.append(nbrs[i])
        if is_clique(nodes) and len(nodes) > len(big_clique):
            big_clique = nodes

    return ",".join(sorted(big_clique))

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = [line.strip() for line in fin.read().strip().split('\n')]

print(part1(lines))
print(part2(lines))