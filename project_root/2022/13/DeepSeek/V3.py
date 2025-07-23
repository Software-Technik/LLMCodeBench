import sys
from functools import cmp_to_key
import json


def part1(data):
    data = [[json.loads(line) for line in data[i:i+2]] for i in range(0, len(data), 3)]
    return sum(i + 1 for i, (a, b) in enumerate(data) if compare(a, b) < 0)

def part2(data):
    packets = [json.loads(line) for line in data if line.strip() != ""]
    packets.extend([[[2]], [[6]]])
    packets.sort(key=cmp_to_key(compare))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else 1 if a > b else 0
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for x, y in zip(a, b):
        res = compare(x, y)
        if res != 0:
            return res
    return -1 if len(a) < len(b) else 1 if len(a) > len(b) else 0

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")