import sys
import numpy as np

def parse_input(text):
    lines = text.strip().splitlines()
    data = np.array([list(line) for line in lines])
    return data

def sum_abs(arr):
    arr_sorted = sorted(arr)
    total = 0
    prefix = 0
    for i, val in enumerate(arr_sorted):
        total += i * val - prefix
        prefix += val
    return total

def compute(data, expansion_factor):
    y, x = np.where(data == "#")
    
    empty_r = [i for i in range(data.shape[0]) if all(data[i] == '.')]
    empty_c = [i for i in range(data.shape[1]) if all(data[:, i] == '.')]
    
    row_mask = np.zeros(data.shape[0], dtype=bool)
    row_mask[empty_r] = True
    row_add = (np.cumsum(row_mask) - row_mask) * expansion_factor
    new_y = y + row_add[y]
    
    col_mask = np.zeros(data.shape[1], dtype=bool)
    col_mask[empty_c] = True
    col_add = (np.cumsum(col_mask) - col_mask) * expansion_factor
    new_x = x + col_add[x]
    
    return sum_abs(new_y) + sum_abs(new_x)

def part1(text):
    data = parse_input(text)
    return compute(data, expansion_factor=1)

def part2(text):
    data = parse_input(text)
    return compute(data, expansion_factor=999_999)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")