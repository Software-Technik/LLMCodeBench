import sys
import re

def part1(data):
    return sum(map(int, re.findall(r"-?\d+", data[0])))

def part2(data):
    doc = data[0]
    stack = []

    i = 0
    while i < len(doc):
        if doc[i] == '{':
            stack.append(i)
        elif doc[i] == '}':
            start = stack.pop()
            if ':"red"' in doc[start:i + 1]:
                doc = doc[:start] + ' ' * (i + 1 - start) + doc[i + 1:]
                i = start
        i += 1

    return part1([doc])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")