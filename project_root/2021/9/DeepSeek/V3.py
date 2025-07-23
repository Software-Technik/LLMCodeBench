import sys
import numpy as np
from skimage.measure import label, regionprops

def part1(data):
    df = np.array([list(map(int, line.strip())) for line in data])
    pad = np.pad(df, 1, constant_values=10)
    mask = (
        (df < pad[1:-1, :-2]) &  # left
        (df < pad[1:-1, 2:]) &    # right
        (df < pad[:-2, 1:-1]) &   # top
        (df < pad[2:, 1:-1])      # bottom
    )
    return (df[mask] + 1).sum()

def part2(data):
    df = np.array([list(map(int, line.strip())) for line in data])
    labeled = label(df < 9, connectivity=1)
    regions = regionprops(labeled)
    areas = sorted([r.area for r in regions], reverse=True)[:3]
    return areas[0] * areas[1] * areas[2]

with open(sys.argv[1]) as f:
    data = [line for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")