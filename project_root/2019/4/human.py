import sys
from collections import Counter

def part1(data):
    lower, upper = map(int, data[0].split("-"))
    n = 0

    for x in range(lower, upper):
        candidate = str(x)
        counts = Counter(candidate)
        twosame = max(counts.values()) >= 2
        increases = list(candidate) == sorted(candidate)
        if twosame and increases: n += 1

    return n 

def part2(data):
    lower, upper = map(int, data[0].split("-"))
    n = 0

    for x in range(lower, upper):
        candidate = str(x)
        counts = Counter(candidate)
        twosame = 2 in counts.values()
        increases = list(candidate) == sorted(candidate)
        if twosame and increases: n += 1

    return n

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")