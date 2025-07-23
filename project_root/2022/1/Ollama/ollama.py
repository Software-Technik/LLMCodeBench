import sys

def part1(data):
    items, max_calories = parse_items(data)
    return max_calories

def part2(data):
    items, _ = parse_items(data)
    return sum(sorted(items)[-3:])

def parse_items(data):
    items = []
    max_calories = 0
    current_total = 0
    for line in data:
        if not line:
            items.append(current_total)
            max_calories = max(max_calories, current_total)
            current_total = 0
        else:
            current_total += int(line)
    return (items, max_calories)

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")