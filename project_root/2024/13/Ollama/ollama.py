import sys
import re

def parse(x):
    nums = map(int, re.findall(r"\d+", x))
    a = [next(nums), next(nums)], [next(nums), next(nums)]
    p = [next(nums), next(nums)]
    return a, p

def part1(lines):
    prices = []
    for a, p in [parse(line) for line in lines]:
        va = 1 << 30
        for i in range(100):
            for j in range(100):
                x, y = a[0][0] * i + (a[1][0] if j else 0), a[0][1] * i + (a[1][1] if j else 0)
                if (x, y) == tuple(p):
                    va = min(va, 3 * i + j)
        prices.append(va)

    return sum(prices)

def part2(lines):
    prices = []
    for a, p in [parse(line) for line in lines]:
        det = a[0][1] * a[1][0] - a[0][0] * a[1][1]
        i = (p[0] * a[1][1] - a[0][0] * p[1]) // det
        j = (a[0][0] * p[1] - p[0] * a[0][1]) // det
        prices.append(3 * int(i) + int(j))

    return sum(prices)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n\n")
    print(part1(lines), part2(lines))