import os
import sys

input_path = sys.argv[1]

if "s" in sys.argv:
    input_file = "input_small.txt"
else:
    input_file = input_path

try:
    with open(input_file) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

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

black_tiles = set()
for line in lines:
    x, y = 0, 0
    for dx, dy in line:
        x += dx
        y += dy
    pos = (x, y)
    if pos in black_tiles:
        black_tiles.remove(pos)
    else:
        black_tiles.add(pos)

result1 = len(black_tiles)

neighbor_offsets = list(dirs.values())

for _ in range(100):
    candidate_tiles = set(black_tiles)
    for (x, y) in black_tiles:
        for dx, dy in neighbor_offsets:
            candidate_tiles.add((x+dx, y+dy))
    
    next_black = set()
    for tile in candidate_tiles:
        count = 0
        for dx, dy in neighbor_offsets:
            nb = (tile[0]+dx, tile[1]+dy)
            if nb in black_tiles:
                count += 1
        if tile in black_tiles:
            if count == 1 or count == 2:
                next_black.add(tile)
        else:
            if count == 2:
                next_black.add(tile)
    black_tiles = next_black

result2 = len(black_tiles)
print(result1, result2)