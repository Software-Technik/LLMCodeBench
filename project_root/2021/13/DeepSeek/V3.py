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
    pixels = img.load()
    width, height = img.size
    return pixels, width, height

def extract_letter(pixels, x_offset):
    letter = []
    for y in range(6):
        row = []
        for x in range(4):
            pixel = pixels[x_offset + x, y]
            row.append('1' if pixel == 255 else '0')
        letter.append(''.join(row))
    return letter
    
def match_letter(bitmap):
    for letter, pattern in LETTER_BITMAPS.items():
        if bitmap == pattern:
            return letter
    return "?"

def recognize_text(image_path):
    pixels, width, height = load_image(image_path)
    recognized = []
    for x in range(0, width, 5):
        letter_bitmap = extract_letter(pixels, x)
        recognized.append(match_letter(letter_bitmap))
    return ''.join(recognized)

def part1(data):
    coords_section, folds_section = data.split("\n\n")
    coords = {tuple(map(int, c.split(","))) for c in coords_section.splitlines()}
    folds = [re.match(r"fold along (x|y)=(\d+)", f).groups() for f in folds_section.splitlines()]
    folds = [(a, int(v)) for a, v in folds]

    axis, v = folds[0]
    if axis == 'y':
        coords = {(x, y) for x, y in coords if y < v} | {(x, 2*v - y) for x, y in coords if y >= v}
    else:
        coords = {(x, y) for x, y in coords if x < v} | {(2*v - x, y) for x, y in coords if x >= v}

    return len(coords)

def part2(data):
    coords_section, folds_section = data.split("\n\n")
    coords = {tuple(map(int, c.split(","))) for c in coords_section.splitlines()}
    folds = [re.match(r"fold along (x|y)=(\d+)", f).groups() for f in folds_section.splitlines()]
    folds = [(a, int(v)) for a, v in folds]

    for axis, v in folds:
        if axis == 'y':
            coords = {(x, y) for x, y in coords if y < v} | {(x, 2*v - y) for x, y in coords if y >= v}
        else:
            coords = {(x, y) for x, y in coords if x < v} | {(2*v - x, y) for x, y in coords if x >= v}

    max_x, max_y = max(c[0] for c in coords), max(c[1] for c in coords)
    grid = np.zeros((max_x + 1, max_y + 1), dtype=np.uint8)

    for x, y in coords:
        grid[x, y] = 255

    img = Image.fromarray(grid.T, 'L')
    img.save("grid.png")
    return recognize_text("grid.png")

with open(sys.argv[1]) as f:
    data = f.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")