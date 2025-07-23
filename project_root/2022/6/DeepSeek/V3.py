import sys

def part1(data):
    return find_marker(data[0], 4)

def part2(data):
    return find_marker(data[0], 14)

def find_marker(buffer, size):
    for i in range(size, len(buffer)):
        if len(set(buffer[i-size:i])) == size:
            return i

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")