import sys

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
PATTERNS = {tuple(v): k for k, v in LETTER_BITMAPS.items()}

def part1(data):
    coords_s, folds_s = data.split("\n\n")
    coords = set()
    for line in coords_s.splitlines():
        x, y = line.split(",")
        coords.add((int(x), int(y)))
    folds = []
    for line in folds_s.splitlines():
        a, v = line.rsplit("=", 1)
        folds.append((a[-1], int(v)))
    axis, v = folds[0]
    if axis == "y":
        coords = {(x, y) for x, y in coords if y < v} | {(x, 2*v - y) for x, y in coords if y >= v}
    else:
        coords = {(x, y) for x, y in coords if x < v} | {(2*v - x, y) for x, y in coords if x >= v}
    return len(coords)

def part2(data):
    coords_s, folds_s = data.split("\n\n")
    coords = set()
    for line in coords_s.splitlines():
        x, y = line.split(",")
        coords.add((int(x), int(y)))
    folds = []
    for line in folds_s.splitlines():
        a, v = line.rsplit("=", 1)
        folds.append((a[-1], int(v)))
    for axis, v in folds:
        if axis == "y":
            coords = {(x, y) for x, y in coords if y < v} | {(x, 2*v - y) for x, y in coords if y >= v}
        else:
            coords = {(x, y) for x, y in coords if x < v} | {(2*v - x, y) for x, y in coords if x >= v}
    max_x = max(x for x, _ in coords)
    max_y = max(y for _, y in coords)
    width, height = max_x + 1, max_y + 1
    grid = [[0]*width for _ in range(height)]
    for x, y in coords:
        grid[y][x] = 1
    result = ""
    for x0 in range(0, width, 5):
        pat = []
        for y in range(height):
            row = "".join("1" if grid[y][x0 + x] else "0" for x in range(4))
            pat.append(row)
        result += PATTERNS.get(tuple(pat), "?")
    return result

if __name__ == "__main__":
    data = open(sys.argv[1]).read()
    sys.stdout.write(f"{part1(data)} {part2(data)}")