import sys

def part1(depths):
    return sum(x < y for x, y in zip(depths, depths[1:]))

def part2(depths):
    return sum(x < y for x, y in zip(depths, depths[3:]))

with open(sys.argv[1]) as f:
    depths = [int(line.strip()) for line in f if line.strip()]

sys.stdout.write(f"{part1(depths)} {part2(depths)}")