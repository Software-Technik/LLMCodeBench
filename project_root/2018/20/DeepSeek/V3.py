import networkx as nx
from collections import deque, Counter
import sys

input_f = sys.argv[1]
with open(input_f) as f:
    directions = f.readline().strip()

graph = nx.Graph()

move = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}

junctions = deque()
junction = (0, 0)
location = (0, 0)

for direction in directions:
    if direction in 'NEWS':
        x, y = location
        dx, dy = move[direction]
        new_location = (x + dx, y + dy)
        graph.add_edge(location, new_location)
        location = new_location
    elif direction == '(':
        junctions.append(junction)
        junction = location
    elif direction == ')':
        junction = junctions.pop()
    elif direction == '|':
        location = junction

shortest_paths = nx.shortest_path_length(graph, (0, 0))
max_distance = max(shortest_paths.values())
count_1000 = sum(1 for dist in shortest_paths.values() if dist >= 1000)

print(max_distance)
print(count_1000)