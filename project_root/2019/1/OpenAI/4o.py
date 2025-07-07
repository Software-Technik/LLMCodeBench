import sys

def part1(data):
    return sum(int(line) // 3 - 2 for line in data)

def fuelFor(input):
    total_fuel = 0
    while input > 0:
        input = input // 3 - 2
        if input > 0:
            total_fuel += input
    return total_fuel

def part2(data):
    return sum(fuelFor(int(line)) for line in data)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")