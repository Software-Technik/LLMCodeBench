import sys
from functools import cmp_to_key
import json

def part1(data):
    data = [[json.loads(data[i]), json.loads(data[i + 1])] for i in range(0, len(data), 3)]
    return sum(idx + 1 for idx, (a, b) in enumerate(data) if compare(a, b) < 0)

def part2(data):
    data = [json.loads(i) for i in data if i] + [[[2]], [[6]]]
    data.sort(key=cmp_to_key(compare))
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a > b) - (a < b)
    if isinstance(a, list) and isinstance(b, list):
        min_len = min(len(a), len(b))
        for idx in range(min_len):
            cmp_result = compare(a[idx], b[idx])
            if cmp_result != 0:
                return cmp_result
        return (len(a) > len(b)) - (len(a) < len(b))
    if isinstance(a, int):
        return compare([a], b)
    return compare(a, [b])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")