import sys
from collections import deque

def part1(data):
    droplets = set(tuple(map(int, line.split(","))) for line in data)
    sides = 0
    neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    for x, y, z in droplets:
        sides += sum((x + dx, y + dy, z + dz) not in droplets for dx, dy, dz in neighbors)

    return sides

def part2(data):
    droplets = set(tuple(map(int, line.split(","))) for line in data)
    sides = 0
    neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    min_x, max_x = min(d[0] for d in droplets), max(d[0] for d in droplets)
    min_y, max_y = min(d[1] for d in droplets), max(d[1] for d in droplets)
    min_z, max_z = min(d[2] for d in droplets), max(d[2] for d in droplets)

    x_range = range(min_x - 1, max_x + 2)
    y_range = range(min_y - 1, max_y + 2)
    z_range = range(min_z - 1, max_z + 2)

    start = (min_x - 1, min_y - 1, min_z - 1)
    queue = deque([start])
    seen = set() | droplets

    while queue:
        x, y, z = queue.popleft()

        if (x, y, z) in seen:
            continue

        seen.add((x, y, z))
        sides += sum((x + dx, y + dy, z + dz) in droplets for dx, dy, dz in neighbors)

        for dx, dy, dz in neighbors:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (nx, ny, nz) not in seen and nx in x_range and ny in y_range and nz in z_range:
                queue.append((nx, ny, nz))

    return sides

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")