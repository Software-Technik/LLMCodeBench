import sys
import re

pattern = re.compile(r'\((\d+)x(\d+)\)')

def part1(data):
    pos = 0
    total = 0
    while pos < len(data):
        match = pattern.search(data, pos)
        if not match:
            total += len(data) - pos
            break
        total += match.start() - pos
        length = int(match.group(1))
        times = int(match.group(2))
        pos = match.end() + length
        total += length * times
    return total

def part2(data):
    stack = []
    stack.append((0, len(data), 1))
    total = 0
    while stack:
        start, end, multiplier = stack.pop()
        pos = start
        while pos < end:
            match = pattern.search(data, pos, end)
            if not match:
                total += (end - pos) * multiplier
                break
            total += (match.start() - pos) * multiplier
            length = int(match.group(1))
            times = int(match.group(2))
            new_start = match.end()
            new_end = new_start + length
            stack.append((new_start, new_end, times * multiplier))
            pos = new_end
    return total

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")