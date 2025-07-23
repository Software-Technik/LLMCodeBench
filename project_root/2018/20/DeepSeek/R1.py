import sys
from collections import deque

input_f = sys.argv[1]
with open(input_f) as f:
    directions = f.readline().strip()

move = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}

graph = {}
junctions = deque()
junction = (0, 0)
location = (0, 0)

for direction in directions:
    if direction in 'NEWS':
        x, y = location
        dx, dy = move[direction]
        new_location = (x + dx, y + dy)
        graph.setdefault(location, set()).add(new_location)
        graph.setdefault(new_location, set()).add(location)
        location = new_location
    elif direction == '(':
        junctions.append(junction)
        junction = location
    elif direction == ')':
        junction = junctions.pop()
    elif direction == '|':
        location = junction

distances = {}
queue = deque([(0, 0)])
distances[(0, 0)] = 0
max_doors = 0
count_doors = 0

while queue:
    x, y = queue.popleft()
    d = distances[(x, y)]
    if d > max_doors:
        max_doors = d
    if d >= 1000:
        count_doors += 1
    for neighbor in graph.get((x, y), set()):
        if neighbor not in distances:
            distances[neighbor] = d + 1
            queue.append(neighbor)

print(max_doors)
print(count_doors)