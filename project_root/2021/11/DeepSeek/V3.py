import sys
import numpy as np
from scipy import signal

def part1(data):
    df = np.array([[int(x) for x in line] for line in data], dtype=np.int8)
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.int8)
    total = 0
    for _ in range(100):
        flashed = np.zeros_like(df, dtype=bool)
        while True:
            df += 1
            flashing = (df > 9) & ~flashed
            if not np.any(flashing):
                break
            flashed |= flashing
            df += signal.convolve(flashing.astype(np.int8), kernel, mode='same')
        df[flashed] = 0
        total += np.sum(flashed)
    return total

def part2(data):
    df = np.array([[int(x) for x in line] for line in data], dtype=np.int8)
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.int8)
    step = 0
    while True:
        step += 1
        flashed = np.zeros_like(df, dtype=bool)
        while True:
            df += 1
            flashing = (df > 9) & ~flashed
            if not np.any(flashing):
                break
            flashed |= flashing
            df += signal.convolve(flashing.astype(np.int8), kernel, mode='same')
        df[flashed] = 0
        if np.all(flashed):
            return step

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")