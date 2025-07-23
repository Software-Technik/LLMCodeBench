import sys
import re

def part1(data):
    return sum(map(int, re.findall(r"-?\d+", data[0])))

def part2(data):
    doc = data[0]
    while ':"red"' in doc:
        idx = doc.index(':"red"')
        bracket_start = 0
        for i in range(idx, -1, -1):
            if doc[i] == '{': bracket_start = i + 1; break
            elif doc[i] == '}': bracket_start += 1

        num_closing_brackets_needed = 1
        idx_to_remove_end = idx + 5
        closing_bracket_match_count = 0
        for i in range(idx_to_remove_end, len(doc)):
            if doc[i] == '"' and (i > idx_to_remove_end or doc[-(idx_to_remove_end - i):].count('"') < closing_bracket_match_count):
                break
            elif doc[i] == '}':
                num_closing_brackets_needed -= 1
                if num_closing_brackets_needed <= 0:
                    idx_to_remove_end = i + 1;break
            elif doc[i] == '{':num_closing_brackets_needed += 1
        doc = doc[:bracket_start - 2] + doc[idx_to_remove_end:]

    return part1([doc])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")