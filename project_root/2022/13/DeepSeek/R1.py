import sys
import json
from functools import cmp_to_key

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else (1 if a > b else 0)
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            c = compare(a[i], b[i])
            if c != 0:
                return c
        return -1 if len(a) < len(b) else (1 if len(a) > len(b) else 0)
    else:
        if isinstance(a, int):
            a = [a]
        else:
            b = [b]
        return compare(a, b)

def part1(data):
    total = 0
    for idx in range(0, len(data), 3):
        a = json.loads(data[idx])
        b = json.loads(data[idx+1])
        if compare(a, b) < 0:
            total += (idx//3) + 1
    return total

def part2(data):
    packets = []
    for line in data:
        if line:
            packets.append(json.loads(line))
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare))
    idx1 = packets.index([[2]]) + 1
    idx2 = packets.index([[6]]) + 1
    return idx1 * idx2

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")