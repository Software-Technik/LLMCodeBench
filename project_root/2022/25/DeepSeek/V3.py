import math
import sys

def part1(data):
    total = 0
    for s in data:
        n = 0
        for c in s:
            n = n * 5 + ("=-012".index(c) - 2)
        total += n
    return d2s(total)

def d2s(d):
    if d == 0:
        return "0"
    digits = []
    while d > 0:
        d, rem = divmod(d, 5)
        digits.append(rem)
    digits.append(0)
    for i in range(len(digits)):
        if digits[i] > 2:
            digits[i] -= 5
            digits[i+1] += 1
    if digits[-1] == 0:
        digits.pop()
    mapping = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    return "".join(mapping[d] for d in reversed(digits))

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n")