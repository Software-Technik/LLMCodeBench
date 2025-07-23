import sys

input_path = sys.argv[1]

with open(input_path) as f:
    lines = f.read().splitlines()

def get_id(line):
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(line[-3:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + column

ids = [get_id(s) for s in lines]
result1 = max(ids)

min_id = min(ids)
max_id = result1
result2 = next(i for i in range(min_id, max_id + 1) if i not in ids)

print(result1, result2)