import sys

def part1(data):
    return find_marker(data, 4)

def part2(data):
    return find_marker(data, 14)

def find_marker(data, size):
    buffer = data[0]
    last_seen = {}
    start = 0

    for i, char in enumerate(buffer):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = i
        if i - start + 1 == size:
            return i + 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")