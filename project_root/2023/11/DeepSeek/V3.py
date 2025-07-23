import sys
import numpy as np

def parse_input(text):
    lines = text.strip().splitlines()
    data = np.array([list(line) for line in lines])
    return data

def compute(data, expansion_factor):
    y, x = np.where(data == "#")
    
    empty_rows = np.where(np.all(data == '.', axis=1))[0]
    empty_cols = np.where(np.all(data == '.', axis=0))[0]
    
    y_expansion = np.searchsorted(empty_rows, y) * expansion_factor
    x_expansion = np.searchsorted(empty_cols, x) * expansion_factor
    
    new_y = y + y_expansion
    new_x = x + x_expansion
    
    total_distance = (np.abs(new_y[:, None] - new_y) + np.abs(new_x[:, None] - new_x)).sum() // 2
    return total_distance

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