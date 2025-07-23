import sys
import numpy as np
from scipy.signal import convolve2d

def enhance(times, data):
    algo_arr = np.array([1 if x == '#' else 0 for x in data[0]], dtype=int)
    img = np.array([[1 if x == '#' else 0 for x in y] for y in data[2:]], dtype=int)
    kernel = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]], dtype=int)
    fillvalue = 0
    for _ in range(times):
        idx = convolve2d(img, kernel, fillvalue=fillvalue).astype(int)
        img = algo_arr[idx]
        fillvalue = algo_arr[0] if fillvalue == 0 else algo_arr[511]
    return img.sum()

def part1(data):
    return enhance(2, data)

def part2(data):
    return enhance(50, data)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")