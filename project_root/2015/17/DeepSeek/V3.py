import sys
from itertools import combinations

def part1(data):
    eggnog = 25 if len(data) == 5 else 150
    containers = list(map(int, data))
    count = 0
    for i in range(1, len(containers) + 1):
        for c in combinations(containers, i):
            if sum(c) == eggnog:
                count += 1
    return count

def part2(data):
    eggnog = 25 if len(data) == 5 else 150
    containers = list(map(int, data))
    min_len = None
    count = 0
    for i in range(1, len(containers) + 1):
        found = False
        current_count = 0
        for c in combinations(containers, i):
            if sum(c) == eggnog:
                current_count += 1
                found = True
        if found:
            if min_len is None:
                min_len = i
                count = current_count
            elif i == min_len:
                count += current_count
            elif i < min_len:
                min_len = i
                count = current_count
    return count

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")