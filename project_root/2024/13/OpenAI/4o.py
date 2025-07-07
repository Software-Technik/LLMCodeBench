import sys
import re

def part1(lines):

    def parse(x):
        lines = x.split("\n")
        a = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])[0]))
        b = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])[0]))
        p = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", lines[2])[0]))
        return a, b, p

    prices = []
    for a, b, p in map(parse, lines):
        va = float('inf')
        for i in range(100):
            for j in range(100):
                if a[0] * i + b[0] * j == p[0] and a[1] * i + b[1] * j == p[1]:
                    va = min(va, 3 * i + j)

        if va < float('inf'):
            prices.append(va)

    return sum(prices)

def part2(lines):

    def parse(x):
        lines = x.split("\n")
        a = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])[0]))
        b = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])[0]))
        p = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", lines[2])[0]))
        return a, b, p

    prices = []
    
    for a, b, p in map(parse, lines):
        p = (p[0] + 10000000000000, p[1] + 10000000000000)
        
        denominator = b[1] * a[0] - b[0] * a[1]
        if denominator != 0:
            i = (p[0] * b[1] - b[0] * p[1]) // denominator
            j = (p[1] - a[1] * i) // b[1]

            if i >= 0 and j >= 0 and a[0] * i + b[0] * j == p[0] and a[1] * i + b[1] * j == p[1]:
                prices.append(3 * i + j)

    return sum(prices)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n\n")
    print(part1(lines), part2(lines))