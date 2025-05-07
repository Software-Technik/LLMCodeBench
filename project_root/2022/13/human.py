import sys
from functools import cmp_to_key
import json


def part1(data):
    data = [[*map(json.loads, data[i : i + 2])] for i in range(0, len(data), 3)]
    return sum(idx + 1 for idx, [a, b] in enumerate(data) if compare(a, b) < 0)

def part2(data):
    data = [*map(json.loads, [i for i in data if i != ""])] + [[[2]], [[6]]]
    data.sort(key=cmp_to_key(compare))
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)

def compare(ax, bx):
    a = ax if type(ax) == int else [x for x in ax]
    b = bx if type(bx) == int else [x for x in bx]
    idx = 0

    res = {"right": -1, "wrong": 1}

    while 1:
        if idx == len(a):
            break

        if idx >= len(b):
            return res["wrong"]
        else:
            type_a = type(a[idx])
            type_b = type(b[idx])

            if type_a != type_b:
                if type_a == int:
                    a[idx] = [a[idx]]
                    type_a = type(a[idx])
                else:
                    b[idx] = [b[idx]]
                    type_b = type(b[idx])

            if type_a == int:
                if a[idx] == b[idx]:
                    idx += 1
                    continue
                else:
                    return res["right" if a[idx] < b[idx] else "wrong"]
            else:
                x = compare(a[idx], b[idx])
                if x in res.values():
                    return x
                else:
                    idx += 1
                    continue

    return res["right"] if idx < len(b) else None

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")