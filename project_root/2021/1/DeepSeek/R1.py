import sys

def part1(depths):
    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            count += 1
    return count

def part2(depths):
    count = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i-3]:
            count += 1
    return count

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [int(line.strip()) for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")