import sys

dirs = {"e": (2, 0), "w": (-2, 0), "se": (1, 1), "ne": (1, -1), "nw": (-1, -1), "sw": (-1, 1)}
neighbor_deltas = list(dirs.values())

def line_transform(line):
    res = []
    i = 0
    while i < len(line):
        if line[i] in ("e", "w"):
            res.append(dirs[line[i]])
            i += 1
        else:
            res.append(dirs[line[i:i+2]])
            i += 2
    return res

with open(sys.argv[1]) as f:
    lines = [line_transform(line.strip()) for line in f if line.strip()]

black = set()
for moves in lines:
    x = y = 0
    for dx, dy in moves:
        x += dx; y += dy
    if (x, y) in black: black.remove((x, y))
    else: black.add((x, y))

result1 = len(black)

for _ in range(100):
    to_check = set()
    for x, y in black:
        to_check.add((x, y))
        for dx, dy in neighbor_deltas:
            to_check.add((x+dx, y+dy))
    new_black = set()
    for x, y in to_check:
        cnt = 0
        for dx, dy in neighbor_deltas:
            if (x+dx, y+dy) in black: cnt += 1
        if (x, y) in black:
            if 1 <= cnt <= 2: new_black.add((x, y))
        else:
            if cnt == 2: new_black.add((x, y))
    black = new_black

print(result1, len(black))