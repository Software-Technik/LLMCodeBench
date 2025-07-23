import sys
from copy import deepcopy

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

tiles = {}

for line in lines:
    x, y = 0, 0
    for dx, dy in line:
        x += dx
        y += dy
    tiles[(x, y)] = not tiles.get((x, y), False)

def count(tiles):
    return sum(1 for state in tiles.values() if state)

result1 = count(tiles)

neighbor_deltas = list(dirs.values())

def get_neighbor_coords(x, y):
    return [(x + dx, y + dy) for dx, dy in neighbor_deltas]

def adjacent(tiles, x, y):
    return sum(1 for xx, yy in get_neighbor_coords(x, y) if tiles.get((xx, yy), False))

for _ in range(100):
    to_check = set()
    for coord, alive in tiles.items():
        if alive:
            to_check.add(coord)
            for neighbor in get_neighbor_coords(coord[0], coord[1]):
                to_check.add(neighbor)
    nu_tiles = {}
    for coord in to_check:
        alive = tiles.get(coord, False)
        adj = adjacent(tiles, coord[0], coord[1])
        if alive and (adj == 1 or adj == 2):
            nu_tiles[coord] = True
        elif not alive and adj == 2:
            nu_tiles[coord] = True
    tiles = nu_tiles

result2 = count(tiles)
print(result1, result2)