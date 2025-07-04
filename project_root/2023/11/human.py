import sys
import numpy as np


def parse_input(text):
    lines = text.strip().splitlines()
    data = np.array([list(line) for line in lines])
    return data

def compute(data, expansion_factor):
    y, x = np.where(data == "#")

    empty_r = [i for i in range(data.shape[0]) if all(data[i] == ".")]
    empty_c = [i for i in range(data.shape[1]) if all(data[:, i] == ".")]

    new_y = y + expansion_factor * np.array([y > r for r in empty_r]).sum(axis=0)
    new_x = x + expansion_factor * np.array([x > c for c in empty_c]).sum(axis=0)

    total_distance = (
        abs(new_y - new_y[:, None]) + abs(new_x - new_x[:, None])
    ).sum() // 2

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