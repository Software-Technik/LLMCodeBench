import sys
import numpy as np
from skimage.measure import label

def part1(data):
    df = np.array([list(map(int, list(line))) for line in data])
    pad = np.pad(df, ((1,1),(1,1)), constant_values=10)
    mask = (
        (df < pad[1:-1, 0:-2]) & 
        (df < pad[1:-1, 2:]) & 
        (df < pad[0:-2, 1:-1]) & 
        (df < pad[2:, 1:-1])
    )
    return (df + 1)[mask].sum()

def part2(data):
    df = np.array([list(map(int, list(line))) for line in data])
    labels = label(df < 9, connectivity=1)
    counts = np.bincount(labels.ravel())[1:]
    sorted_counts = np.sort(counts)
    top3 = sorted_counts[-3:]
    return int(np.prod(top3))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")