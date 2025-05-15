import sys

def part1(data):
    depths = [int(x) for x in data]
    return sum(x < y for x, y in zip(depths, depths[1:]))

def part2(data):
    depths = [int(x) for x in data]
    return sum(x < y for x, y in zip(depths, depths[3:]))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")