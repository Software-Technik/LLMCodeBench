import sys
import re

pattern = re.compile(r'\((\d+)x(\d+)\)')

def calculate(data, recursive):
    pos, total_length = 0, 0
    while pos < len(data):
        parens = pattern.search(data, pos)
        if not parens:
            total_length += len(data) - pos
            break
        total_length += parens.start() - pos
        length, times = map(int, parens.groups())
        start = parens.end()
        if recursive:
            count = calculate(data[start:start + length], True)
        else:
            count = length
        total_length += times * count
        pos = start + length
    return total_length

def part1(data):
    return calculate(data, False)

def part2(data):
    return calculate(data, True)

with open(sys.argv[1], 'r') as infile:
    data = infile.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")