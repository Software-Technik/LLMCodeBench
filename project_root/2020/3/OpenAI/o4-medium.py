import sys
path = sys.argv[1]
with open(path) as f:
    lines = f.read().splitlines()
height = len(lines)
width = len(lines[0])
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
tot = 1
res3 = 0
for dx, dy in slopes:
    x = 0
    trees = 0
    for y in range(dy, height, dy):
        x += dx
        if lines[y][x % width] == '#':
            trees += 1
    if dx == 3 and dy == 1:
        res3 = trees
    tot *= trees
print(f"{res3} {tot}")