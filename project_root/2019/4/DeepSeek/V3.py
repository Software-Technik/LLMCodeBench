import sys
from collections import Counter

def part1(data):
    lower, upper = map(int, data[0].split("-"))
    n = 0

    for x in range(lower, upper):
        s = str(x)
        if any(a == b for a, b in zip(s, s[1:])):
            if all(a <= b for a, b in zip(s, s[1:])):
                n += 1
    return n 

def part2(data):
    lower, upper = map(int, data[0].split("-"))
    n = 0

    for x in range(lower, upper):
        s = str(x)
        if any(s.count(c) == 2 for c in set(s)):
            if all(a <= b for a, b in zip(s, s[1:])):
                n += 1
    return n

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")