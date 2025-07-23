import sys

def part1(data):
    items = parse_items(data)
    return max(items)

def part2(data):
    items = parse_items(data)
    items.sort()
    return sum(items[-3:])

def parse_items(data):
    sums = []
    current = 0
    for line in data:
        if line == "":
            if current != 0:
                sums.append(current)
                current = 0
        else:
            current += int(line)
    if current != 0:
        sums.append(current)
    return sums

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")