import sys
import numpy as np

input_f = sys.argv[1]

with open(input_f) as f:
    points = np.array([tuple(map(int, line.strip().split(","))) for line in f], dtype=int)

dist_matrix = np.abs(points[:, None] - points[None, :]).sum(axis=2)
connected_points = [set() for _ in range(len(points))]
components = len(points)  # start with all points as separate components

for i in range(len(points)):
    connected_points[i].add(i)
    neighbors = np.where(dist_matrix[:, i] <= 3)[0]
    for neighbor in neighbors:
        if not connected_points[i].intersection(connected_points[neighbor]):
            connected_points[i].update(connected_points[neighbor])
            components -= len(connected_points[neighbor]) - 1

sys.stdout.write(f"{components}")