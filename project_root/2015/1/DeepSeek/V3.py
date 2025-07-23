import sys

def part1(data):
    return sum(1 if c == '(' else -1 for c in data[0])

def part2(data):
    floor = 0
    for i, c in enumerate(data[0], 1):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")