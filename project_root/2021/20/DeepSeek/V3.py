import sys
import numpy as np
from scipy.signal import convolve2d

def enhance(times, data):
    algo = np.array([int(x == "#") for x in data[0]])
    img = np.array([[int(x == "#") for x in y] for y in data[2:]], dtype=np.uint8)
    
    matrix = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]], dtype=np.uint16)
    fillvalue = 0
    for _ in range(times):
        idx = convolve2d(img, matrix, fillvalue=fillvalue, mode='same', boundary='fill')
        img = algo[idx]
        fillvalue = algo[0] if fillvalue == 0 else algo[-1]
    return np.sum(img)

def part1(data):
    return enhance(2, data)

def part2(data):
    return enhance(50, data)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")