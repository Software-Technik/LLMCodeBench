import numpy as np
import networkx as nx
from scipy.spatial import distance
import sys

input_f = sys.argv[1]
with open(input_f) as f:
    points = [tuple(map(int, line.strip().split(','))) for line in f]

points_array = np.array(points, dtype=np.int32)
g = nx.Graph()

d = distance.cdist(points_array, points_array, metric="cityblock")

for i in range(len(points)):
    neighbors = np.where(d[i] <= 3)[0]
    for j in neighbors:
        if i != j:
            g.add_edge(points[i], points[j])

sys.stdout.write(f"{nx.number_connected_components(g)}")