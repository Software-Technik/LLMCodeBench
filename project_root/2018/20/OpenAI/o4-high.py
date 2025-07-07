import sys
from collections import defaultdict, deque
s = open(sys.argv[1]).readline().strip()
graph = defaultdict(list)
positions = {(0, 0)}
stack = []
move = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
for c in s:
    if c in move:
        dx, dy = move[c]
        new = set()
        for x, y in positions:
            nx, ny = x + dx, y + dy
            graph[(x, y)].append((nx, ny))
            graph[(nx, ny)].append((x, y))
            new.add((nx, ny))
        positions = new
    elif c == '(':
        stack.append((set(positions), set()))
    elif c == '|':
        saved, res = stack[-1]
        res |= positions
        positions = set(saved)
        stack[-1] = (saved, res)
    elif c == ')':
        saved, res = stack.pop()
        res |= positions
        positions = res
dist = {(0, 0): 0}
q = deque([(0, 0)])
maxd = 0
count_far = 0
while q:
    p = q.popleft()
    d = dist[p]
    if d > maxd: maxd = d
    if d >= 1000: count_far += 1
    for nei in graph[p]:
        if nei not in dist:
            dist[nei] = d + 1
            q.append(nei)
print(maxd)
print(count_far)