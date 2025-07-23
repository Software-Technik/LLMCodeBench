import sys
import functools

def parse(line):
    s, groups = line.strip().split(" ")
    lookup = {"#": 2, "?": 1, ".": 0}
    return tuple(lookup[char] for char in s), tuple(int(g) for g in groups.split(","))

def match_beginning(data, length):
    if len(data) < length:
        return False
    for i in range(length):
        if data[i] == 0:
            return False
    return len(data) == length or data[length] != 2

@functools.cache
def count(data, blocks):
    total = sum(blocks)
    min_required = sum(1 for x in data if x == 2)
    max_possible = sum(1 for x in data if x != 0)
    if min_required > total or max_possible < total:
        return 0
    if not blocks:
        return 0 if 2 in data else 1
    if not data:
        return 0
    
    first_block = blocks[0]
    if data[0] == 0:
        return count(data[1:], blocks)
    if data[0] == 2:
        if match_beginning(data, first_block):
            remaining_data = data[first_block + 1:] if len(data) > first_block else ()
            return count(remaining_data, blocks[1:])
        return 0
    return count(data[1:], blocks) + count((2,) + data[1:], blocks)

def part1(text):
    data = [parse(line) for line in text.strip().splitlines()]
    return sum(count(*line) for line in data)

def part2(text):
    data = [parse(line) for line in text.strip().splitlines()]
    return sum(count(((chars + (1,)) * 5)[:-1], blocks * 5) for chars, blocks in data)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")