import sys
from itertools import groupby

def part1(data):
    seq = data[0]
    for _ in range(40):
        seq = ''.join(f"{len(list(g))}{k}" for k, g in groupby(seq))
    return len(seq)

def part2(data):
    seq = data[0]
    for _ in range(50):
        seq = ''.join(f"{len(list(g))}{k}" for k, g in groupby(seq))
    return len(seq)

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")