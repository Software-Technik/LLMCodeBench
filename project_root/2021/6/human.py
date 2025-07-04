import sys
import numpy as np
from collections import Counter

def part1(data):
    df = np.array([int(x) for x in data.split(",")])

    for day in range(80):
        df -= 1
        new = np.sum(df < 0)
        df = np.where(df < 0, 6, df)
        if new:
            df = np.hstack([df, np.full(new, 8)])

    return df.shape[0] # 362346

def part2(data):
    df = Counter([int(x) for x in data.split(",")])
    for i in range(-1, 9):
        if i not in df:
            df[i] = 0

    for day in range(256):
        for i in range(9):
            df[i-1] = df[i]
        df[6] += df[-1]
        df[8] = df[-1]
        df[-1] = 0

    total = 0
    for i in range(9):
        total += df[i]
    return total    # 1639643057051

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = next(f).strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")