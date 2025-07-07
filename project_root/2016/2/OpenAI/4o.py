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

def solve(data, keypad, offset, is_inside):
    pos = 0+0j
    key_positions = []
    for line in data:
        for direction in line.strip():
            new = pos + DIRECTIONS[direction]
            pos = new if is_inside(new) else pos
        key_positions.append(pos)
    return ''.join(str(keypad[int(pos.imag) + int(offset.imag)][int(pos.real) + int(offset.real)]) for pos in key_positions)

inout_strings = sys.argv[1]

with open(inout_strings) as f:
    data = f.readlines()

part1_result = solve(data, KEYPAD_1, 1+1j, lambda pos: all(abs(coord) <= 1 for coord in {pos.real, pos.imag}))
part2_result = solve(data, KEYPAD_2, 2+2j, lambda pos: abs(pos.real) + abs(pos.imag) <= 2)

sys.stdout.write(f"{part1_result} {part2_result}")