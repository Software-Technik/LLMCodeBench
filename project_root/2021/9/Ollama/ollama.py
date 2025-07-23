import numpy as np

def part1(data):
    df = np.array([list(map(int, [c for c in line])) for line in data])
    pad = np.pad(df, ((1, 1), (1, 1)), "constant", constant_values=10)
    mask = (
        (df < pad[1:-1, 0:-2]).astype(int)  # left
        +(df < pad[1:-1, 2:]).astype(int)   # right
        +( df < pad[0:-2, 1:-1]).astype(int)# top
        +( df< pad[2:, 1:-1]).astype(int)   # bottom
    )
    return (df + 1)[mask == 4].sum()

def part2(data):
    df = np.array([list(map(int, [c for c in line])) for line in data])
    labels, count = label(df < 9, connectivity=1), 0
    props = regionprops(labels)
    return int(np.prod(sorted([r.area for r in props])[-3:]))

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]
sys.stdout.write(f"{part1(data)} {part2(data)}")