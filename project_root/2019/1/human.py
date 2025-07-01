import sys

def part1(data):
    sum = 0

    for line in data: 
        sum += int(line) // 3 - 2

    return sum

def fuelFor(input):
  output = input // 3 - 2
  return 0 if output <= 0 else output + fuelFor(output)

def part2(data):
    sum = 0

    for line in data: 
        sum += fuelFor(int(line))

    return sum

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")   