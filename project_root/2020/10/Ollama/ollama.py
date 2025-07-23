from itertools import combinations
import os
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

def line_transform(line):
    return int(line)

lines = [line_transform(line) for line in lines]
srtd = sorted(lines)

ones = 1
threes = 1

for idx, j in enumerate(srtd[1:], start=1):
    diff = j - srtd[idx - 1]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1

result1 = ones * threes

paths = {0: 1}
for s in srtd:
    paths[s] = sum([paths.get(s - d, 0) for d in [1, 2, 3]])

result2 = paths[srtd[-1]]

print(result1, result2)