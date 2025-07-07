import sys
from itertools import combinations

def part1(data):
    eggnog = 25 if len(data) == 5 else 150
    containers = list(map(int, data))
    return sum(1 for comb in find_combinations(containers, eggnog))

def part2(data):
    eggnog = 25 if len(data) == 5 else 150
    containers = list(map(int, data))
    min_combs = float('inf')
    count = 0
    for comb in find_combinations(containers, eggnog):
        comb_len = len(comb)
        if comb_len < min_combs:
            min_combs = comb_len
            count = 1
        elif comb_len == min_combs:
            count += 1
    return count

def find_combinations(containers, eggnog):
    for i in range(1, len(containers) + 1):
        for comb in combinations(containers, i):
            if sum(comb) == eggnog:
                yield comb

if __name__ == "__main__":
    input_strings = sys.argv[1]
    with open(input_strings) as f:
        data = [line.strip() for line in f]
    sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")