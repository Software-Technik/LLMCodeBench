import networkx as nx
from collections import deque
from sys import argv

input_f = argv[1]
with open(input_f) as f:
    directions = f.readline().strip()

graph = nx.Graph()
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

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

doors = nx.shortest_path_length(graph, (0, 0)).values()
print(max(doors))
print(sum(1 for d in doors if d >= 1000))