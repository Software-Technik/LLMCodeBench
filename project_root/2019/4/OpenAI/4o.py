import sys

def has_adjacent_duplicates(candidate):
    return any(candidate[i] == candidate[i+1] for i in range(5))

def has_exactly_double(candidate):
    groups = [candidate[i] for i in range(6) if i == 0 or candidate[i] != candidate[i-1]] + ['']
    for ch, group in zip(candidate, groups):
        if candidate.count(ch) == 2:
            return True
    return False

def is_non_decreasing(candidate):
    return all(candidate[i] <= candidate[i+1] for i in range(5))

def part1(data):
    lower, upper = map(int, data[0].split("-"))
    n = 0

    for x in range(lower, upper):
        candidate = str(x)
        if has_adjacent_duplicates(candidate) and is_non_decreasing(candidate):
            n += 1

    return n 

def part2(data):
    lower, upper = map(int, data[0].split("-"))
    n = 0

    for x in range(lower, upper):
        candidate = str(x)
        if has_exactly_double(candidate) and is_non_decreasing(candidate):
            n += 1

    return n

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")