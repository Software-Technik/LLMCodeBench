import sys
from collections import defaultdict, deque

def part1(data):
    parent = {}
    for line in data:
        a,b = line.split(')')
        parent[b] = a
    total = 0
    for node in parent:
        curr = node
        while curr in parent:
            total += 1
            curr = parent[curr]
    return total

def part2(data):
    parent = {}
    for line in data:
        a,b = line.split(')')
        parent[b] = a
    adj = defaultdict(list)
    for child, p in parent.items():
        adj[child].append(p)
        adj[p].append(child)
    start = parent["YOU"]
    target = parent["SAN"]
    q = deque([(start,0)])
    seen = {start}
    while q:
        node, d = q.popleft()
        if node == target:
            return d
        for nei in adj[node]:
            if nei not in seen:
                seen.add(nei)
                q.append((nei,d+1))

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read().splitlines()
    print(part1(data), part2(data))