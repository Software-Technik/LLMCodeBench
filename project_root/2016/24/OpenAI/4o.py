import sys
from collections import deque
from itertools import permutations

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    maze = infile.read().splitlines()

def bfs(start, goal):
    DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
    que = deque([(start, 0)])
    seen = set([start])
    
    while que:
        (x, y), steps = que.popleft()
        if (x, y) == goal:
            return steps
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in seen and maze[ny][nx] != '#':
                que.append(((nx, ny), steps + 1))
                seen.add((nx, ny))

def find_shortest(second_part=False):
    min_dist = float('inf')
    for path in permutations(range(1, len(coordinates))):
        path_dist = sum(distances[a][b] for a, b in zip((0,) + path, path))
        if second_part:
            path_dist += distances[path[-1]][0]
        min_dist = min(min_dist, path_dist)
    return min_dist

coordinates = {}
for y, row in enumerate(maze):
    for x, value in enumerate(row):
        if value.isdigit():
            coordinates[int(value)] = (x, y)

distances = [[0] * len(coordinates) for _ in range(len(coordinates))]

for start, start_pos in coordinates.items():
    for goal, goal_pos in coordinates.items():
        if start < goal:
            dist = bfs(start_pos, goal_pos)
            distances[start][goal] = distances[goal][start] = dist

sys.stdout.write(f"{find_shortest()} {find_shortest(True)}")