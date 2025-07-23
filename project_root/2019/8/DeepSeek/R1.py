import sys
import io

def part1(data):
    width, height = 25, 6
    n = width * height
    min_zeros = float('inf')
    result = None
    for start in range(0, len(data), n):
        count0 = count1 = count2 = 0
        for j in range(start, start + n):
            pixel = data[j]
            if pixel == 0:
                count0 += 1
            elif pixel == 1:
                count1 += 1
            elif pixel == 2:
                count2 += 1
        if count0 <= min_zeros:
            min_zeros = count0
            result = count1 * count2
    return result

def part2(data):
    width, height = 25, 6
    n = width * height
    image = [2] * n
    for i, pixel in enumerate(data):
        pos = i % n
        if image[pos] == 2:
            image[pos] = pixel
    rows = []
    for i in range(0, n, width):
        row = image[i:i+width]
        s = ''.join(['░' if p == 0 else '█' if p == 1 else ' ' for p in row])
        rows.append(s)
    ascii_lines = list(reversed(rows))
    
    LETTER_BITMAPS_4x6 = {
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
    }
    LETTER_BITMAPS_4x6 = {tuple(v): k for k, v in LETTER_BITMAPS_4x6.items()}

    def to_binary(line):
        return line.replace('█', '1').replace('░', '0').replace(' ', '0')

    binary_lines = [to_binary(line) for line in ascii_lines]
    result = ""
    line_width = len(ascii_lines[0])
    for col in range(0, line_width, 5):
        block = tuple(line[col:col+4] for line in binary_lines)
        result += LETTER_BITMAPS_4x6.get(block, '?')
    return result

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().splitlines()[0]))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdout.write(f"{part1(data)} {part2(data)}")