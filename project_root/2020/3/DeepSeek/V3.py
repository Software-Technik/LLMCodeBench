import sys

input_path = sys.argv[1]

with open(input_path) as f:
    lines = [line.strip() for line in f]

width = len(lines[0])
height = len(lines)

def find_tree_count(dx, dy):
    x = 0
    y = 0
    tree_cnt = 0
    while y < height:
        if lines[y][x % width] == '#':
            tree_cnt += 1
        x += dx
        y += dy
    return tree_cnt

result1 = find_tree_count(3, 1)
tot = result1 * find_tree_count(1, 1) * find_tree_count(5, 1) * find_tree_count(7, 1) * find_tree_count(1, 2)

print(f"{result1} {tot}")