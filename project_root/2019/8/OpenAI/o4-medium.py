#!/usr/bin/env python3
import sys

def part1(data):
    width, height = 25, 6
    layer_size = width * height
    best_zero = layer_size + 1
    checksum = 0
    for i in range(0, len(data), layer_size):
        z = o = t = 0
        for v in data[i:i+layer_size]:
            if v == 0:
                z += 1
            elif v == 1:
                o += 1
            elif v == 2:
                t += 1
        if z < best_zero:
            best_zero = z
            checksum = o * t
    return checksum

def part2(data):
    width, height = 25, 6
    layer_size = width * height
    pixels = [2] * layer_size
    for i in range(0, len(data), layer_size):
        layer = data[i:i+layer_size]
        for j, v in enumerate(layer):
            if pixels[j] == 2 and v != 2:
                pixels[j] = v
    ascii_lines = []
    for h in range(height):
        line = []
        row = pixels[h*width:(h+1)*width]
        for val in row:
            if val == 0:
                line.append('░')
            elif val == 1:
                line.append('█')
            else:
                line.append(' ')
        ascii_lines.append(''.join(line))
    LETTER_MAP = {tuple(v): k for k, v in {
        "A": ["0110", "1001", "1111", "1001", "1001", "1001"],
        "B": ["1110", "1001", "1110", "1001", "1001", "1110"],
        "C": ["0110", "1001", "1000", "1000", "1001", "0110"],
        "D": ["1110", "1001", "1001", "1001", "1001", "1110"],
        "E": ["1111", "1000", "1110", "1000", "1000", "1111"],
        "F": ["1111", "1000", "1110", "1000", "1000", "1000"],
        "G": ["0111", "1000", "1000", "1011", "1001", "0111"],
        "H": ["1001", "1001", "1111", "1001", "1001", "1001"],
        "I": ["1110", "0100", "0100", "0100", "0100", "1110"],
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
    }.items()}
    binary_lines = [line.replace('█', '1').replace('░', '0').replace(' ', '0') for line in ascii_lines]
    result = []
    for col in range(0, width, 5):
        block = tuple(line[col:col+4] for line in binary_lines)
        result.append(LETTER_MAP.get(block, '?'))
    return ''.join(result)

if __name__ == '__main__':
    data = list(map(int, open(sys.argv[1]).read().strip()))
    p1 = part1(data)
    p2 = part2(data)
    print(f"{p1} {p2}", end='')