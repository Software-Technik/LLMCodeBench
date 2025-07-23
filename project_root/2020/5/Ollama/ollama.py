import sys

input_path = sys.argv[1]

with open(input_path) as f:
    lines = f.read().splitlines()

def get_id(line):
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(line[-3:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col

ids = [get_id(s) for s in lines]
result1 = max(ids)

sort_ids = sorted(ids)
for idx, id in enumerate(sort_ids):
    if sort_ids[idx] != sort_ids[idx - 1] + 1:
        result2 = sort_ids[idx - 1] + 1
        break

print(result1, result2)