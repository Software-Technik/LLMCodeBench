import sys
import json
from functools import cmp_to_key

def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for x, y in zip(a, b):
        c = cmp(x, y)
        if c:
            return c
    return len(a) - len(b)

def part1(parsed):
    res = 0
    for i in range(0, len(parsed), 3):
        if cmp(parsed[i], parsed[i+1]) < 0:
            res += i//3 + 1
    return res

def part2(parsed):
    packets = [p for p in parsed if p is not None]
    div1 = [[2]]
    div2 = [[6]]
    packets.extend((div1, div2))
    packets.sort(key=cmp_to_key(cmp))
    return (packets.index(div1) + 1) * (packets.index(div2) + 1)

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f]
parsed = [json.loads(line) if line else None for line in lines]

print(part1(parsed))
print(part2(parsed))