import sys
from collections import deque

directions = open(sys.argv[1]).readline().strip()

move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
graph = {}
junctions = []
junction = location = (0, 0)

def add_edge(a, b):
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

for c in directions:
    if c in move:
        x, y = location
        dx, dy = move[c]
        new = (x + dx, y + dy)
        add_edge(location, new)
        location = new
    elif c == '(':
        junctions.append(junction)
        junction = location
    elif c == ')':
        junction = junctions.pop()
    elif c == '|':
        location = junction

dist = { (0,0): 0 }
dq = deque([(0,0)])
while dq:
    u = dq.popleft()
    for v in graph.get(u,()):
        if v not in dist:
            dist[v] = dist[u] + 1
            dq.append(v)

dists = dist.values()
print(max(dists))
print(sum(1 for d in dists if d >= 1000))