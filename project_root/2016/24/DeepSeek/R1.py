import sys
from collections import deque
from itertools import permutations

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    maze = infile.read().splitlines()

coordinates = {}
for y, row in enumerate(maze):
    for x, value in enumerate(row):
        if value.isdigit():
            coordinates[value] = (x, y)

points_list = sorted(coordinates.keys(), key=int)
n = len(points_list)
coords_list = [coordinates[p] for p in points_list]
coord_to_index = {coord: idx for idx, coord in enumerate(coords_list)}

D = [[0] * n for _ in range(n)]
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

for i in range(n):
    start_coord = coords_list[i]
    queue = deque([(start_coord, 0)])
    visited = set([start_coord])
    remaining_goals = set(coords_list) - {start_coord}
    while queue and remaining_goals:
        (x, y), steps = queue.popleft()
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if ny < 0 or ny >= len(maze) or nx < 0 or nx >= len(maze[0]):
                continue
            ncoord = (nx, ny)
            if ncoord in visited:
                continue
            if maze[ny][nx] == '#':
                continue
            visited.add(ncoord)
            new_steps = steps + 1
            queue.append((ncoord, new_steps))
            if ncoord in remaining_goals:
                j = coord_to_index[ncoord]
                D[i][j] = new_steps
                D[j][i] = new_steps
                remaining_goals.discard(ncoord)

min1 = float('inf')
min2 = float('inf')
for perm in permutations(range(1, n)):
    total = D[0][perm[0]]
    for i in range(len(perm)-1):
        total += D[perm[i]][perm[i+1]]
    min1 = min(min1, total)
    min2 = min(min2, total + D[perm[-1]][0])

print(f"{min1} {min2}")