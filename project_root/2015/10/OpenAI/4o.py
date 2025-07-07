import sys
from itertools import groupby

def part1(data):
    return transform_sequence(data[0], 40)

def part2(data):
    return transform_sequence(data[0], 50)

def transform_sequence(seq, iterations):
    for _ in range(iterations):
        seq = "".join(f"{sum(1 for _ in g)}{i}" for i, g in groupby(seq))
    return len(seq)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")