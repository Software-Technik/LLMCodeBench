import sys
from collections import deque

def part1(data):
    parent = {}
    for line in data:
        a, b = line.split(')')
        parent[b] = a
    depth = {'COM': 0}
    total = 0
    for node in parent:
        curr = node
        temp = []
        while curr not in depth:
            temp.append(curr)
            curr = parent[curr]
        base = depth[curr]
        for i, n in enumerate(reversed(temp), 1):
            depth[n] = base + i
        total += depth[node]
    return total

def part2(data):
    graph = {}
    for line in data:
        a, b = line.split(')')
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    dq = deque([('YOU', 0)])
    seen = {'YOU'}
    while dq:
        u, d = dq.popleft()
        if u == 'SAN':
            return d - 2
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                dq.append((v, d + 1))

if __name__ == '__main__':
    path = sys.argv[1]
    with open(path) as f:
        data = f.read().splitlines()
    sys.stdout.write(f"{part1(data)} {part2(data)}")