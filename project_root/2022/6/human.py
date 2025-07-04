import sys

def part1(data):
    return find_marker(data, 4)

def part2(data):
    return find_marker(data, 14)

def find_marker(data, size):
    buffer = data[0]
    for i in range(size, len(buffer)):
        if len(set(buffer[:i][-size:])) == size:
            return i
        

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")