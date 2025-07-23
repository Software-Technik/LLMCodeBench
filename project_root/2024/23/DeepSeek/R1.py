import sys
from collections import defaultdict


def part1(lines):
    adj = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        adj[a].append(b)
        adj[b].append(a)
    
    count = 0
    for a in adj:
        nbrs = [n for n in adj[a] if n > a]
        n = len(nbrs)
        for i in range(n):
            u = nbrs[i]
            for j in range(i+1, n):
                v = nbrs[j]
                if v in adj[u]:
                    if a[0]=='t' or u[0]=='t' or v[0]=='t':
                        count += 1
    return count


def part2(lines):
    adj = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        adj[a].append(b)
        adj[b].append(a)
    
    best_clique = []
    for u in adj:
        neighbors = adj[u]
        n = len(neighbors)
        adj_mask = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and neighbors[j] in adj[neighbors[i]]:
                    adj_mask[i] |= (1 << j)
        
        best_size = 0
        best_mask = 0
        for mask in range(1 << n):
            valid = True
            size = 0
            for i in range(n):
                if mask & (1 << i):
                    size += 1
                    T = mask & ~(1 << i)
                    if T & ~adj_mask[i]:
                        valid = False
                        break
            if valid and size > best_size:
                best_size = size
                best_mask = mask
        
        clique_nodes = [u]
        for i in range(n):
            if best_mask & (1 << i):
                clique_nodes.append(neighbors[i])
        if len(clique_nodes) > len(best_clique):
            best_clique = clique_nodes
            
    return ",".join(sorted(best_clique))


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))