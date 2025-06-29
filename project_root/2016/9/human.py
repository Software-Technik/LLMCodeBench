import sys
import re


pattern = re.compile(r'\((\d+)x(\d+)\)')


def part1(data):
    parens = pattern.search(data)
    if not parens:
        return len(data)
    length = int(parens.group(1))
    times = int(parens.group(2))
    start = parens.start() + len(parens.group())
    count = length

    return (len(data[:parens.start()])
            + times * count
            + part1(data[start+length:]))


def part2(data):
    parens = pattern.search(data)
    if not parens:
        return len(data)
    length = int(parens.group(1))
    times = int(parens.group(2))
    start = parens.start() + len(parens.group())
    count = part2(data[start:start+length])

    return (len(data[:parens.start()])
            + times * count
            + part2(data[start+length:]))


inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")     