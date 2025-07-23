import sys
import functools

def parse(line):
    s, groups = line.strip().split(" ")
    lookup = {"#": 2, "?": 1, ".": 0}
    return tuple(lookup[char] for char in s), tuple(int(g) for g in groups.split(","))

def match_beginning(data, length):
    return all(x > 0 for x in data[:length]) and (
        (len(data) == length) or data[length] < 2
    )

@functools.cache
def count(data, blocks):
    total = sum(blocks)
    minimum = sum(x == 2 for x in data)
    maximum = sum(x > 0 for x in data)
    if minimum > total or maximum < total:
        return 0
    if total == 0:
        return 1
    if data[0] == 0:
        return count(data[1:], blocks)
    if data[0] == 2:
        l = blocks[0]
        if match_beginning(data, l):
            if l == len(data):
                return 1
            return count(data[l + 1:], blocks[1:])
        return 0
    return count(data[1:], blocks) + count((2,) + data[1:], blocks)

def part1(text):
    data = [parse(line) for line in text.strip().splitlines()]
    return sum(count(*line) for line in data)

def part2(text):
    data = [parse(line) for line in text.strip().splitlines()]
    chars, blocks = zip(*data)
    expanded_chars = (c * 5 + (1,) for c in chars)
    expanded_blocks = blocks * 5
    return sum(count(((chars + (1,)) * 5)[:-1], blocks * 5) for chars, blocks in data)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")