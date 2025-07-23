import sys

DIRECTIONS = {
    'R': 1,
    'L': -1,
    'D': 1j,
    'U': -1j,
}

KEYPAD_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

KEYPAD_2 = [
    [0,  0,  1,  0,  0],
    [0,  2,  3,  4,  0],
    [5,  6,  7,  8,  9],
    [0, 'A','B','C', 0],
    [0,  0, 'D', 0,  0]
]

def part1(data):
    keypad = KEYPAD_1
    offset = 1+1j
    pos = 0+0j
    keys = []
    for line in data:
        for direction in line.strip():
            new = pos + DIRECTIONS[direction]
            if abs(new.real) <= 1 and abs(new.imag) <= 1:
                pos = new
        adjusted = pos + offset
        keys.append(str(keypad[int(adjusted.imag)][int(adjusted.real)]))
    return ''.join(keys)

def part2(data):
    keypad = KEYPAD_2
    offset = 2+2j
    pos = -2+0j
    keys = []
    for line in data:
        for direction in line.strip():
            new = pos + DIRECTIONS[direction]
            if abs(new.real) + abs(new.imag) <= 2:
                pos = new
        adjusted = pos + offset
        keys.append(str(keypad[int(adjusted.imag)][int(adjusted.real)]))
    return ''.join(keys)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.readlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")