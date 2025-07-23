import sys
from collections import deque

def part1(data):
    droplets = {tuple(map(int, line.split(","))) for line in data}
    sides = 0
    neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    for x, y, z in droplets:
        for dx, dy, dz in neighbors:
            if (x + dx, y + dy, z + dz) not in droplets:
                sides += 1
    return sides

def part2(data):
    droplets = {tuple(map(int, line.split(","))) for line in data}
    sides = 0
    neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    min_x = min(d[0] for d in droplets)
    max_x = max(d[0] for d in droplets)
    min_y = min(d[1] for d in droplets)
    max_y = max(d[1] for d in droplets)
    min_z = min(d[2] for d in droplets)
    max_z = max(d[2] for d in droplets)

    x_range = range(min_x - 1, max_x + 2)
    y_range = range(min_y - 1, max_y + 2)
    z_range = range(min_z - 1, max_z + 2)

    start = (min_x - 1, min_y - 1, min_z - 1)
    queue = deque([start])
    seen = set(droplets)
    seen.add(start)

    while queue:
        x, y, z = queue.popleft()

        for dx, dy, dz in neighbors:
            nd = (x + dx, y + dy, z + dz)
            if nd in droplets:
                sides += 1
            elif nd not in seen and nd[0] in x_range and nd[1] in y_range and nd[2] in z_range:
                seen.add(nd)
                queue.append(nd)
    return sides

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")