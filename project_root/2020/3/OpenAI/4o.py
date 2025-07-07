import sys

input_path = sys.argv[1]

with open(input_path) as f:
    lines = [x.strip() for x in f.readlines()]

width = len(lines[0])
height = len(lines)

def find_tree_count(dx, dy):
    x = 0
    tree_cnt = 0
    for y in range(0, height, dy):
        if lines[y][x % width] == "#":
            tree_cnt += 1
        x += dx
    return tree_cnt

tot = 1
result1 = 0
for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    count = find_tree_count(dx, dy)
    tot *= count
    if dx == 3 and dy == 1:
        result1 = count

print(f"{result1} {tot}")