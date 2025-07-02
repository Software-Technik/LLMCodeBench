import sys
from itertools import combinations

def part1(data):
    eggnog = 25 if len(data) == 5 else 150
    containers = [*map(int, data)]
    return len(find_combinations(containers, eggnog))

def part2(data):
    eggnog = 25 if len(data) == 5 else 150
    containers = [*map(int, data)]
    combs = find_combinations(containers, eggnog)
    min_combs = min(len(i) for i in combs)
    combs = [i for i in combs if len(i) == min_combs]
    return len(combs)

def find_combinations(containers, eggnog):
    combs = []
    for i in range(2, len(containers) + 1):
        combs += list(combinations(containers, i))
    combs = [i for i in combs if sum(i) == eggnog]
    return combs

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")