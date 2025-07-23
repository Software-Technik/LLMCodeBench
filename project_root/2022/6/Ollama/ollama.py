import sys

def part1(data):
    return find_marker(data, 4)

def part2(data):
    return find_marker(data, 14)

def find_marker(data, size):
    seen = set()
    for i in range(len(data)):
        if data[i] not in seen:
            seen.add(data[i])
            if len(seen) == size:
                return i + 1
        else:
            del seen[data]

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")