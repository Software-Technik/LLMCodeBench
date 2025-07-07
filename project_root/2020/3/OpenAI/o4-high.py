import sys

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f]
height = len(lines)
width = len(lines[0])

def tree_count(dx, dy):
    cnt = 0
    x = 0
    for y in range(dy, height, dy):
        x = (x + dx) % width
        if lines[y][x] == '#':
            cnt += 1
    return cnt

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = [tree_count(dx, dy) for dx, dy in slopes]
result1 = counts[1]
tot = 1
for c in counts:
    tot *= c

print(f"{result1} {tot}")