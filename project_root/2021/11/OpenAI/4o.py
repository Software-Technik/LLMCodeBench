import sys
import numpy as np
from scipy import signal

def part1(data):
    df = np.array([[int(x) for x in line] for line in data])

    total = 0
    for _ in range(100):
        df += 1
        flashed = np.zeros_like(df, dtype=bool)
        while True:
            flashing = (df > 9) & ~flashed
            if not np.any(flashing):
                break
            flashed |= flashing
            df += signal.convolve(flashing, np.ones((3, 3), dtype=int), mode='same')
        df[flashed] = 0
        total += np.sum(flashed)
    return total

def part2(data):
    df = np.array([[int(x) for x in line] for line in data])
    step = 0
    while True:
        df += 1
        flashed = np.zeros_like(df, dtype=bool)
        while True:
            flashing = (df > 9) & ~flashed
            if not np.any(flashing):
                break
            flashed |= flashing
            df += signal.convolve(flashing, np.ones((3, 3), dtype=int), mode='same')
        df[flashed] = 0
        step += 1
        if np.all(flashed):
            return step
        
inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")