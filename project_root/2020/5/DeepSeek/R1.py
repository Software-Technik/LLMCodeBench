import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    lines = data.splitlines()

def get_row(s):
    s = s[:7]
    s = s.replace("F", "0")
    s = s.replace("B", "1")
    return int(s, 2)

def get_column(s):
    s = s[-3:]
    s = s.replace("L", "0")
    s = s.replace("R", "1")
    return int(s, 2)

def get_id(line):
    row = get_row(line)
    column = get_column(line)
    return row * 8 + column

min_id = None
max_id = None
total_sum = 0

for line in lines:
    id_val = get_id(line)
    if min_id is None or id_val < min_id:
        min_id = id_val
    if max_id is None or id_val > max_id:
        max_id = id_val
    total_sum += id_val

n = max_id - min_id + 1
expected_total = (min_id + max_id) * n // 2
missing = expected_total - total_sum

result1 = max_id
result2 = str(missing)

print(result1, result2)