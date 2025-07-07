import sys

def get_row(s):
    return int(s[:7].replace("F", "0").replace("B", "1"), 2)

def get_column(s):
    return int(s[-3:].replace("L", "0").replace("R", "1"), 2)

def get_id(line):
    return get_row(line) * 8 + get_column(line)

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

ids = [get_id(s) for s in lines]
result1 = max(ids)

all_ids = set(range(min(ids), max(ids) + 1))
missing_id = all_ids - set(ids)
result2 = next(iter(missing_id))

print(result1, result2)