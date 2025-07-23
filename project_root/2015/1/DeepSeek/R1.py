import sys

def part1(data):
    return sum(1 if i == "(" else -1 for i in data[0])

def part2(data):
    current = 0
    for i, c in enumerate(data[0], start=1):
        current += 1 if c == '(' else -1
        if current == -1:
            return i

input_file = sys.argv[1]
with open(input_file) as f:
    first_line = f.readline()
    if first_line == '':
        data = []
    else:
        data = [first_line.strip()]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")