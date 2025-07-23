import sys
from itertools import combinations

def part1(data):
    eggnog = 25 if len(data) == 5 else 150
    containers = map(int, data)
    return sum(1 for i in range(2, len(data) + 1) for c in combinations(containers, i) if sum(c) == eggnog)

def part2(data):
    eggnog = 25 if len(data) == 5 else 150
    containers = map(int, data)
    min_len = float('inf')
    count = 0
    for i in range(2, len(data) + 1):
        for c in combinations(containers, i):
            s = sum(c)
            if s == eggnog:
                if (l := len(c)) < min_len:
                    min_len, count = l, 1
                elif l == min_len:
                    count += 1
    return count

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")