import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    lines = []

lines = sorted(int(line) for line in lines)

ones = threes = 1

for idx in range(1, len(lines)):
    diff = lines[idx] - lines[idx - 1]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1

result1 = ones * threes

paths = {0: 1}
for s in lines:
    paths[s] = sum(paths.get(s - d, 0) for d in [1, 2, 3])

result2 = paths[lines[-1]]

print(result1, result2)