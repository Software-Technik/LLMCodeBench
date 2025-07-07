import sys
import re
import numpy as np
from PIL import Image

LETTER_BITMAPS = {
    "A": ["0110", "1001", "1001", "1111", "1001", "1001"],
    "B": ["1110", "1001", "1110", "1001", "1001", "1110"],
    "C": ["0110", "1001", "1000", "1000", "1001", "0110"],
    "D": ["1110", "1001", "1001", "1001", "1001", "1110"],
    "E": ["1111", "1000", "1110", "1000", "1000", "1111"],
    "F": ["1111", "1000", "1110", "1000", "1000", "1000"],
    "G": ["0111", "1000", "1000", "1011", "1001", "0111"],
    "H": ["1001", "1001", "1111", "1001", "1001", "1001"],
    "I": ["111",  "010",  "010",  "010",  "010",  "111"],
    "J": ["0011", "0001", "0001", "0001", "1001", "0110"],
    "K": ["1001", "1010", "1100", "1100", "1010", "1001"],
    "L": ["1000", "1000", "1000", "1000", "1000", "1111"],
    "M": ["1001", "1111", "1111", "1001", "1001", "1001"],
    "N": ["1001", "1101", "1101", "1011", "1011", "1001"],
    "O": ["0110", "1001", "1001", "1001", "1001", "0110"],
    "P": ["1110", "1001", "1001", "1110", "1000", "1000"],
    "Q": ["0110", "1001", "1001", "1001", "1010", "0101"],
    "R": ["1110", "1001", "1001", "1110", "1010", "1001"],
    "S": ["0111", "1000", "0110", "0001", "0001", "1110"],
    "T": ["1111", "0100", "0100", "0100", "0100", "0100"],
    "U": ["1001", "1001", "1001", "1001", "1001", "0110"],
    "V": ["1001", "1001", "1001", "1001", "0110", "0100"],
    "W": ["1001", "1001", "1001", "1111", "1111", "1001"],
    "X": ["1001", "1001", "0110", "0110", "1001", "1001"],
    "Y": ["1001", "1001", "0110", "0100", "0100", "0100"],
    "Z": ["1111", "0001", "0010", "0100", "1000", "1111"]
}

def load_image(path):
    img = Image.open(path).convert("1")
    return img.load(), img.size[0], img.size[1]

def extract_letter(pixels, x_offset):
    return ["".join("1" if pixels[x_offset + x, y] == 255 else "0" for x in range(4)) for y in range(6)]

def match_letter(bitmap):
    return next((letter for letter, pattern in LETTER_BITMAPS.items() if bitmap == pattern), "?")

def recognize_text(image_path):
    pixels, width, height = load_image(image_path)
    return "".join(match_letter(extract_letter(pixels, x)) for x in range(0, width, 5))

def part1(data):
    coords_section, folds_section = data.split("\n\n")
    coords = {tuple(map(int, c.split(","))) for c in coords_section.splitlines()}
    axis, v = re.match(r"fold along (x|y)=(\d+)", folds_section.splitlines()[0]).groups()
    v = int(v)
    if axis == 'y':
        coords = {(x, y) if y < v else (x, v - (y - v)) for x, y in coords}
    if axis == 'x':
        coords = {(x, y) if x < v else (v - (x - v), y) for x, y in coords}
    return len(coords)

def part2(data):
    coords_section, folds_section = data.split("\n\n")
    coords = {tuple(map(int, c.split(","))) for c in coords_section.splitlines()}
    folds = [(a, int(v)) for a, v in (re.match(r"fold along (x|y)=(\d+)", f).groups() for f in folds_section.splitlines())]

    for axis, v in folds:
        if axis == 'y':
            coords = {(x, y) if y < v else (x, v - (y - v)) for x, y in coords}
        if axis == 'x':
            coords = {(x, y) if x < v else (v - (x - v), y) for x, y in coords}

    X, Y = max(c[0] for c in coords), max(c[1] for c in coords)
    grid = np.zeros((X + 1, Y + 1), dtype=np.uint8)
    for x, y in coords:
        grid[x, y] = 255

    img = Image.fromarray(grid.T)
    img = img.convert('1')  # Convert to 1-bit pixels, black and white
    img.save("grid.png")
    return recognize_text("grid.png")

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")