import sys
from collections import defaultdict
import io

def part1(data):
    width, height = 25, 6
    layer_size = width * height
    checksums = {}
    
    for i in range(0, len(data), layer_size):
        layer = data[i:i+layer_size]
        count0 = layer.count(0)
        count1 = layer.count(1)
        count2 = layer.count(2)
        checksums[count0] = count1 * count2
    
    return checksums[min(checksums.keys())]

def part2(data):
    width, height = 25, 6
    layer_size = width * height
    image = [2] * layer_size
    
    for i in range(len(data)):
        pos = i % layer_size
        if image[pos] == 2:
            image[pos] = data[i]
    
    ascii_lines = []
    for h in range(height):
        line = []
        for w in range(width):
            val = image[h * width + w]
            if val == 0:
                line.append('░')
            elif val == 1:
                line.append('█')
            else:
                line.append(' ')
        ascii_lines.append(''.join(line))
    
    LETTER_BITMAPS_4x6 = {
        ("0110", "1001", "1111", "1001", "1001", "1001"): "A",
        ("1110", "1001", "1110", "1001", "1001", "1110"): "B",
        ("0110", "1001", "1000", "1000", "1001", "0110"): "C",
        ("1110", "1001", "1001", "1001", "1001", "1110"): "D",
        ("1111", "1000", "1110", "1000", "1000", "1111"): "E",
        ("1111", "1000", "1110", "1000", "1000", "1000"): "F",
        ("0111", "1000", "1000", "1011", "1001", "0111"): "G",
        ("1001", "1001", "1111", "1001", "1001", "1001"): "H",
        ("1110", "0100", "0100", "0100", "0100", "1110"): "I",
        ("0011", "0001", "0001", "0001", "1001", "0110"): "J",
        ("1001", "1010", "1100", "1100", "1010", "1001"): "K",
        ("1000", "1000", "1000", "1000", "1000", "1111"): "L",
        ("1001", "1111", "1111", "1001", "1001", "1001"): "M",
        ("1001", "1101", "1101", "1011", "1011", "1001"): "N",
        ("0110", "1001", "1001", "1001", "1001", "0110"): "O",
        ("1110", "1001", "1001", "1110", "1000", "1000"): "P",
        ("0110", "1001", "1001", "1001", "1010", "0101"): "Q",
        ("1110", "1001", "1001", "1110", "1010", "1001"): "R",
        ("0111", "1000", "0110", "0001", "0001", "1110"): "S",
        ("1111", "0100", "0100", "0100", "0100", "0100"): "T",
        ("1001", "1001", "1001", "1001", "1001", "0110"): "U",
        ("1001", "1001", "1001", "1001", "0110", "0100"): "V",
        ("1001", "1001", "1001", "1111", "1111", "1001"): "W",
        ("1001", "1001", "0110", "0110", "1001", "1001"): "X",
        ("1001", "1001", "0110", "0100", "0100", "0100"): "Y",
        ("1111", "0001", "0010", "0100", "1000", "1111"): "Z"
    }
    
    def to_binary(line):
        return line.replace('█', '1').replace('░', '0').replace(' ', '0')
    
    binary_lines = [to_binary(line) for line in ascii_lines]
    
    result = []
    for col in range(0, width, 5):
        block = tuple(line[col:col+4] for line in binary_lines)
        result.append(LETTER_BITMAPS_4x6.get(block, '?'))
    
    return ''.join(result)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().strip()))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdout.write(f"{part1(data)} {part2(data)}")