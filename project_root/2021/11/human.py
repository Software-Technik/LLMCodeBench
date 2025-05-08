import sys
import numpy as np
from scipy import signal

def part1(data):
    df = np.array([[int(x) for x in line] for line in data])

    total = 0
    for i in range(100):
        energy = np.ones_like(df)
        flashed = np.zeros_like(df)
        while np.any(energy.astype(bool)):
            df += energy
            flashing = np.logical_and((df > 9), np.logical_not(flashed))
            energy = signal.convolve(flashing, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode='same')
            flashed = np.logical_or(flashed, flashing)
        df[flashed] = 0
        total += np.sum(flashed)
    return total    # 1729

def part2(data):
    df = np.array([[int(x) for x in line] for line in data])

    step = 0
    while True:
        energy = np.ones_like(df)
        flashed = np.zeros_like(df)
        while np.any(energy.astype(bool)):
            df += energy
            flashing = np.logical_and((df > 9), np.logical_not(flashed))
            energy = signal.convolve(flashing, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode='same')
            flashed = np.logical_or(flashed, flashing)
        df[flashed] = 0
        step += 1
        if np.all(flashed):
            return step # 237
        
inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")