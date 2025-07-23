import sys

def minmax(_iterable):
    it = iter(_iterable)
    _min = _max = next(it, None)
    if _min is None:
        return float('inf'), float('-inf')
    for x in it:
        _min = min(_min, x)
        _max = max(_max, x)
    return _min, _max

def part1(data):
    droplets = {tuple(map(int, line.split(","))) for line in data}
    sides = 0
    neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    for x, y, z in droplets:
        sides += sum((x + dx, y + dy, z + dz) not in droplets for dx, dy, dz in neighbors)

    return sides

def part2(data):
    droplets = {tuple(map(int, line.split(","))) for line in data}
    sides = 0
    neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    min_x, max_x = minmax(x for x, y, z in droplets)
    min_y, max_y = minmax(y for x, y, z in droplets)
    min_z, max_z = minmax(z for x, y, z in droplets)

    start = (min_x - 1, min_y - 1, min_z - 1)  # Air cube just outside the droplets
    queue = [start]
    seen = droplets.copy()

    while queue:
        x, y, z = queue.pop(0)
        if (x, y, z) in seen: continue

        seen.add((x, y, z))
        neighbor_droplets = [(x + dx, y + dy, z + dz) for dx, dy, dz in neighbors]
        sides += sum(nd in droplets for nd in neighbor_droplets)

        for nd in neighbor_droplets:
            if nd not in seen and min_x - 1 <= nd[0] <= max_x + 1 \
               and min_y - 1 <= nd[1] <= max_y + 1 \
               and min_z - 1 <= nd[2] <= max_z + 1:
                queue.append(nd)

    return sides

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")