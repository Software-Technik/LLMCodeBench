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

def fold(coords, axis, v):
    if axis == "x":
        return {(x if x < v else 2*v - x, y) for x, y in coords}
    return {(x, y if y < v else 2*v - y) for x, y in coords}

def part1(coords, folds):
    return len(fold(coords, folds[0][0], folds[0][1]))

def part2(coords, folds):
    c = coords
    for axis, v in folds:
        c = fold(c, axis, v)
    maxx = max(x for x, y in c)
    maxy = max(y for x, y in c)
    grid = [['0']*(maxx+1) for _ in range(maxy+1)]
    for x, y in c:
        grid[y][x] = '1'
    res = ""
    for x in range(0, maxx+1, 5):
        letter = ["".join(grid[y][x+dx] if x+dx <= maxx else '0' for dx in range(4)) for y in range(6)]
        res += PATTERNS.get(tuple(letter), "?")
    return res

with open(sys.argv[1]) as f:
    coords_s, folds_s = f.read().split("\n\n", 1)
coords = {tuple(map(int, l.split(','))) for l in coords_s.splitlines()}
folds = []
for l in folds_s.splitlines():
    a, v = l.split()[-1].split("=")
    folds.append((a, int(v)))
p1 = part1(coords, folds)
p2 = part2(coords, folds)
sys.stdout.write(f"{p1} {p2}")