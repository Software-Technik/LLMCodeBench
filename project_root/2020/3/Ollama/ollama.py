import sys

input_path = sys.argv[1]

lines = list(map(str.strip, open(input_path)))[::-1]
width, height = len(lines[0]), len(lines)

def find_tree_count(ds):
    dy, dx, tree_cnt = ds[1], ds[0], 0
    for i in range(0, width * height - (dx + dy), dx + dy):
        if lines[i % height][i // height] == "#":
            tree_cnt += 1
    return tree_cnt

result = [find_tree_count(d) for d in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]

print(result[1], eval("*".join(map(str, result))))