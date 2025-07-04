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
    def is_inside(pos):
        return all(abs(coord) <= 1 for coord in {pos.real, pos.imag})

    def get_key(pos):
        return str(keypad[int(pos.imag)][int(pos.real)])


    keypad = KEYPAD_1
    offset = 1+1j   # the center of the keypad
    pos = 0+0j      # start from the 5, in the center
    # start from the 5, two left from the center

    key_positions = []
    for line in data:
        for direction in line.strip():
            new = pos + DIRECTIONS[direction]
            pos = new if is_inside(new) else pos
        key_positions.append(pos)

    return ''.join(get_key(pos+offset) for pos in key_positions)


def part2(data):
    def is_inside(pos):
        return abs(pos.real) + abs(pos.imag) <= 2

    def get_key(pos):
        return str(keypad[int(pos.imag)][int(pos.real)])


    keypad = KEYPAD_2
    offset = 2+2j   # the center of the keypad
    pos = -2+0j     # start from the 5, two left from the center

    key_positions = []
    for line in data:
        for direction in line.strip():
            new = pos + DIRECTIONS[direction]
            pos = new if is_inside(new) else pos
        key_positions.append(pos)

    return ''.join(get_key(pos+offset) for pos in key_positions)


inout_strings = sys.argv[1]

with open(inout_strings) as f:
    data = f.readlines()

sys.stdout.write(f"{part1(data)} {part2(data)}") 
