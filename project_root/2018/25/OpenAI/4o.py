import sys

input_f = sys.argv[1]
with open(input_f) as f:
    points = [tuple(int(n) for n in line.strip().split(",")) for line in f]

def manhattan_dist(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    rootX = find(x, parent)
    rootY = find(y, parent)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

parent = {p: p for p in points}
rank = {p: 0 for p in points}

for i, point1 in enumerate(points):
    for point2 in points[i+1:]:
        if manhattan_dist(point1, point2) <= 3:
            union(point1, point2, parent, rank)

components = set(find(p, parent) for p in points)

sys.stdout.write(f"{len(components)}")