import sys
import re

LETTER_BITMAPS = {
    "A": ["0110", "1001", "1001", "1111", "1001", "1001"],
    "B": ["1110", "1001", "1110", "1001", "1001", "1110"],
    "C": ["0110", "1001", "1000", "1000", "1001", "0110"],
    "D": ["1110", "1001", "1001", "1001", "1001", "1110"],
    "E": ["1111", "1000", "1110", "1000", "1000", "1111"],
    "F": ["1111", "1000", "1110", "1000", "1000", "1000"],
    "G": ["0111", "1000", "1000", "1011", "1001", "0111"],
    "H": ["1001", "1001", "1111", "1001", "1001", "1001"],
    "I": ["111", "010", "010", "010", "010", "111"],
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

def match_letter(bitmap):
    for letter, pattern in LETTER_BITMAPS.items():
        if bitmap == pattern:
            return letter
    return "?"

def recognize_text_from_coords(coords):
    if not coords:
        return ""
    max_x = max(x for x, y in coords)
    num_letters = (max_x + 1) // 5
    recognized = ""
    for i in range(num_letters):
        letter_bitmap = []
        for j in range(6):
            row_str = ""
            for k in range(4):
                x_coord = i * 5 + k
                if (j, x_coord) in coords:
                    row_str += "1"
                else:
                    row_str += "0"
            letter_bitmap.append(row_str)
        recognized += match_letter(letter_bitmap)
    return recognized

def fold_coords(coords, fold):
    axis, v = fold
    new_coords = set()
    if axis == 'y':
        for (x, y) in coords:
            if y < v:
                new_coords.add((x, y))
            else:
                new_coords.add((x, 2*v - y))
    else:
        for (x, y) in coords:
            if x < v:
                new_coords.add((x, y))
            else:
                new_coords.add((2*v - x, y))
    return new_coords

def part1(data):
    coords_section, folds_section = data.split("\n\n")
    coords = {tuple(map(int, c.split(","))) for c in coords_section.splitlines()}
    folds = [re.match(r"fold along (x|y)=(\d+)", f).groups() for f in folds_section.splitlines()]
    folds = [(a, int(v)) for a, v in folds]
    fold = folds[0]
    coords = fold_coords(coords, fold)
    return len(coords)

def part2(data):
    coords_section, folds_section = data.split("\n\n")
    coords = {tuple(map(int, c.split(","))) for c in coords_section.splitlines()}
    folds = [re.match(r"fold along (x|y)=(\d+)", f).groups() for f in folds_section.splitlines()]
    folds = [(a, int(v)) for a, v in folds]
    for fold in folds:
        coords = fold_coords(coords, fold)
    return recognize_text_from_coords(coords)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")