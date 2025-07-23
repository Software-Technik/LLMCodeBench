import numpy as np

def parse_input(text):
    lines = text.strip().splitlines()
    data = np.array([list(line) for line in lines])
    return data

def compute(data, expansion_factor):
    y, x = np.where(data == "#")

    empty_r = [i for i in range(data.shape[0]) if all(data[i] == ".")]
    total_expansion_rows = sum(expansion_factor + 1 for r in empty_r if any(y > r)) * (expansion_factor)
    expanded_y = y + total_expansion_rows

    empty_c = [i for i in range(data.shape[1]) if all(data[:, i] == ".")]
    total_expansion_cols = sum(expansion_factor + 1 for c in empty_c if any(x > c)) * (expansion_factor)
    expanded_x = x + total_expansion_cols

    total_distance = (
        abs(expanded_y - expanded_y[:, None]) + abs(expanded_x - expanded_x[:, None])
    ).sum() // 2

    return int(total_distance)

def part1(text):
    data = parse_input(text)
    return compute(data, expansion_factor=1)

def part2(text):
    data = parse_input(text)
    return compute(data, expansion_factor=999_999)

import sys
inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")