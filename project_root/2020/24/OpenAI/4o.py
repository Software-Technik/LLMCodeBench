import sys
from itertools import chain, combinations

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    lines = []

dirs = {
    "e": (2, 0),
    "w": (-2, 0),
    "se": (1, 1),
    "ne": (1, -1),
    "nw": (-1, -1),
    "sw": (-1, 1),
}

def line_transform(line):
    nu_line = []
    running = ""
    for c in line:
        running += c
        if running in dirs:
            nu_line.append(dirs[running])
            running = ""
    return nu_line

lines = [line_transform(line) for line in lines]

tiles = dict()

for line in lines:
    x, y = (0, 0)
    for dx, dy in line:
        x, y = x + dx, y + dy
    tiles[(x, y)] = not tiles.get((x, y), False)

def count(tiles):
    return sum(tiles.values())

result1 = count(tiles)

neighbor_deltas = dirs.values()

def get_neighbor_coords(x, y):
    for dx, dy in neighbor_deltas:
        yield (x + dx, y + dy)

for i in range(100):
    to_check = set()
    nu_tiles = tiles.copy()
    for coord, alive in tiles.items():
        if alive:
            to_check.add(coord)
            to_check.update(get_neighbor_coords(coord[0], coord[1]))
    for coord in to_check:
        alive = tiles.get(coord, False)
        adj = sum(tiles.get(neighbor, False) for neighbor in get_neighbor_coords(*coord))
        if alive and (adj == 0 or adj > 2):
            del nu_tiles[coord]
        if not alive and adj == 2:
            nu_tiles[coord] = True
    tiles = nu_tiles

result2 = count(tiles)
print(result1, result2)