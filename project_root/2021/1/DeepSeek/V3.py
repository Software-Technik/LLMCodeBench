import sys

def part1(data):
    depths = list(map(int, data))
    return sum(x < y for x, y in zip(depths, depths[1:]))

def part2(data):
    depths = list(map(int, data))
    return sum(depths[i] < depths[i+3] for i in range(len(depths)-3))

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")