import sys

def part1(data):
    return data[0].count('(') - data[0].count(')')

def part2(data):
    floor = 0
    for i, char in enumerate(data[0], 1):
        floor += 1 if char == '(' else -1
        if floor == -1:
            return i

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")