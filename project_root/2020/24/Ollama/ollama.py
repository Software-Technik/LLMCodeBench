import sys
from itertools import chain, combinations

input_path = sys.argv[1]

try:
    with open(input_file if "s" in sys.argv else input_path) as f:
        data = f.read().splitlines()
except:
    data = []

dirs = {
    "e": (2, 0),
    "w": (-2, 0),
    "se": (1, 1),
    "ne": (1, -1),
    "nw": (-1, -1),
    "sw": (-1, 1),
}

def line_transform(line):
    coords = []
    i = 0
    while i < len(line):
        if line[i:i+2] in dirs:
            coords.append(dirs[line[i:i+2]])
            i += 2
        else:
            coords.append(dirs[line[i]])
            i += 1
    return coords

lines = [line_transform(line) for line in data]

tiles = {}

for line in lines:
    x, y = (0, 0)
    for dx, dy in line:
        x += dx
        y += dy
    tiles[(x, y)] = not tiles.get((x, y), False)

def count(tiles):
    return sum(1 for tile in tiles.values() if tile == True)

result1 = count(tiles)

neighbor_deltas = dirs.values()

for _ in range(100):
    nu_tiles = {}
    to_check = set()
    for (x, y) in tiles:
        alive = tiles[(x, y)]
        if alive:
            to_check.add((x, y))
            neighbor_locs = set((x + dx, y + dy) for dx, dy in neighbor_deltas)
            to_check.update(neighbor_locs)

    for (x, y) in to_check:
        adj = sum(tiles.get((x + dx, y + dy), False) for dx, dy in neighbor_deltas)
        alive = tiles.get((x, y), False)
        if alive and (adj == 0 or adj > 2):
            continue
        if not alive and adj == 2:
            nu_tiles[(x, y)] = True
        if alive:
            nu_tiles[(x, y)] = True

    tiles = nu_tiles

result2 = count(tiles)
print(result1, result2)