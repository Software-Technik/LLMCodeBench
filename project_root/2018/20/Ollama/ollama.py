import sys
from collections import deque

input_f = sys.argv[1]
with open(input_f) as f:
    directions = f.readline().strip()

move = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

compound = {}
junctions = deque()
location = junctions.append((0, 0))

for direction in directions:
    if direction in move:
        x, y = location[0]
        dx, dy = move[direction]
        new_location = (x + dx, y + dy)
        path_key = (*location[0], *new_location)

        if location not in compound:
            compound[location] = {}
        compound[location].setdefault(new_location, set()).add(path_key)
        location = deque([(1283, new_location)])

    elif direction == '|':
        location.clear()
        location.append(junctions[-1])

    elif direction == ')':
        junctions.pop()
        location.clear()
        location.append(junctions[-1])
    elif direction == '(':
        junctions.append(location[:])
        location.clear()

def explore(loc, dist):
    for n_loc in compound[loc]:
        explore(n_loc, dist + 1)

distances = {}
explore((0, 0), 0)
print(max(distances.values()))
count = sum(1 for d in distances.values() if d >= 1000)
print(count)