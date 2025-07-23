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
        return -1 <= pos.real <= 1 and -1 <= pos.imag <= 1

    keypad = KEYPAD_1
    offset = 1 + 1j
    pos = 0 + 0j
    result = []
    
    for line in data:
        for direction in line.strip():
            new_pos = pos + DIRECTIONS[direction]
            if is_inside(new_pos):
                pos = new_pos
        x, y = int(pos.real + 1), int(pos.imag + 1)
        result.append(str(keypad[y][x]))
    
    return ''.join(result)

def part2(data):
    def is_inside(pos):
        return abs(pos.real) + abs(pos.imag) <= 2

    keypad = KEYPAD_2
    offset = 2 + 2j
    pos = -2 + 0j
    result = []
    
    for line in data:
        for direction in line.strip():
            new_pos = pos + DIRECTIONS[direction]
            if is_inside(new_pos):
                pos = new_pos
        x, y = int(pos.real + 2), int(pos.imag + 2)
        result.append(str(keypad[y][x]))
    
    return ''.join(result)

with open(sys.argv[1]) as f:
    data = f.readlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")