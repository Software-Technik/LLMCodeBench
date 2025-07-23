import sys

def part1(data):
    return sum(int(line) // 3 - 2 for line in data)

def fuelFor(input):
    output = input // 3 - 2
    return 0 if output <= 0 else output + fuelFor(output)

def part2(data):
    return sum(fuelFor(int(line)) for line in data)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if (s := line.strip())]

print(*map(part1, [data]), *map(part2, [data]))