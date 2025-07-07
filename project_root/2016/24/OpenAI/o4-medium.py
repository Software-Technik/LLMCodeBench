import sys
from collections import deque
from itertools import permutations

with open(sys.argv[1]) as f:
    maze = f.read().splitlines()
H, W = len(maze), len(maze[0]) if maze else (0, 0)
points = {}
for y in range(1, H-1):
    row = maze[y]
    for x in range(1, W-1):
        c = row[x]
        if '0' <= c <= '9':
            points[int(c)] = (x, y)
N = len(points)
coords = [points[i] for i in range(N)]
pos2idx = {coords[i]: i for i in range(N)}
dists = [[0]*N for _ in range(N)]
DELTAS = ((1,0),(-1,0),(0,1),(0,-1))
for i, (sx, sy) in enumerate(coords):
    dist_map = [[-1]*W for _ in range(H)]
    q = deque([(sx, sy)])
    dist_map[sy][sx] = 0
    need = set(range(N)) - {i}
    while q and need:
        x, y = q.popleft()
        d = dist_map[y][x] + 1
        for dx, dy in DELTAS:
            nx, ny = x+dx, y+dy
            if 0 <= nx < W and 0 <= ny < H and dist_map[ny][nx] < 0 and maze[ny][nx] != '#':
                dist_map[ny][nx] = d
                if (nx, ny) in pos2idx:
                    j = pos2idx[(nx, ny)]
                    if j in need:
                        dists[i][j] = dists[j][i] = d
                        need.remove(j)
                q.append((nx, ny))
best1 = float('inf')
best2 = float('inf')
for perm in permutations(range(1, N)):
    dist = dists[0][perm[0]]
    for a, b in zip(perm, perm[1:]):
        dist += dists[a][b]
    if dist < best1:
        best1 = dist
    dist2 = dist + dists[perm[-1]][0]
    if dist2 < best2:
        best2 = dist2
sys.stdout.write(f"{best1} {best2}")