import sys
import re

def part1(lines):
    def parse(x):
        lines = x.split("\n")
        a = list(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])[0]))
        b = list(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])[0]))
        p = list(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", lines[2])[0]))
        return a, b, p

    prices = []
    for group in lines:
        a, b, p = parse(group)
        a0, a1 = a
        b0, b1 = b
        p0, p1 = p
        det = a0 * b1 - a1 * b0
        candidate = None
        if det == 0:
            for i in range(100):
                for j in range(100):
                    if a0 * i + b0 * j == p0 and a1 * i + b1 * j == p1:
                        cost = 3 * i + j
                        if candidate is None or cost < candidate:
                            candidate = cost
        else:
            num_i = p0 * b1 - p1 * b0
            num_j = a0 * p1 - a1 * p0
            if num_i % det == 0 and num_j % det == 0:
                i_val = num_i // det
                j_val = num_j // det
                if 0 <= i_val < 100 and 0 <= j_val < 100:
                    candidate = 3 * i_val + j_val
        if candidate is not None:
            prices.append(candidate)
    spent = 0
    return sum(prices)

def part2(lines):
    def parse(x):
        lines = x.split("\n")
        a = list(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])[0]))
        b = list(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])[0]))
        p = list(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", lines[2])[0]))
        return a, b, p

    prices = []
    bad = 0
    for a, b, p in [parse(line) for line in lines]:
        p[0] += 10000000000000
        p[1] += 10000000000000
        a0, a1 = a
        b0, b1 = b
        p0, p1 = p

        def verify(i, j):
            if i < 0 or j < 0:
                return False
            return (a0 * i + b0 * j == p0) and (a1 * i + b1 * j == p1)

        det = b1 * a0 - b0 * a1
        i_val = (p0 * b1 - b0 * p1) // det
        j_val = (p1 - a1 * i_val) // b1
        if verify(i_val, j_val):
            prices.append(3 * i_val + j_val)
    spent = 0
    return sum(prices)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n\n")
    print(part1(lines), part2(lines))