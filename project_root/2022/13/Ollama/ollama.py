import json
from functools import cmp_to_key

def part1(data):
    return sum(idx + 1 for idx, (a, b) in enumerate(zip(data[::3], data[1::3])) if compare(json.loads(a), json.loads(b)) < 0)

def part2(data):
    packages = [json.loads(p) for p in data if p != ''] + [[[2]], [[6]]]
    packages.sort(key=cmp_to_key(compare))
    return (packages.index([[2]]) + 1) * (packages.index([[6]]) + 1)

def compare(a, b, idx=0):
    if isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else 1
    ax = iter([a]) if isinstance(a, int) else iter(a)
    bx = iter([b]) if isinstance(b, int) else iter(b)

    for a_val in ax:
        try:
            b_val = next(bx)
        except StopIteration:
            return -1

        c = compare(a_val, b_val)
        if c != 0:
            return c
    return 1 if next(bx, None) is not None else 0

data = json.loads(f.read().replace('\n', ' ')).split()
print(part1(data))
print(part2(data))