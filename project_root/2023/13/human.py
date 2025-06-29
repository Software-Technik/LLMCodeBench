import sys
import numpy as np

def find_reflection(array, part=1):
    if part == 1:
        test = lambda a, b: (a == b[::-1]).all()
    else:
        test = lambda a, b: (a != b[::-1]).sum() == 1
    for i in range(1, len(array)):
        l = min(len(array) - i, i)
        if test(array[i - l : i], array[i : i + l]):
            return i
    return None

def parse_input(text):
    return [
        np.array([[char for char in line.strip()] for line in block.strip().split("\n")])
        for block in text.strip().split("\n\n")
    ]

def part1(text):
    arrays = parse_input(text)
    return sum(
        100 * y if (y := find_reflection(array)) is not None
        else find_reflection(np.rot90(array, -1))
        for array in arrays
    )

def part2(text):
    arrays = parse_input(text)
    return sum(
        100 * y if (y := find_reflection(array, part=2)) is not None
        else find_reflection(np.rot90(array, -1), part=2)
        for array in arrays
    )

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")