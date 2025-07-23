import sys
import re

def part1(data):
    return sum(map(int, re.findall(r"-?\d+", data[0])))

def part2(data):
    doc = data[0]
    red_positions = [m.start() for m in re.finditer(':"red"', doc)]
    stack = []
    to_remove = []
    for i, c in enumerate(doc):
        if c == '{':
            stack.append(i)
        elif c == '}':
            if stack:
                start = stack.pop()
                for pos in red_positions:
                    if start < pos < i:
                        to_remove.append((start, i))
                        break
    to_remove.sort()
    result = []
    last_end = 0
    for start, end in to_remove:
        result.append(doc[last_end:start])
        last_end = end + 1
    result.append(doc[last_end:])
    cleaned_doc = ''.join(result)
    return part1([cleaned_doc])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")