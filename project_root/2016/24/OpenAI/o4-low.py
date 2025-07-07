import sys
from collections import deque
from itertools import permutations

maze = sys.stdin if False else open(sys.argv[1]).read().splitlines()

coords = {}
for y, row in enumerate(maze):
    for x, c in enumerate(row):
        if c.isdigit():
            coords[int(c)] = (x, y)
n = len(coords)
points = [coords[i] for i in range(n)]
dist = [[0]*n for _ in range(n)]
D = [(1,0),(-1,0),(0,1),(0,-1)]
H, W = len(maze), len(maze[0])

def bfs(s, t):
    q = deque([s])
    seen = {s}
    steps = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) == t:
                return steps
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= ny < H and 0 <= nx < W and (nx, ny) not in seen and maze[ny][nx] != '#':
                    seen.add((nx, ny))
                    q.append((nx, ny))
        steps += 1

for i in range(n):
    for j in range(i+1, n):
        d = bfs(points[i], points[j])
        dist[i][j] = dist[j][i] = d

def solve(part2=False):
    best = 10**18
    for p in permutations(range(1, n)):
        d = dist[0][p[0]]
        for a, b in zip(p, p[1:]):
            d += dist[a][b]
        if part2:
            d += dist[p[-1]][0]
        if d < best:
            best = d
    return best

sys.stdout.write(f"{solve()} {solve(True)}")