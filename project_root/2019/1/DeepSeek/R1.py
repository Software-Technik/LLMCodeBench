import sys

def part1(masses):
    return sum(mass // 3 - 2 for mass in masses)

def fuelFor(mass):
    total = 0
    f = mass // 3 - 2
    while f > 0:
        total += f
        f = f // 3 - 2
    return total

def part2(masses):
    return sum(fuelFor(mass) for mass in masses)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [int(line.strip()) for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")