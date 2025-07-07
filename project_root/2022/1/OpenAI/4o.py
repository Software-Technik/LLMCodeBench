import sys

def part1(data):
    items = parse_items(data)
    return max(items)

def part2(data):
    items = parse_items(data)
    return sum(sorted(items)[-3:])

def parse_items(data):
    return [sum(map(int, elf.split())) for elf in data.split("\n\n")]

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = f.read().strip()

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")