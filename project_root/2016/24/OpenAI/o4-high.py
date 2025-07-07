import sys
from collections import deque
from itertools import permutations
maze = open(sys.argv[1]).read().splitlines()
H, W = len(maze), len(maze[0])
positions = []
for y, row in enumerate(maze):
    for x, ch in enumerate(row):
        if ch.isdigit():
            positions.append((int(ch), x, y))
positions.sort()
coords = [(x, y) for _, x, y in positions]
n = len(coords)
pos_to_index = {coords[i]: i for i in range(n)}
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
dists = [[0] * n for _ in range(n)]
for i, (sx, sy) in enumerate(coords):
    visited = [bytearray(W) for _ in range(H)]
    dq = deque([(sx, sy, 0)])
    visited[sy][sx] = 1
    remaining = n
    while dq and remaining:
        x, y, d = dq.popleft()
        j = pos_to_index.get((x, y))
        if j is not None:
            dists[i][j] = d
            remaining -= 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and not visited[ny][nx] and maze[ny][nx] != '#':
                visited[ny][nx] = 1
                dq.append((nx, ny, d + 1))
min1 = 10**18; min2 = 10**18
for perm in permutations(range(1, n)):
    d = dists[0][perm[0]]
    for a, b in zip(perm, perm[1:]):
        d += dists[a][b]
    if d < min1: min1 = d
    d2 = d + dists[perm[-1]][0]
    if d2 < min2: min2 = d2
sys.stdout.write(f"{min1} {min2}")