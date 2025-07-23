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
    for a, b, p in [parse(line) for line in lines]:
        min_cost = float('inf')
        for i in range(min(100, (p[0] // a[0]) + 2 if a[0] != 0 else 100)):
            for j in range(min(100, (p[1] // b[1]) + 2 if b[1] != 0 else 100)):
                if (a[0] * i + b[0] * j == p[0]) and (a[1] * i + b[1] * j == p[1]):
                    cost = 3 * i + j
                    if cost < min_cost:
                        min_cost = cost
        if min_cost != float('inf'):
            prices.append(min_cost)
    return sum(prices)


def part2(lines):
    def parse(x):
        lines = x.split("\n")
        a = list(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])[0]))
        b = list(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])[0]))
        p = list(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", lines[2])[0]))
        return a, b, p

    prices = []
    for a, b, p in [parse(line) for line in lines]:
        p_x, p_y = p[0] + 10000000000000, p[1] + 10000000000000
        denominator = a[0] * b[1] - a[1] * b[0]
        if denominator == 0:
            continue
        i_numerator = p_x * b[1] - b[0] * p_y
        j_numerator = p_y * a[0] - p_x * a[1]
        if i_numerator % denominator != 0 or j_numerator % denominator != 0:
            continue
        i = i_numerator // denominator
        j = j_numerator // denominator
        if i >= 0 and j >= 0 and (a[0] * i + b[0] * j == p_x) and (a[1] * i + b[1] * j == p_y):
            prices.append(3 * i + j)
    return sum(prices)


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n\n")
    print(part1(lines), part2(lines))