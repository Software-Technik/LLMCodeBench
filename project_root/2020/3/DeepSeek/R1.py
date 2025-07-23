import sys

input_path = sys.argv[1]

lines = []
with open(input_path) as f:
    lines = [x.strip() for x in f.readlines()]

height = len(lines)
orig_width = len(lines[0])

def find_tree_count(ds):
    dx, dy = ds
    tree_cnt = 0
    x = 0
    y = 0
    while True:
        x += dx
        y += dy
        if y >= height:
            break
        if lines[y][x % orig_width] == '#':
            tree_cnt += 1
    return tree_cnt

tot = 1
result1 = ""
for dd in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    cnt = find_tree_count(dd)
    tot *= cnt
    if dd == (3, 1):
        result1 = cnt

print(str(result1) + " " + str(tot))