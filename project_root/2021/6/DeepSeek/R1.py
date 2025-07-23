import sys

def part1(data):
    counts = [0] * 9
    for x in data.split(','):
        counts[int(x)] += 1
    for _ in range(80):
        temp = counts[0]
        counts = counts[1:] + [temp]
        counts[6] += temp
    return sum(counts)

def part2(data):
    counts = [0] * 9
    for x in data.split(','):
        counts[int(x)] += 1
    for _ in range(256):
        temp = counts[0]
        counts = counts[1:] + [temp]
        counts[6] += temp
    return sum(counts)

infile = sys.argv[1]
with open(infile) as f:
    data = next(f).strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")