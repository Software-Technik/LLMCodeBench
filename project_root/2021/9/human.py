import sys
import numpy as np
from skimage.measure import label, regionprops

def part1(data):
    df = np.array([list(map(int, [c for c in line])) for line in data])
    pad = np.pad(df, ((1, 1), (1, 1)), "constant", constant_values=10)
    mask = (
        (df < pad[1:-1, 0:-2]).astype(int)  # left
        + (df < pad[1:-1, 2:]).astype(int)  # right
        + (df < pad[0:-2, 1:-1]).astype(int)  # top
        + (df < pad[2:, 1:-1]).astype(int)  # bottom
    )
    return (df + 1)[mask == 4].sum()    # 550

def part2(data):
    df = np.array([list(map(int, [c for c in line])) for line in data])
    return int(np.prod(sorted([r.area for r in regionprops(label(df < 9, connectivity=1))])[-3:]))   # 1100682

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")