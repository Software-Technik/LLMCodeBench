import sys

input_path = sys.argv[1]
max_id = 0
min_id = None
sum_ids = 0

with open(input_path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        id = 0
        for c in line:
            id = (id << 1) | (c == 'B' or c == 'R')
        sum_ids += id
        if id > max_id:
            max_id = id
        if min_id is None or id < min_id:
            min_id = id

count = max_id - min_id + 1
expected_sum = (min_id + max_id) * count // 2
missing = expected_sum - sum_ids

print(max_id, missing)