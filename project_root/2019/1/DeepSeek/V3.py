import sys

def part1(data):
    return sum(int(line) // 3 - 2 for line in data)

def fuelFor(input):
    output = input // 3 - 2
    return output + fuelFor(output) if output > 0 else 0

def part2(data):
    return sum(fuelFor(int(line)) for line in data)

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")