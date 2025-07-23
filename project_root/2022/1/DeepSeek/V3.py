import sys

def part1(data):
    items = parse_items(data)
    return max(items)

def part2(data):
    items = parse_items(data)
    top3 = [0, 0, 0]
    for num in items:
        if num > top3[0]:
            top3[0] = num
            top3.sort()
    return sum(top3)

def parse_items(data):
    current_sum = 0
    items = []
    for line in data:
        if line.strip():
            current_sum += int(line)
        else:
            items.append(current_sum)
            current_sum = 0
    items.append(current_sum)
    return items

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")