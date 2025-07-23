import sys
from itertools import groupby

def part1(data):
    seq = data[0]
    for _ in range(40):
        seq = next_seq(seq)
    return len(seq)

def part2(data):
    seq = data[0]
    for _ in range(50):
        seq = next_seq(seq)
    return len(seq)

def next_seq(seq):
    tokens = []
    for digit, group in groupby(seq):
        count = sum(1 for _ in group)
        tokens.append(str(count))
        tokens.append(digit)
    return ''.join(tokens)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")