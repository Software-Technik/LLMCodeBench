import sys

input_file = sys.argv[1]
if "s" in sys.argv:
    input_file = "input_small.txt"
with open(input_file) as f:
    lines = [l.strip() for l in f if l.strip()]

dirs = {"e": (2, 0), "w": (-2, 0), "se": (1, 1), "ne": (1, -1), "nw": (-1, -1), "sw": (-1, 1)}
black = set()
for s in lines:
    x = y = i = 0
    while i < len(s):
        if s[i] in "ew":
            d = s[i]
            i += 1
        else:
            d = s[i:i+2]
            i += 2
        dx, dy = dirs[d]
        x += dx; y += dy
    if (x, y) in black:
        black.remove((x, y))
    else:
        black.add((x, y))
result1 = len(black)

neighbor_deltas = list(dirs.values())
for _ in range(100):
    counts = {}
    for x, y in black:
        for dx, dy in neighbor_deltas:
            nb = (x+dx, y+dy)
            counts[nb] = counts.get(nb, 0) + 1
    new_black = set()
    for tile, cnt in counts.items():
        if cnt == 2 or (cnt == 1 and tile in black):
            new_black.add(tile)
    black = new_black

result2 = len(black)
print(result1, result2)