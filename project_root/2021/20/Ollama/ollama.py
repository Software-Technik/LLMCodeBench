import sys
from scipy.signal import convolve2d

def enhance(times, data):
    algo = [int(x == "#") for x in data[0]]
    img = [[0] * (len(data) - 1)] * 1 + [[int(x == "#") for x in y] for y in data[2:]] + [[0] * (len(data) - 1)]
    img = [[0] * len(img[0])] + img + [[0] * len(img[0])]
    matrix = [1, 2, 4, 8, 16, 32, 64, 128, 256]

    for _ in range(times):
        new_img = []
        for y in range(1, len(img) - 1):
            row = []
            for x in range(1, len(img[0]) - 1):
                idx = int(''.join(str(p) for p in (img[y-1][x-1:x+2] + img[y][x-1:x+2] + img[y+1][x-1:x+2])), base=2)
                row.append(algo[idx])
            new_img.append(row)
        img = new_img
    return sum(sum(row) for row in img)

def part1(data):
    return enhance(2, data)

def part2(data):
    return enhance(50, data)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")