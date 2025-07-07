import sys
from collections import deque, defaultdict
with open(sys.argv[1]) as f:
    s = f.readline().strip()
moves = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
neighbors = defaultdict(list)
stack = []
junction = (0,0)
location = (0,0)
for c in s:
    if c in moves:
        dx,dy = moves[c]
        new = (location[0]+dx, location[1]+dy)
        neighbors[location].append(new)
        neighbors[new].append(location)
        location = new
    elif c == '(':
        stack.append(junction)
        junction = location
    elif c == '|':
        location = junction
    elif c == ')':
        junction = stack.pop()
dist = {(0,0):0}
q = deque([(0,0)])
while q:
    u = q.popleft()
    d = dist[u] + 1
    for v in neighbors[u]:
        if v not in dist:
            dist[v] = d
            q.append(v)
vals = dist.values()
print(max(vals))
print(sum(1 for x in vals if x>=1000))